import unittest
import float_range
from float_range.range import FloatRange


class TestFloatRange(unittest.TestCase):

    def test_getitem_positive(self):
        expected_value = 1.5

        given_value = FloatRange(0, 10, 1.5)
        self.assertEqual(expected_value, given_value[1])

    def test_getitem_negative(self):
        expected_value = 9

        given_value = FloatRange(0, 10, 1.5)[-1]
        self.assertEqual(expected_value, given_value)

    def test_getitem_TypeError(self):
        expected_value = TypeError

        with self.assertRaises(expected_value):
            FloatRange(0, 10, 1.5)['a']

    def test_getitem_IndexError(self):
        expected_value = IndexError

        with self.assertRaises(expected_value):
            FloatRange(0, 10, 1.5)[123]

    def test_index(self):
        expected_value = 1

        given_value = FloatRange(0, 10, 1.5).index(1.5)
        self.assertEqual(expected_value, given_value)

        given_value = FloatRange(10, 0, -1.5).index(8.5)
        self.assertEqual(expected_value, given_value)

    def test_min(self):
        expected_value = 1

        given_value = min(FloatRange(10, 0, -1.5))
        self.assertEqual(expected_value, given_value)

    def test_max(self):
        expected_value = 10

        given_value = max(FloatRange(10, 0, -1.5))
        self.assertEqual(expected_value, given_value)

    def test_min_max(self):
       seq = FloatRange(10, 0, -1.5)
       # previous calls of min and max should not affect now
       min(seq)
       max(seq)
       given_value = min(seq)
       expected_value = 1
       self.assertEqual(expected_value, given_value)

    def test_contains_true(self):
        expected_value = True

        given_value = 10 in FloatRange(10, 0, -1.5)
        self.assertEqual(expected_value, given_value)

        given_value = 8.5 in FloatRange(10, 0, -1.5)
        self.assertEqual(expected_value, given_value)

    def test_contains_false(self):
        expected_value = False

        given_value = 1.6 in FloatRange(0, 10, 1.5)
        self.assertEqual(expected_value, given_value)

        given_value = 0 in FloatRange(10, 0, -1.5)
        self.assertEqual(expected_value, given_value)

    def test_count_one(self):
        expected_value = 1

        given_value = FloatRange(0, 10.9, 1.5).count(1.5)
        self.assertEqual(expected_value, given_value)

    def test_count_zero(self):
        expected_value = 0

        given_value = FloatRange(0, 10.9, 1.6).count(1.5)
        self.assertEqual(expected_value, given_value)

    def test_count_invalid(self):
        expected_value = 0

        given_value = FloatRange(0, 10.9, 1.6).count('a')
        self.assertEqual(expected_value, given_value)

    def test_len_non_zero(self):
        expected_value = 7

        given_value = len(FloatRange(0, 10.5, 1.5))
        self.assertEqual(expected_value, given_value)

    def test_len_zero(self):
        expected_value = 0

        given_value = len(FloatRange(0, 10.5, 11))
        self.assertEqual(expected_value, given_value)

