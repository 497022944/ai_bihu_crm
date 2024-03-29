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
            BasePage.monishijian(driver, 'id', elements["车牌号id"])
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

    '''摄像头进店历史'''
    '''摄像头进店历史车牌号输入功能 例如：license=张三'''
    def jdls_chepaihao(driver, license):
        try:
            license1 = driver.execupt_script("$('#licenseNo').val("+str(license)+")")
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}预期结果:{license}, 摄像头-进店历史-车牌号输入功能异常')

    '''摄像头进店历史进店时间功能 例如:(starttime='2019-11-11', endtime='2019-11-11')'''
    def jdls_jiandianshijian(driver, starttime, endtime):
        try:
            driver.execupt_script("$('.ant-calendar-input').eq(0).val("+str(starttime)+")")
            driver.execupt_script("$('.ant-calendar-input').eq(1).val(" + str(endtime) + ")")
            logger.info(f'{sys._getframe().f_code.co_name},预期开始时间:{starttime},结束时间:{endtime}摄像头-进店历史-进店时间搜索功能异常')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头-进店历史-进店时间搜索功能异常')

    '''摄像头进店历史摄像头名称输入/选择功能 例如：mingcheng=张三'''
    def jdls_shexiangtoumingcheng(driver, mingcheng):
        try:
            driver.execupt_script(elements["进店历史-摄像头名称"])
            driver.execupt_script("$('.ant-select-search__field').eq(0).val("+str(mingcheng)+")")
            logger.info(f'{sys._getframe().f_code.co_name},预期结果:{mingcheng}摄像头-进店历史-进店时间搜索功能异常')
        except  Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头-进店历史-摄像头名称输入功能异常')

    '''摄像头进店历史查询功能'''
    def jdls_chaxun(driver):
        try:
            driver.execupt_script(elements["进店历史-查询"])
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头-进店历史-搜索功能异常')


    '''摄像头进店历史-数据-车辆标签'''
    def jdls_cheliangbiaoqian(driver, biaoqian):
        try:
            biaoqian1 = driver.execupt_script(elements["进店历史-车辆标签"])
            if biaoqian in biaoqian1:
                logger.info(f'{sys._getframe().f_code.co_name}预期结果:{biaoqian}实际结果{biaoqian1},摄像头-进店历史-搜索功能')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头-进店历史-搜索功能异常')

    '''摄像头进店历史数据勾选全部功能'''
    def jdls_gouxuan(driver):
        try:
            driver.execupt_script(elements["进店历史-勾选"])
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头-进店历史-勾选功能异常')


    '''摄像头进店历史数据显示条数功能'''
    def jdls_tiaoshu(driver):
        try:
            driver.execupt_script(elements["进店历史-共条数"])
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头-进店历史-勾选功能异常')

    '''摄像头进店历史数据功能说明功能'''
    def jdls_shuoming(driver):
        try:
            driver.execupt_script(elements["进店历史-说明"])
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头-进店历史-功能说明功能异常')

    '''摄像头进店历史数据功能导出功能'''
    def jdls_daochu(driver):
        try:
            driver.execupt_script(elements["进店历史-导出"])
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头-进店历史-导出功能异常')



    # 摄像头进店设置

    '''摄像头进店设置-摄像头名称 例如：mingcheng=张三'''
    def jdsz_shexiangtoumingcheng(driver, mingcheng):
        try:
            mingcheng1 = driver.execupt_script(elements["进店设置-摄像头名称"])
            if mingcheng in mingcheng1:
                logger.info(f'{sys._getframe().f_code.co_name}预期结果:{mingcheng}实际结果{mingcheng1},摄像头-进店设置-摄像头名称功能')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头-进店设置-摄像头名称功能')

    '''摄像头进店设置-摄像头名称点击功能 例如：mingcheng = 张三'''
    def jdsz_shexiangtoumingchengdianji(driver, mingcheng):
        try:
            mingcheng1 = driver.execupt_script(elements["进店设置-摄像头名称长度"])
            for i in mingcheng1:
                mingchen = driver.execupt_script("return $('.leftSideList').eq("+str(i)+").text()")
                if mingchen == mingcheng:
                    driver.execupt_script("return $('.leftSideList').eq(" + str(i) + ").click()")
                else:
                    logbug.debug(f'{sys._getframe().f_code.co_name},预期结果:{mingcheng},实际结果:{mingchen}摄像头-进店设置-摄像头名称点击功能异常')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头-进店设置-摄像头名称点击功能异常')

    '''摄像头进店设置功能说明功能'''
    def jdsz_shezheshuoming(driver):
        try:
            driver.execupt_script(elements["进店设置-说明"])
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头-进店设置-功能说明功能异常')

    '''摄像头进店设置摄像头id功能'''
    def jdsz_shexiangtouid(driver, shexiangtouid):
        try:
            shexiangtouid1 = driver.execupt_script(elements["进店设置-摄像头id"])
            if shexiangtouid in shexiangtouid1:
                logger.info(f'{sys._getframe().f_code.co_name},预期结果:{shexiangtouid},实际结果:{shexiangtouid1}摄像头-进店设置-摄像头id功能对比正确')
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name},预期结果:{shexiangtouid},实际结果:{shexiangtouid1}摄像头-进店设置-摄像头id功能对比异常')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头-进店设置-摄像头id功能异常')

    '''摄像头进店设置摄像头创建时间功能 例如：shijian=1 查看是否存在'''
    def jdsz_shexiangtoushijian(driver, shijian):
        try:
            shexiangtouid1 = driver.execupt_script(elements["进店设置-摄像头创建时间"])
            if shijian == 1:
                logger.info(f'{sys._getframe().f_code.co_name},实际结果:{shexiangtouid1}摄像头-进店设置-摄像头时间存在')
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name},实际结果:{shexiangtouid1}摄像头-进店设置-摄像头时间不存在')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头-进店设置-摄像头时间功能异常')

    '''摄像头进店设置管理人员功能，说明 例如：renyuan=1 查看是否存在'''
    def jdsz_guanlirenyuan(driver, renyuan):
        try:
            renyuan1 = driver.execupt_script(elements["进店设置-摄像头管理人员说明"])
            if renyuan == 1:
                logger.info(f'{sys._getframe().f_code.co_name},实际结果:{renyuan1}摄像头-进店设置-管理人员说明存在')
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name},实际结果:{renyuan1}摄像头-进店设置-管理人员说明不存在')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头-进店设置-管理人员说明功能异常')

    '''摄像头进店设置管理人员功能，输入 例如：renyuanshuru=102 '''
    def jdsz_guanlirenyuan_shuru(driver, renyuanshuru):
        try:
            renyuan1 = driver.execupt_script(elements["进店设置-摄像头管理人员点击"])
            driver.execupt_script("$('.ant-select-search__field').eq(0).val("+str(renyuanshuru)+")")
            logger.info(f'{sys._getframe().f_code.co_name},实际结果:{renyuanshuru}摄像头-进店设置-管理人员输入')

        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头-进店设置-管理人员说明功能异常')

    '''摄像头进店设置管理人员功能点击保存'''
    def jdsz_guanlirenyuan_baocun(driver):
        try:
            renyuan1 = driver.execupt_script(elements["进店设置-摄像头管理人员保存"])

            renyuan2 = driver.execupt_script(elements["进店设置-摄像头管理人员保存提示"])
            if "更换摄像头管理员后" in renyuan2:
                logger.info(f'{sys._getframe().f_code.co_name},实际结果:{renyuan2}摄像头-进店设置-管理人员功能点击保存提示正确')
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name},实际结果:{renyuan2}摄像头-进店设置-管理人员功能点击保存提示异常非修改管理人员信息')

        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头-进店设置-管理人员功能点击保存提示功能异常')

    '''摄像头进店设置车型设置功能 例如：留存车型(chexing)=1 过滤车型(chexing)=2'''
    def jdsz_chexingshezhi(driver, chexing):
        try:
            if chexing == 1:
                driver.execupt_script(elements["进店设置-摄像头车型设置留存车型"])
            elif chexing == 2:
                driver.execupt_script(elements["进店设置-摄像头车型设置过滤车型"])
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name},摄像头-进店设置-输入选择车型功能不存在')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头-进店设置-功能说明功能异常')

    '''摄像头进店设置车型设置添加车型功能ENTER 例如：pingpai=宝马'''
    def jdsz_chexingshezhi_shuru(driver, pingpai):
        try:
            if pingpai != '' and pingpai != None:
                chexing = driver.find_element_by_class_name(".carInput.ant-input")
                driver.execupt_script(elements["进店设置-摄像头车型设置留存车型"])
                webdriver.ActionChains(driver).move_to_element(chexing).perform()
                chexing.click()
                chexing.keys(Keys.ENTER)
                logger.info(f'{sys._getframe().f_code.co_name},摄像头-进店设置-输入选择车型 enter 新增功能正常')
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name},摄像头-进店设置-输入选择 enter 新增功能不存在')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头-进店设置-输入选择 enter 新增功能异常')

    '''摄像头进店设置车型设置添加车型查看下面新增信息验证功能 例如：pingpai=宝马'''
    def jdsz_chexingshezhi_yanzheng(driver, pingpai):
        try:
            li = driver.execupt_script(elements["进店设置-摄像头车型设置后验证"])
            if pingpai in li:
                logger.info(f'{sys._getframe().f_code.co_name}预期结果{pingpai}实际结果{li},摄像头-进店设置-新增功能验证正常')
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name},摄像头-进店设置-新增功能验证不存在')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头-进店设置-新增功能验证异常')

    '''摄像头进店设置车型设置功能点击保存'''
    def jdsz_chexingshezhi_baocun(driver):
        try:
            renyuan1 = driver.execupt_script(elements["进店设置-摄像头车型设置保存"])

            renyuan2 = driver.execupt_script(elements["提示"])
            if "车型设置保存成功" in renyuan2:
                logger.info(f'{sys._getframe().f_code.co_name},实际结果:{renyuan2}摄像头-进店设置-车型设置添加车型功能点击保存提示正确')
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name},实际结果:{renyuan2}摄像头-进店设置-车型设置添加车型点击保存提示异常非修改车型设置添加车型信息')

        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头-进店设置-车型设置添加车型功能异常')

    '''摄像头进店设置分配设置-匹配范围 例如：mingcheng = 电销一部'''
    def jdsz_fenpeishezhi_pipeifanwei(driver, mingcheng):
        try:
            renyuan1 = driver.execupt_script(elements["进店设置-摄像头匹配设置"])
            if mingcheng != '' and mingcheng != None:
                for i in range(0, driver.execupt_script("return $('.ant-select-dropdown-menu-root').eq(1).find('li').length")):
                    ren = driver.execupt_script("return $('.ant-select-dropdown-menu-root').eq(1).find('li').eq("+str(i)+").text()")
                    if mingcheng == ren:
                        driver.execupt_script("$('.ant-select-dropdown-menu-root').eq(1).find('li').eq("+str(i)+").click()")
                        logger.info(f'{sys._getframe().f_code.co_name},实际结果:{mingcheng}实际结果{ren}，摄像头-进店设置-分配设置分配范围选择正确')
                    else:
                        logbug.debug(f'{sys._getframe().f_code.co_name},实际结果:{mingcheng}实际结果{ren}，摄像头-进店设置-分配设置分配范围选择错误')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头-进店设置-车型设置添加匹配范围功能异常')

    '''摄像头进店设置分配设置分配用户功能'''
    def jdsz_fenpeiyonghu(driver, yonghu):
        try:
            renyuan1 = driver.execupt_script(elements["进店设置-摄像头匹配设置"])
            if yonghu != '' and yonghu != None:
                for i in range(0, driver.execupt_script("return $('.ant-select-dropdown-menu-root').eq(0).find('li').length")):
                    ren = driver.execupt_script("return $('.ant-select-dropdown-menu-root').eq(0).find('li').eq("+str(i)+").text()")
                    if yonghu == ren:
                        driver.execupt_script("$('.ant-select-dropdown-menu-root').eq(0).find('li').eq("+str(i)+").click()")
                        logger.info(f'{sys._getframe().f_code.co_name},实际结果:{yonghu}实际结果{ren}，摄像头-进店设置-分配设置分配用户选择正确')
                    else:
                        logbug.debug(f'{sys._getframe().f_code.co_name},实际结果:{yonghu}实际结果{ren}，摄像头-进店设置-分配设置分配用户选择错误')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头-进店设置-车型设置添加分配用户功能异常')

    '''摄像头进店设置分配设置功能点击保存'''
    def jdsz_fenpeishezhi_baocun(driver):
        try:
            renyuan1 = driver.execupt_script(elements["进店设置-摄像头车型设置保存"])

            renyuan2 = driver.execupt_script(elements["提示"])
            if "车型设置保存成功" in renyuan2:
                logger.info(f'{sys._getframe().f_code.co_name},实际结果:{renyuan2}摄像头-进店设置-分配设置添加车型功能点击保存提示正确')
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name},实际结果:{renyuan2}摄像头-进店设置-分配设置点击保存提示信息异常')

        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头-进店设置-分配设置点击保存提示信息异常')

    '''摄像头进店设置分配设置选择到期及全部功能 例如:tixing = 到期(1) or 全部(2)'''
    def jdsz_tixingshezhi_tixing(driver, tixing):
        try:
            if tixing == 1:
                renyuan1 = driver.execupt_script(elements["进店设置-摄像头提醒设置到期提醒"])
                logger.info(f'{sys._getframe().f_code.co_name},摄像头-提醒设置-成功选择到期提醒')
            elif tixing == 2:
                renyuan1 = driver.execupt_script(elements["进店设置-摄像头提醒设置全部提醒"])
                logger.info(f'{sys._getframe().f_code.co_name},摄像头-提醒设置-成功选择全部提醒')
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name},摄像头-提醒设置-选择提醒方式传值内容不正确')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头-进店设置-车型设置添加车型功能异常')

    '''摄像头进店设置分配设置选择据到期天数 例如:tixing = 100'''
    def jdsz_tixingshezhi_judaoqi(driver, tixing):
        try:
            BasePage.monishijian(driver, 'class', '.ant-input-number-input')
            driver.execupt_script("$('.ant-input-number-input').val("+str(tixing)+")")
            logger.info(f'{sys._getframe().f_code.co_name},摄像头-提醒设置-预取结果{tixing}选择到期天数正确')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头-进店设置-提醒设置选择到期天数异常')

    '''摄像头进店设置分配设置选择本年度已出单/战败车辆，进店后不再提醒 or 疑似次新车提醒并分配（续保失败或注册日期在一年以内） 例如:tixing = 本年度已出单(1) or 疑似次新车(2)''' # 到期天数暂无法使用，无法输入
    def jdsz_tixingshezhi_benniandu(driver, tixing):
        try:
            if tixing == 1:
                driver.execupt_script(elements["摄像头提醒设置本年度"])
                logger.info(f'{sys._getframe().f_code.co_name},摄像头-提醒设置-成功选择摄像头提醒设置本年度')
            elif tixing == 2:
                driver.execupt_script(elements["摄像头提醒设置疑似次新车"])
                logger.info(f'{sys._getframe().f_code.co_name},摄像头-提醒设置-成功选择摄像头提醒设置疑似次新车')
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name},摄像头-提醒设置-选择摄像头提醒设置异常')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头-进店设置-选择摄像头提醒设置异常')

    '''摄像头进店设置提醒设置功能点击保存'''
    def jdsz_tixingshezhi_baocun(driver):
        try:
            renyuan1 = driver.execupt_script(elements["进店设置-摄像头提醒设置保存"])
            renyuan2 = driver.execupt_script(elements["提示"])
            if "提醒设置保存成功" in renyuan2:
                logger.info(f'{sys._getframe().f_code.co_name},实际结果:{renyuan2}摄像头-进店设置--提醒设置添加摄像头提醒设置点击保存提示正确')
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name},实际结果:{renyuan2}摄像头-进店设置--提醒设置点击保存提示异常信息')

        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头-进店设置-提醒设置点击保存提示异常信息')

    '''摄像头进店黑名单ENTER 例如：pingpai=京J*****'''
    def jdsz_heimingdan_shuru(driver, pingpai):
        try:
            if pingpai != '' and pingpai != None:
                driver.execupt_script("$('.ant-input').eq(1).val("+str(pingpai)+")")
                chexing = driver.find_element_by_class_name(".ant-input")
                webdriver.ActionChains(driver).move_to_element(chexing).perform()
                chexing.click()
                chexing.keys(Keys.ENTER)
                logger.info(f'{sys._getframe().f_code.co_name},摄像头-进店设置-输入黑名单 enter 新增功能正常')
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name},摄像头-进店设置-输入黑名单 enter 新增功能不存在')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头-进店设置-输入黑名单 enter 新增功能异常')


    '''摄像头进店设置黑名单功能点击保存'''
    def jdsz_heimingdan_baocun(driver):
        try:
            renyuan1 = driver.execupt_script(elements["进店设置-摄像头黑名单保存"])
            renyuan2 = driver.execupt_script(elements["提示"])
            if "提醒设置保存成功" in renyuan2:
                logger.info(f'{sys._getframe().f_code.co_name},实际结果:{renyuan2}摄像头-进店设置--提醒设置添加摄像头提醒设置点击保存提示正确')
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name},实际结果:{renyuan2}摄像头-进店设置--提醒设置点击保存提示异常信息')

        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},摄像头-进店设置-提醒设置点击保存提示异常信息')















