#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime, timezone
import re


def _parse_iso8601(value):
    """Parses an ISO8601/RFC3339 string, tolerating a trailing 'Z' (UTC designator)
    that datetime.fromisoformat only accepts natively on Python 3.11+. Returns None
    for anything that doesn't parse, rather than raising, so a malformed configured
    or user-supplied date fails the condition instead of crashing evaluation.

    The result is always timezone-aware. A value that carries no timezone information
    -- which includes the date-only values the dashboard's date picker emits, such as
    "2026-07-03" -- is read as UTC, so "2026-07-03" denotes 2026-07-03T00:00:00Z.
    This is the SDK contract (see featureflow-client-sdk-testbed/CONTRACT.md,
    "Operators", decided 2026-07-29): reading a bare date as *local* midnight would
    make the same rule take effect at a different instant on every host depending on
    its timezone, so a scheduled rollout would be non-deterministic across a fleet.
    UTC is the only reading that is identical everywhere, and it is what sdk-server
    and the JavaScript SDK already do via Date.parse.

    Returning aware datetimes throughout also keeps every comparison aware-to-aware:
    Python raises TypeError when a naive datetime is compared with an aware one, and
    an SDK must never throw into the host application."""
    if not isinstance(value, str):
        return None
    if value.endswith('Z'):
        value = value[:-1] + '+00:00'
    try:
        parsed = datetime.fromisoformat(value)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed


class Condition:
    def __init__(self, **args):
        """docstring for __init"""
        self.target = args.get('target', None)
        self.operator = args.get('operator', None)
        self.values = args.get('values', [])

    def evaluate(self, attribute):
        """docstring for evaluate"""
        if self.operator == "equals":
            return attribute == self.values[0]

        if self.operator == "contains" and type(attribute) == str:
            return self.values[0] in attribute

        if self.operator == "startsWith" and type(attribute) == str:
            return attribute.startswith(self.values[0])

        if self.operator == "endsWith" and type(attribute) == str:
            return attribute.endswith(self.values[0])

        if self.operator == "matches" and type(attribute) == str:
            return re.compile(self.values[0]).match(attribute) is not None

        if self.operator == "in" and type(attribute) == str:
            return attribute in self.values

        if self.operator == "notIn" and type(attribute) == str:
            return attribute not in self.values

        if self.operator == "greaterThan" and type(attribute) in [int, float]:
            return attribute > self.values[0]

        if self.operator == "lessThan" and type(attribute) in [int, float]:
            return attribute < self.values[0]

        if self.operator == "greaterThanOrEqual" and type(attribute) in [int, float]:
            return attribute >= self.values[0]

        if self.operator == "lessThanOrEqual" and type(attribute) in [int, float]:
            return attribute <= self.values[0]

        if self.operator == "after" and type(attribute) == str:
            attribute_dt = _parse_iso8601(attribute)
            target_dt = _parse_iso8601(self.values[0])
            if attribute_dt is None or target_dt is None:
                return False
            return attribute_dt > target_dt

        if self.operator == "before" and type(attribute) == str:
            attribute_dt = _parse_iso8601(attribute)
            target_dt = _parse_iso8601(self.values[0])
            if attribute_dt is None or target_dt is None:
                return False
            return attribute_dt < target_dt
