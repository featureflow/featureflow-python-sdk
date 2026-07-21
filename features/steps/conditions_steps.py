from behave import given, when, then

from featureflow.condition import Condition


def _coerce(kind, value):
    return float(value) if kind == 'number' else value


@given('the target is a "{kind}" with the value of "{value}"')
def step_impl(context, kind, value):
    context.target_value = _coerce(kind, value)


@given('the attribute is a "{kind}" with the value of "{value}"')
def step_impl(context, kind, value):
    context.condition_values = [_coerce(kind, value)]


@given('the attribute is an array of values "{values}"')
def step_impl(context, values):
    context.condition_values = values.split(', ')


@when('the operator test "{operator}" is run')
def step_impl(context, operator):
    condition = Condition(target='x', operator=operator, values=context.condition_values)
    context.result = condition.evaluate(context.target_value)


@then('the output should equal "{expected}"')
def step_impl(context, expected):
    result = bool(context.result)
    expected_bool = expected == 'true'
    assert result == expected_bool, f"Expected {result} to equal {expected_bool}"
