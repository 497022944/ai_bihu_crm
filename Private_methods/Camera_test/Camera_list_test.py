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
from Public_methods.Camera import RunMain
from selenium.webdriver.common.keys import Keys

logger = Log()
logbug = LogBug()
log_path = os.path.dirname(os.path.abspath('.')) + "\\Element_methods\\customer_list.json"
element = open(log_path, encoding='utf-8')
elements = json.load(element)

'''摄像头验证相关'''


class Camera_list:
    '''摄像头验证相关内容：车牌号，到期时间，进店时间，分配状态，用户姓名，去年投保公司，摄像头名称'''
    '''摄像头进店，传值：启动（start=启动），车牌（sxtLicense=京******），访问地址（address=qa.interface.com）,代理人id（agentid=13507）,下级id（subordinateid=13507）城市（City='1'）'''
    def camera_request(driver, start, sxtLicense, address, City, agentid, subordinateid):
        try:
            if start == 1:
                url = "http://(" + str(address) + ")/api/CarInsurance/getreinfo?"
                data = {
                    'Agent': agentid,
                    'CanShowNo': '1',
                    'ChildAgent': subordinateid,
                    'CityCode': City,
                    'Group': '1',
                    'LicenseNo': sxtLicense,
                    'RenewalCarType': '0',
                    'RenewalSource': '0',
                    'RenewalType': '3',
                    'ShowAutoMoldCode': '1',
                    'ShowFybc': '1',
                    'ShowInnerInfo': '1',
                    'ShowPACheckCode': '1',
                    'ShowRelation': '1',
                    'ShowRenewalCarType': '1',
                    'ShowSanZheJieJiaRi': '1',
                    'ShowSheBei': '1',
                    'ShowXiuLiChangType': '1',
                    'TimeFormat': '1',
                    'CustKey': 'AE0720D7397BB4AAA61461DD73601276',
                    'SecCode': 'a0f96bf3ae9c773ef65e2b544abb6f63',
                }
                request_start = RunMain(url, 'GET', data)
                if request_start == '':
                    pass
                else:
                    logger.info(f'{sys._getframe().f_code.co_name},摄像头请求结果:{request_start.res["StatusMessage"]}摄像头请求成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头请求异常')

    '''摄像头列表车牌号输入功能 (license=京*****)'''
    def camera_license(driver, license):
        try:
            driver.find_element_by_id(elements["车牌号id"]).send_keys(license)
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头列表-车牌号输入异常')

    '''摄像头列表到期时间输入功能 例如:(starttime='2019-11-11', endtime='2019-11-11')'''
    def Expire_time(driver, starttime, endtime):
        try:
            driver.execupt_script("$('.ant-calendar-input').eq(0).val("+str(starttime)+")")
            driver.execupt_script("$('.ant-calendar-input').eq(1).val(" + str(endtime) + ")")
            logger.info(f'{sys._getframe().f_code.co_name},预期开始时间:{starttime},结束时间:{endtime}摄像头列表-到期时间搜索功能异常')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头列表-到期时间搜索功能异常')

    '''摄像头列表进店时间输入功能 例如:(getstarttime='2019-11-11', getendtime='2019-11-11')'''
    def getinto_time(driver, getstarttime, getendtime):
        try:
            driver.execupt_script("$('.ant-calendar-input').eq(0).val(" + str(getstarttime) + ")")
            driver.execupt_script("$('.ant-calendar-input').eq(1).val(" + str(getendtime) + ")")
            driver.fid_element_by_class_name("ant-calendar-input").send_keys(Keys.ENTER)
            logger.info(f'{sys._getframe().f_code.co_name},预期开始时间:{getstarttime},结束时间:{getendtime}摄像头列表-进店时间搜索功能异常')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头列表-进店时间搜索功能异常')

    '''摄像头列表分配状态选择功能 例如:(distribution='1'（已分配）, distribution='2'（未分配）)'''
    def distribution(driver, distribution):
        try:
            if distribution == '已分配':
                driver.execupt_script(elements["已分配"])
            elif distribution == '未分配':
                driver.execupt_script(elements["未分配"])
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name},预期结果:{distribution},摄像头列表-分配状态选择功能异常')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头列表-分配状态选择功能异常')

    '''摄像头列表用户姓名功能 例如:(username='张三')'''
    def user_name(driver, username):
        try:
            if username != '' and username != None:
                driver.execupt_script("$('#SearchEmployeeIds > div > div > div > div > input').val(" + str(username) + ")")
                usernamelist = driver.execupt_script(elements["用户姓名"])
                if username in usernamelist:
                    logger.info(f'{sys._getframe().f_code.co_name},摄像头列表-用户姓名输入内容代理人list存在')
                else:
                    logbug.debug(f'{sys._getframe().f_code.co_name},预期结果:{username},摄像头列表-用户姓名输入内容代理人list不存在')
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name},预期结果:{username},摄像头列表-用户姓名输入功能异常')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头列表-用户姓名输入功能异常')

    '''摄像头列表去年投保公式选择功能 例如:(insured_year='人保车险')'''
    def insured_last_year(driver, insured_year):
        try:
            if insured_year != '' and insured_year != None:
                insured_years = driver.execupt_script(elements["上年投保公司"])
                if insured_year in insured_years:
                    for i in range(0, 100):
                        insured = driver.execupt_script("return $('div:nth-child(24) > div > div > div > ul > li').eq("+str(i)+").text()")
                        if insured == insured_year:
                            driver.execupt_script("$('div:nth-child(24) > div > div > div > ul > li').eq(" + str(i) + ").click()")
                            break
                else:
                    logbug.debug(f'{sys._getframe().f_code.co_name},预期结果:{insured_year},摄像头列表-去年投保公司入参不存在')
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name},预期结果:{insured_year},摄像头列表-去年投保公司选择功能异常')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头列表-去年投保公司选择功能异常')

    '''摄像头列表摄像头名称功能 例如:(cameraname='张三')'''# 摄像头名称点击事件，其他文本获取选择等未开发
    def camera_name(driver, cameraname):
        try:
            if cameraname != '' and cameraname != None:
                driver.execupt_script(elements["摄像头名称"])
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头列表-摄像头名称选择功能异常')

    '''摄像头列表查询功能 '''# 功能不完善
    def camera_query(driver):
        try:
            driver.execupt_script(elements["查询"])
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头列表-摄像头点击查询功能异常')

    '''摄像头列表导出功能 '''
    def camera_export(driver):
        try:
            driver.execupt_script(elements["导出"])
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头列表-摄像头点击导出功能异常')

    '''摄像头列表页面提示功能  例如：（masg='网络超时'）'''
    def alert_masg(driver, masg):
        try:
            alert_masg = driver.execupt_script(elements["提示"])
            if masg == alert_masg:
                logger.info(f'{sys._getframe().f_code.co_name}预期结果:{masg}实际结果{alert_masg}, 摄像头列表-页面提示功能正确')
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name}预期结果:{masg}实际结果{alert_masg}, 摄像头列表-页面提示功能异常')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}, 摄像头列表-页面提示功能异常')

    '''摄像头列表数据删除功能 '''# 功能不完善
    def data_delete(driver):
        pass

    '''摄像头列表数据业务员功能 '''# 功能不完善
    def salesman(driver):
        pass

    '''摄像头列表数据选择checkbox功能 '''# 功能不完善
    def data_choice(driver):
        pass



