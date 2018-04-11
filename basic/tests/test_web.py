import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestLoginTemplate(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://chrome:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)

    def test_login_template(self):
        self.driver.get('http://taskit:8000/basic/login')
        login = self.driver.find_element_by_id('login')
        signup = self.driver.find_element_by_id('signup')
        reset_password = self.driver.find_element_by_id('reset_password')
        self.assertIsNotNone(login)
        self.assertIsNotNone(signup)
        self.assertIsNotNone(reset_password)

    def tearDown(self):
        self.driver.quit
