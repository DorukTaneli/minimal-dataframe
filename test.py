import unittest
from series import StringSeries, BooleanSeries, IntegerSeries, FloatSeries


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

        self.assertEqual(ss1, ss2)
        self.assertNotEqual(ss1, ss3)
        self.assertNotEqual(ss1, ss4)


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

        self.assertEqual(bs1, bs2)
        self.assertNotEqual(bs1, bs3)
        self.assertNotEqual(bs1, bs4)

    def test_BooleanSeries_invert(self):
        bs1 = BooleanSeries([True, False, False])
        bs2 = BooleanSeries([False, True, True])
        bs3 = BooleanSeries([True, None, False])
        bs4 = BooleanSeries([False, None, True])

        self.assertEqual(bs1, ~bs2)
        self.assertEqual(bs3, ~bs4, msg='bs3:{} bs4:{} ~bs4:{}'.format(bs3, bs4, ~bs4))


class IntegerSeriesTestCases(unittest.TestCase):
    def test_greaterThan(self):
        is1 = IntegerSeries([3, 5, 10])
        is2 = IntegerSeries([5, 10])
        self.assertEqual(is1 > 4, is2, msg=is1 > 4)


class FloatSeriesTestCases(unittest.TestCase):
    def test_greaterThan(self):
        is1 = FloatSeries([3.0, 5.0, 10.0])
        is2 = FloatSeries([5.0, 10.0])
        self.assertEqual(is1 > 4.0, is2, msg=is1 > 4.0)


if __name__ == '__main__':
    unittest.main()
