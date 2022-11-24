#!/usr/bin/python3
import unittest
from program import isOdd
class TestCase(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(isOdd(4), 1)
    def testcase2(self):
        self.assertEqual(isOdd(6), 1)
    def testcase3(self):
        self.assertEqual(isOdd(86), 1)

if __name__ == '__main__':
    unittest.main()
