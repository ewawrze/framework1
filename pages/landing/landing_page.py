import logging
import time

import utilities.custom_logger as CL
from base.basepage import BasePage


class LandingPage(BasePage):
    # it inherited from SeleniumDriver class.
    # if we want to use base.basepage - all web classes should inherit
    # from basepage. Basepage already inherits fromSeleniumDriver class!

    log = CL.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

#Locators
    _promotions = "//span[contains(text(),'Promocje %')]" #xpath
    _environmental = "//span[contains(text(),'Przyjazno')]" #xpath

#Actions
    def click_promotions(self):
        self.element_click(self._promotions,'xpath')

    def find_environmental(self):
        time.sleep(5)
        return self.is_element_present(self._environmental,'xpath')

#Methods
    def verify_environmental(self):
        try:
            self.click_promotions()
            time.sleep(5)
        except:
            self.take_screenshot()
            time.sleep(5)
        self.find_environmental()
        if self.find_environmental() is None or self.find_environmental() is False:
            self.take_screenshot()
        return self.find_environmental()