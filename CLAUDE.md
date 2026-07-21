# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

The official Python server-side SDK for Featureflow (`featureflow-sdk` on PyPI). It polls the Featureflow management API for flag configuration, evaluates flags locally against a `User`, and asynchronously reports evaluation events back to the server. See the root workspace `CLAUDE.md` for how this repo fits into the broader Featureflow system (this is one of six actively-maintained server-side SDKs, alongside Java/Node/Go/Ruby/.NET).

## Commands

```bash
# Install for development (editable + test extra)
python3 -m pip install -e ".[test]"

# Unit tests (stdlib unittest, auto-discovers test/test_*.py)
python3 -m unittest discover -s test

# Run a single unit test
python3 -m unittest test.test_client.EvaluateTest.test_disabled

# BDD conformance suite (behave), config/tag-exclusions in behave.ini
behave
```

There is no lint/typecheck config in this repo (no flake8/mypy/black config present) — don't invent one.

## Architecture

### Runtime evaluation flow

`Featureflow(api_key)` (`featureflow/featureflow.py`) is the SDK entrypoint. On construction it starts two daemon-less background `Thread`s and holds an in-memory `_features` dict:

- `PollingClient` (`polling_client.py`) — polls `GET /api/sdk/v1/features` on `app.featureflow.io` every 30s, replacing `client._features` wholesale on success.
- `Events` (`events.py`) — buffers evaluation events in memory and flushes them via `POST /api/sdk/v1/events` every 30s (or immediately if the queue hits `MAX_QUEUE_LENGTH`). Also exposes `register_features()` (`PUT /api/sdk/v1/register`) for pre-registering flags client-side.

`Featureflow.evaluate(feature_key, user)` returns an `Evaluate` (`evaluate.py`), which computes the variant **eagerly in `__init__`** via `_calculate_variant()`, then reports an evaluation event to `Events` as a side effect of `.value()` / `.is_()` / `.isOn()` / `.isOff()` — calling these methods multiple times reports duplicate events.

### Local evaluation logic (the part covered by conformance tests)

This is the pure, no-network part of the SDK and is what the `features/` BDD suite exercises:

- `Feature` (`feature.py`) wraps the raw dict from the API. `get_variant_value(user)` computes the bucketing hash: `SHA1("{variantSalt}:{key}:{user.key}")` → first 15 hex chars → int mod 100 + 1. This algorithm **must stay bit-for-bit identical across all Featureflow SDKs** (see root `CLAUDE.md` cross-repo conventions) — don't change it without updating `testbed/`.
- `Rule` (`rule.py`) — `match(user)` checks the default-rule flag, then ANDs each `Condition` against `user.attributes` merged with `user.session_attributes` (session takes precedence in the merge). `get_variant_split_key()` walks `variantSplits` accumulating percentages until the bucketed value falls within a split.
- `Condition` (`condition.py`) — operators (`equals`, `contains`, `startsWith`, `matches`, `before`/`after` on ISO8601 dates, numeric comparisons, etc.). Unknown/mismatched-type operator+attribute combos fall through and return `None` (falsy), not an exception.
- `Evaluate._calculate_variant()` ties it together: disabled feature → `off_variant_key`; otherwise first matching rule determines the variant split.

### Testbed submodule (`testbed/`)

`testbed/` is a **git submodule** pointing at `featureflow-sdk-testbed`, a shared Gherkin contract consumed by every Featureflow SDK (Node, Go, Ruby, Python, ...) so bucketing/rule/condition behavior stays identical across languages. `features/*.feature` are **symlinks into `testbed/gherkin/`** — never fork/copy the feature files locally; if a scenario needs to change, it changes in the submodule (`testbed/CHANGELOG.md` records what's been promoted there and why). `features/steps/*.py` contains only this SDK's step definitions, mapping Gherkin phrases onto internal helpers like `Feature._calculate_hash`.

`json_value.feature` is deliberately not symlinked in — this SDK has no `jsonValue()`-equivalent yet. `behave.ini` excludes `@integration` and tags for behaviors this SDK's `User`/`Feature` intentionally doesn't implement (see the comments there for the reasoning per tag, e.g. `@builder-injects-implicit-attributes` doesn't apply since this SDK never injects `featureflow.user.id`/`featureflow.date` implicitly).

If you update the submodule pointer, run `git submodule update --init` to pull the new `testbed/` commit before running `behave`.

### Serialization conventions

`User.toJSON()` and `Event.toJSON()` produce the camelCase wire format the server expects (`sessionAttributes`, `featureKey`, `evaluatedVariant`, ...) — internal Python attributes stay snake_case; only the `toJSON()` boundary translates casing.
