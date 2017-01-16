import unittest
import float_range


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

    def test_start_stop_step(self):
        expected_value = [i for i in range(10, 20, 2)]
        given_value = [i for i in float_range.range(10, 20, 2)]

        self.assertEqual(expected_value, given_value)

        expected_value = [10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5]
        given_value = [i for i in float_range.range(10, 14, 0.5)]

        self.assertEqual(expected_value, given_value)


if __name__ == '__main__':
    unittest.main()
