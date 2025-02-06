import unittest
import logging
from functools import wraps

from ltcd.array import two_sum

logging.basicConfig(level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt = '%Y-%m-%d-%H:%M:%S')

class TestTwoSum(unittest.TestCase):
    def test_normal_case(self):
        result = two_sum.solution([1, 2, 3, 4, 5], 6)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], 1)
        self.assertEqual(result[1], 3)
