#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from polling_client import PollingClient
from events import Events
from evaluate import Evaluate


class Featureflow:
    DEFAULT_FEATURE_VARIANT = "off"

    def __init__(self, api_key, with_features=[]):
        """docstring for __init__"""
        self.api_key = api_key
        self._polloing_client = PollingClient(self)
        self._events_client = Events(self)

        self._features = {}

        if with_features != []:
            self._events_client.register_features(with_features)

    def update_features(self, features):
        self._features = features

    def evaluate(feature_key, user=None):
        return Evaluate(self._features.get(feature_key, {}), user)
