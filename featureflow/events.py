#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import requests


class Events:
    API_BASE = "https://app.featureflow.io/api/sdk/v1"
    POLLING_INTERVAL = 30
    _events_url = "{}/events".format(API_BASE)
    _register_url = "{}/register".format(API_BASE)

    def __init__(self, client):
        """Constructor for Events service"""
        self._client = client

        self._headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self._client.api_key),
            'X-Featureflow-Client': 'PythonClient/1.0.0'
        }

        self._events = []

        self._events_loop()

    def register(self, features):
        """Registers new features on the server"""
        if features != []:
            requests.put(self._register_url, headers=self._headers, json=features)

    def evaluate(self, events):
        """Adds the evaluation event to queue to push to the server"""
        self._events += events
        if len(self._events) >= self.MAX_QUEUE_LENGTH:
            self._publish_events()

    def _publish_events(self):
        """Publishes events queue to server"""
        if self._events != []:
            print("Submitting {} events".format(len(self._events)))
            requests.post(self._events_url, headers=self._headers, json=self._events)
            self._events = []

    def _events_loop(self):
        """docstring for _events_loop"""
        while True:
            self._publish_events()
            time.sleep(self.POLLING_INTERVAL)
