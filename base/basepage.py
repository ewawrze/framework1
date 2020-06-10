"""
@package base

Base Page class implementation
It implements methods which are common to all the pages throughout the application

This class needs to be inherited by all the page classes
This should not be used by creating object instances

Example:
    Class LoginPage(BasePage)
"""
from base.selenium_driver import SeleniumDriver
from utilities.util import Util
from traceback import print_stack


class BasePage(SeleniumDriver):

    def __init__(self, driver):

        super(BasePage,self).__init__(driver) # =super().__init__(driver)
        self.driver=driver
        self.util=Util()

    def verify_page_title(self,title_to_verify):
        '''
        Verify the page Title

        :param title_to_verify: Title on the page that needs to be verified
        :return: bool
        '''
        try:
            actual_title=self.get_title()
            return self.util.verify_text_contains(title_to_verify,actual_title)
        except:
            self.log.error('Failed to get page title!')
            print_stack()
            return False