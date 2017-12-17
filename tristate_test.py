#!/usr/bin/env python3
"""Questo modulo contiene i test di Unittest per tristate.py"""

__author__ = 'Marco Garipoli marcuslxxii@gmail.com'

# self.assertEqual(func(arg1, arg2), result)  # func(arg1, arg2)==result
# self.assertNotEqual(func(arg1, arg2), result)  # func(arg1, arg2)!=result
# self.assertCountEqual  #Quando il confronto è tra liste con più di 1 elemento
# self.assertMultiLineEqual  #Quando il confronto è fra str
# self.assertTrue(func(arg1, arg2))  # bool(func(arg1, arg2)) is True
# self.assertFalse(func(arg1, arg2))  # bool(func(arg1, arg2)) is False
# self.assertIs(func(arg1, arg2), result)  # func(arg1, arg2) is result
# self.assertIsNot(func(arg1, arg2), result)  # func(arg1, arg2) is not result
# self.assertIsNone(func(arg1, arg2))  # func(arg1, arg2) is None
# self.assertIsNotNone(func(arg1, arg2))  # func(arg1, arg2) is not None
# self.assertIn(func(arg1, arg2), result)  # func(arg1, arg2) in result
# self.assertNotIn(func(arg1, arg2), result)  # func(arg1, arg2) not in result
# self.assertIsInstance(func(arg1), result)  # isinstance(func(arg1), result)
# self.assertNotIsInstance(func(arg1), res)  # not isinstance(func(arg1), res)
# with self.assertRaises(ValueError):  #Inserire al suo interno il codice che
#                                      #deve dare l'errore specificato
# with self.assertRaisesRegex(ValueError, "invalid literal for.*XYZ'$",
#                             int, 'XYZ'):
# with self.assertWarns(SomeWarning):
# with self.assertWarnsRegex(RuntimeWarning, 'unsafe frobnicating'):

import unittest
from tristate import Tristate


# Python 2/3 compatibility
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class TestTristate(unittest.TestCase):
    
    v = Tristate(True)
    f = Tristate(False)
    n = Tristate()  # equivalente a n = Tristate(None)
    
    def test_base(self):
        self.assertEqual(self.v, self.v)
        self.assertEqual(self.v, True)
        self.assertEqual(self.v, 1)
        self.assertEqual(self.n, 0)
        self.assertEqual(self.f, -1)
        self.assertEqual(self.n, None)
        self.assertEqual(self.n, Tristate(None))
        self.assertEqual(self.v.isknown(), True)
        self.assertEqual(self.n.isunknown(), True)
        self.assertEqual(self.v.isfalse(), False)
        self.assertNotEqual(self.v, self.f)
        self.assertNotEqual(self.v, self.n)
        self.assertNotEqual(self.n, self.f)
    
    def test_not_1(self):
        self.assertEqual(self.v.not_(), False)
        self.assertEqual(self.f.not_(), True)
        self.assertEqual(self.n.not_(), None)
    
    def test_not_2(self):
        self.assertEqual(self.v.not_(), self.f)
        self.assertEqual(self.f.not_(), self.v)
        self.assertEqual(self.n.not_(), self.n)
    
    def test_and_1(self):
        s = [self.f, self.v, self.n]
        ris = [False, False, False, False, True, None, False, None, None]
        i = 0
        for a in s:
            for b in s:
                #print('{} and {} = {}'.format(a, b, a & b))
                self.assertEqual(a & b, ris[i])
                i += 1
    
    def test_and_2(self):
        s = [self.f, self.v, self.n]
        ris = [self.f, self.f, self.f, self.f, self.v, self.n, self.f, self.n,
               self.n]
        i = 0
        for a in s:
            for b in s:
                #print('{} and {} = {}'.format(a, b, a & b))
                self.assertEqual(a & b, ris[i])
                i += 1
    
    def test_or_1(self):
        s = [self.f, self.v, self.n]
        ris = [False, True, None, True, True, True, None, True, None]
        i = 0
        for a in s:
            for b in s:
                #print('{} or {} = {}'.format(a, b, a | b))
                self.assertEqual(a | b, ris[i])
                i += 1
    
    def test_or_2(self):
        s = [self.f, self.v, self.n]
        ris = [self.f, self.v, self.n, self.v, self.v, self.v, self.n, self.v,
               self.n]
        i = 0
        for a in s:
            for b in s:
                #print('{} or {} = {}'.format(a, b, a | b))
                self.assertEqual(a | b, ris[i])
                i += 1
    
    def test_xor_1(self):
        s = [self.f, self.v, self.n]
        ris = [False, True, None, True, False, None, None, None, None]
        i = 0
        for a in s:
            for b in s:
                #print('{} xor {} = {}'.format(a, b, a ^ b))
                self.assertEqual(a ^ b, ris[i])
                i += 1
    
    def test_xor_2(self):
        s = [self.f, self.v, self.n]
        ris = [self.f, self.v, self.n, self.v, self.f, self.n, self.n, self.n,
               self.n]
        i = 0
        for a in s:
            for b in s:
                #print('{} xor {} = {}'.format(a, b, a ^ b))
                self.assertEqual(a ^ b, ris[i])
                i += 1
    
    def test_imp(self):
        s = [self.f, self.v, self.n]
        ris = [self.v, self.v, self.v, self.f, self.v, self.n, self.n, self.v,
               self.n]
        i = 0
        for a in s:
            for b in s:
                #print('{} xor {} = {}'.format(a, b, a ^ b))
                self.assertEqual(a.imp(b), ris[i])
                i += 1
    


if __name__ == '__main__':
    unittest.main()
