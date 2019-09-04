# -*- coding: utf-8 -*-
from utils.getConfig import *
import time
from utils.Log import Log
from utils.Logbug import LogBug
import re
import json
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import datetime
from selenium.webdriver.support.ui import Select
from Publicmethod.PublicMethod import BasePage
from interfase.Camera import RunMain
from helppage.Contrastofinsuranceparameters import *
from selenium.webdriver.common.action_chains import ActionChains
import unittest
from helppage.Mine import *
import requests


log_path = os.path.dirname(os.path.abspath('.')) + "\\elements\kehuliebiao.json"
element = open(log_path, encoding='utf-8')
elements = json.load(element)
haoshi_path = os.path.dirname(os.path.abspath('.')) + "\\configs\haoshi.txt"
one_file = open(haoshi_path,'a',encoding='utf-8-sig')
yongli_path = os.path.dirname(os.path.abspath('.')) + "\\configs\yongli.txt"
ele = open(yongli_path, 'r',encoding='utf-8-sig')
c = ele.readlines()
lists = [x.strip('\n') for x in c]
yongliline = c.__len__()

shot_path = os.path.dirname(os.path.abspath('.')) + "\\picture"
capturename = os.path.join(shot_path, time.strftime("%Y-%m-%d-%H_%M_%S") + '.png')
logger = Log()
logbug = LogBug()
logger.info(yongliline)


"""前置方法前置方法前置方法前置方法前置方法前置方法前置方法前置方法前置方法前置方法前置方法前置方法前置方法前置方法
前置方法前置方法前置方法前置方法前置方法前置方法前置方法前置方法前置方法前置方法前置方法前置方法前置方法前置方法
前置方法前置方法前置方法前置方法前置方法前置方法前置方法前置方法前置方法前置方法前置方法前置方法前置方法前置方法
前置方法前置方法前置方法前置方法前置方法前置方法前置方法前置方法前置方法前置方法前置方法前置方法前置方法前置方法"""
#1 进入客户列表基本操作
def click_kehuliebiao_link(driver):
    try:
        # kehu = driver.find_element_by_class_name(elements["kehu_class_name"])
        # ActionChains(driver).move_to_element(kehu).perform()
        # time.sleep(1)
        # driver.find_element_by_xpath(elements["kehuliebiao_linktext_Xpath"]).click()
        time.sleep(5)
        driver.get(elements["kehuliebiao_url"])
        time.sleep(8)
        logger.info(f'进入客户列表，全部tab共有{total}条数据')
    except Exception:
        logbug.debug("前端--客户列表-- 异常")

#2 删除_创建测试数据
def clear_and_create_test_data(driver):
    click_kehuliebiao_link(driver)
    try:
        selector = Select(driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_dropdownlist_css"]))
        selector.select_by_value("1")
        driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_text_css"]).send_keys(
            elements["kehuliebiao_test_licenseno"])
        driver.find_element_by_class_name(elements["kehuliebiao_sousuo_button_class"]).click()
        time.sleep(5)
        total = driver.find_element_by_class_name(elements["kehuliebiao_total_count_class"]).text
        logger.info(f'车牌号共搜索出{total}条数据')
        time.sleep(1)
        driver.find_element_by_css_selector(elements["kehuliebiao_select_all_css"]).click()
        time.sleep(1)
        driver.find_element_by_id(elements["kehuliebiao_shanchu_button_id"]).click()
        time.sleep(1)
        driver.find_element_by_xpath(elements["kehuliebiao_shanchu_ok_Xpath"]).click()
        time.sleep(1)
        logger.info(f'客户列表测试数据{elements["kehuliebiao_test_licenseno"]}共{total}条删除成功')
    except Exception:
        logbug.debug("前端--客户列表--测试数据删除异常")


    try:
        #创建测试数据
        url = 'http://it.91bihu.me/api/CarInsurance/getreinfo'
        data = {
            'LicenseNo': elements["kehuliebiao_test_licenseno"],
            'CityCode': '1',
            'Group': '1',
            'Agent': '191260',
            'CustKey': '4DE9B7822E0DE81FC734BC5689AB6F03',
            'SecCode': '23c73b3be4c698971dbf320699431545'
        }
        requests.get(url,params=data)
        logger.info("前端--客户列表--测试数据创建成功")
    except Exception:
        logbug.debug("前端--客户列表--测试数据创建异常")

    set_kehumingcheng_kehudianhua(driver)



#3 进入测试数据详情
def enter_testdata_detail(driver):
    try:
        click_kehuliebiao_link(driver)
        time.sleep(1)
        selector = Select(driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_dropdownlist_css"]))
        selector.select_by_value("1")
        driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_text_css"]).send_keys(
            elements["kehuliebiao_test_licenseno"])
        time.sleep(1)
        driver.find_element_by_class_name(elements["kehuliebiao_sousuo_button_class"]).click()
        time.sleep(1)
        driver.find_element_by_css_selector(elements["kehuliebiao_first_data_link_css"]).click()
        time.sleep(1)
        logger.info(f'进入{elements["kehuliebiao_test_licenseno"]}详情成功')
    except Exception:
        logbug.debug(f'进入{elements["kehuliebiao_test_licenseno"]}详情失败')


