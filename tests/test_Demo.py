import unittest
import logging
from functools import wraps

from algo import demo

logging.basicConfig(level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt = '%Y-%m-%d-%H:%M:%S')

class TestDemo(unittest.TestCase):

    def _test_decorator(test_func):
        @wraps(test_func)
        def decorator(args):
            logging.info(test_func.__name__ + " started...")
            return test_func(args)

        return decorator

    @_test_decorator
    def test_normal_case(self):
        self.assertEqual(demo.add(2, 2), 4)
