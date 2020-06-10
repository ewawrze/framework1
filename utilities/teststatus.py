
# The super() builtin returns a proxy object
# (temporary object of the superclass) that allows us
# to access methods of the base class. In Python, super()
# has two major use cases: allows us to avoid using
# the base class name explicitly and
# working with Multiple Inheritance

# super is used to call the constructor , methods
# and properties of parent class. You may also use the super
# keyword in the sub class when you want to invoke a method
# from the parent class when you have overridden it in
# the subclass

import logging
from base.selenium_driver import SeleniumDriver
from utilities import custom_logger


class TestStatus(SeleniumDriver):

    log = custom_logger.customLogger(logging.INFO)

    def __init__(self,driver):
        '''
        Inits checkpoint class
        Result list keeps track of all the results
        '''
        super(TestStatus,self).__init__(driver)
        self.result_list=[]

    def set_result(self,result,result_message):
        try:
            if result is not None:
                if result is True:
                    self.result_list.append('PASS')
                    self.log.info("VERIFICATION SUCCESSFUL: "+result_message)
                else:
                    self.result_list.append('FAIL')
                    self.log.error('VERIFICATION FAILED: '+result_message)
            else:
                self.result_list.append("FAIL")
                self.log.error('EXCEPTION OCCURRED: '+result_message)
        except:
            self.result_list.append('FAIL')
            self.log.error(' ---- EXCEPTION OCCURED! ---- ')


    def mark(self,result,result_message):
        '''
        Mark the result of the verification point in a test case
        '''
        self.set_result(result,result_message)


    def mark_final(self,test_name,result,result_message):
        '''
        Mark the final result of the verification point
        in a test case. Must be called at least once in a test case
        and should be a final test status of a test case.
        '''
        self.set_result(result,result_message)

        if 'FAIL' in self.result_list:
            self.log.error(test_name+' TEST FAILED: ')
            self.result_list.clear()
            assert True == False
        else:
            self.log.info(test_name+' TEST SUCCESSFUL ')
            self.result_list.clear()
            assert True == True

