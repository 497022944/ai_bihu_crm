# coding=utf-8
import unittest
from selenium import webdriver
import time

from utils.Log import Log
from utils.browser_engine import BrowserEngin
from Private_methods.Private_login_test.login_test import login
from Public_methods.New_offer_menu import menu
from Private_methods.The_new_quotation_test.new_quotation_tset import new_quotation_case
from Private_methods.The_new_quotation_test.public_new_quotation import quotation_license
logger = Log()
#  说的读取配置文件

class Login(unittest.TestCase):
    @classmethod
    def setUp(self):
        browser = BrowserEngin()
        self.driver = browser.open_browser()

    #新增报价车牌
    def test01(self):
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')

        ##调用菜单
        menu1 = menu()
        menu1.Select_Menu_case(self.driver , '新增报价')
        #输入车牌
        quotation_license.quotation_license_input(self.driver, license='')
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1 = new_quotation_case()
        new_quotation_case1.license_check(self.driver, hint='请输入正确的车牌号')
        quotation_license.quotation_license_claer(self.driver)
    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()