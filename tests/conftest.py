import pytest
from base.webdriverfactory import WebDriverFactory
#from pages.home.login_page import LoginPage

@pytest.fixture()
def setUp():
    print('---- Starting the test.......')
    yield
    print('.......test finished.')

@pytest.fixture(scope='class')
def oneTimeSetUp(request, browser):
    print('STARTING THE TEST SESSION')
    factory=WebDriverFactory(browser)
    driver=factory.get_web_driver_instance()
    #lp=LoginPage(driver)
    #lp.login('dane@wp.pl','haslo1')
    # if we want to be logged in before every test!

    if request.cls is not None:
        request.cls.driver=driver


    yield driver
    print('TEST SESSION FINISHED')
    driver.quit()

def pytest_addoption(parser):
    parser.addoption('--browser')

@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption('--browser')
