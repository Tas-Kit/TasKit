import unittest

from selenium import webdriver
from django.urls import reverse
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestLoginTemplate(unittest.TestCase):
    pass
    # @classmethod
    # def setUpClass(cls):
    #     cls.driver = webdriver.Remote(
    #         command_executor='http://chrome:4444/wd/hub',
    #         desired_capabilities=DesiredCapabilities.CHROME)

    # def setUp(self):
    #     self.base_url = 'http://taskit:8000'
    #     self.username = 'testclient'
    #     self.password = 'password'
    #     self.driver = self.__class__.driver

    # def test_login_template(self):
    #     self.driver.get(self.base_url + reverse('basic:login'))
    #     login = self.driver.find_element_by_id('login')
    #     signup = self.driver.find_element_by_id('signup')
    #     reset_password = self.driver.find_element_by_id('reset_password')
    #     self.assertIsNotNone(login)
    #     self.assertIsNotNone(signup)
    #     self.assertIsNotNone(reset_password)

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()
