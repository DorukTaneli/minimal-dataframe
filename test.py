import unittest

import series
from series import StringSeries, BooleanSeries, IntegerSeries, FloatSeries, Series


class StringSeriesTestCases(unittest.TestCase):
    def test_construct_StringSeries(self):
        ss1 = StringSeries(['apple', 'banana', 'pear'])
        self.assertEqual(len(ss1.data), 3)

        ss2 = StringSeries(['apple', None, 'pear'])
        self.assertEqual(len(ss2.data), 3)

        with self.assertRaises(TypeError):
            StringSeries(['apple', 5, 'pear'])

    def test_StringSeries_equality(self):
        ss1 = StringSeries(['apple', 'banana', 'pear'])
        ss2 = StringSeries(['apple', 'banana', 'pear'])
        ss3 = StringSeries(['apple', 'banana', 'pear', 'cherry'])
        ss4 = StringSeries(['apple', 'banana', 'orange'])

        self.assertTrue(ss1.has_same_data(ss2))
        self.assertFalse(ss1.has_same_data(ss3))
        self.assertFalse(ss1.has_same_data(ss4))


class BooleanSeriesTestCases(unittest.TestCase):
    def test_construct_BooleanSeries(self):
        bs1 = BooleanSeries([True, False, False])
        self.assertEqual(len(bs1.data), 3)

        bs2 = BooleanSeries([True, None, False])
        self.assertEqual(len(bs2.data), 3)

        with self.assertRaises(TypeError):
            BooleanSeries(['apple', True, False])

    def test_BooleanSeries_equality(self):
        bs1 = BooleanSeries([True, False, False])
        bs2 = BooleanSeries([True, False, False])
        bs3 = BooleanSeries([True, False, False, True])
        bs4 = BooleanSeries([True, False, True])

        self.assertTrue(bs1.has_same_data(bs2))
        self.assertFalse(bs1.has_same_data(bs3))
        self.assertFalse(bs1.has_same_data(bs4))

    def test_BooleanSeries_invert(self):
        bs1 = BooleanSeries([True, False, False])
        bs2 = BooleanSeries([False, True, True])
        bs3 = BooleanSeries([True, None, False])
        bs4 = BooleanSeries([False, None, True])

        self.assertTrue(bs1.has_same_data(~bs2))
        self.assertTrue(bs3.has_same_data(~bs4), msg='bs3:{} bs4:{} ~bs4:{}'.format(bs3, bs4, ~bs4))

    # TODO: __and__ does not work
    def dont_test_BooleanSeries_and(self):
        bs1 = BooleanSeries([True, True, False, False, None, None])
        bs2 = BooleanSeries([True, False, True, False, True, None])

        self.assertEqual((bs1 and bs2).data, [True, False, False, False, None, None])


class NumericalSeriesTestCases(unittest.TestCase):
    def test_greater_than(self):
        is1 = IntegerSeries([3, 5, 10])
        is2 = IntegerSeries([1, None, 11])
        self.assertEqual((is1 > is2).data, [True, None, False])

        fs1 = FloatSeries([3.0, 5.0, 10.0])
        self.assertEqual((fs1 > 4).data, [False, True, True])

    def test_addition(self):
        is1 = IntegerSeries([3, 5, 10])
        is2 = IntegerSeries([1, None, 11])
        self.assertEqual((is1 + is2).data, [4, None, 21])

        fs1 = FloatSeries([3.0, None, 10.0])
        self.assertEqual((fs1 + 4.0).data, [7.0, None, 14.0])


class SeriesTestCases(unittest.TestCase):
    def test_factory(self):
        bs = series.factory(bool, [True, False, None], 'myBooleanSeries')
        self.assertIsInstance(bs, BooleanSeries)

    def test_eq(self):
        is1 = IntegerSeries([3, 5, 10])
        is2 = IntegerSeries([3, 8, 10])
        res = BooleanSeries([True, False, True])
        self.assertTrue(res.has_same_data(is1 == is2))

    def test_eq_with_single_value(self):
        is1 = IntegerSeries([3, 3, 5])
        self.assertEqual((is1 == 3).data, [True, True, False])


if __name__ == '__main__':
    unittest.main()
