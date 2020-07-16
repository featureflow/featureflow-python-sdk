#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from feature import Feature


class Evaluate:
    DEFAULT_FEATURE_VARIANT = "off"

    def __init__(self, feature, user):
        """docstring for __init__"""
        self._feature = Feature(feature)
        self._user = user

        self._evaluated_variant = self._calculate_variant()

    def _calculate_variant(self):
        if not self._feature.enabled:
            return self._feature.off_variant_key

        for rule in self._feature.rules:
            if rule.match(user):
               variant_value = self._feature.get_variant_value(user)
               return rule.get_variant_split_key(variant_value)


