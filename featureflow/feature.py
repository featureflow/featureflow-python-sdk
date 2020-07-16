#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from hashlib import sha1
from rule import Rule

import base64


class Feature:
    def __init__(self, feature):
        """docstring for __init__"""
        self._feature = feature

    @property
    def enabled(self):
        return self._feature.get('enabled', False)

    @property
    def key(self):
        return self._feature.get('key', False)

    @property
    def variant_salt(self):
        return self._feature.get('variantSalt', False)

    @property
    def rules(self):
        rules = self._feature.get('rules', [])
        return [Rule(rule) for rule in rules]

    def get_variant_value(self, user):
        return int(self._calculate_hash(user), 16) % 100 + 1

    def _calculate_hash(self, user):
        sha = sha1(b"{}:{}:{}".format(self._feature.variant_salt,
                                      self._feature.key,
                                      user.key)).digest()

        return base64.encodebytes(sha)[0:15]