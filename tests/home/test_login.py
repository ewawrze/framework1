import unittest
from pages.home.login_page import LoginPage
import pytest
import time
from ddt import ddt,data,unpack
from utilities.read_data import get_csv_data


@pytest.mark.usefixtures('setUp','oneTimeSetUp')
@ddt
class TestLogin(unittest.TestCase):
# Zapewniają one stały punkt odniesienia, tak aby wykonać testy
# i niezawodnie produkować spójne i powtarzalne wyniki.
# Fixture może skonfigurować usługi, stan początkowy
# lub inne środowiska operacyjne.


    @pytest.fixture(autouse=True)
    def classSetUp(self,oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.lp.accept_cookies_click_login()

    @pytest.mark.run(order=1)
    @data(*get_csv_data("C:/Users/wrzes/Desktop/testowanie_z_hindusem/testingframework1/testdata.csv"))
    @unpack
    def test_validlogin(self,email,password):

        self.lp.login(email, password)
        logging_result=self.lp.verify_successful_logging_in()
        assert logging_result==True

    @pytest.mark.run(order=2)
    def test_valid_account(self):
        logging_error1 = self.lp.verify_account_error()
        assert logging_error1==False

    @pytest.mark.run(order=3)
    def test_valid_email(self):
        logging_error2=self.lp.verify_email_error()
        assert logging_error2==False

    @pytest.mark.run(order=4)
    def test_valid_password(self):
        logging_error3 = self.lp.verify_password_error()
        assert logging_error3 == False or logging_error3 is None

    @pytest.mark.run(order=5)
    def test_valid_landingpage(self):
        time.sleep(5)
        current_address=self.lp.get_web_address()
        wanted_address="https://www.zalando.pl/myaccount/"
        assert wanted_address in current_address

    @pytest.mark.run(order=6)
    def test_valid_title(self):
        title_check = self.lp.verify_title()
        assert title_check == True