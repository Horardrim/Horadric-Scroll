import unittest

from tests import *

if __name__ =='__main__':
    testsuite = unittest.TestLoader().discover('./tests')
    unittest.TextTestRunner(verbosity=1).run(testsuite)
