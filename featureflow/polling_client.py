#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import requests


class PollingClient:
    API_ENDPOINT = "https://app.featureflow.io/api/sdk/v1/features"
    POLLING_INTERVAL = 30

    def __init__(self, client):
        """Constructor for PollingClient"""
        self._client = client
        self._api_key = client.api_key

        self._headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self._api_key),
            'X-Featureflow-Client': 'PythonClient/1.0.0'
        }

        #self._polling_loop()

    def poll(self):
        """Polling data from API periodically"""
        response = requests.get(self.API_ENDPOINT, headers=self._headers)
        if response.status_code == 200:
            self._client.update_features(response.json())
        else:
            print("PollingClient got error from API code {} message {}".format(
                response.status_code, response.reason))

    def _polling_loop(self):
        while True:
            self.poll()
            time.sleep(self.POLLING_INTERVAL)
