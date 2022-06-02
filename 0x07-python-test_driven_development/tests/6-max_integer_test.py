#!/usr/bin/python3

"""Max integer - Unittest"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Tests cases"""

def test_max_integer(self):
    list = [0, 1, 2, 3]
    self.assertEqual(max_integer(list), 3)

def test_max_end(self):
    list = [1, 4, 8, 20, 35]
    self.assertEqual(max_integer(list), 35)

def test_max_beginning(self):
    list = [65, 56, 43, 22]
    self.assertEqual(max_integer(list), 65)

def test_max_middle(self):
    list = [4, 6, 45, 12, 32]
    self.assertEqual(max_integer(list), 45)

def test_max_one_negative(self):
    list = [1, -6, 6, 8, 18]
    self.assertEqual(max_integer(list), 18)

def test_max_only_negative(self):
    list = [-12, -45, -34, -5, -1]
    self.assertEqual(max_integer(list), -1)

def test_max_one_element(self):
    list = [10]
    self.assertEqual(max_integer(list), 10)

def test_max_empty(self):
    list = []
    self.assertEqual(max_integer(list), None)
