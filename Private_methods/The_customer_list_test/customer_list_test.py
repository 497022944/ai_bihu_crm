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


class customerlist:
    def customer_list_tab_select(driver,select_tab):
        if select_tab == '当期客户':
            try:
                driver.find_elements_by_css_selector(elements["kehuliebiao_tab_css"])[0].click()
                logger.info(f"{select_tab} 打开成功")
            except Exception:
                logbug.debug(f"{select_tab} 打开失败")

        elif select_tab == '首访客户':
            try:
                driver.find_elements_by_css_selector(elements["kehuliebiao_tab_css"])[1].click()
                logger.info(f"{select_tab} 打开成功")
            except Exception:
                logbug.debug(f"{select_tab} 打开失败")

        elif select_tab == '未回访':
            try:
                driver.find_elements_by_css_selector(elements["kehuliebiao_tab_css"])[2].click()
                logger.info(f"{select_tab} 打开成功")
            except Exception:
                logbug.debug(f"{select_tab} 打开失败")

        elif select_tab == '计划回访':
            try:
                driver.find_elements_by_css_selector(elements["kehuliebiao_tab_css"])[3].click()
                logger.info(f"{select_tab} 打开成功")
            except Exception:
                logbug.debug(f"{select_tab} 打开失败")

        elif select_tab == '今日到店':
            try:
                driver.find_elements_by_css_selector(elements["kehuliebiao_tab_css"])[4].click()
                logger.info(f"{select_tab} 打开成功")
            except Exception:
                logbug.debug(f"{select_tab} 打开失败")

        elif select_tab == '预约进店':
            try:
                driver.find_elements_by_css_selector(elements["kehuliebiao_tab_css"])[5].click()
                logger.info(f"{select_tab} 打开成功")
            except Exception:
                logbug.debug(f"{select_tab} 打开失败")

        elif select_tab == '逾期客户':
            try:
                driver.find_elements_by_css_selector(elements["kehuliebiao_tab_css"])[6].click()
                logger.info(f"{select_tab} 打开成功")
            except Exception:
                logbug.debug(f"{select_tab} 打开失败")

        elif select_tab == '全部客户':
            try:
                driver.find_elements_by_css_selector(elements["kehuliebiao_tab_css"])[7].click()
                logger.info(f"{select_tab} 打开成功")
            except Exception:
                logbug.debug(f"{select_tab} 打开失败")
        else:
            pass


    def search_chepai(driver,input_chepai = elements["test_licenseno"]):
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_dropdown_css"]).click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo1_dropdown_selection_css"])[0].click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_textbox_css"]).send_keys(input_chepai)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_button_css"]).click()
            time.sleep(1)
            logger.info(f'{input_chepai} 搜索成功')
        except Exception:
            logbug.debug(f'{input_chepai} 搜索失败')

    def search_chejia(driver,input_chejia = elements["test_vin"]):
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_dropdown_css"]).click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo1_dropdown_selection_css"])[0].click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_textbox_css"]).send_keys(input_chejia)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_button_css"]).click()
            time.sleep(1)
            logger.info(f'{input_chejia} 搜索成功')
        except Exception:
            logbug.debug(f'{input_chejia} 搜索失败')


    def search_chezhuxingming(driver,input_chezhuxingming = elements["test_chezhuxingming"]):
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_dropdown_css"]).click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo1_dropdown_selection_css"])[1].click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_textbox_css"]).send_keys(input_chezhuxingming)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_button_css"]).click()
            time.sleep(1)
            logger.info(f'{input_chezhuxingming} 搜索成功')
        except Exception:
            logbug.debug(f'{input_chezhuxingming} 搜索失败')

    def search_kehumingcheng(driver,input_kehumingcheng = elements["test_kehumingcheng"]):
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_dropdown_css"]).click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo1_dropdown_selection_css"])[2].click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_textbox_css"]).send_keys(input_kehumingcheng)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_button_css"]).click()
            time.sleep(1)
            logger.info(f'{input_kehumingcheng} 搜索成功')
        except Exception:
            logbug.debug(f'{input_kehumingcheng} 搜索失败')

    def search_kehudianhua(driver, input_kehudianhua=elements["test_kehudianhua1"]):
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_dropdown_css"]).click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo1_dropdown_selection_css"])[3].click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_textbox_css"]).send_keys(
                input_kehudianhua)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_button_css"]).click()
            time.sleep(1)
            logger.info(f'{input_kehudianhua} 搜索成功')
        except Exception:
            logbug.debug(f'{input_kehudianhua} 搜索失败')

    def search_daoqishijian(driver, input_daoqishijian=elements["test_kehudianhua1"]):
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo2_daoqishijian_css"]).click()
            time.sleep(1)
            logger.info(f'{input_daoqishijian} 搜索成功')
        except Exception:
            logbug.debug(f'{input_daoqishijian} 搜索失败')


