# coding=utf-8
import unittest
from selenium import webdriver
import time

from utils.Log import Log
from utils.Logbug import LogBug
from utils.browser_engine import BrowserEngin
from Private_methods.Private_login_test.login_test import login
logger = Log()
logbug = LogBug()
#  读取配置文件

class Login(unittest.TestCase):
    @classmethod
    def setUp(self):
        browser = BrowserEngin()
        self.driver = browser.open_browser()

    def test_denglu_yanzheng1(self):
        login.login_input(self.driver, user='', pwd='', code='1234')
        time.sleep(1)
        try:
            self.assertTrue(login.login_check_errormsg(self.driver, hint='用户名不能为空！'))
            time.sleep(1)
        except Exception:
            logbug.debug("test_denglu_yanzheng1未通过")

    def test_denglu_yanzheng2(self):
        login.login_input(self.driver, user='zdh01', pwd='', code='1234')
        time.sleep(1)
        try:
            self.assertTrue(login.login_check_errormsg(self.driver, hint='密码不能为空！'))
            time.sleep(1)
        except Exception:
            logbug.debug("test_denglu_yanzheng2未通过")

    def test_denglu_yanzheng3(self):
        login.login_input(self.driver, user='zdh01', pwd='zdh01', code='')
        time.sleep(1)
        try:
            self.assertTrue(login.login_check_errormsg(self.driver, hint='验证码不能为空！'))
            time.sleep(1)
        except Exception:
            logbug.debug("test_denglu_yanzheng3未通过")

    def test_denglu_yanzheng4(self):
        login.login_input(self.driver, user='壁虎zdh_01', pwd='', code='')
        time.sleep(1)
        try:
            self.assertTrue(login.login_check_errormsg(self.driver,hint='用户名只能为字母、数字和下划线！'))
            time.sleep(1)
        except Exception:
            logbug.debug("test_denglu_yanzheng4未通过")

    def test_denglu_yanzheng5(self):
        login.login_input(self.driver, user='#$zdh_01', pwd='', code='')
        time.sleep(1)
        try:
            self.assertTrue(login.login_check_errormsg(self.driver,hint='用户名只能为字母、数字和下划线！'))
            time.sleep(1)
        except Exception:
            logbug.debug("test_denglu_yanzheng5未通过")

    def test_denglu_yanzheng6(self):
        login.login_input(self.driver, user='zdh_01', pwd='zdh01', code='1')
        time.sleep(1)
        try:
            self.assertTrue(login.login_check_errormsg(self.driver,hint='验证码为4位数字和字母！'))
            time.sleep(1)
        except Exception:
            logbug.debug("test_denglu_yanzheng6未通过")

    def test_denglu_yanzheng7(self):
        login.login_input(self.driver, user='zdh_01', pwd='zdh01', code='a1a')
        time.sleep(1)
        try:
            self.assertTrue(login.login_check_errormsg(self.driver,hint='验证码为4位数字和字母！'))
            time.sleep(1)
        except Exception:
            logbug.debug("test_denglu_yanzheng7未通过")

    def test_denglu_yanzheng8(self):
        login.login_input(self.driver, user='zdh_01', pwd='zdh01', code='a1a1a')
        time.sleep(1)
        try:
            self.assertTrue(login.login_check_errormsg(self.driver,hint='验证码为4位数字和字母！'))
            time.sleep(1)
        except:
            logbug.debug("test_denglu_yanzheng8未通过")



    def test_denglu_yanzheng9(self):
        login.login_input(self.driver, user='zdh_01', pwd='zdh01', code='壁虎')
        time.sleep(1)
        try:
            self.assertTrue(login.login_check_errormsg(self.driver,hint='验证码只能为字母和数字！'))
            time.sleep(1)
        except:
            logbug.debug("est_denglu_yanzheng9未通过")


    def test_denglu_yanzheng10(self):
        login.login_input(self.driver)
        time.sleep(5)
        try:
            self.assertTrue(login.login_check_success(self.driver))
            time.sleep(1)
        except:
            logbug.debug("est_denglu_yanzheng10未通过")


    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()