#!/usr/bin/python3
"""unittest state"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """unittest"""
    def setUp(self):
        s = State()

    def testName(self):
        self.assertEqual(s.name, "")