#5 设置回访状态
# zhuangtai = '5'忙碌中待联系'17'已报价考虑中（普通）'13'已报价考虑中（重点）'14'其他'20'预约到店'9'成功出单'4'战败'16'无效数据（停机、空号）
# select_time:0=今天1=明天2=后天3三天7一周14两周
def set_huifang_zhuangtai(driver,zhuangtai,select_time):
    if select_time == 0:#今天
        click_kehuliebiao_link(driver)
        time.sleep(1)
        enter_testdata_detail(driver)
        time.sleep(1)
        driver.find_element_by_css_selector(elements["kehuxiangqing_lurugenjin_css"]).click()
        time.sleep(1)
        selector = Select(driver.find_element_by_id(elements["kehuxiangqing_lurugenjin_genjinzhuangtai_id"]))
        selector.select_by_value(zhuangtai)
        time.sleep(1)
        driver.find_element_by_id(elements["kehuxiangqing_lurugenjin_xiacihuifangshijian_id"]).click()
        time.sleep(1)
        driver.find_element_by_css_selector(elements["kehuxiangqing_lurugenjin_xiacihuifangshijian_id_queren_css"]).click()
        time.sleep(1)
        driver.find_element_by_id(elements["kehuxiangqing_lurugenjin_bencigenjinneirong_id"]).send_keys('1')
        time.sleep(1)
        driver.find_element_by_css_selector(elements["kehuxiangqing_lurugenjin_ok_css"]).click()
        time.sleep(1)
        logger.info(f'设置回访状态{zhuangtai}成功，回访日期今天')
    elif select_time == 1:#明天
        click_kehuliebiao_link(driver)
        time.sleep(1)
        enter_testdata_detail(driver)
        time.sleep(1)
        driver.find_element_by_css_selector(elements["kehuxiangqing_lurugenjin_css"]).click()
        time.sleep(1)
        selector = Select(driver.find_element_by_id(elements["kehuxiangqing_lurugenjin_genjinzhuangtai_id"]))
        selector.select_by_value(zhuangtai)
        time.sleep(1)
        driver.find_elements_by_css_selector(elements["kehuxiangqing_lurugenjin_huifangshijian_mingtian_class"])[
            0].click()
        time.sleep(1)
        driver.find_element_by_id(elements["kehuxiangqing_lurugenjin_bencigenjinneirong_id"]).send_keys('1')
        time.sleep(1)
        driver.find_element_by_css_selector(elements["kehuxiangqing_lurugenjin_ok_css"]).click()
        time.sleep(1)
        logger.info(f'设置回访状态{zhuangtai}成功，回访日期明天')
    elif select_time == 2:#后天
        click_kehuliebiao_link(driver)
        time.sleep(1)
        enter_testdata_detail(driver)
        time.sleep(1)
        driver.find_element_by_css_selector(elements["kehuxiangqing_lurugenjin_css"]).click()
        time.sleep(1)
        selector = Select(driver.find_element_by_id(elements["kehuxiangqing_lurugenjin_genjinzhuangtai_id"]))
        selector.select_by_value(zhuangtai)
        time.sleep(1)
        driver.find_elements_by_css_selector(elements["kehuxiangqing_lurugenjin_huifangshijian_houtian_class"])[
            1].click()
        time.sleep(1)
        driver.find_element_by_id(elements["kehuxiangqing_lurugenjin_bencigenjinneirong_id"]).send_keys('1')
        time.sleep(1)
        driver.find_element_by_css_selector(elements["kehuxiangqing_lurugenjin_ok_css"]).click()
        time.sleep(1)
        logger.info(f'设置回访状态{zhuangtai}成功，回访日期后天')
    elif select_time == 3:#三天
        click_kehuliebiao_link(driver)
        time.sleep(1)
        enter_testdata_detail(driver)
        time.sleep(1)
        driver.find_element_by_css_selector(elements["kehuxiangqing_lurugenjin_css"]).click()
        time.sleep(1)
        selector = Select(driver.find_element_by_id(elements["kehuxiangqing_lurugenjin_genjinzhuangtai_id"]))
        selector.select_by_value(zhuangtai)
        time.sleep(1)
        driver.find_elements_by_css_selector(elements["kehuxiangqing_lurugenjin_huifangshijian_santian_class"])[
            2].click()
        time.sleep(1)
        driver.find_element_by_id(elements["kehuxiangqing_lurugenjin_bencigenjinneirong_id"]).send_keys('1')
        time.sleep(1)
        driver.find_element_by_css_selector(elements["kehuxiangqing_lurugenjin_ok_css"]).click()
        time.sleep(1)
        logger.info(f'设置回访状态{zhuangtai}成功，回访日期三天')
    elif select_time == 7:#一周
        click_kehuliebiao_link(driver)
        time.sleep(1)
        enter_testdata_detail(driver)
        time.sleep(1)
        driver.find_element_by_css_selector(elements["kehuxiangqing_lurugenjin_css"]).click()
        time.sleep(1)
        selector = Select(driver.find_element_by_id(elements["kehuxiangqing_lurugenjin_genjinzhuangtai_id"]))
        selector.select_by_value(zhuangtai)
        time.sleep(1)
        driver.find_elements_by_css_selector(elements["kehuxiangqing_lurugenjin_huifangshijian_yizhou_class"])[
            3].click()
        time.sleep(1)
        driver.find_element_by_id(elements["kehuxiangqing_lurugenjin_bencigenjinneirong_id"]).send_keys('1')
        time.sleep(1)
        driver.find_element_by_css_selector(elements["kehuxiangqing_lurugenjin_ok_css"]).click()
        time.sleep(1)
        logger.info(f'设置回访状态{zhuangtai}成功，回访日期一周')
    elif select_time == 14:#两周
        click_kehuliebiao_link(driver)
        time.sleep(1)
        enter_testdata_detail(driver)
        time.sleep(1)
        driver.find_element_by_css_selector(elements["kehuxiangqing_lurugenjin_css"]).click()
        time.sleep(1)
        selector = Select(driver.find_element_by_id(elements["kehuxiangqing_lurugenjin_genjinzhuangtai_id"]))
        selector.select_by_value(zhuangtai)
        time.sleep(1)
        driver.find_elements_by_css_selector(elements["kehuxiangqing_lurugenjin_huifangshijian_liangzhou_class"])[
            4].click()
        time.sleep(1)
        driver.find_element_by_id(elements["kehuxiangqing_lurugenjin_bencigenjinneirong_id"]).send_keys('1')
        time.sleep(1)
        driver.find_element_by_css_selector(elements["kehuxiangqing_lurugenjin_ok_css"]).click()
        time.sleep(1)
        logger.info(f'设置回访状态{zhuangtai}成功，回访日期两周')
    else:
        pass

