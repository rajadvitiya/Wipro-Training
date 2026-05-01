import sys
import unittest

from src.calculations import add, sub, mul, div, ne


class TestCalculations(unittest.TestCase):

    @unittest.skipIf(sys.version_info > (10, 13), reason='Not implemented yet')
    def test_add(self):
        res = add(10, 5)
        self.assertEqual(15, res, msg='Add Error')

    def test_sub(self):
        res = sub(10, 5)
        self.assertEqual(5,res,msg='Sub Error')


    def test_mul(self):
        res = mul(10, 5)
        self.assertEqual(50,res,msg='Mul Error')

    def test_div(self):
        res = div(10, 5)
        self.assertEqual(2.0,res,msg='Div Error')


    # def test_ne(self):
    #     res = ne(10, 100)
    #     self.assertTrue(res, msg='NE')

