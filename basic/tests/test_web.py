import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestSignup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://chrome:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)

    def test_signup_fire(self):
        self.driver.get('http://taskit:8000/basic/login')
        # print self.driver.page_source.encode("utf-8")
        login = self.driver.find_element_by_id('login')
        print login

    def tearDown(self):
        self.driver.quit

if __name__ == '__main__':
    unittest.main()
