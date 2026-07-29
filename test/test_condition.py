from datetime import date, datetime, timedelta, timezone
import os
import time
import unittest

from featureflow.condition import Condition, _parse_iso8601
from .test_helpers import values, fake


class ConditionTest(unittest.TestCase):
    """Tests for Featureflow.Condition"""
    def test_equals(self):
        """Test 'equals' operator for all supported types"""
        operator = 'equals'
        vals = [fake.word(), fake.random_int(0, 100), fake.date()]
        # Equals case
        for val in vals:
            condition = Condition(operator=operator, values=values(value=val))
            self.assertTrue(condition.evaluate(val))

        # Not equals case
        for val in vals:
            condition = Condition(operator=operator, values=values())
            self.assertFalse(condition.evaluate(val))

    def test_contains(self):
        """Test 'contains' operator for strings"""
        operator = 'contains'

        val = fake.word()

        length = len(val) // 2

        substr = val[fake.random_int(0, length):fake.random_int(1, length)]

        condition = Condition(operator=operator, values=values(value=substr))
        self.assertTrue(condition.evaluate(val))

        # Not
        condition = Condition(operator=operator, values=values(value=fake.word()))
        self.assertFalse(condition.evaluate(val))

    def test_starts_with(self):
        """Test 'startsWith' operator for strings"""
        operator = 'startsWith'

        val = fake.word()

        length = len(val) // 2

        substr = val[0:fake.random_int(1, length)]

        condition = Condition(operator=operator, values=values(value=substr))
        self.assertTrue(condition.evaluate(val))

        # Not
        condition = Condition(operator=operator, values=values(value=fake.word()))
        self.assertFalse(condition.evaluate(val))

    def test_ends_with(self):
        """Test 'endsWith' operator for strings"""
        operator = 'endsWith'

        val = fake.word()

        length = len(val) // 2

        substr = val[fake.random_int(0, length):]

        condition = Condition(operator=operator, values=values(value=substr))
        self.assertTrue(condition.evaluate(val))

        # Not
        condition = Condition(operator=operator, values=values(value=fake.word()))
        self.assertFalse(condition.evaluate(val))

    def test_matches(self):
        """Test 'matches' operator for strings"""
        operator = 'matches'

        val = fake.word()

        length = len(val) // 2

        substr = val[fake.random_int(0, length):fake.random_int(1, length)]
        regex = ".*{}.*".format(substr)

        condition = Condition(operator=operator, values=values(value=regex))
        self.assertTrue(condition.evaluate(val))

        # Not
        condition = Condition(operator=operator, values=values(value=fake.word()))
        self.assertFalse(condition.evaluate(val))

    def test_in(self):
        """Test 'in' operator for strings"""
        operator = 'in'

        val = fake.word()

        condition = Condition(operator=operator, values=values(value=val))
        self.assertTrue(condition.evaluate(val))

        # Not
        condition = Condition(operator=operator, values=values(value=fake.word()))
        self.assertFalse(condition.evaluate(val))

    def test_not_in(self):
        """Test 'notIn' operator for strings"""
        operator = 'notIn'

        val = fake.word()

        condition = Condition(operator=operator, values=values(value=val))
        self.assertFalse(condition.evaluate(val))

        # Not
        condition = Condition(operator=operator, values=values(value=fake.word()))
        self.assertTrue(condition.evaluate(val))

    def test_before(self):
        """Test 'before' operator for strings"""
        operator = 'before'

        val = fake.date()

        # 'before' means the attribute is earlier than the target, so a
        # true match needs a target *after* val and a false match a target
        # at-or-before val.
        val_true = fake.date_between(start_date=date.fromisoformat(val)).isoformat()
        val_false = fake.date(end_datetime=date.fromisoformat(val))

        condition = Condition(operator=operator, values=values(value=val_true))
        self.assertTrue(condition.evaluate(val))

        # Not
        condition = Condition(operator=operator, values=values(value=val_false))
        self.assertFalse(condition.evaluate(val))

    def test_after(self):
        """Test 'after' operator for strings"""
        operator = 'after'

        val = fake.date()

        # 'after' means the attribute is later than the target, so a true
        # match needs a target *before* val and a false match a target
        # at-or-after val.
        val_true = fake.date(end_datetime=date.fromisoformat(val))
        val_false = fake.date_between(start_date=date.fromisoformat(val)).isoformat()

        condition = Condition(operator=operator, values=values(value=val_true))
        self.assertTrue(condition.evaluate(val))

        # Not
        condition = Condition(operator=operator, values=values(value=val_false))
        self.assertFalse(condition.evaluate(val))

    def test_greater_than(self):
        """Test 'greaterThan' operator for strings"""
        operator = 'greaterThan'

        val = fake.random_int(1, 100)

        val_true = val - fake.random_int(1, val)
        val_false = val + fake.random_int(0, 100)

        condition = Condition(operator=operator, values=values(value=val_true))
        self.assertTrue(condition.evaluate(val))

        # Not
        condition = Condition(operator=operator, values=values(value=val_false))
        self.assertFalse(condition.evaluate(val))

    def test_less_than(self):
        """Test 'lessThan' operator for strings"""
        operator = 'lessThan'

        val = fake.random_int(1, 100)

        val_true = val + fake.random_int(1, val)
        val_false = val - fake.random_int(0, 100)

        condition = Condition(operator=operator, values=values(value=val_true))
        self.assertTrue(condition.evaluate(val))

        # Not
        condition = Condition(operator=operator, values=values(value=val_false))
        self.assertFalse(condition.evaluate(val))

    def test_greater_than_or_equal(self):
        """Test 'greaterThanOrEqual' operator for strings"""
        operator = 'greaterThanOrEqual'

        val = fake.random_int(1, 100)

        val_true = val - fake.random_int(1, val)
        val_false = val + fake.random_int(1, 100)

        # Greater
        condition = Condition(operator=operator, values=values(value=val_true))
        self.assertTrue(condition.evaluate(val))

        # Equal
        condition = Condition(operator=operator, values=values(value=val))
        self.assertTrue(condition.evaluate(val))

        # Not
        condition = Condition(operator=operator, values=values(value=val_false))
        self.assertFalse(condition.evaluate(val))

    def test_less_than_or_equal(self):
        """Test 'lessThanOrEqual' operator for strings"""
        operator = 'lessThanOrEqual'

        val = fake.random_int(1, 100)

        val_true = val + fake.random_int(1, val)
        val_false = val - fake.random_int(1, 100)

        # Less
        condition = Condition(operator=operator, values=values(value=val_true))
        self.assertTrue(condition.evaluate(val))

        # Equal
        condition = Condition(operator=operator, values=values(value=val))
        self.assertTrue(condition.evaluate(val))

        # Not
        condition = Condition(operator=operator, values=values(value=val_false))
        self.assertFalse(condition.evaluate(val))


