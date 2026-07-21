from behave import given, when, then

from featureflow.feature import Feature
from featureflow.user import User


@given('the salt is "{salt}", the feature is "{feature_key}" and the id is "{id}"')
def step_impl(context, salt, feature_key, id):
    context.salt = salt
    context.feature_key = feature_key
    context.id = id


@when('the variant value is calculated')
def step_impl(context):
    feature = Feature({'key': context.feature_key, 'variantSalt': context.salt})
    user = User(key=context.id)
    context.hash = feature._calculate_hash(user).decode().lower()
    context.result = feature.get_variant_value(user)


@then('the hash value calculated should equal "{hash}"')
def step_impl(context, hash):
    assert context.hash == hash, f"Expected {context.hash} to be {hash}"


@then('the result from the variant calculation should be {result:d}')
def step_impl(context, result):
    assert context.result == result, f"Expected {context.result} to be {result}"