#6 设置客户名称和电话
def set_kehumingcheng_kehudianhua(driver):
    click_kehuliebiao_link(driver)
    time.sleep(1)
    enter_testdata_detail(driver)
    time.sleep(1)
    driver.find_elements_by_css_selector(elements["kehuxiangqing_kehumingcheng_css"])[0].send_keys(
        elements["kehuliebiao_test_kehumingcheng"])
    time.sleep(1)
    driver.find_elements_by_css_selector(elements["kehuxiangqing_kehudianhua1_css"])[0].send_keys(
        elements["kehuliebiao_test_kehudianhua1"])
    time.sleep(1)
    driver.find_elements_by_css_selector(elements["kehuxiangqing_kehudianhua2_css"])[1].send_keys(
        elements["kehuliebiao_test_kehudianhua2"])
    time.sleep(1)
    driver.find_element_by_css_selector(elements["kehuxiangqing_kehuxinxi_save_css"]).click()
    time.sleep(1)


#7 测试数据分配
def fenpei_test_data(driver):
    click_kehuliebiao_link(driver)
    time.sleep(3)
    selector = Select(driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_dropdownlist_css"]))
    time.sleep(1)
    selector.select_by_value('1')
    time.sleep(1)
    driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_text_css"]).send_keys(
        elements['kehuliebiao_test_licenseno'])
    time.sleep(1)
    driver.find_element_by_class_name(elements["kehuliebiao_sousuo_button_class"]).click()
    time.sleep(8)

    total = driver.find_element_by_class_name(elements["kehuliebiao_total_count_class"]).text
    logger.info(f'车牌号共搜索出{total}条数据')
    time.sleep(1)
    driver.find_element_by_css_selector(elements["kehuliebiao_select_all_css"]).click()
    time.sleep(1)
    driver.find_elements_by_id(elements["kehuliebiao_fenpei_button_id"])[2].click()
    time.sleep(3)
    driver.find_element_by_css_selector(elements["kehuliebiao_fenpei_button_id_select_yewuyuan_css"]).click()
    time.sleep(1)
    driver.find_element_by_css_selector(elements["kehuliebiao_fenpei_button_id_OK_css"]).click()
    time.sleep(3)
    logger.info(f'客户列表测试数据{elements["kehuliebiao_test_licenseno"]}共{total}条分配成功')
    click_kehuliebiao_link(driver)
    time.sleep(3)



#8 测试数据回收
def huishou_test_data(driver):
    click_kehuliebiao_link(driver)
    time.sleep(3)
    selector = Select(driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_dropdownlist_css"]))
    time.sleep(1)
    selector.select_by_value('1')
    time.sleep(1)
    driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_text_css"]).send_keys(
        elements['kehuliebiao_test_licenseno'])
    time.sleep(1)
    driver.find_element_by_class_name(elements["kehuliebiao_sousuo_button_class"]).click()
    time.sleep(8)

    total = driver.find_element_by_class_name(elements["kehuliebiao_total_count_class"]).text
    logger.info(f'车牌号共搜索出{total}条数据')
    time.sleep(1)
    driver.find_element_by_css_selector(elements["kehuliebiao_select_all_css"]).click()
    time.sleep(1)
    driver.find_elements_by_id(elements["kehuliebiao_huishou_button_id"])[1].click()
    time.sleep(2)
    driver.find_element_by_css_selector(elements["kehuliebiao_huishou_button_id_queren_css"]).click()
    time.sleep(3)
    logger.info(f'客户列表测试数据{elements["kehuliebiao_test_licenseno"]}共{total}条回收成功')


