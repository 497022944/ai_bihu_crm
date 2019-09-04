from utils.getConfig import *
from utils.Log import Log
from utils.Logbug import LogBug
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import json
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import datetime
from selenium.webdriver.support.ui import Select
from Public_methods.PublicMethod import BasePage

log_path = os.path.dirname(os.path.abspath('.')) + "\\Element_methods\login.json"
element = open(log_path, encoding='utf-8')
elements = json.load(element)
shot_path = os.path.dirname(os.path.abspath('.')) + "\\picture"
capturename = os.path.join(shot_path, time.strftime("%Y-%m-%d-%H_%M_%S") + '.png')
logger = Log()
logbug = LogBug()


class login:
    def login_input(driver, user, pwd, code):
        ActionChains(driver).double_click(driver.find_element_by_id(elements["Dengluzhanghao_id"])).perform()
        time.sleep(1)
        driver.find_element_by_id(elements["Dengluzhanghao_id"]).send_keys(user)
        time.sleep(1)
        ActionChains(driver).double_click(driver.find_element_by_id(elements["Denglumima_id"])).perform()
        time.sleep(1)
        driver.find_element_by_id(elements["Denglumima_id"]).send_keys(pwd)
        time.sleep(1)
        ActionChains(driver).double_click(driver.find_element_by_id(elements["Dengluyanzhengma_id"])).perform()
        time.sleep(1)
        driver.find_element_by_id(elements["Dengluyanzhengma_id"]).send_keys(code)
        time.sleep(1)
        driver.find_element_by_css_selector(elements["Denglu_anniu_css"]).click()
        time.sleep(1)

    def login_clear(driver):
        driver.find_element_by_id(elements["Dengluzhanghao_id"]).clear()
        time.sleep(1)
        driver.find_element_by_id(elements["Denglumima_id"]).clear()
        time.sleep(1)
        driver.find_element_by_id(elements["Dengluyanzhengma_id"]).clear()
        time.sleep(1)

    def login_check(self, driver, hint):
        try:
            test = driver.find_element_by_class_name(elements["Denglu_errormessage_class"]).text
        except Exception:
            print("异常内容.")
        else:

            if hint == test:
                logger.info("传值为:{}结果为:{}".format(hint,test))
                return True
            else:
                logbug.debug("传值为:{}结果为:{}".format(hint,test))
                return test

