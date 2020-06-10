from traceback import print_stack
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import *
import utilities.custom_logger as CL
import logging
from datetime import datetime
import os

class SeleniumDriver:

    log=CL.customLogger(logging.DEBUG)

    def __init__(self,driver):
        self.driver=driver

    def take_screenshot(self):
        now = datetime.now()
        filename = str(now.strftime('%Y%m%d%H%M%S'))+'.png'
        directory = '../screenshots/'
        relative_filename = directory + filename

        current_directory=os.path.dirname(__file__)

        destination_filename = os.path.join(current_directory,relative_filename)
        destination_directory = os.path.join(current_directory,directory)

        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_filename)
            self.log.info('Screenshot saved:' +destination_filename)
        except:
            self.log.error("Exception occurred while taking screenshot")
            print_stack()


    def get_by_type(self,locatortype):
        locatortype=locatortype.lower()
        if locatortype=='id':
            return By.ID
        elif locatortype=='name':
            return By.NAME
        elif locatortype=='xpath':
            return By.XPATH
        elif locatortype=='css':
            return By.CSS_SELECTOR
        elif locatortype=='classname' or locatortype=='class':
            return By.CLASS_NAME
        elif locatortype=='linktext' or locatortype=='link':
            return By.LINK_TEXT
        else:
            self.log.info('ERROR: Locator type ('+locatortype+
                          ') not correct / not supported')
            return False
#tutaj wcięłam to False, żeby było w warunku "else", hindi ma na równi

    def get_element(self,locator,locatortype='id'):
        element=None
        try:
            locatortype=locatortype.lower()
            bytype=self.get_by_type(locatortype)
            element=self.driver.find_element(bytype,locator)
            self.log.info('Element found: '+locator)
        except:
            self.log.info('Element not found: '+locator)
        return element

    def get_element_list(self,locator,locatortype='id'):
        '''
        Returns list of elements
        '''
        element=None
        try:
            bytype=self.get_by_type(locatortype)
            element=self.driver.find_elements(bytype,locator)
            self.log.info('Element list found: '+locator)
        except:
            self.log.info('Element list not found: '+locator)
        return element


    def clear_text_box_field(self, locator, locatortype="id", element=None):
        try:
            if locator:
                element = self.get_element(locator, locatortype)
            element.clear()
            self.log.info("Element cleared: " + locator)
        except:
            self.log.info("Cannot clear the element: " + locator)
            print_stack()

    def element_click(self, locator, locatortype='id',element=None):
        try:
            if locator: #is not empty
                element=self.get_element(locator,locatortype)
            element.click()
            self.log.info('Clicked on the element: '+locator)
        except:
            self.log.info(
                'Cannot click on the element: '+locator)
            print_stack()

    def element_send_keys(self, data, locator='', locatortype='id',element=None):
        try:
            if locator:
                element=self.get_element(locator,locatortype)
            element.send_keys(data)
            self.log.info('Sent data to the element: '+locator)
        except:
            self.log.info(
                'Cannot send data to the element: '+locator)
            print_stack()

    def get_text(self,locator='',locatortype='id',element=None):
        '''
        Get the element's text. e.g. if a button has text on it
        '''
        try:
            if locator:
                self.get_element(locator,locatortype)
            text=element.text
            if len(text)==0:
                self.log.debug('The length of the text is 0, element: '+locator)
            if len(text)!=0:
                self.log.info('Getting the text of the element: '+locator)
                self.log.info('The text is: "'+text+'"')
                text=text.strip()
        except:
            self.log.error('Failed to get the text from the element: '+locator)
            print_stack()
            text=None
        return text

    def is_element_present(self,locator,locatortype='id',element=None):
        try:
            if locator:
                element = self.get_element(locator,locatortype)
            if element is not None:
                self.log.info('Element found: '+locator)
                return True
            else:
                self.log.info('Element not present: '+locator)
                return False
        except:
            self.log.info('Element not found: '+locator)
            return False

    def element_presence_check(self,locator,bytype):
        try:
            elementlist = self.driver.find_elements(bytype,locator)
            if len(elementlist)>0:
                self.log.info('Element(s) found: '+locator)
                return True
            else:
                self.log.info('Element(s) not found: '+locator)
                return False
        except:
            self.log.info('Element(s) not found: '+locator)
            return False

    def wait_for_element(self,locator,locatortype='id',
                         timeout=10,poll_frequency=0.5):
        element=None
        try:
            bytype=self.get_by_type(locatortype)
            self.log.info('Waiting for maximum ::'+timeout+
                  ':: seconds for element to be clickable: '+locator)
            wait=WebDriverWait(self.driver,10,poll_frequency,
                               ignored_exceptions=[NoSuchElementException,
                                                   ElementNotVisibleException,
                                                   ElementNotSelectableException])
            element=wait.until(expected_conditions.element_to_be_clickable(
                bytype,locator))

            self.log.info('Element appeared on the web page: '+locator)
        except:
            self.log.info("Element didn't appear on the web page: "+locator)
            print_stack()
        return element

    def get_web_address(self):
        actualweb = self.driver.current_url
        self.log.info('Got to the web page: '+actualweb)
        return actualweb

    def get_title(self):
        actualtitle=self.driver.title
        self.log.info('Got to the web page: ' + actualtitle)
        return actualtitle

    def is_element_displayed(self,locator='',locatortype='id',element=None):
        is_it_displayed = False
        try:
            if locator:
                element=self.get_element(locator,locatortype)
            if locator is not None:
                is_it_displayed=element.is_displayed()
                self.log.info('Element is displayed: '+locator)
            else:
                self.log.info('Element not displayed: '+str(locator))
            return is_it_displayed
        except:
            self.log.info('Element not found: '+locator)
            return False

    def web_scroll(self,direction='up'):
        if direction.lower()=='up':
            self.driver.execute_script("window.scrollBy(0,-1000);")
        if direction.lower()=='down':
            self.driver.execute_script("window.scrollBy(0,1000)")