class DateConditionTest(unittest.TestCase):
    """Tests for date handling in 'before'/'after'.

    A date-only value such as "2026-07-03" -- which is what the dashboard's date
    picker emits -- denotes UTC midnight, per CONTRACT.md. Reading it as local
    midnight would make the same rule fire at a different instant on every host,
    so these tests run under a deliberately non-UTC TZ: a local-time regression
    would shift the instant and fail them.
    """

    # +09:00, no DST, so local midnight is never UTC midnight.
    TZ = 'Asia/Tokyo'

    def setUp(self):
        self._original_tz = os.environ.get('TZ')
        os.environ['TZ'] = self.TZ
        if hasattr(time, 'tzset'):
            time.tzset()

    def tearDown(self):
        if self._original_tz is None:
            os.environ.pop('TZ', None)
        else:
            os.environ['TZ'] = self._original_tz
        if hasattr(time, 'tzset'):
            time.tzset()

    def test_date_only_is_utc_midnight(self):
        """A date-only value resolves to exactly UTC midnight, not local midnight"""
        parsed = _parse_iso8601('2026-07-03')

        self.assertIsNotNone(parsed)
        self.assertEqual(parsed.utcoffset(), timedelta(0))
        self.assertEqual(parsed, datetime(2026, 7, 3, 0, 0, 0, tzinfo=timezone.utc))

    def test_date_only_boundary(self):
        """One second after UTC midnight is 'after' the date; one second before isn't"""
        condition = Condition(operator='after', values=['2026-07-03'])
        self.assertTrue(condition.evaluate('2026-07-03T00:00:01Z'))
        self.assertFalse(condition.evaluate('2026-07-02T23:59:59Z'))

        condition = Condition(operator='before', values=['2026-07-03'])
        self.assertTrue(condition.evaluate('2026-07-02T23:59:59Z'))
        self.assertFalse(condition.evaluate('2026-07-03T00:00:01Z'))

    def test_date_only_on_both_sides(self):
        """Two date-only values compare as the UTC midnights they denote"""
        condition = Condition(operator='after', values=['2026-07-02'])
        self.assertTrue(condition.evaluate('2026-07-03'))
        self.assertFalse(condition.evaluate('2026-07-02'))

    def test_explicit_timezones_are_not_shifted(self):
        """A value carrying 'Z' or a numeric offset keeps its own instant"""
        self.assertEqual(
            _parse_iso8601('2026-07-21T06:00:00Z'),
            datetime(2026, 7, 21, 6, 0, 0, tzinfo=timezone.utc))

        # 02:00-05:00 is 07:00Z -- the offset must be applied, not ignored.
        self.assertEqual(
            _parse_iso8601('2026-07-21T02:00:00-05:00'),
            datetime(2026, 7, 21, 7, 0, 0, tzinfo=timezone.utc))

        # ...and 07:00Z is after 06:00Z, even though "02..." sorts before "06..."
        condition = Condition(operator='after', values=['2026-07-21T06:00:00Z'])
        self.assertTrue(condition.evaluate('2026-07-21T02:00:00-05:00'))

    def test_naive_and_aware_mix_does_not_raise(self):
        """A naive value compared with an aware one must not raise TypeError"""
        # Both orderings: the naive side is the attribute, then the target.
        condition = Condition(operator='after', values=['2026-07-03T00:00:00Z'])
        self.assertFalse(condition.evaluate('2026-07-02T12:00:00'))
        self.assertTrue(condition.evaluate('2026-07-04T12:00:00'))

        condition = Condition(operator='before', values=['2026-07-03T00:00:00'])
        self.assertTrue(condition.evaluate('2026-07-02T12:00:00Z'))
        self.assertFalse(condition.evaluate('2026-07-04T12:00:00Z'))

    def test_unparseable_returns_no_match(self):
        """Anything unparseable fails the condition rather than raising"""
        self.assertIsNone(_parse_iso8601('not-a-date'))
        self.assertIsNone(_parse_iso8601(''))
        self.assertIsNone(_parse_iso8601(None))
        self.assertIsNone(_parse_iso8601(20260703))

        for operator in ('before', 'after'):
            condition = Condition(operator=operator, values=['2026-07-03'])
            self.assertFalse(condition.evaluate('not-a-date'))

            # ...and an unparseable *target*, including a non-string one.
            condition = Condition(operator=operator, values=['nonsense'])
            self.assertFalse(condition.evaluate('2026-07-03T00:00:00Z'))

            condition = Condition(operator=operator, values=[20260703])
            self.assertFalse(condition.evaluate('2026-07-03T00:00:00Z'))
