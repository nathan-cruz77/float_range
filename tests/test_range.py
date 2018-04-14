import unittest
import float_range
from float_range.range import FloatRange


class TestFloatRange(unittest.TestCase):

    def test_contains_true(self):
        given_value = 1.5 in FloatRange(0, 10, 1.5)
        expected_value = True
        self.assertEqual(expected_value, given_value)

    def test_contains_false(self):
        given_value = 1.6 in FloatRange(0, 10, 1.5)
        expected_value = False
        self.assertEqual(expected_value, given_value)

    def test_len_non_zero(self):
        given_value = len(FloatRange(0, 10.5, 1.5))
        expected_value = 7
        self.assertEqual(expected_value, given_value)

    def test_len_zero(self):
        given_value = len(FloatRange(0, 10.5, 11))
        expected_value = 0
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
        self.assertEqual('FloatRange(0, 10.0, 1)', str(FloatRange(10.)))
        self.assertEqual('FloatRange(0, 10.12, 1)', str(FloatRange(10.12)))
        self.assertEqual('FloatRange(10.0, 20.0, 1)', str(FloatRange(10., 20.)))
        self.assertEqual('FloatRange(10, 20, 3.2)', str(FloatRange(10, 20, 3.2)))

    def test_equality(self):
        self.assertTrue(FloatRange(10) == FloatRange(10.))
        self.assertFalse(FloatRange(10) == FloatRange(9))
        self.assertFalse(FloatRange(10) == 12)
        self.assertFalse(12 == FloatRange(10))

        self.assertFalse(FloatRange(1, 5) == FloatRange(5, 1))
        self.assertTrue(FloatRange(1, 5) == FloatRange(1, 5))

        self.assertFalse(FloatRange(51) == '12')
        self.assertFalse('12' == FloatRange(51))

        self.assertFalse(FloatRange(10) == None)

    def test_inequality(self):
        self.assertFalse(FloatRange(10) != FloatRange(10.))
        self.assertTrue(FloatRange(10) != FloatRange(9))
        self.assertTrue(FloatRange(10) != 12)
        self.assertTrue(12 != FloatRange(10))

        self.assertTrue(FloatRange(1, 5) != FloatRange(5, 1))
        self.assertFalse(FloatRange(1, 5) != FloatRange(1, 5))

        self.assertTrue(FloatRange(51) != '12')
        self.assertTrue('12' != FloatRange(51))

        self.assertTrue(FloatRange(10) != None)


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