# last 客户列表搜索_验证测试数据
def search_and_check(driver,shuzi,neirong):
    selector = Select(driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_dropdownlist_css"]))
    time.sleep(1)
    selector.select_by_value(shuzi)
    time.sleep(1)
    driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_text_css"]).send_keys(
        elements[neirong])
    time.sleep(1)
    driver.find_element_by_class_name(elements["kehuliebiao_sousuo_button_class"]).click()
    time.sleep(8)
    total = driver.find_element_by_class_name(elements["kehuliebiao_total_count_class"]).text
    try:
        assert total == 1
        logger.info(f'正确共搜索出{total}条数据')
        return True
    except Exception:
        logbug.debug(f'错误共搜索出{total}条数据')
        return False



"""用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例
用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例
用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例
用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例用例"""
# 测试客户列表各tab功能start----------------------------------------------------------------------------------------------
def test_kehuliebiao_tab(driver):
    """客户列表tab测试"""
    time.sleep(2)
    click_kehuliebiao_link(driver)
    time.sleep(1)
    #全部tab
    driver.find_element_by_css_selector(elements["kehuliebiao_quanbu_tab_css"]).click()
    time.sleep(3)
    try:
        search_and_check(driver,'1','kehuliebiao_test_licenseno')
        logger.info(f'客户列表-全部tab-功能正确')
    except Exception:
        logbug.debug("前端--客户列表--全部tab异常")
    finally:
        driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_cancel_css"]).click()
        time.sleep(1)


    #未分配tab
    driver.find_element_by_css_selector(elements["kehuliebiao_weifenpei_tab_css"]).click()
    time.sleep(3)
    try:
        search_and_check(driver,'1','kehuliebiao_test_licenseno')
        logger.info('客户列表-未分配tab-功能正确')
    except Exception:
        logbug.debug("前端--客户列表--未分配tab异常")
    finally:
        driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_cancel_css"]).click()
        time.sleep(1)


    #续保期未回访，数据问题无法测试，仅作冒烟测试
    try:
        driver.find_element_by_css_selector(elements["kehuliebiao_xubaoqiweihuifang_tab_css"]).click()
        time.sleep(1)
        logger.info('客户列表-续保期未回访tab-功能正确')
    except Exception:
        logbug.debug("前端--客户列表--续保期未回访tab异常")



    #计划回访-明天tab
    set_huifang_zhuangtai(driver,'5',1)
    click_kehuliebiao_link(driver)
    driver.find_element_by_css_selector(elements["kehuliebiao_jihuahuifang_tab_css"]).click()
    time.sleep(1)
    driver.find_element_by_css_selector(elements["kehuliebiao_jihuahuifang_mingtian_tab_css"]).click()
    time.sleep(1)
    try:
        search_and_check(driver,'1','kehuliebiao_test_licenseno')
        logger.info('客户列表-计划回访-明天tab-功能正确')
    except Exception:
        logbug.debug("客户列表-计划回访-明天tab-功能异常")
    finally:
        driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_cancel_css"]).click()
        time.sleep(1)


    # 计划回访-今天tab
    set_huifang_zhuangtai(driver,'5', 0)
    click_kehuliebiao_link(driver)
    driver.find_element_by_css_selector(elements["kehuliebiao_jihuahuifang_tab_css"]).click()
    time.sleep(1)
    driver.find_element_by_css_selector(elements["kehuliebiao_jihuahuifang_jintian_tab_css"]).click()
    time.sleep(1)
    try:
        search_and_check(driver, '1', 'kehuliebiao_test_licenseno')
        logger.info('客户列表-计划回访-今天tab-功能正确')
    except Exception:
        logbug.debug("客户列表-计划回访-今天tab-功能异常")
    finally:
        driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_cancel_css"]).click()
        time.sleep(1)


    # 今日进店续保期，数据问题无法测试，仅作冒烟测试
    try:
        driver.find_element_by_css_selector(elements["kehuliebiao_jinrijindianxubaoqi_tab_css"]).click()
        time.sleep(1)
        logger.info('客户列表-今日进店续保期tab-功能正确')
    except Exception:
        logbug.debug("前端--客户列表--今日进店续保期tab异常")

    # 预约到店tab
    set_huifang_zhuangtai(driver,'20',0)
    click_kehuliebiao_link(driver)
    driver.find_element_by_css_selector(elements["kehuliebiao_yuyuedaodian_tab_css"]).click()
    time.sleep(1)
    try:
        search_and_check(driver,'1','kehuliebiao_test_licenseno')
        logger.info('客户列表-计划回访-预约到店tab-功能正确')
    except Exception:
        logbug.debug("客户列表-计划回访-预约到店tab-功能异常")
    finally:
        driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_cancel_css"]).click()
        time.sleep(1)


    # 逾期客户，数据问题无法测试，仅作冒烟测试
    try:
        driver.find_element_by_css_selector(elements["kehuliebiao_yuqikehu_tab_css"]).click()
        time.sleep(1)
        logger.info('客户列表-逾期客户tab-功能正确')
    except Exception:
        logbug.debug("前端--客户列表--逾期客户tab异常")
# 测试客户列表各tab功能end----------------------------------------------------------------------------------------------


