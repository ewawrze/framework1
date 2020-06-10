import unittest
from tests.home.test_login import TestLogin
from tests.landing.test_landing import TestLanding

# #get all tests from the test classes
# test_1 = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
# test_2 = unittest.TestLoader().loadTestsFromTestCase(TestLanding)
#
# #create test suite combining the classes
# smoke_test = unittest.TestSuite([test_1,test_2])
#
# unittest.TextTestRunner(verbosity=2).run(smoke_test)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestLogin())
    suite.addTest(TestLanding())
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())