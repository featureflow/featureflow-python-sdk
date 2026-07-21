def before_scenario(context, scenario):
    context.rule_dict = {'defaultRule': False, 'audience': {'conditions': []}, 'variantSplits': []}
    context.user_attributes = {}
