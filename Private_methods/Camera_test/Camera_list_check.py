import unittest, os, json, sys, re
from time import sleep
from utils.Logbug import LogBug
from utils.Log import Log
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Public_methods.PublicMethod import BasePage
from Private_methods.The_customer_list_test.customer_list_test import customerlist
from selenium.webdriver.common.keys import Keys
from Public_methods.Camera import RunMain
from selenium.webdriver.common.keys import Keys

logger = Log()
logbug = LogBug()
log_path = os.path.dirname(os.path.abspath('.')) + "\\Element_methods\\customer_list.json"
element = open(log_path, encoding='utf-8')
elements = json.load(element)

'''摄像头验证check相关'''


class Camera_list_check:

    '''进店设置check点'''
    '''进店设置-url地址check'''
    def jdsz_url(driver, newname):
        try:
            name = driver.current_url()
            if newname == name:
                logger.info(f'{sys._getframe().f_code.co_name},预期结果{newname}实际结果:{name}摄像头-进店设置-url地址对比正确')
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name},预期结果{newname}实际结果:{name}摄像头-进店设置-url地址对比错误')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头-进店设置-url地址查询异常')

    '''进店设置-功能说明 如：功能说明：进店设置支持对摄像头管理员、黑名单、进店提醒、进店分配、车型过滤。'''
    def jdsz_shezheshuoming(driver, mewname):
        try:
            name = driver.execupt_script(elements["进店设置-说明"])
            if mewname == name:
                logger.info(f'{sys._getframe().f_code.co_name},预期结果{mewname}实际结果:{name}摄像头-进店设置-功能说明对比正确')
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name},预期结果{mewname}实际结果:{name}摄像头-进店设置-功能说明对比正确')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头-进店设置-功能说明功能异常')















































































