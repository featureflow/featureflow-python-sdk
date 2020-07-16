#! /usr/bin/env python3
# -*- coding: utf-8 -*-


class Featureflow:
    def __init__(self, api_key, with_features=[]):
        """docstring for __init__"""
        self.api_key = api_key
        self._polloing_client = PollingClient(self)
        self._events_client = EventsService(self)

