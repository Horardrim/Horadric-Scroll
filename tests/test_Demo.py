import unittest

from algo import demo

class TestDemo(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(demo.add(2, 2), 4)
