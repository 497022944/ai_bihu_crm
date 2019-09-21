# coding=utf-8
import unittest
from selenium import webdriver
import time

from utils.Log import Log
from utils.Logbug import LogBug
from utils.browser_engine import BrowserEngin
from Private_methods.Private_login_test.login_test import login
from Public_methods.New_offer_menu import menu
from Private_methods.The_customer_list_test.customer_list_test import customerlist
logger = Log()
logbug = LogBug()
#  读取配置文件

class Customer_Lict(unittest.TestCase):
    @classmethod
    def setUp(self):
        browser = BrowserEngin()
        self.driver = browser.open_browser()

    def test_customer_list_tab(self):
        login.login_input(self.driver)
        time.sleep(5)
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        time.sleep(5)
        customerlist.customer_list_tab_select(self.driver,'全部客户')
        time.sleep(2)
        customerlist.search_1_0_chepai_gotofirst_detail(self.driver, '京J97896')
        time.sleep(2)
        customerlist.kehuxiangqing_guanxirenxinxi_chezhuxinxi_tongtoubaoren(self.driver,'同投保人')
        time.sleep(2)
        # customerlist.kehuxiangqing_baojiaxinxi_xiuliqijianfeiyongbuchang(self.driver,1,100,2)
        time.sleep(2)
        # self.driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
        # time.sleep(1)
        # customerlist.test_search(self.driver)
        # time.sleep(2)




    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()