import unittest

from algo import demo

class test_Demo(unittest.TestCase):
    def normal_test(self):
        self.assertEqual(demo.add(2, 2), 4)
