import json

from behave import given, when, then

from featureflow.rule import Rule
from featureflow.user import User


@given('the rule is a default rule')
def step_impl(context):
    context.rule_dict['defaultRule'] = True


@when('the rule is matched against the user')
def step_impl(context):
    rule = Rule(context.rule_dict)
    user = User(key='anonymous', attributes=context.user_attributes)
    context.match_result = rule.match(user)


@then('the result from the match should be {expected}')
def step_impl(context, expected):
    expected_bool = expected == 'true'
    assert context.match_result == expected_bool, f"Expected {context.match_result} to be {expected_bool}"


@given('the user attributes are')
def step_impl(context):
    for row in context.table:
        context.user_attributes[row['key']] = json.loads(row['value'])


@given("the rule's audience conditions are")
def step_impl(context):
    conditions = []
    for row in context.table:
        conditions.append({
            'operator': row['operator'],
            'target': row['target'],
            'values': json.loads(row['values']),
        })
    context.rule_dict['audience'] = {'conditions': conditions}


@given('the variant value of {value:d}')
def step_impl(context, value):
    context.variant_value = value


@given('the variant splits are')
def step_impl(context):
    context.rule_dict['variantSplits'] = [
        {'variantKey': row['variantKey'], 'split': float(row['split'])} for row in context.table
    ]


@when('the variant split key is calculated')
def step_impl(context):
    rule = Rule(context.rule_dict)
    context.split_result = rule.get_variant_split_key(context.variant_value)


@then('the resulting variant should be "{expected}"')
def step_impl(context, expected):
    assert context.split_result == expected, f"Expected {context.split_result} to be {expected}"
