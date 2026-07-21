#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from .condition import Condition


class Rule:
    def __init__(self, rule):
        """docstring for __init__"""
        self._rule = rule

    @property
    def default(self):
        return self._rule.get('defaultRule', False)

    @property
    def conditions(self):
        audience = self._rule.get('audience') or {}
        return [Condition(**c) for c in audience.get('conditions', [])]

    @property
    def variant_splits(self):
        return self._rule.get('variantSplits', [])

    def match(self, user):
        if self.default:
            return True

        conditions = self.conditions

        if not conditions:
            return True

        if user is None:
            return False

        attributes = {**user.attributes, **user.session_attributes}

        for condition in conditions:
            values = attributes.get(condition.target)
            if values is None:
                return False
            if not isinstance(values, list):
                values = [values]

            if not any(condition.evaluate(value) for value in values):
                return False

        return True

    def get_variant_split_key(self, variant_value):
        """docstring for get_variant_split_key"""
        percent = 0
        for vs in self.variant_splits:
            percent += vs['split']
            if percent >= variant_value:
                return vs['variantKey']
