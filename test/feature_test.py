from datetime import date
import unittest

from featureflow.feature import Feature
from .test_helpers import values, fake


class FeatureTest(unittest.TestCase):
    """Tests for Featureflow.Feature"""
    def test_disabled(self):
        feature = Feature(


