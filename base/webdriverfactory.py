import traceback
from selenium import webdriver

class WebDriverFactory:

    def __init__(self,browser):
        '''
        inits WebDriverFactory class
        returns None
        :param browser:
        '''
        self.browser=browser

    def get_web_driver_instance(self):
        '''
        get WebDriver instance based on the browser configuration

        :return: 'WebDriver instance'
        '''
        if self.browser == None:
            driver = webdriver.Chrome()
            print('Running test on Chrome browser')
        elif self.browser.lower() == 'chrome':
            driver = webdriver.Chrome()
            print('Running test on Chrome browser')
        elif self.browser.lower() == 'ie' or self.browser.lower() == 'iexplorer':
            driver=webdriver.Ie()
            print('Running test on Internet Explorer browser')
        elif self.browser.lower() == 'firefox' or self.browser.lower() == 'ff':
            driver=webdriver.Firefox()
            print('Running test on Firefox browser')
        else:
            driver=webdriver.Chrome()
            print("RUNNING TEST ON CHROME BROWSER")

        homeurl = "https://www.zalando.pl/"
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(homeurl)

        return driver
