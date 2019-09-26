from utils.getConfig import *
import sys
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

class list_check:

    '''车辆信息相关提示--开始'''
    # 车牌号check车牌号必填
    def License_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['车牌号提示'])
            if hint in License_hint:
                logger.info(f"请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件正确")
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint}，提示代码异常未执行')

    # 车架号check车架号提示必填
    def VIN_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['车架号提示'])
            if hint in License_hint:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:,{hint},实际结果:{License_hint},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:,{hint},实际结果:{License_hint},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:,{hint}，提示代码异常未执行')

    # 发动机号check发动机号提示必填
    def Engine_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['发动机号提示'])
            if hint in License_hint:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint}，提示代码异常未执行')

    # 注册日期check注册日期提示必填
    def Registrationdate_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['注册日期提示'])
            if hint in License_hint:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:,{hint},实际结果:{License_hint},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:,{hint},实际结果:{License_hint},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:,{hint}，提示代码异常未执行')

    # 品牌型号check品牌型号提示必填
    def model_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['品牌型号提示'])
            if hint in License_hint:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint}，提示代码异常未执行')

    # 车型check车型提示必填
    def Vehicle_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['车型提示'])
            if hint in License_hint:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:,{hint},实际结果:{License_hint},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:,{hint},实际结果:{License_hint},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:,{hint}，提示代码异常未执行')

    # 新车购置价check新车购置价提示必填
    def purchaseprice_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['新车购置价提示'])
            if hint in License_hint:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:,{hint},实际结果:{License_hint},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:,{hint},实际结果:{License_hint},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:,{hint}，提示代码异常未执行')

    # 座位数check品牌型号座位数提示必填
    def Seatnumber_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['座位数提示'])
            if hint in License_hint:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint}，提示代码异常未执行')

    # 排量check车型排量提示必填
    def displacement_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['排量提示'])
            if hint in License_hint:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:,{hint},实际结果:{License_hint},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:,{hint},实际结果:{License_hint},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:,{hint}，提示代码异常未执行')

    '''车辆信息相关提示--结束'''


    '''关系人信息相关提示--开始'''
    # 被保险人姓名check被保险人姓名必填
    def Insuredperson_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['被保险人姓名'])
            if hint in License_hint:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint}，提示代码异常未执行')

    # 被保险人证件类型check被保险人证件类型提示必填
    def Documenttype_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['被保险人证件类型'])
            if hint in License_hint:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:,{hint},实际结果:{License_hint},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:,{hint},实际结果:{License_hint},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:,{hint}，提示代码异常未执行')

    # 被保险人证件号码check被保险人证件号码提示必填
    def InsuredCertificateNumber_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['被保险人证件号码'])
            if hint in License_hint:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint}，提示代码异常未执行')

    # 被保险人电话check被保险人电话提示必填
    def InsuredTelephone_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['被保险人电话'])
            if hint in License_hint:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:,{hint},实际结果:{License_hint},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:,{hint},实际结果:{License_hint},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:,{hint}，提示代码异常未执行')

    # 被保险人邮箱check被保险人邮箱提示必填
    def Insuredmailbox_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['被保险人邮箱'])
            if hint in License_hint:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint}，提示代码异常未执行')


    # 投保人姓名check投保人姓名提示必填
    def InsuredName_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['投保人姓名'])
            if hint in License_hint:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint}，提示代码异常未执行')

    # 投保人证件类型check投保人证件类型提示必填
    def applicanttype_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['投保人证件类型'])
            if hint in License_hint:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:,{hint},实际结果:{License_hint},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:,{hint},实际结果:{License_hint},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:,{hint}，提示代码异常未执行')

    # 投保人证件号码check投投保人证件号码提示必填
    def applicantCertificates_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['投保人证件号码'])
            if hint in License_hint:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint}，提示代码异常未执行')

    # 投保人电话check投保人电话提示必填
    def applicantphone_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['投保人电话'])
            if hint in License_hint:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint}，提示代码异常未执行')

    # 投保人邮箱check投保人邮箱提示必填
    def applicantmailbox_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['投保人邮箱'])
            if hint in License_hint:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint}，提示代码异常未执行')

    # 车主姓名check车主姓名提示必填
    def Nameowner_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['车主姓名'])
            if hint in License_hint:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint}，提示代码异常未执行')

    # 车主证件类型check车主证件类型提示必填
    def ownertype_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['车主证件类型'])
            if hint in License_hint:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint}，提示代码异常未执行')

    # 车主证件号码check车主证件号码提示必填
    def ownerCertificates_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['车主证件号码'])
            if hint in License_hint:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint}，提示代码异常未执行')

        '''临时关系人开始'''

    #  个人临时名称信息check个人临时名称信息提示必填
    def Personaltemporarynameinformation_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['个人临时名称信息'])
            if hint in License_hint:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint}，提示代码异常未执行')

    #  个人临时证件类型check个人临时证件类型提示必填
    def Temporarydocuments_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['个人临时证件类型'])
            if hint in License_hint:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint}，提示代码异常未执行')

    #  个人临时证件号码check个人临时证件号码提示必填
    def Temporarynumber_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['个人临时证件号码'])
            if hint in License_hint:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint}，提示代码异常未执行')

    #  个人临时电话信息check个人临时电话信息提示必填
    def Temporarycall_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['个人临时电话信息'])
            if hint in License_hint:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint}，提示代码异常未执行')

    #  个人临时邮箱信息check个人临时邮箱信息提示必填
    def Temporarymailbox_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['个人临时邮箱信息'])
            if hint in License_hint:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint}，提示代码异常未执行')

    #  公户临时名称信息check公户临时名称信息提示必填
    def companyPersonaltemporarynameinformation_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['公户临时名称信息'])
            if hint in License_hint:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint}，提示代码异常未执行')

    #  公户临时证件类型check公户临时证件类型提示必填
    def companyTemporarydocuments_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['公户临时证件类型'])
            if hint in License_hint:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint}，提示代码异常未执行')

    #  公户临时证件号码check公户临时证件号码提示必填
    def companyTemporarynumber_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['公户临时证件号码'])
            if hint in License_hint:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint}，提示代码异常未执行')

    #  公户临时电话信息check公户临时电话信息提示必填
    def companyTemporarycall_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['公户临时电话信息'])
            if hint in License_hint:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint}，提示代码异常未执行')

    #  公户临时邮箱信息check公户临时邮箱信息提示必填
    def companyTemporarymailbox_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['公户临时邮箱信息'])
            if hint in License_hint:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint}，提示代码异常未执行')

    #  点击临时关系个人新增3个临时标签
    def geren_Temporary_label_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['个人点击临时标签返回标签数量'])
            License_hintwenben = driver.execute_script(elements['个人点击临时标签返回标签文本'])
            if hint == 3:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint}结果文本为{License_hintwenben},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint}结果文本为{License_hintwenben},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint}，提示代码异常未执行')

    #  点击临时关系公户新增3个临时标签
    def gonghu_Temporary_label_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['公户点击临时标签返回标签数量'])
            License_hintwenben = driver.execute_script(elements['公户点击临时标签返回标签文本'])
            if hint == 3:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint}结果文本为{License_hintwenben},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint}结果文本为{License_hintwenben},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint}，提示代码异常未执行')
        '''临时关系人结束'''

        '''报价信息开始'''

        #  投保地区check投保地区提示必填
    def Insuredarea_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['投保地区'])
            if hint in License_hint:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint}，提示代码异常未执行')

    #  商业起保时间check商业起保时间提示必填
    def business_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['商业起保时间'])
            if hint in License_hint:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint}，提示代码异常未执行')

    #  交强起保时间check交强起保时间提示必填
    def Crossstrength_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['交强起保时间'])
            if hint in License_hint:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint}，提示代码异常未执行')

    #  报价公司check报价公司提示必填
    def Quotationcompany_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['报价公司'])
            if hint in License_hint:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint}，提示代码异常未执行')


    #  客户信息箭头缩放功能  例如：传值1，功能为放开状态，传值2，功能为合并状态
    def Quotationzoom_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['客户信息箭头缩放功能'])
            if hint == 1:
                if License_hint == 'display: none;':
                    se_hint = driver.execute_script(elements['客户信息箭头缩放功能ID'])
            elif hint == 2:
                if License_hint == 'display: none;':
                    logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},已隐藏无需操作')
                else:
                    se_hint = driver.execute_script(elements['客户信息箭头缩放功能ID'])
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint}，提示代码异常未执行')

    #  车辆信息箭头缩放功能  例如：传值1，功能为放开状态，传值2，功能为合并状态
    def Quotationzoom_check_hint1(driver, hint):
        try:
            License_hint = driver.execute_script(elements['车辆信息箭头缩放功能'])
            if hint == 1:
                if License_hint == 'display: none;':
                    se_hint = driver.execute_script(elements['车辆信息箭头缩放功能ID'])
            elif hint == 2:
                if License_hint == 'display: none;':
                    logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},已隐藏无需操作')
                else:
                    se_hint = driver.execute_script(elements['车辆信息箭头缩放功能ID'])
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint}，提示代码异常未执行')

    #  上年投保信息箭头缩放功能  例如：传值1，功能为放开状态，传值2，功能为合并状态
    def Quotationzoom_check_hint2(driver, hint):
        try:
            License_hint = driver.execute_script(elements['上年投保信息箭头缩放功能'])
            if hint == 1:
                if License_hint == 'display: none;':
                    se_hint = driver.execute_script(elements['上年投保信息箭头缩放功能ID'])
            elif hint == 2:
                if License_hint == 'display: none;':
                    logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},已隐藏无需操作')
                else:
                    se_hint = driver.execute_script(elements['上年投保信息箭头缩放功能ID'])
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint}，提示代码异常未执行')

    #  关系人箭头缩放功能  例如：传值1，功能为放开状态，传值2，功能为合并状态
    def Quotationzoom_check_hint3(driver, hint):
        try:
            License_hint = driver.execute_script(elements['关系人信息箭头缩放功能'])
            if hint == 1:
                if License_hint == 'display: none;':
                    se_hint = driver.execute_script(elements['关系人信息箭头缩放功能ID'])
            elif hint == 2:
                if License_hint == 'display: none;':
                    logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},已隐藏无需操作')
                else:
                    se_hint = driver.execute_script(elements['关系人信息箭头缩放功能ID'])
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint}，提示代码异常未执行')

    #  报价信息箭头缩放功能  例如：传值1，功能为放开状态，传值2，功能为合并状态
    def Quotationzoom_check_hint4(driver, hint):
        try:
            License_hint = driver.execute_script(elements['报价信息箭头缩放功能'])
            if hint == 1:
                if License_hint == 'display: none;':
                    se_hint = driver.execute_script(elements['报价信息箭头缩放功能ID'])
            elif hint == 2:
                if License_hint == 'display: none;':
                    logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},已隐藏无需操作')
                else:
                    se_hint = driver.execute_script(elements['报价信息箭头缩放功能ID'])
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint}，提示代码异常未执行')



        '''报价信息结束'''














    #  报价信息页面点击一键报价返回信息check报价信息页面点击一键报价返回信息提示请您先按照提示完善信息后保存
    def Onepricequote_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['报价信息页面点击一键报价返回信息'])
            if hint in License_hint:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint}，提示代码异常未执行')

    #  报价信息页面点击一键报价返回信息 非check点返回信息
    def return_Onepricequote_check_hint(driver):
        try:
            License_hint = driver.execute_script(elements['报价信息页面点击一键报价非check点返回信息'])
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},实际结果:{License_hint},提示代码异常未执行')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},提示代码异常未执行')
        return

    #  报价信息页面点击保存返回信息check报价信息页面点击保存返回信息提示请您先按照提示完善信息后保存
    def Save_back_check_hint(driver, hint):
        try:
            License_hint = driver.execute_script(elements['报价信息页面点击保存返回信息'])
            if hint in License_hint:
                logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件正确')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint},实际结果:{License_hint},相比条件错误')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{hint}，提示代码异常未执行')

    '''关系人信息相关提示--结束'''