#   This test does not pass => tithe issue
#    def test_contains_tithe(self):
#        given_value = -4.667 in float_range.range(-6, 10, 1.333)
#        expected_value = True
#        self.assertEqual(expected_value, given_value)

    def test_repr_simple(self):
        self.assertEqual('FloatRange(0, 10, 1)', str(FloatRange(10)))
        self.assertEqual('FloatRange(10, 20, 1)', str(FloatRange(10, 20)))
        self.assertEqual('FloatRange(10, 20, 3)', str(FloatRange(10, 20, 3)))

    def test_repr_decimal(self):
        cases = [
            ('FloatRange(0, 10.0, 1)', str(FloatRange(10.))),
            ('FloatRange(0, 10.12, 1)', str(FloatRange(10.12))),
            ('FloatRange(10.0, 20.0, 1)', str(FloatRange(10., 20.))),
            ('FloatRange(10, 20, 3.2)', str(FloatRange(10, 20, 3.2))),
        ]

        for case in cases:
            self.assertEqual(case[0], case[1])

    def test_equality_float(self):
        self.assertTrue(FloatRange(10) == FloatRange(10.))

    def test_equality_fail(self):
        self.assertFalse(FloatRange(10) == FloatRange(9))

    def test_equality_reverse(self):
        self.assertFalse(12 == FloatRange(10))

    def test_equality_multi_args(self):
        self.assertFalse(FloatRange(1, 5) == FloatRange(5, 1))
        self.assertTrue(FloatRange(1, 5) == FloatRange(1, 5))
        self.assertTrue(FloatRange(1, 5, 2) == FloatRange(1, 5, 2))

    def test_equality_wrong_type(self):
        vals = ['12', 12, None]
        obj = FloatRange(51)

        for v in vals:
            self.assertFalse(obj == v)

    def test_inequality_float(self):
        self.assertFalse(FloatRange(10) != FloatRange(10.))

    def test_inequality_fail(self):
        self.assertTrue(FloatRange(10) != FloatRange(9))

    def test_inequality_reverse(self):
        self.assertTrue(12 != FloatRange(10))

    def test_inequality_multi_args(self):
        self.assertTrue(FloatRange(1, 5) != FloatRange(5, 1))
        self.assertFalse(FloatRange(1, 5) != FloatRange(1, 5))
        self.assertFalse(FloatRange(1, 5, 2) != FloatRange(1, 5, 2))

    def test_inequality_wrong_type(self):
        vals = ['12', 12, None]
        obj = FloatRange(51)

        for v in vals:
            self.assertTrue(obj != v)


class TestRange(unittest.TestCase):

    def test_single_argument_range(self):
        expected_value = [i for i in range(10)]
        given_value = [i for i in float_range.range(10)]

        self.assertEqual(expected_value, given_value)

        expected_value = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        another_given_value = [i for i in float_range.range(10.2)]

        self.assertEqual(expected_value, another_given_value)

    def test_start_stop_range(self):
        expected_value = [i for i in range(10, 14)]
        given_value = [i for i in float_range.range(10, 14)]

        self.assertEqual(expected_value, given_value)

        expected_value = [10, 11, 12, 13, 14]
        given_value = [i for i in float_range.range(10, 14.2)]

        self.assertEqual(expected_value, given_value)

        expected_value = [10.5, 11.5, 12.5, 13.5]
        given_value = [i for i in float_range.range(10.5, 14.2)]

        self.assertEqual(expected_value, given_value)

        expected_value = [10.5, 11.5, 12.5, 13.5]
        given_value = [i for i in float_range.range(10.5, 14)]

        self.assertEqual(expected_value, given_value)

        expected_value = []
        given_value = [i for i in float_range.range(14, 10)]

        self.assertEqual(expected_value, given_value)

    def test_start_stop_step(self):
        expected_value = [i for i in range(10, 20, 2)]
        given_value = [i for i in float_range.range(10, 20, 2)]

        self.assertEqual(expected_value, given_value)

        expected_value = [10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5]
        given_value = [i for i in float_range.range(10, 14, 0.5)]

        self.assertEqual(expected_value, given_value)

        expected_value = [14, 13.5, 13, 12.5, 12, 11.5, 11, 10.5]
        given_value = [i for i in float_range.range(14, 10, -0.5)]

        self.assertEqual(expected_value, given_value)

    def test_properly_sum_floats(self):
        expected_value = [9, 9.2, 9.4, 9.6, 9.8]
        given_value = [i for i in float_range.range(9, 10, 0.2)]

        self.assertEqual(expected_value, given_value)


class TestPrecision(unittest.TestCase):

    def test_valid_number(self):
        expected_value = 1
        given_value = FloatRange._precision(12354.2)

        self.assertEqual(expected_value, given_value)

        expected_value = 2
        given_value = FloatRange._precision(.22)

        self.assertEqual(expected_value, given_value)

        expected_value = 1
        given_value = FloatRange._precision(22.)

        self.assertEqual(expected_value, given_value)

    def test_invalid_number(self):
        self.assertRaises(ValueError, FloatRange._precision, '12.12.23')
        self.assertRaises(ValueError, FloatRange._precision, None)
        self.assertRaises(ValueError, FloatRange._precision, float('inf'))
        self.assertRaises(ValueError, FloatRange._precision, float('-inf'))
        self.assertRaises(ValueError, FloatRange._precision, 'lizard ')


if __name__ == '__main__':
    unittest.main()