# 测试客户列表搜索start-------------------------------------------------------------------------------------------------
def test_kehuliebiao_search(driver):

    click_kehuliebiao_link(driver)
    """搜索start"""
    try: #车牌号搜索
        # selector = Select(driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_dropdownlist_css"]))
        # selector.select_by_value("1")
        # driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_text_css"]).send_keys(elements["kehuliebiao_test_licenseno"])
        # driver.find_element_by_class_name(elements["kehuliebiao_sousuo_button_class"]).click()
        # time.sleep(5)
        search_and_check(driver,'1','kehuliebiao_test_licenseno')
        total = driver.find_element_by_class_name(elements["kehuliebiao_total_count_class"]).text
        logger.info(f'车牌号共搜索出{total}条数据')
        time.sleep(1)
        driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_cancel_css"]).click()
        time.sleep(1)
    except Exception:
        logbug.debug("前端--客户列表--车牌号搜索异常")

    try: #车架号搜索
        # selector.select_by_value("1")
        # driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_text_css"]).send_keys(elements["kehuliebiao_test_VIN"])
        # driver.find_element_by_class_name(elements["kehuliebiao_sousuo_button_class"]).click()
        # time.sleep(5)
        search_and_check(driver, '1', 'kehuliebiao_test_VIN')
        total = driver.find_element_by_class_name(elements["kehuliebiao_total_count_class"]).text
        logger.info(f'车架号共搜索出{total}条数据')
        time.sleep(1)
        driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_cancel_css"]).click()
        time.sleep(1)
    except Exception:
        logbug.debug("前端--客户列表--车架号搜索异常")

    try: #车主姓名搜索
        # selector.select_by_value("2")
        # driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_text_css"]).send_keys(elements["kehuliebiao_test_chezhu"])
        # driver.find_element_by_class_name(elements["kehuliebiao_sousuo_button_class"]).click()
        # time.sleep(5)
        search_and_check(driver, '2', 'kehuliebiao_test_chezhu')
        total = driver.find_element_by_class_name(elements["kehuliebiao_total_count_class"]).text
        logger.info(f'车主姓名共搜索出{total}条数据')
        time.sleep(1)
        driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_cancel_css"]).click()
        time.sleep(1)
    except Exception:
        logbug.debug("前端--客户列表--车主姓名搜索异常")

    try: #客户名称搜索
        # selector = Select(driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_dropdownlist_css"]))
        # selector.select_by_value("3")
        # driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_text_css"]).send_keys(elements["kehuliebiao_test_kehumingcheng"])
        # driver.find_element_by_class_name(elements["kehuliebiao_sousuo_button_class"]).click()
        # time.sleep(5)
        search_and_check(driver, '3', 'kehuliebiao_test_kehumingcheng')
        total = driver.find_element_by_class_name(elements["kehuliebiao_total_count_class"]).text
        logger.info(f'客户名称共搜索出{total}条数据')
        time.sleep(1)
        driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_cancel_css"]).click()
        time.sleep(1)
    except Exception:
        logbug.debug("前端--客户列表--客户名称搜索异常")

    try: #客户电话1搜索
        # selector.select_by_value("4")
        # driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_text_css"]).send_keys(elements["kehuliebiao_test_kehudianhua"])
        # driver.find_element_by_class_name(elements["kehuliebiao_sousuo_button_class"]).click()
        # time.sleep(5)
        search_and_check(driver,'4','kehuliebiao_test_kehudianhua1')
        total = driver.find_element_by_class_name(elements["kehuliebiao_total_count_class"]).text
        logger.info(f'客户电话1共搜索出{total}条数据')
        time.sleep(1)
        driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_cancel_css"]).click()
        time.sleep(1)
    except Exception:
        logbug.debug("前端--客户列表--客户电话1搜索异常")

    try:  # 客户电话2搜索
        # selector.select_by_value("4")
        # driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_text_css"]).send_keys(elements["kehuliebiao_test_kehudianhua"])
        # driver.find_element_by_class_name(elements["kehuliebiao_sousuo_button_class"]).click()
        # time.sleep(5)
        search_and_check(driver, '4', 'kehuliebiao_test_kehudianhua2')
        total = driver.find_element_by_class_name(elements["kehuliebiao_total_count_class"]).text
        logger.info(f'客户电话2共搜索出{total}条数据')
        time.sleep(1)
        driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_cancel_css"]).click()
        time.sleep(1)
    except Exception:
        logbug.debug("前端--客户列表--客户电话2搜索异常")

    """搜索end"""

# 测试客户列表搜索end-------------------------------------------------------------------------------------------------

