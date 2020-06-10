import logging
import time

from selenium.webdriver import ActionChains

import utilities.custom_logger as CL
from base.basepage import BasePage


class LoginPage(BasePage):
    # it inherited from SeleniumDriver class.
    # if we want to use base.basepage - all web classes should inherit
    # from basepage. Basepage already inherits fromSeleniumDriver class!

    log = CL.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    _loginlink = "//span[contains(text(),'Zaloguj się')]"  # xpath
    _emailfield = "login.email"  # id
    _cookiebutton = "uc-btn-accept-banner"  # id
    _passwordfield = "login.password"  # id
    _loginbutton = "//button[contains(text(),'Zaloguj się')]"  # xpath

    _loggedinbanner = "//span[contains(text(),'Moje konto')]"  # xpath

    # Actions
    def click_loginlink(self):
        self.element_click(self._loginlink, 'xpath')

    def enter_email(self, email):
        self.element_send_keys(email, self._emailfield, 'id')

    def click_cookiebutton(self):
        self.element_click(self._cookiebutton, 'id')

    def enter_password(self, password):
        # self.get_element(self._passwordfield,'id').clear()
        self.element_send_keys(password, self._passwordfield, 'id')

    def click_loginbutton(self):
        self.element_click(self._loginbutton, 'xpath')

    # Final action in just 1 method

    def accept_cookies_click_login(self):
        time.sleep(5)
        try:
            self.get_element(self._cookiebutton, 'id')
            self.click_cookiebutton()
        except:
            pass
        self.click_loginlink()

    def login(self, email='', password=''):
        time.sleep(5)
        self.clear_text_box_field(self._emailfield)
        self.enter_email(email)
        time.sleep(3)
        self.clear_text_box_field(self._passwordfield)
        self.enter_password(password)
        self.click_loginbutton()

    def verify_successful_logging_in(self):
        result = self.is_element_present(self._loggedinbanner, 'xpath')
        if result == False:
            self.take_screenshot()
        return result

    def verify_account_error(self):
        result = self.is_element_present(
            "//div[@data-testid='login_error_notification']//span[contains(text(),'Coś poszło nie tak')]",
            'xpath')
        if result == True:
            self.take_screenshot()
        return result

    def verify_email_error(self):
        emailerror = self.is_element_present("//span[contains(text(),'Podaj pełny adres')]",
                                             'xpath')
        if emailerror == True:
            self.take_screenshot()
        return emailerror

    def verify_password_error(self):
        passworderror = self.is_element_present(
            "//div[@class='reef-zds_alert reef-zds_error']", 'xpath')
        if passworderror == True:
            self.take_screenshot()
            return True
        return False

    def logout_method(self):
        logout_menu = self.get_element(
            "//a[@href='/myaccount/']//span[contains(text(),'Moje konto')]", 'xpath')
        logout_button = self.get_element(
            "//a[@href='/logout/']")

        mousehover = ActionChains(self.driver)
        mousehover.move_to_element(logout_menu).perform()
        time.sleep(1)
        mousehover.move_to_element(logout_button).click().perform()

    def verify_title(self):
        if "Moje konto" in self.get_title():
            return True
        else:
            self.take_screenshot()
            return False

# Other idea to define locators (with them the method would be different
#
# def get_loginlink(self):
#     return self.driver.find_element(By.XPATH, self._loginlink)
#
# def get_emailfield(self):
#     return self.driver.find_element(By.ID, self._emailfield)
#
# def get_cookiebutton(self):
#     return self.driver.find_element(By.ID, self._cookiebutton)
#
# def get_passwordfield(self):
#     return self.driver.find_element(By.ID, self._passwordfield)
#
# def get_loginbutton(self):
#     return self.driver.find_element(By.XPATH, self._loginbutton)
