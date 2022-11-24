#!/usr/bin/python3
import unittest
from program import odd
class TestCase(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(odd(1), 1)
    def testcase2(self):
        self.assertEqual(odd(5), 1)
    def testcase3(self):
        self.assertEqual(odd(87), 1)