# 测试客户列表筛选start-------------------------------------------------------------------------------------------------
def test_kehuliebiao_shaixuan(driver):
    click_kehuliebiao_link(driver)

    """筛选start"""
    # try: #商业险到期时间，流程测试
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_button_css"]).click()
    #     time.sleep(3)
    #     driver.find_element_by_id(elements["kehuliebiao_shaixuan_shangyexiandaoqishijian_id"]).click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_shangyexiandaoqishijian_id_queren_css"]).click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_queren_css"]).click()
    #     time.sleep(3)
    #     total = driver.find_element_by_class_name(elements["kehuliebiao_total_count_class"]).text
    #     logger.info(f'客户列表筛选-商业险到期时间共搜索出{total}条数据')
    # except Exception:
    #     logbug.debug("前端--客户列表--商业险到期时间搜索异常")
    # finally:
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_button_css"]).click()
    #     time.sleep(3)
    #     driver.find_element_by_id(elements["kehuliebiao_shaixuan_shangyexiandaoqishijian_id"]).click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(
    #         elements["kehuliebiao_shaixuan_shangyexiandaoqishijian_id_qingchu_css"]).click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_queren_css"]).click()
    #     time.sleep(3)
    #
    #
    # try: #交强险到期时间，流程测试
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_button_css"]).click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_jiaoqiangxiandaoqishijian_css"]).click()
    #     time.sleep(3)
    #     driver.find_elements_by_css_selector(elements["kehuliebiao_shaixuan_jiaoqiangxiandaoqishijian_css_queren_css"])[1].click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_queren_css"]).click()
    #     time.sleep(3)
    #     total = driver.find_element_by_class_name(elements["kehuliebiao_total_count_class"]).text
    #     logger.info(f'客户列表筛选-交强险到期时间共搜索出{total}条数据')
    # except Exception:
    #     logbug.debug("前端--客户列表--交强险到期时间搜索异常")
    # finally:
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_button_css"]).click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_jiaoqiangxiandaoqishijian_css"]).click()
    #     time.sleep(3)
    #     driver.find_elements_by_css_selector(
    #         elements["kehuliebiao_shaixuan_jiaoqiangxiandaoqishijian_css_qingchu_css"])[1].click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_queren_css"]).click()
    #     time.sleep(3)
    #
    #
    # try: #续保状态，流程测试
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_button_css"]).click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_xubaozhuangtai_css"]).click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_xubaozhuangtai_css_quanxuan_css"]).click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_queren_css"]).click()
    #     time.sleep(3)
    #     total = driver.find_element_by_class_name(elements["kehuliebiao_total_count_class"]).text
    #     logger.info(f'客户列表筛选-续保状态共搜索出{total}条数据')
    # except Exception:
    #     logbug.debug("前端--客户列表--续保状态搜索异常")
    # finally:
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_button_css"]).click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_xubaozhuangtai_css"]).click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_xubaozhuangtai_css_quanxuan_css"]).click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_queren_css"]).click()
    #     time.sleep(3)
    #
    #
    # try: #进店时间，流程测试
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_button_css"]).click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_jindianshijian_css"]).click()
    #     time.sleep(3)
    #     driver.find_elements_by_css_selector(elements["kehuliebiao_shaixuan_jindianshijian_css_queren_css"])[2].click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_queren_css"]).click()
    #     time.sleep(3)
    #     total = driver.find_element_by_class_name(elements["kehuliebiao_total_count_class"]).text
    #     logger.info(f'客户列表筛选-续保状态共搜索出{total}条数据')
    # except Exception:
    #     logbug.debug("前端--客户列表--续保状态搜索异常")
    # finally:
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_button_css"]).click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_jindianshijian_css"]).click()
    #     time.sleep(3)
    #     driver.find_elements_by_css_selector(elements["kehuliebiao_shaixuan_jindianshijian_css_qingchu_css"])[2].click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_queren_css"]).click()
    #     time.sleep(3)
    #
    #
    #
    # try: #未分配测试
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_button_css"]).click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_fenpeizhuangtai_weifenpei_css"]).click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_queren_css"]).click()
    #     time.sleep(3)
    #     search_and_check(driver,'1','kehuliebiao_test_licenseno')
    #     time.sleep(5)
    #     total = driver.find_element_by_class_name(elements["kehuliebiao_total_count_class"]).text
    #     logger.info(f'客户列表筛选-未分配搜索出{total}调数据，功能正确')
    # except Exception:
    #     logbug.debug("前端--客户列表--未分配搜索异常")
    # finally:
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_cancel_css"]).click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_button_css"]).click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_fenpeizhuangtai_weifenpei_css"]).click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_queren_css"]).click()
    #     time.sleep(3)
    #
    #
    # try: #已分配测试
    #     fenpei_test_data(driver)
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_button_css"]).click()
    #     time.sleep(3)
    #     driver.find_elements_by_css_selector(elements["kehuliebiao_shaixuan_fenpeizhuangtai_yifenpei_css"])[1].click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_queren_css"]).click()
    #     time.sleep(3)
    #     search_and_check(driver,'1','kehuliebiao_test_licenseno')
    #     time.sleep(5)
    #     total = driver.find_element_by_class_name(elements["kehuliebiao_total_count_class"]).text
    #     logger.info(f'客户列表筛选-已分配搜索出{total}调数据，功能正确')
    # except Exception:
    #     logbug.debug("前端--客户列表--已分配搜索异常")
    # finally:
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_cancel_css"]).click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_button_css"]).click()
    #     time.sleep(3)
    #     driver.find_elements_by_css_selector(elements["kehuliebiao_shaixuan_fenpeizhuangtai_yifenpei_css"])[1].click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_queren_css"]).click()
    #     time.sleep(3)
    #
    #
    #
    #
    # try: #分配时间测试
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_button_css"]).click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_fenpeishijian_css"]).click()
    #     time.sleep(3)
    #     driver.find_elements_by_css_selector(elements["kehuliebiao_shaixuan_fenpeishijian_css_queren_css"])[3].click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_queren_css"]).click()
    #     time.sleep(3)
    #     search_and_check(driver,'1','kehuliebiao_test_licenseno')
    #     time.sleep(5)
    #     total = driver.find_element_by_class_name(elements["kehuliebiao_total_count_class"]).text
    #     logger.info(f'客户列表筛选-分配时间搜索出{total}调数据，功能正确')
    # except Exception:
    #     logbug.debug("前端--客户列表--分配时间搜索异常")
    # finally:
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_cancel_css"]).click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_button_css"]).click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_fenpeishijian_css"]).click()
    #     time.sleep(3)
    #     driver.find_elements_by_css_selector(elements["kehuliebiao_shaixuan_fenpeishijian_css_quxiao_css"])[3].click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_queren_css"]).click()
    #     time.sleep(3)
    #
    #
    #
    # try:  # 业务员测试
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_button_css"]).click()
    #     time.sleep(3)
    #     driver.find_elements_by_css_selector(elements["kehuliebiao_shaixuan_yewuyuan_css"])[1].click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_yewuyuan_css_quanxuan_css"]).click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_queren_css"]).click()
    #     time.sleep(3)
    #     search_and_check(driver, '1', 'kehuliebiao_test_licenseno')
    #     time.sleep(5)
    #     total = driver.find_element_by_class_name(elements["kehuliebiao_total_count_class"]).text
    #     logger.info(f'客户列表筛选-业务员搜索出{total}调数据，功能正确')
    # except Exception:
    #     logbug.debug("前端--客户列表--业务员搜索异常")
    # finally:
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_cancel_css"]).click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_button_css"]).click()
    #     time.sleep(3)
    #     driver.find_elements_by_css_selector(elements["kehuliebiao_shaixuan_yewuyuan_css"])[1].click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_yewuyuan_css_quanxuan_css"]).click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_queren_css"]).click()
    #     time.sleep(3)
    #     huishou_test_data(driver)
    #     time.sleep(3)
    #
    #
    # try:  # 计划回访时间测试
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_button_css"]).click()
    #     time.sleep(3)
    #     #-----------------拖到可见
    #     target = driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_jihuahuifangshijian_css"])
    #     driver.execute_script("arguments[0].scrollIntoView();", target)
    #     # -----------------拖到可见
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_jihuahuifangshijian_css"]).click()
    #     time.sleep(3)
    #     driver.find_elements_by_css_selector(elements["kehuliebiao_shaixuan_jihuahuifangshijian_css_queren_css"])[4].click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_queren_css"]).click()
    #     time.sleep(3)
    #     search_and_check(driver, '1', 'kehuliebiao_test_licenseno')
    #     time.sleep(5)
    #     total = driver.find_element_by_class_name(elements["kehuliebiao_total_count_class"]).text
    #     logger.info(f'客户列表筛选-计划回访时间搜索出{total}调数据，功能正确')
    # except Exception:
    #     logbug.debug("前端--客户列表--计划回访时间搜索异常")
    # finally:
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_cancel_css"]).click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_button_css"]).click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_jihuahuifangshijian_css"]).click()
    #     time.sleep(3)
    #     driver.find_elements_by_css_selector(elements["kehuliebiao_shaixuan_jihuahuifangshijian_css_qingchu_css"])[4].click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_queren_css"]).click()
    #     time.sleep(3)
    #
    #
    # try:  # 录入回访日期测试
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_button_css"]).click()
    #     time.sleep(3)
    #     #-----------------拖到可见
    #     target = driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_luruhuifangriqi_css"])
    #     driver.execute_script("arguments[0].scrollIntoView();", target)
    #     # -----------------拖到可见
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_luruhuifangriqi_css"]).click()
    #     time.sleep(3)
    #     driver.find_elements_by_css_selector(elements["kehuliebiao_shaixuan_luruhuifangriqi_css_queren_css"])[5].click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_queren_css"]).click()
    #     time.sleep(3)
    #     search_and_check(driver, '1', 'kehuliebiao_test_licenseno')
    #     time.sleep(5)
    #     total = driver.find_element_by_class_name(elements["kehuliebiao_total_count_class"]).text
    #     logger.info(f'客户列表筛选-计划回访时间搜索出{total}调数据，功能正确')
    # except Exception:
    #     logbug.debug("前端--客户列表--计划回访时间搜索异常")
    # finally:
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_cancel_css"]).click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_button_css"]).click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_luruhuifangriqi_css"]).click()
    #     time.sleep(3)
    #     driver.find_elements_by_css_selector(elements["kehuliebiao_shaixuan_luruhuifangriqi_css_qingchu_css"])[5].click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_queren_css"]).click()
    #     time.sleep(3)
    #
    #
    #
    # try:  # 报价状态-未报价测试
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_button_css"]).click()
    #     time.sleep(3)
    #     #-----------------拖到可见
    #     target = driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_jindianshijian_css"])
    #     driver.execute_script("arguments[0].scrollIntoView();", target)
    #     # -----------------拖到可见
    #     time.sleep(3)
    #     driver.find_elements_by_css_selector(elements["kehuliebiao_shaixuan_baojiazhuangtai_weibaojia_css"])[2].click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_queren_css"]).click()
    #     time.sleep(3)
    #     # search_and_check(driver, '1', 'kehuliebiao_test_licenseno')
    #     # time.sleep(5)
    #     total = driver.find_element_by_class_name(elements["kehuliebiao_total_count_class"]).text
    #     logger.info(f'客户列表筛选-未报价搜索出{total}调数据，功能正确')
    # except Exception:
    #     logbug.debug("前端--客户列表--未报价搜索异常")
    # finally:
    #     time.sleep(3)
    #     # driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_cancel_css"]).click()
    #     # time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_button_css"]).click()
    #     time.sleep(3)
    #     driver.find_elements_by_css_selector(elements["kehuliebiao_shaixuan_baojiazhuangtai_weibaojia_css"])[2].click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_queren_css"]).click()
    #     time.sleep(3)
    #
    #
    #
    # try:  # 报价状态-报价成功测试
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_button_css"]).click()
    #     time.sleep(3)
    #     #-----------------拖到可见
    #     target = driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_jindianshijian_css"])
    #     driver.execute_script("arguments[0].scrollIntoView();", target)
    #     # -----------------拖到可见
    #     time.sleep(3)
    #     driver.find_elements_by_css_selector(elements["kehuliebiao_shaixuan_baojiazhuangtai_baojiachenggong_css"])[3].click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_queren_css"]).click()
    #     time.sleep(3)
    #     # search_and_check(driver, '1', 'kehuliebiao_test_licenseno')
    #     # time.sleep(5)
    #     total = driver.find_element_by_class_name(elements["kehuliebiao_total_count_class"]).text
    #     logger.info(f'客户列表筛选-报价成功搜索出{total}调数据，功能正确')
    # except Exception:
    #     logbug.debug("前端--客户列表--报价成功搜索异常")
    # finally:
    #     time.sleep(3)
    #     # driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_cancel_css"]).click()
    #     # time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_button_css"]).click()
    #     time.sleep(3)
    #     driver.find_elements_by_css_selector(elements["kehuliebiao_shaixuan_baojiazhuangtai_baojiachenggong_css"])[3].click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_queren_css"]).click()
    #     time.sleep(3)
    #
    #
    #
    # try:  # 报价状态-报价失败测试
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_button_css"]).click()
    #     time.sleep(3)
    #     #-----------------拖到可见
    #     target = driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_jindianshijian_css"])
    #     driver.execute_script("arguments[0].scrollIntoView();", target)
    #     # -----------------拖到可见
    #     time.sleep(3)
    #     driver.find_elements_by_css_selector(elements["kehuliebiao_shaixuan_baojiazhuangtai_baojiashibai_css"])[4].click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_queren_css"]).click()
    #     time.sleep(3)
    #     # search_and_check(driver, '1', 'kehuliebiao_test_licenseno')
    #     # time.sleep(5)
    #     total = driver.find_element_by_class_name(elements["kehuliebiao_total_count_class"]).text
    #     logger.info(f'客户列表筛选-报价成功搜索出{total}调数据，功能正确')
    # except Exception:
    #     logbug.debug("前端--客户列表--报价成功搜索异常")
    # finally:
    #     time.sleep(3)
    #     # driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_cancel_css"]).click()
    #     # time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_button_css"]).click()
    #     time.sleep(3)
    #     driver.find_elements_by_css_selector(elements["kehuliebiao_shaixuan_baojiazhuangtai_baojiashibai_css"])[4].click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_queren_css"]).click()
    #     time.sleep(3)



    try:  # 客户状态测试
        driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_button_css"]).click()
        time.sleep(3)
        #-----------------拖到可见
        target = driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_jindianshijian_css"])
        driver.execute_script("arguments[0].scrollIntoView();", target)
        # -----------------拖到可见
        time.sleep(3)
        driver.find_elements_by_css_selector(elements["kehuliebiao_shaixuan_kehuzhuangtai_css"])[2].click()
        time.sleep(3)
        driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_kehuzhuangtai_css_quanxuan_css"]).click()
        time.sleep(3)
        driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_queren_css"]).click()
        time.sleep(3)
        # search_and_check(driver, '1', 'kehuliebiao_test_licenseno')
        # time.sleep(5)
        total = driver.find_element_by_class_name(elements["kehuliebiao_total_count_class"]).text
        logger.info(f'客户列表筛选-客户状态搜索出{total}调数据，功能正确')
    except Exception:
        logbug.debug("前端--客户列表--客户状态搜索异常")
    finally:
        time.sleep(3)
        # driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_cancel_css"]).click()
        # time.sleep(3)
        driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_button_css"]).click()
        time.sleep(3)
        #-----------------拖到可见
        target = driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_jindianshijian_css"])
        driver.execute_script("arguments[0].scrollIntoView();", target)
        # -----------------拖到可见
        driver.find_elements_by_css_selector(elements["kehuliebiao_shaixuan_kehuzhuangtai_css"])[2].click()
        time.sleep(3)
        driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_kehuzhuangtai_css_quanxuan_css"]).click()
        time.sleep(3)
        driver.find_element_by_css_selector(elements["kehuliebiao_shaixuan_queren_css"]).click()
        time.sleep(3)



def test_kehuliebiao_run(driver):
    clear_and_create_test_data(driver)
    test_kehuliebiao_tab(driver)
    test_kehuliebiao_search(driver)
    test_kehuliebiao_shaixuan(driver)

    driver.close()




if __name__ == '__main__':
    test_kehuliebiao_run()







