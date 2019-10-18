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
log_path = os.path.dirname(os.path.abspath('.')) + "\\Element_methods\\insurance_order.json"
element = open(log_path, encoding='utf-8')
elements = json.load(element)

'''车险订单用例以及check相关'''


class insurance_order:
    '''车险订单列表，所有功能校验用例条件，以及check点'''
    '''车险订单-待支付-用例校验 例如：table=待支付'''
    def chexian_daizhifu(driver, table, ):
        try:
            if table == '待支付':
                driver.execupt_script(elements["待支付-点击"])
                logger.logger(f'{sys._getframe().f_code.co_name},{table}车险订单-点击待支付成功')
            elif table == '已承保':
                driver.execupt_script(elements["已承保-点击"])
                logger.logger(f'{sys._getframe().f_code.co_name},{table}车险订单-点击已承保成功')
            elif table == '已取消':
                driver.execupt_script(elements["已取消-点击"])
                logger.logger(f'{sys._getframe().f_code.co_name},{table}车险订单-点击已取消成功')
            elif table == '已过期':
                driver.execupt_script(elements["已过期-点击"])
                logger.logger(f'{sys._getframe().f_code.co_name},{table}车险订单-点击已过期成功')
            elif table == '全部':
                driver.execupt_script(elements["全部-点击"])
                logger.logger(f'{sys._getframe().f_code.co_name},{table}车险订单-点击全部成功')
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name},{table}车险订单-入参-页面不存在')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{table}车险订单-选择切换table-异常')

    '''车险订单-车牌号输入功能'''
    def chexian_chepai(driver, name):
        try:
            BasePage.monishijian(driver, 'id', 'LicenseNo')
            driver.execupt_script("$('#LicenseNo').val("+str(name)+")")
            logger.logger(f'{sys._getframe().f_code.co_name},{name}车险订单-输入车牌成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{name}车险订单-输入车牌-异常')

    '''车险订单-搜索后-暂无数据'''
    def chexian_zanwu(driver):
        try:
            driver.execupt_script(elements["车险订单-暂无数据"])
            logger.logger(f'{sys._getframe().f_code.co_name},车险订单-暂无数据功能显示成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},车险订单-暂无数据功能显示-异常')

    '''车险订单-提交时间输入功能 例如：starttime= 2019-01-01 endtime= 2019-01-01'''
    def chexian_tijiaoshijian(driver, starttime, endtime):
        try:
            BasePage.monishijian(driver, 'sclass', '.ant-calendar-input','0')
            driver.execupt_script("$('.ant-calendar-input').eq(0).val("+str(starttime)+")")
            BasePage.monishijian(driver, 'sclass', '.ant-calendar-input', '1')
            driver.execupt_script("$('.ant-calendar-input').eq(1).val(" + str(endtime) + ")")
            logger.logger(f'{sys._getframe().f_code.co_name},开始时间{starttime}结束时间{endtime}车险订单-提交时间功能输入成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},车险订单-提交时间功能输入-异常')


    '''车险订单-投保公司选择 toubao=人保车险'''
    def chexian_toubao(driver, toubao):
        try:
            if toubao !=None and toubao !='':
                name = driver.execupt_script(elements["车险订单-投保公司"])
                if toubao in name:
                    names = driver.execupt_script(elements["车险订单-投保公司长度"])
                    for i in range(0, names):
                        driver.execupt_script("$('.ant-select-dropdown-content').find('li').eq("+str(i)+").click()")
                        logger.logger(f'{sys._getframe().f_code.co_name},预期结果{toubao}车险订单-选择投保公司功能成功')
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name},车险订单-选择投保公司功能-入参不符合')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},车险订单-选择投保公司功能-异常')

    '''车险订单-业务员选择 toubao=张三'''
    def chexian_yewuyuan(driver, toubao):
        try:
            if toubao !=None and toubao !='':
                name = driver.execupt_script(elements["车险订单-业务员"])
                if toubao in name:
                    names = driver.execupt_script(elements["车险订单-业务员长度"])
                    for i in range(0, names):
                        driver.execupt_script("$('.ant-select-dropdown-content').find('li').eq("+str(i)+").click()")
                        logger.logger(f'{sys._getframe().f_code.co_name},预期结果{toubao}车险订单-选择业务员功能成功')
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name},车险订单-选择业务员功能-入参不符合')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},车险订单-选择业务员功能-异常')


    '''车险订单-出单员选择 toubao=张三'''
    def chexian_chudanyuan(driver, toubao):
        try:
            if toubao !=None and toubao !='':
                name = driver.execupt_script(elements["车险订单-出单员"])
                if toubao in name:
                    names = driver.execupt_script(elements["车险订单-出单员长度"])
                    for i in range(0, names):
                        driver.execupt_script("$('.ant-select-dropdown-content').find('li').eq("+str(i)+").click()")
                        logger.logger(f'{sys._getframe().f_code.co_name},预期结果{toubao}车险订单-选择出单员功能成功')
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name},车险订单-选择出单员功能-入参不符合')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},车险订单-选择出单员功能-异常')


    '''车险订单-部门选择 toubao=张三'''
    def chexian_bumen(driver, toubao):
        try:
            if toubao !=None and toubao !='':
                name = driver.execupt_script(elements["车险订单-部门"])
                if toubao in name:
                    names = driver.execupt_script(elements["车险订单-部门长度"])
                    for i in range(0, names):
                        driver.execupt_script("$('.ant-select-dropdown-content').find('li').eq("+str(i)+").click()")
                        logger.logger(f'{sys._getframe().f_code.co_name},预期结果{toubao}车险订单-选择部门功能成功')
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name},车险订单-选择部门功能-入参不符合')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},车险订单-选择部门功能-异常')

    '''车险订单-查询按钮点击'''
    def chexian_chaxun(driver):
        try:
            driver.execupt_script(elements["车险订单-查询"])
            logger.logger(f'{sys._getframe().f_code.co_name},车险订单-查询功能显示成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},车险订单-查询功能显示-异常')

    '''车险订单-查询按钮点击'''
    def chexian_daochu(driver):
        try:
            driver.execupt_script(elements["车险订单-导出"])
            logger.logger(f'{sys._getframe().f_code.co_name},车险订单-导出功能显示成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},车险订单-导出功能显示-异常')


    '''车险订单-下一页按钮点击'''
    def chexian_xiayiye(driver):
        try:
            driver.execupt_script(elements["车险订单-下一页"])
            logger.logger(f'{sys._getframe().f_code.co_name},车险订单-下一页功能显示成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},车险订单-下一页功能显示-异常')

    '''车险订单-页码总数获取'''
    def chexian_zongshu(driver, nubb):
        try:
            nub = driver.execupt_script(elements["车险订单-页码总数"])
            logger.logger(f'{sys._getframe().f_code.co_name}预期结果{nubb}实际结果{nub},车险订单-页码总数显示成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}预期结果{nubb},车险订单-页码总数显示-异常')


















