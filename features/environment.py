"""behave hooks for the shared-testbed conformance suite.

Beyond the per-scenario fixtures, this file holds two guards that stop the suite
looking green while proving nothing. Both exist because that has already happened:
the Go SDK ran 24 of its 93 scenarios for weeks without anyone noticing, and the
date scenarios here were inert for as long as the runner sat on UTC.
"""

import os
import time

# A date-only condition value such as "2026-07-03" must denote UTC midnight on every
# SDK and every host (testbed CONTRACT.md, "Operators"). An implementation that parses
# it in the host's local time passes those scenarios anyway whenever the runner sits on
# UTC -- which is how the bug survived unnoticed in three SDKs. Asia/Tokyo is +09:00 all
# year: a whole-hour offset with no DST, so expected instants stay easy to reason about.
# test/test_condition.py pins the same zone for the unit tests.
# Do NOT remove this to make a failing date scenario go green.
TEST_TIMEZONE = 'Asia/Tokyo'

# Floor, not an exact count: 105 scenarios run today. Scenarios are added to the testbed
# regularly, so this is expected to lag the real total. Raise it when the testbed grows;
# never lower it to accommodate a sudden drop without first working out where the
# missing scenarios went.
MIN_SCENARIOS = 85

# Module-level, not a context attribute: behave pushes a fresh context layer per
# scenario and pops it afterwards, so anything after_scenario writes to `context` is
# discarded before after_all sees it.
_scenarios_run = 0


def before_all(context):
    global _scenarios_run
    _scenarios_run = 0

    os.environ['TZ'] = TEST_TIMEZONE
    if hasattr(time, 'tzset'):
        time.tzset()


def before_scenario(context, scenario):
    context.rule_dict = {'defaultRule': False, 'audience': {'conditions': []}, 'variantSplits': []}
    context.user_attributes = {}


def after_scenario(context, scenario):
    global _scenarios_run
    _scenarios_run += 1


def after_all(context):
    """The two suite-level guards. Either one failing fails the run (behave reports a
    HOOK-ERROR and exits non-zero)."""
    _assert_no_undefined_steps(context)
    _assert_scenario_floor()


def _assert_no_undefined_steps(context):
    """Fail on an undefined step rather than reporting it and moving on.

    behave >= 1.3 already errors on undefined steps, but `behave` is unpinned in
    setup.py and behave dropped the explicit --strict option, so the strictness is
    implicit and version-dependent. The testbed is a submodule: a step renamed upstream
    stops matching here with no other signal -- exactly how 69 scenarios silently
    stopped running in the Go SDK. This check does not depend on the behave version.

    Checked here rather than in after_step because behave does not run after_step
    hooks for a step it could not match.
    """
    undefined = getattr(getattr(context, '_runner', None), 'undefined_steps', None)
    if not undefined:
        return
    locations = ', '.join(sorted({'%s %s' % (s.keyword, s.name) for s in undefined}))
    raise AssertionError(
        '%d undefined step(s): %s. The testbed submodule has probably moved ahead of '
        'features/steps/ -- add or rename the step definition rather than letting the '
        'scenarios be skipped.' % (len(undefined), locations))


def _assert_scenario_floor():
    """Fail if the suite barely ran anything.

    The undefined-step guard cannot catch a suite that stopped loading its feature
    files at all: behave reports "0 scenarios passed" and exits zero. features/*.feature
    are symlinks into testbed/gherkin, so an uninitialised submodule leaves them all
    dangling.
    """
    if _scenarios_run < MIN_SCENARIOS:
        raise AssertionError(
            'Only %d scenarios ran, expected at least %d. The testbed submodule is '
            'probably uninitialised (features/*.feature are symlinks into testbed/gherkin), '
            'or behave.ini tags now exclude far more than intended.'
            % (_scenarios_run, MIN_SCENARIOS))
