from behave import given, when, then

from featureflow.evaluate import Evaluate
from featureflow.user import User


class _StubEventsClient:
    def evaluate(self, events):
        return events


class _StubClient:
    def __init__(self):
        self.events_client = _StubEventsClient()


@given('the feature "{key}" with an offVariantKey "{off_variant_key}", a default key of "{default_key}" is {enabled_or_disabled}')
def step_impl(context, key, off_variant_key, default_key, enabled_or_disabled):
    context.evaluation_feature = {
        'key': key,
        'offVariantKey': off_variant_key,
        'enabled': enabled_or_disabled == 'enabled',
        'rules': [
            {'defaultRule': True, 'variantSplits': [{'variantKey': default_key, 'split': 100}]}
        ],
    }


@when('the feature is evaluated with a user "{user_id}"')
def step_impl(context, user_id):
    user = User(key=user_id)
    evaluate = Evaluate(_StubClient(), context.evaluation_feature, user)
    context.evaluated_variant = evaluate.value()


@then('the evaluated variant should be "{expected}"')
def step_impl(context, expected):
    assert context.evaluated_variant == expected, f"Expected {context.evaluated_variant} to be {expected}"
