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

log_path = os.path.dirname(os.path.abspath('.')) + "\\Element_methods\customer_list.json"
element = open(log_path, encoding='utf-8')
elements = json.load(element)
shot_path = os.path.dirname(os.path.abspath('.')) + "\\picture"
capturename = os.path.join(shot_path, time.strftime("%Y-%m-%d-%H_%M_%S") + '.png')
logger = Log()
logbug = LogBug()


class login:
    def login_input(driver, user = elements["Denglu_tast_account"], pwd = elements["Denglu_test_password"], code = elements["Denglu_test_verifycode"]):
        ActionChains(driver).double_click(driver.find_element_by_id(elements["Dengluzhanghao_id"])).perform()
        time.sleep(1)
        # driver.find_element_by_id(elements["Dengluzhanghao_id"]).send_keys(Keys.BACKSPACE)
        # driver.find_element_by_id(elements["Dengluzhanghao_id"]).clear()
        # time.sleep(1)
        driver.find_element_by_id(elements["Dengluzhanghao_id"]).send_keys(user)
        time.sleep(1)
        ActionChains(driver).double_click(driver.find_element_by_id(elements["Denglumima_id"])).perform()
        time.sleep(1)
        # driver.find_element_by_id(elements["Denglumima_id"]).send_keys(Keys.BACKSPACE)
        # driver.find_element_by_id(elements["Denglumima_id"]).clear()
        # time.sleep(1)
        driver.find_element_by_id(elements["Denglumima_id"]).send_keys(pwd)
        time.sleep(1)
        ActionChains(driver).double_click(driver.find_element_by_id(elements["Dengluyanzhengma_id"])).perform()
        time.sleep(1)
        # driver.find_element_by_id(elements["Dengluyanzhengma_id"]).clear()
        # driver.find_element_by_id(elements["Dengluyanzhengma_id"]).send_keys(Keys.BACKSPACE)
        # time.sleep(1)
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

    def login_check_errormsg(driver, hint):
        test = driver.find_element_by_class_name(elements["Denglu_errormessage_class"]).text
        if test == hint:
            logger.info("传值为:{}结果为:{}".format(hint, test))
            return True
        else:
            logbug.debug("传值为:{}结果为:{}".format(hint, test))
            return False

    def login_check_success(driver):
        if driver.find_element_by_css_selector(
                elements["Denglu_success_dropdown_css"]).text == elements["Denglu_success_dropdown_check_text"]:
            logger.info("{}登录成功".format(elements["Denglu_tast_account"]))
            return True
        else:
            logbug.debug("{}登录失败".format(elements["Denglu_tast_account"]))
            return False
