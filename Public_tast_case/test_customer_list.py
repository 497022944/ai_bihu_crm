# coding=utf-8
import unittest
from selenium import webdriver
import time

from utils.Log import Log
from utils.Logbug import LogBug
from utils.browser_engine import BrowserEngin
from Private_methods.Private_login_test.login_test import login
from Public_methods.New_offer_menu import menu
logger = Log()
logbug = LogBug()
#  读取配置文件

class Customer_Lict(unittest.TestCase):
    @classmethod
    def setUp(self):
        browser = BrowserEngin()
        self.driver = browser.open_browser()

    def test_customer_list_yanzheng1(self):
       menu1 = menu()
       menu1.Select_Menu_case(self.driver,'新增报价')

    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()