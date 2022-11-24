#!/usr/bin/python3
import unittest
from program import prog
class TestCase(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(prog(4), 1)
    def testcase2(self):
        self.assertEqual(prog(6), 1)
    def testcase3(self):
        self.assertEqual(prog(86), 1)
