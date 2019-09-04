# coding=utf-8
import unittest
from selenium import webdriver
import time

from utils.Log import Log
from utils.browser_engine import BrowserEngin
from Private_methods.Private_login_test.login_test import login
logger = Log()
#  读取配置文件

class Login(unittest.TestCase):
    @classmethod
    def setUp(self):
        browser = BrowserEngin()
        self.driver = browser.open_browser()

    def test01(self):
        #  pass
        #  只输入电话号码为123，验证码为空
        #  login(self.driver,phone='123',verify="")
        #login.login(self.driver)h
        login.login_input(self.driver, user='', pwd='', code='1234')
        time.sleep(1)
        login.login_check(self.driver, hint='用户名不能为空！')
        time.sleep(1)
    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()