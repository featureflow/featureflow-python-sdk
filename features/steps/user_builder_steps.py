# featureflow-python-sdk has no separate UserBuilder class -- User is a plain data
# class constructed directly (User(key=..., attributes=...)). These steps simulate the
# builder vocabulary the shared scenarios use, over that direct constructor. Scenarios
# this SDK can't honestly claim to support are excluded by tag rather than faked here:
#   @builder-injects-implicit-attributes / @builder-defers-implicit-attributes -- this
#     SDK doesn't inject featureflow.user.id/date anywhere (neither at construction nor
#     evaluate time), unlike every other SDK -- a real gap, not yet implemented.
#   @user-builder-validates-empty-id -- User.__init__ accepts an empty id silently.

from behave import given, when, then

from featureflow.user import User


@given('there is access to the User Builder module')
def step_impl(context):
    assert User is not None


@when('the builder is initialised with the id "{id}"')
def step_impl(context, id):
    context.builder_id = id
    context.builder_attributes = {}


@when('the builder is given the following attributes')
def step_impl(context):
    for row in context.table:
        context.builder_attributes[row['key']] = row['value']


@when('the user is built using the builder')
def step_impl(context):
    context.built_user = User(key=context.builder_id, attributes=context.builder_attributes)


@then('the result user should have an id "{id}"')
def step_impl(context, id):
    assert context.built_user.key == id, f"Expected {context.built_user.key} to be {id}"


@then('the result user should have no attributes')
def step_impl(context):
    assert len(context.built_user.attributes) == 0, \
        f"Expected no attributes, got {context.built_user.attributes}"


@then('the result user should have a attribute with key "{key}" and value "{value}"')
def step_impl(context, key, value):
    actual = str(context.built_user.attributes[key])
    assert actual == value, f"Expected {actual} to be {value}"
