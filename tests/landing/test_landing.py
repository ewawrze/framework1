import unittest
from pages.landing.landing_page import LandingPage
import pytest


@pytest.mark.usefixtures('setUp','oneTimeSetUp')
class TestLanding(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self,oneTimeSetUp):
        self.lanp = LandingPage(self.driver)

    @pytest.mark.run
    def test_environmental(self):
        env_result = self.lanp.verify_environmental()
        assert env_result == True
