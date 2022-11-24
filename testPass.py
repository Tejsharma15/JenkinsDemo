#!/usr/bin/python3
import unittest
from program import isOdd
class TestCase(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(isOdd(1), 1)
    def testcase2(self):
        self.assertEqual(isOdd(5), 1)
    def testcase3(self):
        self.assertEqual(isOdd(87), 1)
if __name__ == '__main__':
    unittest.main()
