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
log_path = os.path.dirname(os.path.abspath('.')) + "\\Element_methods\\Batch_renewal_list.json"
element = open(log_path, encoding='utf-8')
elements = json.load(element)

'''批量续保验证相关'''

class Batch_renewal:

    '''批量续保验证相关：任务状态，文件名，操作人，操作时间，车牌/车架号，查询，新增导入，批续额度，删除，重新查询，更改查询方式'''
    '''批量续保-任务状态查询功能，status=1 (未执行)or 2 （执行中）or 3（已完成）'''
    def pl_task_status(driver, status):
        try:
            if status == 1:
                driver.execupt_script(elements["任务状态-未执行"])
            elif status == 2:
                driver.execupt_script(elements["任务状态-执行中"])
            elif status == 3:
                driver.execupt_script(elements["任务状态-已完成"])
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name}, 预期结果{status}，批量续保-任务状态选择异常')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}，预期结果{status},批量续保-任务状态选择异常')

    '''批量续保-文件名输入功能，file=张三'''
    def pl_file_name(driver, file):
        try:
            if file != '' and file != None:
                driver.execupt_script("$('#fileName').val('+str(file)+')")
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name}, 预期结果{file}，批量续保-任务状态选择异常')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},预期结果{file}，批量续保-任务状态选择异常')

    '''批量续保-操作人选择功能 例如:(username='张三')'''
    def pl_user_name(driver, username):
        try:
            if username != '' and username != None:
                driver.execupt_script("$('.ant-select-search__field').val(' + str(username) + ')")
                usernamelist = driver.execupt_script(elements["操作人list"])
                if username in usernamelist:
                    logger.info(f'{sys._getframe().f_code.co_name},批量续保-操作人选择内容代理人list存在')
                else:
                    logbug.debug(f'{sys._getframe().f_code.co_name},预期结果:{username},批量续保-操作人选择内容代理人list存在')
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name},预期结果:{username},批量续保-操作人选择功能异常')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},批量续保-操作人选择功能异常')

    '''批量续保-操作时间输入功能，getstarttime=2019-01-01，getendtime=2019-01-01'''
    def pl_get_time(driver, getstarttime, getendtime):
        try:
            driver.execupt_script("$('.ant-calendar-input ').eq(0).val(" + str(getstarttime) + ")")
            driver.execupt_script("$('.ant-calendar-input ').eq(1).val(" + str(getendtime) + ")")
            driver.fid_element_by_class_name("ant-calendar-input").send_keys(Keys.ENTER)
            logger.info(f'{sys._getframe().f_code.co_name},预期开始时间:{getstarttime},结束时间:{getendtime}批量续保-操作时间输入功能异常')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},批量续保-操作时间输入功能异常')

    '''批量续保-车牌/车架号输入功能，licenseNoname=京****** 或者 licenseNoname=FJHKSJERFNKDJFSAD'''
    def pl_licenseNo_name(driver, licenseNoname):
        try:
            if licenseNoname != '' and licenseNoname != None:
                driver.execupt_script("$('#licenseNo').val('+str(licenseNoname)+')")
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name}, 预期结果{licenseNoname}，批量续保-车牌/车架号输入功能异常')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},预期结果{licenseNoname}，批量续保-车牌/车架号输入功能异常')

    '''批量续保-查询功能'''
    def pl_batch_query(driver):
        try:
            driver.execupt_script(elements["查询"])
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}，批量续保-查询功能异常')

    '''批量续保-新增导入功能'''
    def pl_new_imports(driver):
        try:
            driver.execupt_script(elements["新增导入"])
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}，批量续保-新增导入功能异常')

    '''批量续保-批量续保模板点击功能'''
    def pl_new_importsmoban(driver):
        try:
            driver.execupt_script(elements["批量续保模板"])
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}，批量续保-批量续保模板点击功能异常')

    '''批量续保-投保地区选择功能 insured='北京'''
    def pl_areas_insured(driver, insured):
        try:
            if insured != '' and insured != None:
                insuredname = driver.execupt_script(elements["投保地区"])
                if insured in insuredname:
                    for i in range(1, 100):
                        name = driver.execupt_script("return $('.ant-select-dropdown-menu.ant-select-dropdown-menu-vertical.ant-select-dropdown-menu-root > li:nth-child("+str(i)+")').eq(2).text()")
                        if insured == name:
                            driver.execupt_script("return $('.ant-select-dropdown-menu.ant-select-dropdown-menu-vertical.ant-select-dropdown-menu-root > li:nth-child(" +str(i)+ ")').eq(2).click()")
                            break
                else:
                    logbug.debug(f'{sys._getframe().f_code.co_name}实际结果{insuredname}预期结果{insured}，批量续保-批量续保模板点击功能异常')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}，批量续保-批量续保模板点击功能异常')

    '''批量续保-上传功能功能 uploadnis= r"C：/123.excel"'''
    def pl_upload(driver, uploadnis):
        try:
            nis = driver.find_element_by_css_selector(elements["上传文件"])
            nis.send_keys(uploadnis)
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}，批量续保-上传文件功能异常')

    '''批量续保-覆盖字段业务员功能'''
    def pl_cover(driver):
        try:
            driver.execupt_script(elements["覆盖字段-业务员"])
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}，批量续保-覆盖字段-业务员功能异常')

    '''批量续保-批量导入功能'''
    def pl_Import(driver):
        try:
            driver.execupt_script(elements["批量导入"])
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}，批量续保-批量导入功能异常')

    '''批量续保-批量导入功能'''
    def pl_Renewal_of_insuranc(driver):
        try:
            driver.execupt_script(elements["批量续保"])
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}，批量续保-批量续保功能异常')

    '''批量续保-选择文件功能-----该功能不起实际效果，能触发点击事件，不能上传形式，例如：检查功能是否可用'''
    def pl_Select_files(driver):
        try:
            driver.execupt_script(elements["选择文件"])
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}，批量续保-选择文件功能异常')

    '''批量续保-弹窗X功能'''
    def pl_Close(driver):
        try:
            driver.execupt_script(elements["弹窗关闭"])
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}，批量续保-关闭弹窗功能异常')

    '''批量续保-数据行-重新查询按钮 支持保险公司:平安车险+太平洋车险****'''
    def pl_search(driver, baoshi):
        try:
            driver.execupt_script(elements["重新查询"])
            if baoshi != '' and baoshi != None:
                lisnum = driver.execupt_script("$('.ant-checkbox-group').text()")
                if baoshi in lisnum:
                    baoshidict = baoshi.split('+')
                    for baoshidictli in baoshidict:
                        if baoshidictli == '平安车险':
                            driver.execupt_script(elements["平安车险"])
                            driver.execupt_script(elements["重新查询-确定按钮"])
                        elif baoshidictli == '太平洋车险':
                            driver.execupt_script(elements["太平洋车险"])
                            driver.execupt_script(elements["重新查询-确定按钮"])
                        elif baoshidictli == '人保车险':
                            driver.execupt_script(elements["人保车险"])
                            driver.execupt_script(elements["重新查询-确定按钮"])
                        elif baoshidictli == '中国人寿财险':
                            driver.execupt_script(elements["中国人寿财险"])
                            driver.execupt_script(elements["重新查询-确定按钮"])
                        elif baoshidictli == '中华联合车险':
                            driver.execupt_script(elements["中华联合车险"])
                            driver.execupt_script(elements["重新查询-确定按钮"])
                        elif baoshidictli == '大地车险':
                            driver.execupt_script(elements["大地车险"])
                            driver.execupt_script(elements["重新查询-确定按钮"])
                        elif baoshidictli == '阳光车险':
                            driver.execupt_script(elements["阳光车险"])
                            driver.execupt_script(elements["重新查询-确定按钮"])
                        elif baoshidictli == '太平车险':
                            driver.execupt_script(elements["太平车险"])
                            driver.execupt_script(elements["重新查询-确定按钮"])
                        elif baoshidictli == '华安车险':
                            driver.execupt_script(elements["华安车险"])
                            driver.execupt_script(elements["重新查询-确定按钮"])
                        elif baoshidictli == '天安':
                            driver.execupt_script(elements["天安"])
                            driver.execupt_script(elements["重新查询-确定按钮"])
                        elif baoshidictli == '英大泰和车险':
                            driver.execupt_script(elements["英大泰和车险"])
                            driver.execupt_script(elements["重新查询-确定按钮"])
                        elif baoshidictli == '安心车险':
                            driver.execupt_script(elements["安心车险"])
                            driver.execupt_script(elements["重新查询-确定按钮"])
                        elif baoshidictli == '利宝车险':
                            driver.execupt_script(elements["利宝车险"])
                            driver.execupt_script(elements["重新查询-确定按钮"])
                        elif baoshidictli == '安邦车险':
                            driver.execupt_script(elements["安邦车险"])
                            driver.execupt_script(elements["重新查询-确定按钮"])
                        else:
                            driver.execupt_script(elements["重新查询-X按钮"])
                            logbug.debug(f'{sys._getframe().f_code.co_name}，预期结果{baoshi}批量续保-重新查询-输入保险公司信息异常')

                else:
                    driver.execupt_script(elements["重新查询-X按钮"])
                    logbug.debug(f'{sys._getframe().f_code.co_name}，预期结果{baoshi}批量续保-重新查询-输入保险公司信息异常')
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name}，预期结果{baoshi}批量续保-重新查询-输入保险公司信息异常')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}，批量续保-重新查询功能异常')

    '''批量续保-数据行-删除按钮'''
    def pl_shuju_Close(driver):
        try:
            driver.execupt_script(elements["数据行-删除"])
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}，批量续保-输出数据功能异常')

    '''批量续保-数据行-更改查询方式'''# 未开发
    def pl_change(driver):
        pass




