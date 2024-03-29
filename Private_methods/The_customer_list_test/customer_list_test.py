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
from selenium.webdriver.common.keys import Keys

log_path = os.path.dirname(os.path.abspath('.')) + "\\Element_methods\customer_list.json"
element = open(log_path, encoding='utf-8')
elements = json.load(element)
shot_path = os.path.dirname(os.path.abspath('.')) + "\\picture"
capturename = os.path.join(shot_path, time.strftime("%Y-%m-%d-%H_%M_%S") + '.png')
logger = Log()
logbug = LogBug()
#客户列表，向右拖拽至最右侧（div是整个table的div）
js = "$('#app > section > section > main > div > div > div.ant-spin-nested-loading > div > div > div:nth-child(1) > div > div.el-table__body-wrapper.is-scrolling-left').scrollLeft('3000')"


class customerlist:
    def customer_list_tab_select(driver,select_tab):
        """客户列表-选择客户列表tab，参数要传具体的tab名称，如‘当期客户’"""
        if select_tab == '当期客户':
            try:
                driver.find_elements_by_css_selector(elements["kehuliebiao_tab_css"])[0].click()
                logger.info(f"{sys._getframe().f_code.co_name},{select_tab} 打开成功")
            except Exception:
                logbug.debug(f"{sys._getframe().f_code.co_name},{select_tab} 打开失败")

        elif select_tab == '首访客户':
            try:
                driver.find_elements_by_css_selector(elements["kehuliebiao_tab_css"])[1].click()
                logger.info(f"{sys._getframe().f_code.co_name},{select_tab} 打开成功")
            except Exception:
                logbug.debug(f"{sys._getframe().f_code.co_name},{select_tab} 打开失败")

        elif select_tab == '未回访':
            try:
                driver.find_elements_by_css_selector(elements["kehuliebiao_tab_css"])[2].click()
                logger.info(f"{sys._getframe().f_code.co_name},{select_tab} 打开成功")
            except Exception:
                logbug.debug(f"{sys._getframe().f_code.co_name},{select_tab} 打开失败")

        elif select_tab == '计划回访':
            try:
                driver.find_elements_by_css_selector(elements["kehuliebiao_tab_css"])[3].click()
                logger.info(f"{sys._getframe().f_code.co_name},{select_tab} 打开成功")
            except Exception:
                logbug.debug(f"{sys._getframe().f_code.co_name},{select_tab} 打开失败")

        elif select_tab == '今日到店':
            try:
                driver.find_elements_by_css_selector(elements["kehuliebiao_tab_css"])[4].click()
                logger.info(f"{sys._getframe().f_code.co_name}{select_tab} 打开成功")
            except Exception:
                logbug.debug(f"{sys._getframe().f_code.co_name}{select_tab} 打开失败")

        elif select_tab == '预约进店':
            try:
                driver.find_elements_by_css_selector(elements["kehuliebiao_tab_css"])[5].click()
                logger.info(f"{sys._getframe().f_code.co_name},{select_tab} 打开成功")
            except Exception:
                logbug.debug(f"{sys._getframe().f_code.co_name},{select_tab} 打开失败")

        elif select_tab == '逾期客户':
            try:
                driver.find_elements_by_css_selector(elements["kehuliebiao_tab_css"])[6].click()
                logger.info(f"{sys._getframe().f_code.co_name},{select_tab} 打开成功")
            except Exception:
                logbug.debug(f"{sys._getframe().f_code.co_name},{select_tab} 打开失败")

        elif select_tab == '全部客户':
            try:
                driver.find_elements_by_css_selector(elements["kehuliebiao_tab_css"])[7].click()
                logger.info(f"{sys._getframe().f_code.co_name},{select_tab} 打开成功")
            except Exception:
                logbug.debug(f"{sys._getframe().f_code.co_name},{select_tab} 打开失败")
        else:
            pass


    def search_1_0_chepai(driver,input_chepai = elements["test_licenseno"]):
        """客户列表-车牌号搜索，参数要传具体车牌，如‘京J97896’"""
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_dropdown_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_dropdown_selection1_chepaichejia_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_textbox_css"]).send_keys(input_chepai)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_chepai} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_chepai} 搜索失败')

    def search_1_0_chepai_gotofirst_detail(driver,input_chepai = elements["test_licenseno"]):
        """客户列表-进入搜索车牌的详情，参数要传具体车牌，如‘京J97896’"""
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_dropdown_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_dropdown_selection1_chepaichejia_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_textbox_css"]).send_keys(input_chepai)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_button_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_chepaihao_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},进入{input_chepai} 详情成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},进入{input_chepai} 详情失败')

    def search_1_1_chejia(driver,input_chejia = elements["test_vin"]):
        """客户列表-车架号搜索，参数要传具体车架，如‘LS5A3ADD7CB152216’"""
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_dropdown_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_dropdown_selection1_chepaichejia_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_textbox_css"]).send_keys(input_chejia)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_chejia} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_chejia} 搜索失败')


    def search_1_2_chezhuxingming(driver,input_chezhuxingming = elements["test_chezhuxingming"]):
        """客户列表-车主姓名搜索，参数要传具体车主姓名，如‘梁浩’"""
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_dropdown_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_dropdown_selection2_chezhuxingming_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_textbox_css"]).send_keys(input_chezhuxingming)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_chezhuxingming} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_chezhuxingming} 搜索失败')

    def search_1_3_kehudianhua(driver, input_kehudianhua=elements["test_kehudianhua1"]):
        """客户列表-客户电话搜索，参数要传具体电话，如‘13666668888’"""
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_dropdown_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_dropdown_selection3_kehudianhua_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_textbox_css"]).send_keys(
                input_kehudianhua)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_kehudianhua} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_kehudianhua} 搜索失败')

    def search_1_4_kehuxingming(driver,input_kehuxingming = elements["test_kehuxingming"]):
        """客户列表-客户姓名搜索，参数要传具体客户姓名，如‘梁浩途观’"""
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_dropdown_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_dropdown_selection4_kehuxingming_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_textbox_css"]).send_keys(input_kehuxingming)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_kehuxingming} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_kehuxingming} 搜索失败')

    def search_2_daoqishijian(driver, input_daoqishijian='2019-01-11+2019-01-12'):
        """客户列表-到期时间搜索，参数要传时间格式，包括起始时间和结束时间，必须传递两个时间，中间加号分割,如‘2019-01-01+2019-01-02’
        另：时间必须真实存在，且与业务要求吻合，不要输入不存在，不可选择的时间"""
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo2_daoqishijian_css"]).click()
            time.sleep(1)
            input_daoqishijian = input_daoqishijian.split('+')
            driver.find_element_by_css_selector(
                elements["kehuliebiao_sousuo2_daoqishijian_qishishijian_css"]).send_keys(
                input_daoqishijian[0])
            time.sleep(1)
            driver.find_element_by_css_selector(
                elements["kehuliebiao_sousuo2_daoqishijian_jieshushijian_css"]).send_keys(
                input_daoqishijian[1])
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_daoqishijian} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_daoqishijian} 搜索失败')


    def search_3_kehuleibie(driver, input_kehuleibie='新转续+续转续+潜转续+间转续+进店+空值'):
        """客户列表-客户类别搜索，参数要传具体类别，可以单个也可以多传，中间加号分隔，文字必须保持和列表一致，如‘新转续+空值’"""
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuliebiao_sousuo3_kehuleibie_css"]).click()
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo3_kehuleibie_css"]).click()
            time.sleep(1)
            input_kehuleibie = input_kehuleibie.split('+')
            for kehuleibie in input_kehuleibie:
                driver.find_element_by_css_selector(elements["kehuliebiao_sousuo3_kehuleibie_input_css"]).send_keys(kehuleibie)
                time.sleep(1)
                driver.find_element_by_css_selector(elements["kehuliebiao_sousuo3_kehuleibie_selection_css"]).click()
                time.sleep(1)
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuliebiao_sousuo3_kehuleibie_dropdown_input_css"]).
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_kehuleibie} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_kehuleibie} 搜索失败')


    def search_4_pinpaixinghao(driver, input_pinpaixinghao=elements["test_kehudianhua1"]):
        """客户列表-品牌型号搜索，参数要传具体品牌型号，如‘长安SC7103G轿车’"""
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuliebiao_sousuo3_kehuleibie_css"]).click()
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo4_pinpaixinghao_css"]).send_keys(input_pinpaixinghao)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_pinpaixinghao} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_pinpaixinghao} 搜索失败')

    def search_5_shangniantoubaogongsi(driver, input_shangniantoubaogongsi=elements["test_shangniantoubaogongsi"]):
        """客户列表-上年投保公司搜索，参数可模糊传递，但必须保证列表中能搜索到结果，如‘人保’‘人’都可以，选择搜索结果中第一个"""
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo5_shangniantoubaogongsi_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo5_shangniantoubaogongsi_input_css"]).send_keys(input_shangniantoubaogongsi)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo5_shangniantoubaogongsi_select_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_shangniantoubaogongsi} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_shangniantoubaogongsi} 搜索失败')

    def search_6_shangchuanpici(driver, input_shangchuanpici='6956'):
        """客户列表-上传批次搜索，参数可模糊传递，但必须保证列表中能搜索到结果，如‘批次a’‘a’都可以，选择搜索结果中第一个"""
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo6_shangchuanpici_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo6_shangchuanpici_input_css"]).send_keys(input_shangchuanpici)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo6_shangchuanpici_select_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_shangchuanpici} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_shangchuanpici} 搜索失败')


    def search_7_shangyedaoqishijian(driver, input_shangyedaoqishijian='2019-01-11+2019-01-12'):
        """客户列表-商业到期时间搜索，参数要传时间格式，包括起始时间和结束时间，必须传递两个时间，中间加号分割,如‘2019-01-01+2019-01-02’
        另：时间必须真实存在，且与业务要求吻合，不要输入不存在，不可选择的时间"""
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo7_shangyedaoqishijian_css"]).click()
            time.sleep(1)
            input_shangyedaoqishijian=input_shangyedaoqishijian.split('+')
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo7_shangyedaoqishijian_qishishijian_css"]).send_keys(input_shangyedaoqishijian[0])
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo7_shangyedaoqishijian_jieshushijian_css"]).send_keys(input_shangyedaoqishijian[1])
            time.sleep(1)
            #点一下别处，收回时间框
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_textbox_css"]).click()
            time.sleep(1)
            # 点一下别处，收回时间框
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_shangyedaoqishijian} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_shangyedaoqishijian} 搜索失败')


    def search_8_jiaoqiangdaoqishijian(driver, input_jiaoqiangdaoqishijian='2019-01-11+2019-01-12'):
        """客户列表-交强到期时间搜索，参数要传时间格式，包括起始时间和结束时间，必须传递两个时间，中间加号分割,如‘2019-01-01+2019-01-02’
        另：时间必须真实存在，且与业务要求吻合，不要输入不存在，不可选择的时间"""
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo8_jiaoqiangdaoqishijian_css"]).click()
            time.sleep(1)
            input_jiaoqiangdaoqishijian = input_jiaoqiangdaoqishijian.split('+')
            driver.find_element_by_css_selector(
                elements["kehuliebiao_sousuo8_jiaoqiangdaoqishijian_qishishijian_css"]).send_keys(
                input_jiaoqiangdaoqishijian[0])
            time.sleep(1)
            driver.find_element_by_css_selector(
                elements["kehuliebiao_sousuo8_jiaoqiangdaoqishijian_jieshushijian_css"]).send_keys(
                input_jiaoqiangdaoqishijian[1])
            time.sleep(1)
            #点一下别处，收回时间框
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_textbox_css"]).click()
            time.sleep(1)
            # 点一下别处，收回时间框
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_jiaoqiangdaoqishijian} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_jiaoqiangdaoqishijian} 搜索失败')

    def search_9_shangyedaoqiyuefen(driver, input_shangyedaoqiyuefen='01月份到期'):
        """客户列表-商业到期月份搜索，参数要传具体月份，与下拉框文本保持一致，如‘01月份到期’"""
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo9_shangyedaoqiyuefen_css"]).click()
            time.sleep(1)
            if input_shangyedaoqiyuefen == '01月份到期':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo9_shangyedaoqiyuefen_select_css"])[0].click()
                time.sleep(1)
            elif input_shangyedaoqiyuefen == '02月份到期':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo9_shangyedaoqiyuefen_select_css"])[1].click()
                time.sleep(1)
            elif input_shangyedaoqiyuefen == '03月份到期':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo9_shangyedaoqiyuefen_select_css"])[2].click()
                time.sleep(1)
            elif input_shangyedaoqiyuefen == '04月份到期':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo9_shangyedaoqiyuefen_select_css"])[3].click()
                time.sleep(1)
            elif input_shangyedaoqiyuefen == '05月份到期':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo9_shangyedaoqiyuefen_select_css"])[4].click()
                time.sleep(1)
            elif input_shangyedaoqiyuefen == '06月份到期':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo9_shangyedaoqiyuefen_select_css"])[5].click()
                time.sleep(1)
            elif input_shangyedaoqiyuefen == '07月份到期':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo9_shangyedaoqiyuefen_select_css"])[6].click()
                time.sleep(1)
            elif input_shangyedaoqiyuefen == '08月份到期':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo9_shangyedaoqiyuefen_select_css"])[7].click()
                time.sleep(1)
            elif input_shangyedaoqiyuefen == '09月份到期':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo9_shangyedaoqiyuefen_select_css"])[8].click()
                time.sleep(1)
            elif input_shangyedaoqiyuefen == '10月份到期':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo9_shangyedaoqiyuefen_select_css"])[9].click()
                time.sleep(1)
            elif input_shangyedaoqiyuefen == '11月份到期':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo9_shangyedaoqiyuefen_select_css"])[10].click()
                time.sleep(1)
            elif input_shangyedaoqiyuefen == '12月份到期':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo9_shangyedaoqiyuefen_select_css"])[11].click()
                time.sleep(1)
            else:
                pass

            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_shangyedaoqiyuefen} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_shangyedaoqiyuefen} 搜索失败')

    def search_10_jiaoqiangdaoqiyuefen(driver, input_jiaoqiangdaoqiyuefen='01月份到期'):
        """客户列表-交强到期月份搜索，参数要传具体月份，与下拉框文本保持一致，如‘01月份到期’"""
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo10_jiaoqiangdaoqiyuefen_css"]).click()
            time.sleep(1)
            if input_jiaoqiangdaoqiyuefen == '01月份到期':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo10_jiaoqiangdaoqiyuefen_select_css"])[0].click()
                time.sleep(1)
            elif input_jiaoqiangdaoqiyuefen == '02月份到期':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo10_jiaoqiangdaoqiyuefen_select_css"])[1].click()
                time.sleep(1)
            elif input_jiaoqiangdaoqiyuefen == '03月份到期':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo10_jiaoqiangdaoqiyuefen_select_css"])[2].click()
                time.sleep(1)
            elif input_jiaoqiangdaoqiyuefen == '04月份到期':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo10_jiaoqiangdaoqiyuefen_select_css"])[3].click()
                time.sleep(1)
            elif input_jiaoqiangdaoqiyuefen == '05月份到期':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo10_jiaoqiangdaoqiyuefen_select_css"])[4].click()
                time.sleep(1)
            elif input_jiaoqiangdaoqiyuefen == '06月份到期':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo10_jiaoqiangdaoqiyuefen_select_css"])[5].click()
                time.sleep(1)
            elif input_jiaoqiangdaoqiyuefen == '07月份到期':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo10_jiaoqiangdaoqiyuefen_select_css"])[6].click()
                time.sleep(1)
            elif input_jiaoqiangdaoqiyuefen == '08月份到期':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo10_jiaoqiangdaoqiyuefen_select_css"])[7].click()
                time.sleep(1)
            elif input_jiaoqiangdaoqiyuefen == '09月份到期':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo10_jiaoqiangdaoqiyuefen_select_css"])[8].click()
                time.sleep(1)
            elif input_jiaoqiangdaoqiyuefen == '10月份到期':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo10_jiaoqiangdaoqiyuefen_select_css"])[9].click()
                time.sleep(1)
            elif input_jiaoqiangdaoqiyuefen == '11月份到期':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo10_jiaoqiangdaoqiyuefen_select_css"])[10].click()
                time.sleep(1)
            elif input_jiaoqiangdaoqiyuefen == '12月份到期':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo10_jiaoqiangdaoqiyuefen_select_css"])[11].click()
                time.sleep(1)
            else:
                pass
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_jiaoqiangdaoqiyuefen} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_jiaoqiangdaoqiyuefen} 搜索失败')


    def search_11_zhuceshijian(driver, input_zhuceshijian='2019-01-11+2019-01-12'):
        """客户列表-注册时间搜索，参数要传时间格式，包括起始时间和结束时间，必须传递两个时间，中间加号分割,如‘2019-01-01+2019-01-02’
        另：时间必须真实存在，且与业务要求吻合，不要输入不存在，不可选择的时间"""
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo11_zhuceshijian_css"]).click()
            time.sleep(1)
            input_zhuceshijian = input_zhuceshijian.split('+')
            driver.find_element_by_css_selector(
                elements["kehuliebiao_sousuo11_zhuceshijian_qishishijian_css"]).send_keys(
                input_zhuceshijian[0])
            time.sleep(1)
            driver.find_element_by_css_selector(
                elements["kehuliebiao_sousuo11_zhuceshijian_jieshushijian_css"]).send_keys(
                input_zhuceshijian[1])
            time.sleep(1)
            #点一下别处，收回时间框
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_textbox_css"]).click()
            time.sleep(1)
            # 点一下别处，收回时间框
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_zhuceshijian} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_zhuceshijian} 搜索失败')



    def search_12_zhuceyuefen(driver, input_zhuceyuefen='02月份'):
        """客户列表-注册月份搜索，参数要传具体月份，与下拉框文本保持一致，如‘01月份’"""
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo12_zhuceyuefen_css"]).click()
            time.sleep(1)
            if input_zhuceyuefen == '01月份':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo12_zhuceyuefen_dropdown_css"])[0].click()
                time.sleep(1)
            elif input_zhuceyuefen == '02月份':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo12_zhuceyuefen_dropdown_css"])[1].click()
                time.sleep(1)
            elif input_zhuceyuefen == '03月份':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo12_zhuceyuefen_dropdown_css"])[2].click()
                time.sleep(1)
            elif input_zhuceyuefen == '04月份':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo12_zhuceyuefen_dropdown_css"])[3].click()
                time.sleep(1)
            elif input_zhuceyuefen == '05月份':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo12_zhuceyuefen_dropdown_css"])[4].click()
                time.sleep(1)
            elif input_zhuceyuefen == '06月份':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo12_zhuceyuefen_dropdown_css"])[5].click()
                time.sleep(1)
            elif input_zhuceyuefen == '07月份':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo12_zhuceyuefen_dropdown_css"])[6].click()
                time.sleep(1)
            elif input_zhuceyuefen == '08月份':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo12_zhuceyuefen_dropdown_css"])[7].click()
                time.sleep(1)
            elif input_zhuceyuefen == '09月份':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo12_zhuceyuefen_dropdown_css"])[8].click()
                time.sleep(1)
            elif input_zhuceyuefen == '10月份':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo12_zhuceyuefen_dropdown_css"])[9].click()
                time.sleep(1)
            elif input_zhuceyuefen == '11月份':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo12_zhuceyuefen_dropdown_css"])[10].click()
                time.sleep(1)
            elif input_zhuceyuefen == '12月份':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo12_zhuceyuefen_dropdown_css"])[11].click()
                time.sleep(1)
            else:
                pass
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_zhuceyuefen} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_zhuceyuefen} 搜索失败')


    def search_13_kehuzhuangtai(driver, input_kehuzhuangtai='0+1+2+3+4'):
        """客户列表-客户状态搜索，参数可模糊传递，但必须保证列表中能搜索到结果，可以单个也可以多传，中间加号分隔，文字必须保持和列表一致，
        如‘预约到店+战败’都可以，选择搜索结果中第一个"""
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo13_kehuzhuangtai_css"]).click()
            time.sleep(1)
            input_kehuzhuangtai = input_kehuzhuangtai.split('+')
            for kehuzhuangtai in input_kehuzhuangtai:
                driver.find_element_by_css_selector(elements["kehuliebiao_sousuo13_kehuzhuangtai_input_css"]).send_keys(kehuzhuangtai)
                time.sleep(1)
                driver.find_element_by_css_selector(elements["kehuliebiao_sousuo13_kehuzhuangtai_select_css"]).click()
                time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_kehuzhuangtai} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_kehuzhuangtai} 搜索失败')


    def search_14_xubaozhuangtai(driver, input_xubaozhuangtai='0+1+2+3'):
        """客户列表-续保状态搜索，参数可单独传递，如‘续保失败’，也可多传，如'续保失败+续保成功+报价解析+只取到行驶本+未处理'，中间加号分隔"""
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo14_xubaozhuangtai_css"]).click()
            time.sleep(1)
            input_xubaozhuangtai=input_xubaozhuangtai.split('+')
            for xubaozhuangtai in input_xubaozhuangtai:
                driver.find_element_by_css_selector(elements["kehuliebiao_sousuo14_xubaozhuangtai_input_css"]).send_keys(xubaozhuangtai)
                time.sleep(1)
                driver.find_element_by_css_selector(elements["kehuliebiao_sousuo14_xubaozhuangtai_select_css"]).click()
                time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_xubaozhuangtai}, 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_xubaozhuangtai},搜索失败')

    def search_15_baojiazhuangtai(driver, input_baojiazhuangtai='未报价+报价失败+报价成功'):
        """客户列表-报价状态搜索，参数可单独传递，如‘报价失败’，也可多传，如'报价失败+未报价+成功+失败+重复投保'，中间加号分隔"""
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo15_baojiazhuangtai_css"]).click()
            time.sleep(1)
            input_baojiazhuangtai=input_baojiazhuangtai.split('+')
            for baojiazhuangtai in input_baojiazhuangtai:
                driver.find_element_by_css_selector(elements["kehuliebiao_sousuo15_baojiazhuangtai_input_css"]).send_keys(baojiazhuangtai)
                time.sleep(1)
                driver.find_element_by_css_selector(elements["kehuliebiao_sousuo15_baojiazhuangtai_select_css"]).click()
                time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_baojiazhuangtai} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_baojiazhuangtai} 搜索失败')


    def search_16_fenpeizhuangtai(driver, input_fenpeizhuangtai='未分配+已分配'):
        """客户列表-分配状态搜索，参数可单独传递，如‘未分配’，也可多传，如'未分配+已分配'，中间加号分隔"""
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            input_fenpeizhuangtai = input_fenpeizhuangtai.split('+')
            for fenpeizhuangtai in input_fenpeizhuangtai:
                if fenpeizhuangtai == '未分配':
                    driver.find_element_by_css_selector(elements["kehuliebiao_sousuo16_fenpeizhuangtai_weifenpei_css"]).click()
                    time.sleep(1)
                if fenpeizhuangtai == '已分配':
                    driver.find_element_by_css_selector(elements["kehuliebiao_sousuo16_fenpeizhuangtai_yifenpei_css"]).click()
                    time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_fenpeizhuangtai} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_fenpeizhuangtai} 搜索失败')



    def search_17_fenpeishijian(driver, input_fenpeishijian='2019-01-11+2019-01-12'):
        """客户列表-分配时间搜索，参数要传时间格式，包括起始时间和结束时间，必须传递两个时间，中间加号分割,如‘2019-01-01+2019-01-02’
        另：时间必须真实存在，且与业务要求吻合，不要输入不存在，不可选择的时间"""
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo17_fenpeishijian_css"]).click()
            time.sleep(1)
            input_fenpeishijian = input_fenpeishijian.split('+')
            driver.find_element_by_css_selector(
                elements["kehuliebiao_sousuo17_fenpeishijian_qishishijian_css"]).send_keys(
                input_fenpeishijian[0])
            time.sleep(1)
            driver.find_element_by_css_selector(
                elements["kehuliebiao_sousuo17_fenpeishijian_jieshushijian_css"]).send_keys(
                input_fenpeishijian[1])
            time.sleep(1)
            #点一下别处，收回时间框
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_textbox_css"]).click()
            time.sleep(1)
            # 点一下别处，收回时间框
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuliebiao_sousuo16_fenpeizhuangtai_yifenpei_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_fenpeishijian} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_fenpeishijian} 搜索失败')


    def search_18_yuyueshijian(driver, input_yuyueshijian='2019-01-11+2019-01-12'):
        """客户列表-预约时间搜索，参数要传时间格式，包括起始时间和结束时间，必须传递两个时间，中间加号分割,如‘2019-01-01+2019-01-02’
        另：时间必须真实存在，且与业务要求吻合，不要输入不存在，不可选择的时间"""
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo18_yuyueshijian_css"]).click()
            time.sleep(1)
            input_yuyueshijian = input_yuyueshijian.split('+')
            driver.find_element_by_css_selector(
                elements["kehuliebiao_sousuo18_yuyueshijian_qishishijian_css"]).send_keys(
                input_yuyueshijian[0])
            time.sleep(1)
            driver.find_element_by_css_selector(
                elements["kehuliebiao_sousuo18_yuyueshijian_jieshushijian_css"]).send_keys(
                input_yuyueshijian[1])
            time.sleep(1)
            #点一下别处，收回时间框
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_textbox_css"]).click()
            time.sleep(1)
            # 点一下别处，收回时间框
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_yuyueshijian} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_yuyueshijian} 搜索失败')


    def search_19_huifangshijian(driver, input_huifangshijian='2019-01-11+2019-01-12'):
        """客户列表-回访时间搜索，参数要传时间格式，包括起始时间和结束时间，必须传递两个时间，中间加号分割,如‘2019-01-01+2019-01-02’
        另：时间必须真实存在，且与业务要求吻合，不要输入不存在，不可选择的时间"""
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo19_huifangshijian_css"]).click()
            time.sleep(1)
            input_huifangshijian = input_huifangshijian.split('+')
            driver.find_element_by_css_selector(
                elements["kehuliebiao_sousuo19_huifangshijian_qishishijian_css"]).send_keys(
                input_huifangshijian[0])
            time.sleep(1)
            driver.find_element_by_css_selector(
                elements["kehuliebiao_sousuo19_huifangshijian_jieshushijian_css"]).send_keys(
                input_huifangshijian[1])
            time.sleep(1)
            #点一下别处，收回时间框
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_textbox_css"]).click()
            time.sleep(1)
            # 点一下别处，收回时间框
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_huifangshijian} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_huifangshijian} 搜索失败')


    def search_20_lurufangshi(driver, input_lurufangshi='摄像头+PC录入+批量导入+APP+微信+小程序录入+新车批改'):
        """客户列表-录入方式搜索，参数可单独传递，如‘摄像头’，也可多传，如'摄像头+PC录入+批量导入+APP+微信'，中间加号分隔"""
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo20_lurufangshi_css"]).click()
            time.sleep(1)
            input_lurufangshi = input_lurufangshi.split('+')
            for lurufangshi in input_lurufangshi:
                driver.find_element_by_css_selector(elements["kehuliebiao_sousuo20_lurufangshi_input_css"]).send_keys(lurufangshi)
                time.sleep(1)
                driver.find_element_by_css_selector(elements["kehuliebiao_sousuo20_lurufangshi_select_css"]).click()
                time.sleep(1)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_lurufangshi} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_lurufangshi} 搜索失败')


    def search_21_jindianshijian(driver, input_jindianshijian='2019-01-11+2019-01-12'):
        """客户列表-进店时间搜索，参数要传时间格式，包括起始时间和结束时间，必须传递两个时间，中间加号分割,如‘2019-01-01+2019-01-02’
        另：时间必须真实存在，且与业务要求吻合，不要输入不存在，不可选择的时间"""
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo21_jindianshijian_css"]).click()
            time.sleep(1)
            input_jindianshijian = input_jindianshijian.split('+')
            driver.find_element_by_css_selector(
                elements["kehuliebiao_sousuo21_jindianshijian_qishishijian_css"]).send_keys(
                input_jindianshijian[0])
            time.sleep(1)
            driver.find_element_by_css_selector(
                elements["kehuliebiao_sousuo21_jindianshijian_jieshushijian_css"]).send_keys(
                input_jindianshijian[1])
            time.sleep(1)
            #点一下别处，收回时间框
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_textbox_css"]).click()
            time.sleep(1)
            # 点一下别处，收回时间框
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_jindianshijian} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_jindianshijian} 搜索失败')


    def search_22_kehudianhua(driver, input_kehudianhua='有+无'):
        """客户列表-客户电话搜索，参数可单独传递，如‘有’，也可多传，如'有+无'，中间加号分隔"""
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            input_kehudianhua = input_kehudianhua.split('+')
            for kehudianhua in input_kehudianhua:
                if kehudianhua == '有':
                    driver.find_element_by_css_selector(elements["kehuliebiao_sousuo22_kehudianhua_you_css"]).click()
                    time.sleep(1)
                if kehudianhua == '无':
                    driver.find_element_by_css_selector(elements["kehuliebiao_sousuo22_kehehudianhua_wu_css"]).click()
                    time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_kehudianhua} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_kehudianhua} 搜索失败')



    def search_23_yewuyuan(driver, input_yewuyuan='测试+效果'):
        """客户列表-业务员搜索，参数可单独传递，如‘梁浩’，也可多传，如'梁浩+武延军+刘静怡'，但必须保证列表中能搜索到结果，选择搜索结果中第一个"""
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo23_yewuyuan_css"]).click()
            time.sleep(1)
            input_yewuyuan = input_yewuyuan.split('+')
            for yewuyuan in input_yewuyuan:
                driver.find_element_by_css_selector(elements["kehuliebiao_sousuo23_yewuyuan_input_css"]).send_keys(yewuyuan)
                time.sleep(1)
                driver.find_element_by_css_selector(elements["kehuliebiao_sousuo23_yewuyuan_select_css"]).click()
                time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_yewuyuan} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_yewuyuan} 搜索失败')


    def search_24_bumenmingcheng(driver, input_bumenmingcheng='2+1'):
        """客户列表-部门名称搜索，参数可单独传递，如‘电销1部’，也可多传，如'电销1部+测试1部'，但必须保证列表中能搜索到结果，选择搜索结果中第一个"""
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo24_bumenmingcheng_css"]).click()
            time.sleep(1)
            input_bumenmingcheng = input_bumenmingcheng.split('+')
            for bumenmingcheng in input_bumenmingcheng:
                driver.find_element_by_css_selector(elements["kehuliebiao_sousuo24_bumenmingcheng_input_css"]).send_keys(bumenmingcheng)
                time.sleep(1)
                driver.find_element_by_css_selector(elements["kehuliebiao_sousuo24_bumenmingcheng_select_css"]).click()
                time.sleep(1)
            #点一下别处，收回时间框
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_textbox_css"]).click()
            time.sleep(1)
            # 点一下别处，收回时间框
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_bumenmingcheng} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_bumenmingcheng} 搜索失败')

    def search_25_gengxinshijian(driver, input_gengxinshijian='2019-01-11+2019-01-12'):
        """客户列表-跟进时间搜索，参数要传时间格式，包括起始时间和结束时间，必须传递两个时间，中间加号分割,如‘2019-01-01+2019-01-02’
        另：时间必须真实存在，且与业务要求吻合，不要输入不存在，不可选择的时间"""
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo25_gengxinshijian_css"]).click()
            time.sleep(1)
            input_gengxinshijian = input_gengxinshijian.split('+')
            driver.find_element_by_css_selector(
                elements["kehuliebiao_sousuo25_gengxinshijian_qishishijian_css"]).send_keys(
                input_gengxinshijian[0])
            time.sleep(1)
            driver.find_element_by_css_selector(
                elements["kehuliebiao_sousuo25_gengxinshijian_jieshushijian_css"]).send_keys(
                input_gengxinshijian[1])
            time.sleep(1)
            #点一下别处，收回时间框
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_textbox_css"]).click()
            time.sleep(1)
            # 点一下别处，收回时间框
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_gengxinshijian} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_gengxinshijian} 搜索失败')


    def search_26_shifougenjin(driver, input_shifougenjin='否'):
        """客户列表-是否跟进搜索，参数要传是或否,如‘是’"""
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo26_shifougenjin_css"]).click()
            time.sleep(1)
            if input_shifougenjin == '是':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo26_bumenmingcheng_select_css"])[0].click()
                time.sleep(1)
            elif input_shifougenjin == '否':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo26_bumenmingcheng_select_css"])[1].click()
                time.sleep(1)
            #点一下别处，收回时间框
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_textbox_css"]).click()
            time.sleep(1)
            # 点一下别处，收回时间框
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_shifougenjin} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_shifougenjin} 搜索失败')


# 以下为客户列表check方法

    def kehuliebiao_check_chepaihao(driver, input_chepaihao = elements["test_licenseno"]):
        """客户列表-验证列表中第一个车牌号，参数传车牌号即可，如‘京PG1776’"""
        try:
            if input_chepaihao == driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_chepaihao_css"]).text:
                logger.info(f'{sys._getframe().f_code.co_name}, 期望结果{input_chepaihao},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_chepaihao_css"]).text},结果正确')
            else:
                logbug.debug(
                    f'{sys._getframe().f_code.co_name}, 期望结果{input_chepaihao},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_chepaihao_css"]).text},结果错误')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},功能有误')


    # def kehuliebiao_check_kehumingcheng(driver, input_kehumingcheng = elements["test_kehuxingming"]):
    #     """客户列表-验证列表中第一个到期天数，参数传具体时间即可，格式要和页面保持一致，如‘xx测试’"""
    #     try:
    #         if input_kehumingcheng == driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_kehumingcheng_css"]).text:
    #             logger.info(f'{sys._getframe().f_code.co_name}, 期望结果{input_kehumingcheng},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_kehumingcheng_css"]).text},结果正确')
    #         else:
    #             logbug.debug(
    #                 f'{sys._getframe().f_code.co_name}, 期望结果{input_kehumingcheng},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_kehumingcheng_css"]).text},结果错误')
    #     except Exception:
    #         logbug.debug(f'{sys._getframe().f_code.co_name},功能有误')


    def kehuliebiao_check_chejiahao(driver, input_chejiahao = elements["test_vin"]):
        """客户列表-验证列表中第一个车架号，参数传具体车架号即可，如‘LFV3A23C8D3078082’"""
        try:
            if input_chejiahao == driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_chejiahao_css"]).text:
                logger.info(f'{sys._getframe().f_code.co_name}, 期望结果{input_chejiahao},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_chejiahao_css"]).text},结果正确')
            else:
                logbug.debug(
                    f'{sys._getframe().f_code.co_name}, 期望结果{input_chejiahao},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_chejiahao_css"]).text},结果错误')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},功能有误')

    def kehuliebiao_check_pinpaixinghao(driver, input_pinpaixinghao = elements["test_vin"]):
        """客户列表-验证列表中第一个品牌型号，参数传具体品牌型号即可，如‘大众FV7207FCDWG轿车’"""
        try:
            if input_pinpaixinghao == driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_pinpaixinghao_css"]).text:
                logger.info(f'{sys._getframe().f_code.co_name}, 期望结果{input_pinpaixinghao},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_pinpaixinghao_css"]).text},结果正确')
            else:
                logbug.debug(
                    f'{sys._getframe().f_code.co_name}, 期望结果{input_pinpaixinghao},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_pinpaixinghao_css"]).text},结果错误')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},功能有误')


    def kehuliebiao_check_zhuceriqi(driver, input_zhuceriqi = elements["test_zhuceriqi"]):
        """客户列表-验证列表中第一个注册日期，参数传具体日期即可，格式为yyyy-mm-dd，如‘2017-07-06’"""
        try:
            if input_zhuceriqi == driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_zhuceriqi_css"]).text:
                logger.info(f'{sys._getframe().f_code.co_name}, 期望结果{input_zhuceriqi},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_zhuceriqi_css"]).text},结果正确')
            else:
                logbug.debug(
                    f'{sys._getframe().f_code.co_name}, 期望结果{input_zhuceriqi},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_zhuceriqi_css"]).text},结果错误')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},功能有误')

    def kehuliebiao_check_shangniantoubaogongsi(driver, input_shangniantoubaogongsi = elements["test_shangniantoubaogongsi"]):
        """客户列表-验证列表中第一个上年投保公司，参数传具体公司即可，内容保持和列表文字一致，如‘人保车险’"""
        try:
            if input_shangniantoubaogongsi == driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_shangniantoubaogongsi_css"]).text:
                logger.info(f'{sys._getframe().f_code.co_name}, 期望结果{input_shangniantoubaogongsi},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_shangniantoubaogongsi_css"]).text},结果正确')
            else:
                logbug.debug(
                    f'{sys._getframe().f_code.co_name}, 期望结果{input_shangniantoubaogongsi},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_shangniantoubaogongsi_css"]).text},结果错误')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},功能有误')

    def kehuliebiao_check_shangyedaoqi(driver, input_shangyedaoqi = '2019-03-09 23:59:59'):
        """客户列表-验证列表中第一个商业到期时间，参数传具体时间即可，内容保持和列表文字一致，如‘2019-03-09 23:59:59’"""
        try:
            if input_shangyedaoqi == driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_shangyedaoqi_css"]).text:
                logger.info(f'{sys._getframe().f_code.co_name}, 期望结果{input_shangyedaoqi},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_shangyedaoqi_css"]).text},结果正确')
            else:
                logbug.debug(
                    f'{sys._getframe().f_code.co_name}, 期望结果{input_shangyedaoqi},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_shangyedaoqi_css"]).text},结果错误')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},功能有误')


    def kehuliebiao_check_jiaoqiangdaoqi(driver, input_jiaoqiangdaoqi = '2019-03-09 23:59:59'):
        """客户列表-验证列表中第一个交强到期时间，参数传具体时间即可，内容保持和列表文字一致，如‘2019-03-09 23:59:59’"""
        try:
            if input_jiaoqiangdaoqi == driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_jiaoqiangdaoqi_css"]).text:
                logger.info(f'{sys._getframe().f_code.co_name}, 期望结果{input_jiaoqiangdaoqi},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_jiaoqiangdaoqi_css"]).text},结果正确')
            else:
                logbug.debug(
                    f'{sys._getframe().f_code.co_name}, 期望结果{input_jiaoqiangdaoqi},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_jiaoqiangdaoqi_css"]).text},结果错误')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},功能有误')

    def kehuliebiao_check_baojiazhuangtai(driver, input_baojiazhuangtai = '人保 (失败)'):
        """客户列表-验证列表中第一个报价状态，参数传具体状态即可，内容保持和列表文字一致，如‘人保 (失败)’"""
        try:
            #-----------------拖到可见
            target = driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_baojiazhuangtai_css"])
            driver.execute_script("arguments[0].scrollIntoView();", target)
            # -----------------拖到可见
            if input_baojiazhuangtai == driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_baojiazhuangtai_css"]).text:
                logger.info(f'{sys._getframe().f_code.co_name}, 期望结果{input_baojiazhuangtai},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_baojiazhuangtai_css"]).text},结果正确')
            else:
                logbug.debug(
                    f'{sys._getframe().f_code.co_name}, 期望结果{input_baojiazhuangtai},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_baojiazhuangtai_css"]).text},结果错误')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},功能有误')

    def kehuliebiao_check_hebaozhuangtai(driver, input_hebaozhuangtai = '未核保'):
        """客户列表-验证列表中第一个核保状态，参数传具体状态即可，内容保持和列表文字一致，如‘未核保’"""
        try:
            #-----------------拖到可见
            target = driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_hebaozhuangtai_css"])
            driver.execute_script("arguments[0].scrollIntoView();", target)
            time.sleep(1)
            # -----------------拖到可见
            if input_hebaozhuangtai == driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_hebaozhuangtai_css"]).text:
                logger.info(f'{sys._getframe().f_code.co_name}, 期望结果{input_hebaozhuangtai},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_hebaozhuangtai_css"]).text},结果正确')
            else:
                logbug.debug(
                    f'{sys._getframe().f_code.co_name}, 期望结果{input_hebaozhuangtai},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_hebaozhuangtai_css"]).text},结果错误')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},功能有误')

    def kehuliebiao_check_genjincishu(driver, input_genjincishu = '0'):
        """客户列表-验证列表中第一个跟进次数，参数传具体次数即可，内容保持和列表文字一致，如‘0’"""
        try:
            #-----------------拖到可见
            driver.execute_script(js)
            time.sleep(1)
            target = driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_genjincishu_css"])
            driver.execute_script("arguments[0].scrollIntoView();", target)
            time.sleep(1)
            # target = driver.find_element_by_css_selector('#app > section > section > main > div > div > div.el-row > div:nth-child(1) > div > div.el-table__body-wrapper.is-scrolling-left')
            # ActionChains(driver).drag_and_drop_by_offset(target, 1110, 0).perform()
            # time.sleep(10)
            # -----------------拖到可见
            if input_genjincishu == driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_genjincishu_css"]).text:
                logger.info(f'{sys._getframe().f_code.co_name}, 期望结果{input_genjincishu},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_genjincishu_css"]).text},结果正确')
            else:
                logbug.debug(
                    f'{sys._getframe().f_code.co_name}, 期望结果{input_genjincishu},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_genjincishu_css"]).text},结果错误')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},功能有误')

    def kehuliebiao_check_genjinshijian(driver, input_genjinshijian = '2019-01-01 00:00:00'):
        """客户列表-验证列表中第一个跟进时间，参数传具体时间即可，内容保持和列表文字一致，如‘2019-01-01 00:00:00’"""
        try:
            #-----------------拖到可见
            driver.execute_script(js)
            time.sleep(1)
            target = driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_genjinshijian_css"])
            driver.execute_script("arguments[0].scrollIntoView();", target)
            time.sleep(1)
            # target = driver.find_element_by_css_selector('#app > section > section > main > div > div > div.el-row > div:nth-child(1) > div > div.el-table__body-wrapper.is-scrolling-left')
            # ActionChains(driver).drag_and_drop_by_offset(target, 1110, 0).perform()
            # time.sleep(10)
            # -----------------拖到可见
            if input_genjinshijian == driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_genjinshijian_css"]).text:
                logger.info(f'{sys._getframe().f_code.co_name}, 期望结果{input_genjinshijian},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_genjinshijian_css"]).text},结果正确')
            else:
                logbug.debug(
                    f'{sys._getframe().f_code.co_name}, 期望结果{input_genjinshijian},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_genjinshijian_css"]).text},结果错误')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},功能有误')

    def kehuliebiao_check_genjinneirong(driver, input_genjinneirong = 'xxx客户，第一次跟进'):
        """客户列表-验证列表中第一个跟进内容，参数传具体内容即可，内容保持和列表文字一致，如‘xxx客户，第一次跟进’"""
        try:
            #-----------------拖到可见
            driver.execute_script(js)
            time.sleep(1)
            target = driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_genjinneirong_css"])
            driver.execute_script("arguments[0].scrollIntoView();", target)
            time.sleep(1)
            # target = driver.find_element_by_css_selector('#app > section > section > main > div > div > div.el-row > div:nth-child(1) > div > div.el-table__body-wrapper.is-scrolling-left')
            # ActionChains(driver).drag_and_drop_by_offset(target, 1110, 0).perform()
            # time.sleep(10)
            # -----------------拖到可见
            if input_genjinneirong == driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_genjinneirong_css"]).text:
                logger.info(f'{sys._getframe().f_code.co_name}, 期望结果{input_genjinneirong},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_genjinneirong_css"]).text},结果正确')
            else:
                logbug.debug(
                    f'{sys._getframe().f_code.co_name}, 期望结果{input_genjinneirong},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_genjinneirong_css"]).text},结果错误')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},功能有误')

    def kehuliebiao_check_yuyueshijian(driver, input_yuyueshijian = '2019-01-01 00:00:00'):
        """客户列表-验证列表中第一个预约时间，参数传具体内容即可，内容保持和列表文字一致，如‘2019-01-01 00:00:00’"""
        try:
            #-----------------拖到可见
            driver.execute_script(js)
            time.sleep(1)
            target = driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_yuyueshijian_css"])
            driver.execute_script("arguments[0].scrollIntoView();", target)
            time.sleep(1)
            # target = driver.find_element_by_css_selector('#app > section > section > main > div > div > div.el-row > div:nth-child(1) > div > div.el-table__body-wrapper.is-scrolling-left')
            # ActionChains(driver).drag_and_drop_by_offset(target, 1110, 0).perform()
            # time.sleep(10)
            # -----------------拖到可见
            if input_yuyueshijian == driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_yuyueshijian_css"]).text:
                logger.info(f'{sys._getframe().f_code.co_name}, 期望结果{input_yuyueshijian},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_yuyueshijian_css"]).text},结果正确')
            else:
                logbug.debug(
                    f'{sys._getframe().f_code.co_name}, 期望结果{input_yuyueshijian},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_yuyueshijian_css"]).text},结果错误')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},功能有误')

    def kehuliebiao_check_lurufangshi(driver, input_lurufangshi = 'PC端录入'):
        """客户列表-验证列表中第一个录入方式，参数传具体内容即可，内容保持和列表文字一致，如‘PC端录入’"""
        try:
            #-----------------拖到可见
            driver.execute_script(js)
            time.sleep(1)
            target = driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_lurufangshi_css"])
            driver.execute_script("arguments[0].scrollIntoView();", target)
            time.sleep(1)
            # target = driver.find_element_by_css_selector('#app > section > section > main > div > div > div.el-row > div:nth-child(1) > div > div.el-table__body-wrapper.is-scrolling-left')
            # ActionChains(driver).drag_and_drop_by_offset(target, 1110, 0).perform()
            # time.sleep(10)
            # -----------------拖到可见
            if input_lurufangshi == driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_lurufangshi_css"]).text:
                logger.info(f'{sys._getframe().f_code.co_name}, 期望结果{input_lurufangshi},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_lurufangshi_css"]).text},结果正确')
            else:
                logbug.debug(
                    f'{sys._getframe().f_code.co_name}, 期望结果{input_lurufangshi},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_lurufangshi_css"]).text},结果错误')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},功能有误')

    def kehuliebiao_check_jigoumingcheng(driver, input_jigoumingcheng = '传续业务部'):
        """客户列表-验证列表中第一个机构名称，参数传具体内容即可，内容保持和列表文字一致，如‘传续业务部’"""
        try:
            #-----------------拖到可见
            driver.execute_script(js)
            time.sleep(1)
            target = driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_jigoumingcheng_css"])
            driver.execute_script("arguments[0].scrollIntoView();", target)
            time.sleep(1)
            # target = driver.find_element_by_css_selector('#app > section > section > main > div > div > div.el-row > div:nth-child(1) > div > div.el-table__body-wrapper.is-scrolling-left')
            # ActionChains(driver).drag_and_drop_by_offset(target, 1110, 0).perform()
            # time.sleep(10)
            # -----------------拖到可见
            if input_jigoumingcheng == driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_jigoumingcheng_css"]).text:
                logger.info(f'{sys._getframe().f_code.co_name}, 期望结果{input_jigoumingcheng},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_jigoumingcheng_css"]).text},结果正确')
            else:
                logbug.debug(
                    f'{sys._getframe().f_code.co_name}, 期望结果{input_jigoumingcheng},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_jigoumingcheng_css"]).text},结果错误')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},功能有误')

    def kehuliebiao_check_kehuzhuangtai(driver, input_kehuzhuangtai = '首访客户'):
        """客户列表-验证列表中第一个客户状态，参数传具体内容即可，内容保持和列表文字一致，如‘首访客户’"""
        try:
            #-----------------拖到可见
            driver.execute_script(js)
            time.sleep(1)
            target = driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_kehuzhuangtai_css"])
            driver.execute_script("arguments[0].scrollIntoView();", target)
            time.sleep(1)
            # target = driver.find_element_by_css_selector('#app > section > section > main > div > div > div.el-row > div:nth-child(1) > div > div.el-table__body-wrapper.is-scrolling-left')
            # ActionChains(driver).drag_and_drop_by_offset(target, 1110, 0).perform()
            # time.sleep(10)
            # -----------------拖到可见
            if input_kehuzhuangtai == driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_kehuzhuangtai_css"]).text:
                logger.info(f'{sys._getframe().f_code.co_name}, 期望结果{input_kehuzhuangtai},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_kehuzhuangtai_css"]).text},结果正确')
            else:
                logbug.debug(
                    f'{sys._getframe().f_code.co_name}, 期望结果{input_kehuzhuangtai},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_kehuzhuangtai_css"]).text},结果错误')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},功能有误')

    def kehuliebiao_check_kehuleibie(driver, input_kehuleibie = '客户类别'):
        """客户列表-验证列表中第一个客户类别，参数传具体内容即可，内容保持和列表文字一致，如‘客户类别’"""
        try:
            #-----------------拖到可见
            driver.execute_script(js)
            time.sleep(1)
            target = driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_kehuleibie_css"])
            driver.execute_script("arguments[0].scrollIntoView();", target)
            time.sleep(1)
            # target = driver.find_element_by_css_selector('#app > section > section > main > div > div > div.el-row > div:nth-child(1) > div > div.el-table__body-wrapper.is-scrolling-left')
            # ActionChains(driver).drag_and_drop_by_offset(target, 1110, 0).perform()
            # time.sleep(10)
            # -----------------拖到可见
            if input_kehuleibie == driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_kehuleibie_css"]).text:
                logger.info(f'{sys._getframe().f_code.co_name}, 期望结果{input_kehuleibie},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_kehuleibie_css"]).text},结果正确')
            else:
                logbug.debug(
                    f'{sys._getframe().f_code.co_name}, 期望结果{input_kehuleibie},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_kehuleibie_css"]).text},结果错误')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},功能有误')

    def kehuliebiao_check_yewuyuan(driver, input_yewuyuan = '马小翠顶级'):
        """客户列表-验证列表中第一个业务员，参数传具体内容即可，内容保持和列表文字一致，如‘马小翠’"""
        try:
            #-----------------拖到可见
            driver.execute_script(js)
            time.sleep(1)
            target = driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_yewuyuan_css"])
            driver.execute_script("arguments[0].scrollIntoView();", target)
            time.sleep(1)
            # target = driver.find_element_by_css_selector('#app > section > section > main > div > div > div.el-row > div:nth-child(1) > div > div.el-table__body-wrapper.is-scrolling-left')
            # ActionChains(driver).drag_and_drop_by_offset(target, 1110, 0).perform()
            # time.sleep(10)
            # -----------------拖到可见
            if input_yewuyuan == driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_yewuyuan_css"]).text:
                logger.info(f'{sys._getframe().f_code.co_name}, 期望结果{input_yewuyuan},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_yewuyuan_css"]).text},结果正确')
            else:
                logbug.debug(
                    f'{sys._getframe().f_code.co_name}, 期望结果{input_yewuyuan},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_yewuyuan_css"]).text},结果错误')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},功能有误')

    def kehuliebiao_check_gengxinshijian(driver, input_gengxinshijian = '2019-11-08 11:35:37'):
        """客户列表-验证列表中第一个更新时间，参数传具体内容即可，内容保持和列表文字一致，如‘2019-11-08 11:35:37’"""
        try:
            #-----------------拖到可见
            driver.execute_script(js)
            time.sleep(1)
            target = driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_gengxinshijian_css"])
            driver.execute_script("arguments[0].scrollIntoView();", target)
            time.sleep(1)
            # target = driver.find_element_by_css_selector('#app > section > section > main > div > div > div.el-row > div:nth-child(1) > div > div.el-table__body-wrapper.is-scrolling-left')
            # ActionChains(driver).drag_and_drop_by_offset(target, 1110, 0).perform()
            # time.sleep(10)
            # -----------------拖到可见
            if input_gengxinshijian == driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_gengxinshijian_css"]).text:
                logger.info(f'{sys._getframe().f_code.co_name}, 期望结果{input_gengxinshijian},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_gengxinshijian_css"]).text},结果正确')
            else:
                logbug.debug(
                    f'{sys._getframe().f_code.co_name}, 期望结果{input_gengxinshijian},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_gengxinshijian_css"]).text},结果错误')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},功能有误')

    def kehuliebiao_check_bumenmingcheng(driver, input_bumenmingcheng = '北京诚信为本汽车销售有限公司'):
        """客户列表-验证列表中第一个部门名称，参数传具体内容即可，内容保持和列表文字一致，如‘北京诚信为本汽车销售有限公司’"""
        try:
            #-----------------拖到可见
            driver.execute_script(js)
            time.sleep(1)
            target = driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_bumenmingcheng_css"])
            driver.execute_script("arguments[0].scrollIntoView();", target)
            time.sleep(1)
            # target = driver.find_element_by_css_selector('#app > section > section > main > div > div > div.el-row > div:nth-child(1) > div > div.el-table__body-wrapper.is-scrolling-left')
            # ActionChains(driver).drag_and_drop_by_offset(target, 1110, 0).perform()
            # time.sleep(10)
            # -----------------拖到可见
            if input_bumenmingcheng == driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_bumenmingcheng_css"]).text:
                logger.info(f'{sys._getframe().f_code.co_name}, 期望结果{input_bumenmingcheng},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_bumenmingcheng_css"]).text},结果正确')
            else:
                logbug.debug(
                    f'{sys._getframe().f_code.co_name}, 期望结果{input_bumenmingcheng},实际结果{driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_bumenmingcheng_css"]).text},结果错误')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},功能有误')

# 以上为客户列表check方法


    def kehuxiangqing_kehuxinxi_kehuxingming(driver,input_kehuxingming = elements["test_chezhuxingming"]):
        """客户详情-客户信息-客户姓名修改，参数要传具体姓名，如‘梁浩’"""
        try:
            # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
            # time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_kehuxinxi_tab_css"])[0].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_kehuxinxi_kehuxingming_css"])[2].clear()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_kehuxinxi_kehuxingming_css"])[2].send_keys(input_kehuxingming)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_kehuxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_kehuxingming}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_kehuxingming} 修改失败')

    def kehuxiangqing_kehuxinxi_dianhua1(driver, input_dianhua1=elements["test_kehudianhua1"]):
        """客户详情-客户信息-客户电话1修改，参数要传具体电话，如‘13666668888’"""
        try:
            # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
            # time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_kehuxinxi_tab_css"])[0].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_kehuxinxi_dianhua1_css"])[3].clear()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_kehuxinxi_dianhua1_css"])[3].send_keys(input_dianhua1)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_kehuxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_dianhua1}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_dianhua1} 修改失败')

    def kehuxiangqing_kehuxinxi_dianhua2(driver, input_dianhua1=elements["test_kehudianhua2"]):
        """客户详情-客户信息-客户电话2修改，参数要传具体电话，如‘13666668888’"""
        try:
            # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
            # time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_kehuxinxi_tab_css"])[0].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_kehuxinxi_dianhua2_css"])[4].clear()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_kehuxinxi_dianhua2_css"])[4].send_keys(input_dianhua1)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_kehuxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_dianhua1}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_dianhua1} 修改失败')

    def kehuxiangqing_kehuxinxi_leibie(driver, input_leibie='潜转续'):
        """客户详情-客户信息-客户类别修改，参数要传具体类别，如‘间转续’"""
        try:
            # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
            # time.sleep(1)
            # driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_leibie_id"]).clear()
            # time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_kehuxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_kehuxinxi_leibie_css"]).click()
            time.sleep(1)
            # input_leibie = input_leibie.split('+')
            # for leibie in input_leibie:
            # driver.find_element_by_css_selector(elements["kehuxiangqing_kehuxinxi_leibie_select1_css"]).click()
            time.sleep(1)
            if input_leibie == '新转续':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul li:nth-child(1)').click()")
                time.sleep(1)
            elif input_leibie == '续转续':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul li:nth-child(2)').click()")
                time.sleep(1)
            elif input_leibie == '潜转续':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul li:nth-child(3)').click()")
                time.sleep(1)
            elif input_leibie == '间转续':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul li:nth-child(4)').click()")
                time.sleep(1)
            elif input_leibie == '进店':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul li:nth-child(5)').click()")
                time.sleep(1)
            elif input_leibie == '空值':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul li:nth-child(6)').click()")
                time.sleep(1)
            else:
                pass
            driver.find_element_by_css_selector(elements["kehuxiangqing_kehuxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_leibie}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_leibie} 修改失败')

    def kehuxiangqing_kehuxinxi_dizhi(driver, input_dizhi='北京市海淀区上地'):
        """客户详情-客户信息-地址修改，参数要传具体地址，如‘北京市海淀区上地’"""
        try:
            # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
            # time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_kehuxinxi_tab_css"])[0].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_kehuxinxi_dizhi_css"])[5].clear()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_kehuxinxi_dizhi_css"])[5].send_keys(input_dizhi)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_kehuxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_dizhi}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_dizhi} 修改失败')

    def kehuxiangqing_kehuxinxi_beizhu1(driver, input_beizhu1='备注1'):
        """客户详情-客户信息-备注1修改，参数要传具体备注，如‘备注1111备注1111’"""
        try:
            # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
            # time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_kehuxinxi_tab_css"])[0].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_kehuxinxi_beizhu1_css"])[6].clear()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_kehuxinxi_beizhu1_css"])[6].send_keys(input_beizhu1)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_kehuxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_beizhu1}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_beizhu1} 修改失败')

    def kehuxiangqing_kehuxinxi_beizhu2(driver, input_beizhu2='备注2'):
        """客户详情-客户信息-备注2修改，参数要传具体备注，如‘备注2222备注2222’"""
        try:
            # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
            # time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_kehuxinxi_tab_css"])[0].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_kehuxinxi_beizhu2_css"])[7].clear()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_kehuxinxi_beizhu2_css"])[7].send_keys(input_beizhu2)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_kehuxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_beizhu2}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_beizhu2} 修改失败')




    def kehuxiangqing_cheliangxinxi_chepaihao(driver, input_chepaihao=elements["test_licenseno"]):
        """客户详情-车辆信息-车牌号修改，参数要传具体车牌，如‘京J97896’"""
        try:
            # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
            # time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"])[1].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_chepaihao_css"])[8].clear()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_chepaihao_css"])[8].send_keys(input_chepaihao)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_chepaihao}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_chepaihao} 修改失败')


    def kehuxiangqing_cheliangxinxi_chejiahao(driver, input_chejiahao=elements["test_vin"]):
        """客户详情-车辆信息-车架号修改，参数要传具体车架，如‘LSVDM49FX62182255’"""
        try:
            # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
            # time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"])[1].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_chejiahao_input_css"])[9].clear()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_chejiahao_input_css"])[9].send_keys(input_chejiahao)
            time.sleep(1)
            # driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_chejiahao_sousuo_css"])[2].click()
            # time.sleep(5)
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_chejiahao}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_chejiahao} 修改失败')

    def kehuxiangqing_cheliangxinxi_chejiahao_chaxunchexing(driver):
        """客户详情-车辆信息-车架号查车型，无需传递参数，直接按照所填数据查询
        选择展示在最上面（最低）车型"""
        try:
            # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
            # time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"])[1].click()
            time.sleep(1)
            # driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_chejiahao_input_css"])[9].clear()
            # time.sleep(1)
            # driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_chejiahao_input_css"])[9].send_keys(input_chejiahao)
            # time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_chejiahao_sousuo_css"])[2].click()
            time.sleep(20)
            driver.execute_script(
                "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1) > span').click()")
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},查询成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},查询失败')


    def kehuxiangqing_cheliangxinxi_fadongjihao(driver, input_fadongjihao=elements["test_vin"]):
        """客户详情-车辆信息-发动机号修改，参数要传具体发动机号，如‘222569’"""
        try:
            # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
            # time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"])[1].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_fadongjihao_css"])[10].clear()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_fadongjihao_css"])[10].send_keys(input_fadongjihao)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_fadongjihao}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_fadongjihao} 修改失败')

    def kehuxiangqing_cheliangxinxi_zhuceriqi(driver, input_zhuceriqi='2019-01-01'):
        """客户详情-车辆信息-注册日期修改，参数要传时间格式，如‘2019-01-01’
        另：时间必须真实存在，且与业务要求吻合，不要输入不存在，不可选择的时间"""
        try:
            # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
            # time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"])[1].click()
            time.sleep(1)
            # driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_zhuceriqi_id"])[11].click()
            # time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_zhuceriqi_input_css"])[11].clear()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_zhuceriqi_input_css"])[11].send_keys(input_zhuceriqi)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_zhuceriqi}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_zhuceriqi} 修改失败')

    def kehuxiangqing_cheliangxinxi_pinpaixinghao(driver, input_pinpaixinghao=elements["test_vin"]):
        """客户详情-车辆信息-品牌型号修改，参数要传具体品牌，如‘帕萨特SVW7183MJi轿车’"""
        try:
            # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
            # time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"])[1].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(
                elements["kehuxiangqing_cheliangxinxi_pinpaixinghao_input_css"])[12].clear()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_pinpaixinghao_input_css"])[12].send_keys(
                input_pinpaixinghao)
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_pinpaixinghao_sousuo_css"]).click()
            # time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_pinpaixinghao}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_pinpaixinghao} 修改失败')


    def kehuxiangqing_cheliangxinxi_pinpaixinghaohao_chaxunchexing(driver):
        """客户详情-车辆信息-品牌型号查车型，无需传递参数，直接按照所填数据查询
        选择展示在最上面（最低）车型"""
        try:
            # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
            # time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"])[1].click()
            time.sleep(1)
            # driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_chejiahao_input_css"])[9].clear()
            # time.sleep(1)
            # driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_chejiahao_input_css"])[9].send_keys(input_chejiahao)
            # time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_chejiahao_sousuo_css"])[3].click()
            time.sleep(20)
            driver.execute_script(
                "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1) > span').click()")
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},查询成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}, 查询失败')

    #  因为此功能，涉及到车型查询，需要和车架号/品牌型号查车型联动，故不单独定义方法
    # def kehuxiangqing_cheliangxinxi_chexing(driver, input_chexing=elements["test_vin"]):
    #     """客户详情-车辆信息-车型修改，此方法待完善，有可能需要和品牌型号联动"""
    #     try:
    #         # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
    #         # time.sleep(1)
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"]).click()
    #         time.sleep(1)
    #         driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_chexing_id"]).click()
    #         time.sleep(1)
    #         # driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_fadongjihao_id"]).send_keys(input_zhuceriqi)
    #         # time.sleep(1)
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
    #         time.sleep(1)
    #         # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
    #         # time.sleep(1)
    #         logger.info(f'{sys._getframe().f_code.co_name},{input_chexing}修改成功')
    #     except Exception:
    #         logbug.debug(f'{sys._getframe().f_code.co_name},{input_chexing} 修改失败')

    def kehuxiangqing_cheliangxinxi_xinchegouzhijia(driver, input_xinchegouzhijia='1122'):
        """客户详情-车辆信息-新车购置价修改，参数要传具体价格，如‘121314’"""
        try:
            # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
            # time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"])[1].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_xinchegouzhijia_css"])[13].clear()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_xinchegouzhijia_css"])[13].send_keys(input_xinchegouzhijia)
            time.sleep(1)
            # driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_fadongjihao_id"]).send_keys(input_zhuceriqi)
            # time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_xinchegouzhijia}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_xinchegouzhijia} 修改失败')

    def kehuxiangqing_cheliangxinxi_zuoweishu(driver, input_zuoweishu='8座'):
        """客户详情-车辆信息-座位数修改，参数要传具体座位数，如‘3座’，与下拉框文本保持一致"""
        try:
            # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
            # time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"])[1].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_zuoweishu_css"])[2].click()
            time.sleep(2)
            if input_zuoweishu == '3座':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)').click()")
                time.sleep(1)
            elif input_zuoweishu == '4座':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)').click()")
                time.sleep(1)
            elif input_zuoweishu == '5座':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(3)').click()")
                time.sleep(1)
            elif input_zuoweishu == '6座':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(4)').click()")
                time.sleep(1)
            elif input_zuoweishu == '7座':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(5)').click()")
                time.sleep(1)
            elif input_zuoweishu == '8座':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(6)').click()")
                time.sleep(1)
            elif input_zuoweishu == '9座':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(7)').click()")
                time.sleep(1)
            elif input_zuoweishu == '10座':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(8)').click()")
                time.sleep(1)
            else:
                pass
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_zuoweishu}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_zuoweishu} 修改失败')

    def kehuxiangqing_cheliangxinxi_pailiang(driver, input_pailiang='1.111'):
        """客户详情-车辆信息-排量修改，参数要传具体排量，如‘1.781’"""
        try:
            # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
            # time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"])[1].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_pailiang_css"])[14].clear()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_pailiang_css"])[14].send_keys(
                input_pailiang)
            time.sleep(1)
            # driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_fadongjihao_id"]).send_keys(input_zhuceriqi)
            # time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_pailiang}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_pailiang} 修改失败')

    def kehuxiangqing_cheliangxinxi_guohuche(driver , input_shifou = '否', input_guohuriqi='2019-01-01'):
        """客户详情-车辆信息-过户车修改，参数要传两个，第一个‘是’或‘否’，第二个日期，格式为‘2019-01-01’
        传‘是’，则必须传递日期，传‘否’，则无需传递日期"""
        try:
            # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
            # time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"])[1].click()
            time.sleep(1)
            if input_shifou == '是':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_guohuche_css"])[3].click()
                time.sleep(1)
                driver.execute_script(
                    "$('body > div:nth-child(24) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)').click()")
                time.sleep(1)
                driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_guohuriqi_css"])[15].click()
                time.sleep(1)
                driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_guohuriqi_css"])[15].clear()
                time.sleep(1)
                driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_guohuriqi_css"])[15].send_keys(input_guohuriqi)
                time.sleep(1)
            elif input_shifou == '否':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_guohuche_css"])[3].click()
                time.sleep(1)
                driver.execute_script(
                    "$('body > div:nth-child(24) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)').click()")
                time.sleep(1)
            else:
                pass
            # driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_fadongjihao_id"]).send_keys(input_zhuceriqi)
            # time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_shifou},{input_guohuriqi}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_shifou},{input_guohuriqi} 修改失败')

    def kehuxiangqing_cheliangxinxi_daikuanche(driver, input_shifou='是', input_diyishouyiren='第一受益'):
        """客户详情-车辆信息-贷款车修改，参数要传两个，第一个‘是’或‘否’，第二个第一受益人，参数要传具体人名，如‘刘海’
        传‘是’，则必须传递第一受益人，传‘否’，则无需传递第一受益人"""
        try:
            # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
            # time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"])[1].click()
            time.sleep(1)
            if input_shifou == '是':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_daikuanche_css"])[4].click()
                time.sleep(1)
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)').click()")
                time.sleep(1)
                driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_diyishouyiren_css"])[16].send_keys(input_diyishouyiren)
                time.sleep(1)
            elif input_shifou == '否':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_daikuanche_css"])[4].click()
                time.sleep(1)
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)').click()")
                time.sleep(1)
            else:
                pass
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_shifou}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_shifou} 修改失败')

    # def kehuxiangqing_cheliangxinxi_diyishouyiren(driver, input_diyishouyiren=elements["test_vin"]):
    #     try:
    #         # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
    #         # time.sleep(1)
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"]).click()
    #         time.sleep(1)
    #         driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_diyishouyiren_id"]).send_keys(
    #             input_diyishouyiren)
    #         time.sleep(1)
    #         # driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_fadongjihao_id"]).send_keys(input_zhuceriqi)
    #         # time.sleep(1)
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
    #         time.sleep(1)
    #         # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
    #         # time.sleep(1)
    #         logger.info(f'{sys._getframe().f_code.co_name},{input_diyishouyiren}修改成功')
    #     except Exception:
    #         logbug.debug(f'{sys._getframe().f_code.co_name},{input_diyishouyiren} 修改失败')

    # def kehuxiangqing_cheliangxinxi_cheliangfenlei(driver, input_cheliangfenlei=elements["test_vin"]):
    #     try:
    #         # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
    #         # time.sleep(1)
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"]).click()
    #         time.sleep(1)
    #         driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_cheliangfenlei_id"]).send_keys(
    #             input_cheliangfenlei)
    #         time.sleep(1)
    #         # driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_fadongjihao_id"]).send_keys(input_zhuceriqi)
    #         # time.sleep(1)
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
    #         time.sleep(1)
    #         # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
    #         # time.sleep(1)
    #         logger.info(f'{sys._getframe().f_code.co_name},{input_cheliangfenlei}修改成功')
    #     except Exception:
    #         logbug.debug(f'{sys._getframe().f_code.co_name},{input_cheliangfenlei} 修改失败')
    #
    # def kehuxiangqing_cheliangxinxi_cheliangleixing(driver, input_cheliangleixing=elements["test_vin"]):
    #     try:
    #         # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
    #         # time.sleep(1)
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"]).click()
    #         time.sleep(1)
    #         driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_cheliangleixing_id"]).send_keys(
    #             input_cheliangleixing)
    #         time.sleep(1)
    #         # driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_fadongjihao_id"]).send_keys(input_zhuceriqi)
    #         # time.sleep(1)
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
    #         time.sleep(1)
    #         # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
    #         # time.sleep(1)
    #         logger.info(f'{sys._getframe().f_code.co_name},{input_cheliangleixing}修改成功')
    #     except Exception:
    #         logbug.debug(f'{sys._getframe().f_code.co_name},{input_cheliangleixing} 修改失败')
    #
    #
    # def kehuxiangqing_cheliangxinxi_zaizhongliang(driver, input_zaizhongliang=elements["test_vin"]):
    #     try:
    #         # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
    #         # time.sleep(1)
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"]).click()
    #         time.sleep(1)
    #         driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_zaizhongliang_id"]).send_keys(
    #             input_zaizhongliang)
    #         time.sleep(1)
    #         # driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_fadongjihao_id"]).send_keys(input_zhuceriqi)
    #         # time.sleep(1)
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
    #         time.sleep(1)
    #         # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
    #         # time.sleep(1)
    #         logger.info(f'{sys._getframe().f_code.co_name},{input_zaizhongliang}修改成功')
    #     except Exception:
    #         logbug.debug(f'{sys._getframe().f_code.co_name},{input_zaizhongliang} 修改失败')
    #
    # def kehuxiangqing_cheliangxinxi_cheliangshiyongxingzhi(driver, input_cheliangshiyongxingzhi=elements["test_vin"]):
    #     try:
    #         # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
    #         # time.sleep(1)
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"]).click()
    #         time.sleep(1)
    #         driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_cheliangshiyongxingzhi_id"]).send_keys(
    #             input_cheliangshiyongxingzhi)
    #         time.sleep(1)
    #         # driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_fadongjihao_id"]).send_keys(input_zhuceriqi)
    #         # time.sleep(1)
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
    #         time.sleep(1)
    #         # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
    #         # time.sleep(1)
    #         logger.info(f'{sys._getframe().f_code.co_name},{input_cheliangshiyongxingzhi}修改成功')
    #     except Exception:
    #         logbug.debug(f'{sys._getframe().f_code.co_name},{input_cheliangshiyongxingzhi} 修改失败')

    def kehuxiangqing_cheliangxinxi_beizhuxinxi(driver, input_beizhuxinxi='备注信息'):
        """客户详情-车辆信息-备注信息修改，参数要传具体备注，如‘备注备注’"""
        try:
            driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"])[1].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_beizhuxinxi_css"])[17].send_keys(
                input_beizhuxinxi)
            time.sleep(1)
            # driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_fadongjihao_id"]).send_keys(input_zhuceriqi)
            # time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_beizhuxinxi}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_beizhuxinxi} 修改失败')







    def kehuxiangqing_shangniantoubaoxinxi_toubaogongsi(driver, input_toubaogongsi='大地车险'):
        """客户详情-上年投保信息-投保公司修改，参数要传具体公司，如‘太平洋车险’，和下拉框文本保持一致"""
        try:
            driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"])[2].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_zhankai_css"])[2].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_css"])[5].click()
            time.sleep(1)
            if input_toubaogongsi == '太平洋车险':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)').click()")
                time.sleep(1)
            elif input_toubaogongsi == '平安车险':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)').click()")
                time.sleep(1)
            elif input_toubaogongsi == '人保车险':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(3)').click()")
                time.sleep(1)
            elif input_toubaogongsi == '中国人寿财险':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(4)').click()")
                time.sleep(1)
            elif input_toubaogongsi == '中华联合车险':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(5)').click()")
                time.sleep(1)
            elif input_toubaogongsi == '大地车险':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(6)').click()")
                time.sleep(1)
            elif input_toubaogongsi == '阳光车险':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(7)').click()")
                time.sleep(1)
            elif input_toubaogongsi == '太平车险':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(8)').click()")
                time.sleep(1)
            elif input_toubaogongsi == '华安车险':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(9)').click()")
                time.sleep(1)
            elif input_toubaogongsi == '天安车险':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(10)').click()")
                time.sleep(1)
            elif input_toubaogongsi == '英大泰和车险':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(11)').click()")
                time.sleep(1)
            elif input_toubaogongsi == '安盛天平车险':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(12)').click()")
                time.sleep(1)
            elif input_toubaogongsi == '安心车险':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(13)').click()")
                time.sleep(1)
            elif input_toubaogongsi == '亚太车险':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(14)').click()")
                time.sleep(1)
            elif input_toubaogongsi == '合众车险':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(15)').click()")
                time.sleep(1)
            elif input_toubaogongsi == '利宝车险':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(16)').click()")
                time.sleep(1)
            elif input_toubaogongsi == '永安车险':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(17)').click()")
                time.sleep(1)
            elif input_toubaogongsi == '安诚车险':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(18)').click()")
                time.sleep(1)
            elif input_toubaogongsi == '锦泰车险':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(19)').click()")
                time.sleep(1)
            elif input_toubaogongsi == '安邦车险':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(20)').click()")
                time.sleep(1)
            elif input_toubaogongsi == '永诚车险':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(21)').click()")
                time.sleep(1)
            elif input_toubaogongsi == '华泰车险':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(22)').click()")
                time.sleep(1)
            elif input_toubaogongsi == '渤海车险':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(23)').click()")
                time.sleep(1)
            elif input_toubaogongsi == '信达车险':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(24)').click()")
                time.sleep(1)
            elif input_toubaogongsi == '安华农业车险':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(25)').click()")
                time.sleep(1)
            elif input_toubaogongsi == '鼎和车险':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(26)').click()")
                time.sleep(1)
            elif input_toubaogongsi == '中煤车险':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(27)').click()")
                time.sleep(1)
            elif input_toubaogongsi == '诚泰车险':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(28)').click()")
                time.sleep(1)
            elif input_toubaogongsi == '长江车险':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(29)').click()")
                time.sleep(1)
            elif input_toubaogongsi == '北部湾车险':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(30)').click()")
                time.sleep(1)
            elif input_toubaogongsi == '恒邦车险':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(31)').click()")
                time.sleep(1)
            elif input_toubaogongsi == '中铁车险':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(32)').click()")
                time.sleep(1)
            elif input_toubaogongsi == '美亚车险':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(33)').click()")
                time.sleep(1)
            elif input_toubaogongsi == '富邦车险':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(34)').click()")
                time.sleep(1)
            elif input_toubaogongsi == '众诚车险':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(35)').click()")
                time.sleep(1)
            elif input_toubaogongsi == '东京海上车险':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(36)').click()")
                time.sleep(1)
            elif input_toubaogongsi == '其他':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(37)').click()")
                time.sleep(1)
            else:
                pass
            # driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_fadongjihao_id"]).send_keys(input_zhuceriqi)
            # time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_baocun_button_css"])[1].click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_toubaogongsi}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_toubaogongsi} 修改失败')

    def kehuxiangqing_shangniantoubaoxinxi_shangyedaoqi(driver, input_shangyedaoqidate='此刻',input_shangyedaoqitime= '13:00:00'):
        """客户详情-上年投保信息-商业到期修改，参数要传2个，前面是日期，格式如‘2019-01-01’，后面是时间，格式如：‘23：59：59’
        如果想选择‘此刻’，则日期参数要传‘此刻’，时间参数无需传递
        另：时间必须真实存在，且与业务要求吻合，不要输入不存在，不可选择的时间"""
        try:
            driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"])[2].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_zhankai_css"])[2].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_shangyedaoqi_css"])[18].click()
            time.sleep(1)
            if input_shangyedaoqidate == '此刻':
                driver.find_element_by_css_selector(
                    elements["kehuxiangqing_shangniantoubaoxinxi_shangyedaoqi_cike_css"]).click()
                time.sleep(1)
            else:
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_shangyedaoqi_inputdate_css"])[0].clear()
                time.sleep(1)
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_shangyedaoqi_inputdate_css"])[0].send_keys(input_shangyedaoqidate)
                time.sleep(1)
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_shangyedaoqi_inputtime_css"])[1].clear()
                time.sleep(1)
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_shangyedaoqi_inputtime_css"])[1].send_keys(input_shangyedaoqitime)
                time.sleep(1)
                # 点一下确认，收回时间框
                driver.find_element_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_shangyedaoqi_inputtime_queding_css"]).click()
                time.sleep(1)
                driver.find_element_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_shangyedaoqi_queren_css"]).click()
                time.sleep(1)
                # 点一下确认，收回时间框
            driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_baocun_button_css"])[1].click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_shangyedaoqidate}, {input_shangyedaoqitime}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_shangyedaoqidate}, {input_shangyedaoqitime}修改失败')

    def kehuxiangqing_shangniantoubaoxinxi_jiaoqiangdaoqi(driver, input_jiaoqiangdaoqidate='2019-01-01',input_jiaoqiangdaoqitime= '13:00:00'):
        """客户详情-上年投保信息-交强到期修改，参数要传2个，前面是日期，格式如‘2019-01-01’，后面是时间，格式如：‘23：59：59’
        如果想选择‘此刻’，则日期参数要传‘此刻’，时间参数无需传递
        另：时间必须真实存在，且与业务要求吻合，不要输入不存在，不可选择的时间"""
        try:
            driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"])[2].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_zhankai_css"])[2].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_jiaoqiangdaoqi_css"])[19].click()
            time.sleep(1)
            if input_jiaoqiangdaoqidate == '此刻':
                driver.find_element_by_css_selector(
                    elements["kehuxiangqing_shangniantoubaoxinxi_jiaoqiangdaoqi_cike_css"]).click()
                time.sleep(1)
            else:
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_jiaoqiangdaoqi_inputdate_css"])[0].clear()
                time.sleep(1)
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_jiaoqiangdaoqi_inputdate_css"])[0].send_keys(input_jiaoqiangdaoqidate)
                time.sleep(1)
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_jiaoqiangdaoqi_inputtime_css"])[1].clear()
                time.sleep(1)
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_jiaoqiangdaoqi_inputtime_css"])[1].send_keys(input_jiaoqiangdaoqitime)
                time.sleep(1)
                # 点一下确认，收回时间框
                driver.find_element_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_jiaoqiangdaoqi_inputtime_queding_css"]).click()
                time.sleep(1)
                driver.find_element_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_jiaoqiangdaoqi_queren_css"]).click()
                time.sleep(1)
                # 点一下确认，收回时间框
            driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_baocun_button_css"])[1].click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_jiaoqiangdaoqidate}, {input_jiaoqiangdaoqitime}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_jiaoqiangdaoqidate}, {input_jiaoqiangdaoqitime}修改失败')

    def kehuxiangqing_shangniantoubaoxinxi_beibaoxianren(driver, input_beibaoxianren='李明'):
        """客户详情-上年投保信息-被保险人修改，参数要传具体人名，如‘李明’"""
        try:
            driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"])[2].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_zhankai_css"])[2].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_beibaoxianren_css"])[20].clear()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_beibaoxianren_css"])[20].send_keys(input_beibaoxianren)
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_baocun_button_css"])[1].click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_beibaoxianren}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_beibaoxianren}修改失败')

    def kehuxiangqing_shangniantoubaoxinxi_zhengjianleixing(driver,input_zhengjianleixing= '身份证', input_zhengjianhaoma='110106199602070314'):
        """客户详情-上年投保信息-证件类型+号码修改，参数要传具体类型，如‘身份证’，和下拉框文本保持一致
        证件号码要传具体号码，如‘110100196609010009’"""
        try:
            driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"])[2].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_zhankai_css"])[2].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_zhengjianleixing_css"])[6].click()
            time.sleep(1)
            if input_zhengjianleixing == '身份证':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)').click()")
                time.sleep(1)
            elif input_zhengjianleixing == '组织机构代码证':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)').click()")
                time.sleep(1)
            elif input_zhengjianleixing == '营业执照/统一社会信用代码':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(3)').click()")
                time.sleep(1)
            elif input_zhengjianleixing == '港澳居民来往内地通行证':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(4)').click()")
                time.sleep(1)
            elif input_zhengjianleixing == '港澳身份证':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(5)').click()")
                time.sleep(1)
            else:
                pass
            driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_zhengjianhaoma_css"])[21].clear()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_zhengjianhaoma_css"])[21].send_keys(
                input_zhengjianhaoma)
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_baocun_button_css"])[1].click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_zhengjianleixing}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_zhengjianleixing}修改失败')

    def kehuxiangqing_shangniantoubaoxinxi_jigoumingcheng(driver,input_jigoumingcheng='壁虎测试机构'):
        """客户详情-上年投保信息-机构名称修改，参数要传具体机构名称，如‘投保机构’"""
        try:

            driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"])[2].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_zhankai_css"])[2].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_jigoumingcheng_css"])[22].clear()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_jigoumingcheng_css"])[22].send_keys(input_jigoumingcheng)
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_baocun_button_css"])[1].click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_jigoumingcheng}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_jigoumingcheng}修改失败')

    def kehuxiangqing_shangniantoubaoxinxi_shangyedanhao(driver,input_shangyedanhao='PDAA201811010001467506'):
        """客户详情-上年投保信息-商业险保单号修改，参数要传具体保单号，如‘PDAA201911010000447156’"""
        try:

            driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"])[2].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_zhankai_css"])[2].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_shangyedanhao_css"])[23].clear()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_shangyedanhao_css"])[23].send_keys(input_shangyedanhao)
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_baocun_button_css"])[1].click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_shangyedanhao}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_shangyedanhao}修改失败')

    def kehuxiangqing_shangniantoubaoxinxi_jiaoqiangdanhao(driver,input_jiaoqiangdanhao='PDZA201811010001499349'):
        """客户详情-上年投保信息-交强险保单号修改，参数要传具体保单号，如‘PDZA201911010000491560’"""
        try:

            driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"])[2].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_zhankai_css"])[2].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_jiaoqiangdanhao_css"])[24].clear()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_jiaoqiangdanhao_css"])[24].send_keys(input_jiaoqiangdanhao)
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_baocun_button_css"])[1].click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_jiaoqiangdanhao}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_jiaoqiangdanhao}修改失败')



    # def kehuxiangqing_guanxirenxinxi_shezhilinshiguanxiren(driver):
    #     """客户详情-关系人信息-设置临时关系人修改，此方法暂不维护"""
    #     try:
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"]).click()
    #         time.sleep(1)
    #         driver.find_element_by_css_selector(
    #             elements["kehuxiangqing_guanxirenxinxi_shezhilinshiguanxiren_css"]).click()
    #         time.sleep(1)
    #         # driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
    #         # time.sleep(1)
    #         # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
    #         # time.sleep(1)
    #         logger.info(f'{sys._getframe().f_code.co_name},修改成功')
    #     except Exception:
    #         logbug.debug(f'{sys._getframe().f_code.co_name},修改失败')


    def kehuxiangqing_guanxirenxinxi_chezhuxinxi_tongtoubaoren(driver,input_tongtoubaoren = '不同投保人'):
        """客户详情-关系人信息-车主信息-同投保人，参数要传相同或不同，如‘同投保人’‘不同投保人’"""
        try:
            driver.find_elements_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"])[3].click()
            time.sleep(1)
            if input_tongtoubaoren == '同投保人':
                if driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_chezhuxinxi_tongtoubaoren_css"]).get_attribute('class') == elements["kehuxiangqing_guanxirenxinxi_chezhuxinxi_tongtoubaoren_checked_class"]:
                    pass
                    time.sleep(1)
                else:
                    driver.find_element_by_css_selector(
                        elements["kehuxiangqing_guanxirenxinxi_chezhuxinxi_tongtoubaoren_css"]).click()
                    time.sleep(1)
            elif input_tongtoubaoren == '不同投保人':
                if driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_chezhuxinxi_tongtoubaoren_css"]).get_attribute('class') == elements["kehuxiangqing_guanxirenxinxi_chezhuxinxi_tongtoubaoren_checked_class"]:
                    driver.find_element_by_css_selector(
                        elements["kehuxiangqing_guanxirenxinxi_chezhuxinxi_tongtoubaoren_css"]).click()
                    time.sleep(1)
                else:
                    pass
                    time.sleep(1)
            else:
                pass
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},修改失败')


    def kehuxiangqing_guanxirenxinxi_chezhuxinxi_gonghu(driver):
        """客户详情-关系人信息-车主信息-快速选择‘公户’，无需传递参数"""
        try:
            driver.find_elements_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"])[3].click()
            time.sleep(1)
            driver.find_element_by_css_selector(
                elements["kehuxiangqing_guanxirenxinxi_chezhuxinxi_quickselect_gonghu_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},修改失败')

    def kehuxiangqing_guanxirenxinxi_chezhuxinxi_geren(driver):
        """客户详情-关系人信息-车主信息-快速选择‘个人’，无需传递参数"""
        try:
            driver.find_elements_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"])[3].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(
                elements["kehuxiangqing_guanxirenxinxi_chezhuxinxi_quickselect_geren_css"])[1].click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},修改失败')

    def kehuxiangqing_guanxirenxinxi_chezhuxinxi_xingming(driver, input_chezhuxingming='李明'):
        """客户详情-关系人信息-车主信息-车主姓名，参数要传具体姓名，如‘李明’"""
        try:
            driver.find_elements_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"])[3].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_chezhuxinxi_chezhuxingming_css"])[25].send_keys(Keys.CONTROL + 'a')
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_chezhuxinxi_chezhuxingming_css"])[25].send_keys(Keys.BACKSPACE)
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_chezhuxinxi_chezhuxingming_css"])[25].send_keys(input_chezhuxingming)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_chezhuxingming} 修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_chezhuxingming} 修改失败')

    def kehuxiangqing_guanxirenxinxi_chezhuxinxi_zhengjianleixing(driver, input_zhengjianleixing='身份证', input_zhengjianhaoma='371525199202093330'):
        """客户详情-关系人信息-车主信息-证件类型+号码，参数要传具体类型，如‘身份证’，与下拉框中文本保持一致
                号码要传具体号码，如‘110100199999999999’"""
        try:
            driver.find_elements_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"])[3].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_chezhuxinxi_zhengjianleixing_css"])[7].click()
            time.sleep(1)
            if input_zhengjianleixing == '身份证':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)').click()")
                time.sleep(1)
            elif input_zhengjianleixing == '组织机构代码证':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)').click()")
                time.sleep(1)
            elif input_zhengjianleixing == '营业执照/统一社会信用代码':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(3)').click()")
                time.sleep(1)
            elif input_zhengjianleixing == '港澳居民来往内地通行证':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(4)').click()")
                time.sleep(1)
            elif input_zhengjianleixing == '港澳身份证':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(5)').click()")
                time.sleep(1)
            else:
                pass
            driver.find_elements_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_chezhuxinxi_zhengjianhaoma_css"])[26].clear()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_chezhuxinxi_zhengjianhaoma_css"])[26].send_keys(input_zhengjianhaoma)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_zhengjianleixing} 修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_zhengjianleixing} 修改失败')


    def kehuxiangqing_guanxirenxinxi_toubaorenxinxi_gonghu(driver):
        """客户详情-关系人信息-投保人信息-快速选择‘公户’，无需传递参数"""
        try:
            driver.find_elements_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"])[3].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(
                elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_quickselect_gonghu_css"])[2].click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},修改失败')

    def kehuxiangqing_guanxirenxinxi_toubaorenxinxi_geren(driver):
        """客户详情-关系人信息-投保人信息-快速选择‘个人’，无需传递参数"""
        try:
            driver.find_elements_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"])[3].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(
                elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_quickselect_geren_css"])[3].click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},修改失败')

    def kehuxiangqing_guanxirenxinxi_toubaorenxinxi_toubaorenxingming(driver, input_toubaorenxingming='李明'):
        """客户详情-关系人信息-投保人信息-投保人姓名，参数要传具体姓名，如‘李明’"""
        try:
            driver.find_elements_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"])[3].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_toubaorenxingming_css"])[27].send_keys(Keys.CONTROL + 'a')
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_toubaorenxingming_css"])[27].send_keys(Keys.BACKSPACE)
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_toubaorenxingming_css"])[27].send_keys(
                input_toubaorenxingming)
            time.sleep(1)
            # driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_fadongjihao_id"]).send_keys(input_zhuceriqi)
            # time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_toubaorenxingming}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_toubaorenxingming} 修改失败')

    def kehuxiangqing_guanxirenxinxi_toubaorenxinxi_zhengjianleixing(driver, input_zhengjianleixing='身份证', input_zhengjianhaoma='371525199202093330'):
        """客户详情-关系人信息-投保人信息-证件类型+号码，参数要传具体类型，如‘身份证’，与下拉框中文本保持一致
                号码要传具体号码，如‘110100199999999999’"""
        try:
            driver.find_elements_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"])[3].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_zhengjianleixing_css"])[8].click()
            time.sleep(1)
            if input_zhengjianleixing == '身份证':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)').click()")
                time.sleep(1)
            elif input_zhengjianleixing == '组织机构代码证':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)').click()")
                time.sleep(1)
            elif input_zhengjianleixing == '营业执照/统一社会信用代码':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(3)').click()")
                time.sleep(1)
            elif input_zhengjianleixing == '港澳居民来往内地通行证':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(4)').click()")
                time.sleep(1)
            elif input_zhengjianleixing == '港澳身份证':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(5)').click()")
                time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_zhengjianhaoma_css"])[28].send_keys(Keys.CONTROL + 'a')
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_zhengjianhaoma_css"])[28].send_keys(Keys.BACKSPACE)
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_zhengjianhaoma_css"])[28].send_keys(input_zhengjianhaoma)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_zhengjianleixing}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_zhengjianleixing} 修改失败')

    def kehuxiangqing_guanxirenxinxi_toubaorenxinxi_toubaorendianhua(driver, input_toubaorendianhua='138666666666'):
        """客户详情-关系人信息-投保人信息-投保人电话，参数要传具体电话，如‘13000009999’"""
        try:
            driver.find_elements_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"])[3].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_toubaorendianhua_css"])[29].send_keys(Keys.CONTROL + 'a')
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_toubaorendianhua_css"])[29].send_keys(Keys.BACKSPACE)
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_toubaorendianhua_css"])[29].send_keys(input_toubaorendianhua)
            time.sleep(1)
            # driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_fadongjihao_id"]).send_keys(input_zhuceriqi)
            # time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_toubaorendianhua}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_toubaorendianhua} 修改失败')

    # def kehuxiangqing_guanxirenxinxi_toubaorenxinxi_toubaorenyouxiang(driver, input_toubaorenyouxiang=elements["test_vin"]):
    #     """客户详情-关系人信息-投保人信息-投保人邮箱，参数要传具体邮箱，如‘fff@91bihu.com’"""
    #     try:
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"]).click()
    #         time.sleep(1)
    #         driver.find_element_by_id(
    #             elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_toubaorenyouxiang_id"]).clear()
    #         time.sleep(1)
    #         driver.find_element_by_id(
    #             elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_toubaorenyouxiang_id"]).send_keys(
    #             input_toubaorenyouxiang)
    #         time.sleep(1)
    #         # driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_fadongjihao_id"]).send_keys(input_zhuceriqi)
    #         # time.sleep(1)
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
    #         time.sleep(1)
    #         # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
    #         # time.sleep(1)
    #         logger.info(f'{sys._getframe().f_code.co_name},{input_toubaorenyouxiang}修改成功')
    #     except Exception:
    #         logbug.debug(f'{sys._getframe().f_code.co_name},{input_toubaorenyouxiang} 修改失败')
    #
    # def kehuxiangqing_guanxirenxinxi_toubaorenxinxi_zhuzhi(driver, input_zhuzhi=elements["test_vin"]):
    #     """客户详情-关系人信息-投保人信息-住址，参数要传具体住址，如‘北京市海淀区’"""
    #     try:
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"]).click()
    #         time.sleep(1)
    #         driver.find_element_by_id(
    #             elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_zhuzhi_id"]).clear()
    #         time.sleep(1)
    #         driver.find_element_by_id(
    #             elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_zhuzhi_id"]).send_keys(
    #             input_zhuzhi)
    #         time.sleep(1)
    #         # driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_fadongjihao_id"]).send_keys(input_zhuceriqi)
    #         # time.sleep(1)
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
    #         time.sleep(1)
    #         # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
    #         # time.sleep(1)
    #         logger.info(f'{sys._getframe().f_code.co_name},{input_zhuzhi}修改成功')
    #     except Exception:
    #         logbug.debug(f'{sys._getframe().f_code.co_name},{input_zhuzhi} 修改失败')
    #
    # def kehuxiangqing_guanxirenxinxi_toubaorenxinxi_minzu(driver, input_minzu=elements["test_vin"]):
    #     """客户详情-关系人信息-投保人信息-民族，参数要传具体民族，如‘汉族’"""
    #     try:
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"]).click()
    #         time.sleep(1)
    #         driver.find_element_by_id(
    #             elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_minzu_id"]).clear()
    #         time.sleep(1)
    #         driver.find_element_by_id(
    #             elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_minzu_id"]).send_keys(
    #             input_minzu)
    #         time.sleep(1)
    #         # driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_fadongjihao_id"]).send_keys(input_zhuceriqi)
    #         # time.sleep(1)
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
    #         time.sleep(1)
    #         # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
    #         # time.sleep(1)
    #         logger.info(f'{sys._getframe().f_code.co_name},{input_minzu}修改成功')
    #     except Exception:
    #         logbug.debug(f'{sys._getframe().f_code.co_name},{input_minzu} 修改失败')
    #
    # def kehuxiangqing_guanxirenxinxi_toubaorenxinxi_qianfajiguan(driver, input_qianfajiguan=elements["test_vin"]):
    #     """客户详情-关系人信息-投保人信息-签发机关，参数要传具体签发机关，如‘xx机关’"""
    #     try:
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"]).click()
    #         time.sleep(1)
    #         driver.find_element_by_id(
    #             elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_qianfajiguan_id"]).clear()
    #         time.sleep(1)
    #         driver.find_element_by_id(
    #             elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_qianfajiguan_id"]).send_keys(
    #             input_qianfajiguan)
    #         time.sleep(1)
    #         # driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_fadongjihao_id"]).send_keys(input_zhuceriqi)
    #         # time.sleep(1)
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
    #         time.sleep(1)
    #         # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
    #         # time.sleep(1)
    #         logger.info(f'{sys._getframe().f_code.co_name},{input_qianfajiguan}修改成功')
    #     except Exception:
    #         logbug.debug(f'{sys._getframe().f_code.co_name},{input_qianfajiguan} 修改失败')


#-----------------------------------------------------------------以下内容暂未维护
    def kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_tongtoubaoren(driver,input_tongtoubaoren = '不同投保人'):
        """客户详情-关系人信息-被保险人信息-同投保人，参数要传相同或不同，如‘同投保人’‘不同投保人’"""
        try:
            driver.find_elements_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"])[3].click()
            time.sleep(1)
            if input_tongtoubaoren == '同投保人':
                if driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_tongtoubaoren_css"]).get_attribute('class') == elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_tongtoubaoren_checked_class"]:
                    pass
                    time.sleep(1)
                else:
                    driver.find_element_by_css_selector(
                        elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_tongtoubaoren_css"]).click()
                    time.sleep(1)
            elif input_tongtoubaoren == '不同投保人':
                if driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_tongtoubaoren_css"]).get_attribute('class') == elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_tongtoubaoren_checked_class"]:
                    driver.find_element_by_css_selector(
                        elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_tongtoubaoren_css"]).click()
                    time.sleep(1)
                else:
                    pass
                    time.sleep(1)
            else:
                pass
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},修改失败')

    def kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_gonghu(driver):
        """客户详情-关系人信息-被保险人信息-快速选择‘公户’，无需传递参数"""
        try:
            driver.find_elements_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"])[3].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(
                elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_quickselect_gonghu_css"])[4].click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},修改失败')
    #
    # def kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_geren(driver):
    #     """客户详情-关系人信息-被保险人信息-快速选择‘个人’，无需传递参数"""
    #     try:
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"]).click()
    #         time.sleep(1)
    #         driver.find_element_by_css_selector(
    #             elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_quickselect_geren_css"])[5].click()
    #         time.sleep(1)
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
    #         time.sleep(1)
    #         # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
    #         # time.sleep(1)
    #         logger.info(f'{sys._getframe().f_code.co_name},修改成功')
    #     except Exception:
    #         logbug.debug(f'{sys._getframe().f_code.co_name},修改失败')
    #
    # def kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_beibaoxianrenxingming(driver, input_beibaoxianrenxingming=elements["test_vin"]):
    #     """客户详情-关系人信息-被保险人信息-被保险人姓名，参数要传具体姓名，如‘李明’"""
    #     try:
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"]).click()
    #         time.sleep(1)
    #         driver.find_element_by_id(elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_beibaoxianrenxingming_id"]).click()
    #         time.sleep(1)
    #         driver.find_element_by_id(elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_beibaoxianrenxingming_id"]).send_keys(input_beibaoxianrenxingming)
    #         time.sleep(1)
    #         # driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_fadongjihao_id"]).send_keys(input_zhuceriqi)
    #         # time.sleep(1)
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
    #         time.sleep(1)
    #         # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
    #         # time.sleep(1)
    #         logger.info(f'{sys._getframe().f_code.co_name},{input_beibaoxianrenxingming}修改成功')
    #     except Exception:
    #         logbug.debug(f'{sys._getframe().f_code.co_name},{input_beibaoxianrenxingming} 修改失败')
    #
    # def kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianleixing(driver, input_zhengjianleixing, input_zhengjianhaoma=elements["test_vin"]):
    #     """客户详情-关系人信息-被保险人信息-证件类型+号码，参数要传具体类型，如‘身份证’，与下拉框中文本保持一致
    #     号码要传具体号码，如‘110100199999999999’"""
    #     try:
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"]).click()
    #         time.sleep(1)
    #         driver.find_element_by_id(elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianleixing_id"]).click()
    #         time.sleep(1)
    #         if input_zhengjianleixing == '身份证':
    #             driver.find_elements_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianleixing_css"])[4].click()
    #             time.sleep(1)
    #             driver.find_element_by_id(
    #                 elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianhaoma_id"]).clear()
    #             time.sleep(1)
    #             driver.find_element_by_id(
    #                 elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianhaoma_id"]).send_keys(input_zhengjianhaoma)
    #             time.sleep(1)
    #         elif input_zhengjianleixing == '组织机构代码证':
    #             driver.find_elements_by_css_selector(
    #                 elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianleixing_css"])[5].click()
    #             time.sleep(1)
    #             driver.find_element_by_id(
    #                 elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianhaoma_id"]).clear()
    #             time.sleep(1)
    #             driver.find_element_by_id(
    #                 elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianhaoma_id"]).send_keys(input_zhengjianhaoma)
    #             time.sleep(1)
    #         elif input_zhengjianleixing == '营业执照/统一社会信用代码':
    #             driver.find_elements_by_css_selector(
    #                 elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianleixing_css"])[6].click()
    #             time.sleep(1)
    #             driver.find_element_by_id(
    #                 elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianhaoma_id"]).clear()
    #             time.sleep(1)
    #             driver.find_element_by_id(
    #                 elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianhaoma_id"]).send_keys(input_zhengjianhaoma)
    #             time.sleep(1)
    #         elif input_zhengjianleixing == '港澳居民来往内地通行证':
    #             driver.find_elements_by_css_selector(
    #                 elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianleixing_css"])[7].click()
    #             time.sleep(1)
    #             driver.find_element_by_id(
    #                 elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianhaoma_id"]).clear()
    #             time.sleep(1)
    #             driver.find_element_by_id(
    #                 elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianhaoma_id"]).send_keys(input_zhengjianhaoma)
    #             time.sleep(1)
    #         elif input_zhengjianleixing == '港澳身份证':
    #             driver.find_elements_by_css_selector(
    #                 elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianleixing_css"])[8].click()
    #             time.sleep(1)
    #             driver.find_element_by_id(
    #                 elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianhaoma_id"]).clear()
    #             time.sleep(1)
    #             driver.find_element_by_id(
    #                 elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianhaoma_id"]).send_keys(input_zhengjianhaoma)
    #             time.sleep(1)
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
    #         time.sleep(1)
    #         # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
    #         # time.sleep(1)
    #         logger.info(f'{sys._getframe().f_code.co_name},{input_zhengjianleixing}修改成功')
    #     except Exception:
    #         logbug.debug(f'{sys._getframe().f_code.co_name},{input_zhengjianleixing} 修改失败')
    #
    # def kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_beibaoxianrendianhua(driver,
    #                                                                           input_beibaoxianrendianhua=elements[
    #                                                                               "test_vin"]):
    #     """客户详情-关系人信息-被保险人信息-被保险人电话，参数要传具体电话，如‘13300009999’"""
    #     try:
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"]).click()
    #         time.sleep(1)
    #         driver.find_element_by_id(
    #             elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_beibaoxianrendianhua_id"]).clear()
    #         time.sleep(1)
    #         driver.find_element_by_id(
    #             elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_beibaoxianrendianhua_id"]).send_keys(
    #             input_beibaoxianrendianhua)
    #         time.sleep(1)
    #         # driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_fadongjihao_id"]).send_keys(input_zhuceriqi)
    #         # time.sleep(1)
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
    #         time.sleep(1)
    #         # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
    #         # time.sleep(1)
    #         logger.info(f'{sys._getframe().f_code.co_name},{input_beibaoxianrendianhua}修改成功')
    #     except Exception:
    #         logbug.debug(f'{sys._getframe().f_code.co_name},{input_beibaoxianrendianhua} 修改失败')
    # def kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_beibaoxianrenyouxiang(driver,
    #                                                                           input_beibaoxianrenyouxiang=elements[
    #                                                                               "test_vin"]):
    #     """客户详情-关系人信息-被保险人信息-被保险人邮箱，参数要传具体邮箱，如‘fff@91bihu.com’"""
    #     try:
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"]).click()
    #         time.sleep(1)
    #         driver.find_element_by_id(
    #             elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_beibaoxianrenyouxiang_id"]).clear()
    #         time.sleep(1)
    #         driver.find_element_by_id(
    #             elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_beibaoxianrenyouxiang_id"]).send_keys(
    #             input_beibaoxianrenyouxiang)
    #         time.sleep(1)
    #         # driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_fadongjihao_id"]).send_keys(input_zhuceriqi)
    #         # time.sleep(1)
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
    #         time.sleep(1)
    #         # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
    #         # time.sleep(1)
    #         logger.info(f'{sys._getframe().f_code.co_name},{input_beibaoxianrenyouxiang}修改成功')
    #     except Exception:
    #         logbug.debug(f'{sys._getframe().f_code.co_name},{input_beibaoxianrenyouxiang} 修改失败')
    #
    # def kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhuzhi(driver, input_zhuzhi=elements["test_vin"]):
    #     """客户详情-关系人信息-被保险人信息-住址，参数要传具体住址，如‘北京市海淀区’"""
    #     try:
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"]).click()
    #         time.sleep(1)
    #         driver.find_element_by_id(elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhuzhi_id"]).clear()
    #         time.sleep(1)
    #         driver.find_element_by_id(elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhuzhi_id"]).send_keys(
    #             input_zhuzhi)
    #         time.sleep(1)
    #         # driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_fadongjihao_id"]).send_keys(input_zhuceriqi)
    #         # time.sleep(1)
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
    #         time.sleep(1)
    #         # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
    #         # time.sleep(1)
    #         logger.info(f'{sys._getframe().f_code.co_name},{input_zhuzhi}修改成功')
    #     except Exception:
    #         logbug.debug(f'{sys._getframe().f_code.co_name},{input_zhuzhi} 修改失败')
    #
    # def kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_minzu(driver, input_minzu=elements["test_vin"]):
    #     """客户详情-关系人信息-被保险人信息-民族，参数要传具体民族，如‘汉族’"""
    #     try:
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"]).click()
    #         time.sleep(1)
    #         driver.find_element_by_id(elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_minzu_id"]).clear()
    #         time.sleep(1)
    #         driver.find_element_by_id(elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_minzu_id"]).send_keys(
    #             input_minzu)
    #         time.sleep(1)
    #         # driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_fadongjihao_id"]).send_keys(input_zhuceriqi)
    #         # time.sleep(1)
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
    #         time.sleep(1)
    #         # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
    #         # time.sleep(1)
    #         logger.info(f'{sys._getframe().f_code.co_name},{input_minzu}修改成功')
    #     except Exception:
    #         logbug.debug(f'{sys._getframe().f_code.co_name},{input_minzu} 修改失败')
    #
    # def kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_qianfajiguan(driver, input_qianfajiguan=elements["test_vin"]):
    #     """客户详情-关系人信息-被保险人信息-签发机关，参数要传具体签发机关，如‘xxx机关’"""
    #     try:
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"]).click()
    #         time.sleep(1)
    #         driver.find_element_by_id(elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_qianfajiguan_id"]).clear()
    #         time.sleep(1)
    #         driver.find_element_by_id(elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_qianfajiguan_id"]).send_keys(
    #             input_qianfajiguan)
    #         time.sleep(1)
    #         # driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_fadongjihao_id"]).send_keys(input_zhuceriqi)
    #         # time.sleep(1)
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
    #         time.sleep(1)
    #         # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
    #         # time.sleep(1)
    #         logger.info(f'{sys._getframe().f_code.co_name},{input_qianfajiguan}修改成功')
    #     except Exception:
    #         logbug.debug(f'{sys._getframe().f_code.co_name},{input_qianfajiguan} 修改失败')
# -----------------------------------------------------------------以上内容暂未维护


#-----------------拖到可见
# target = driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baocun_button_css"])
# driver.execute_script("arguments[0].scrollIntoView();", target)
# -----------------拖到可见

    def kehuxiangqing_baojiaxinxi_toubaodiqu(driver, input_toubaodiqu='3'):
        """客户详情-报价信息-投保地区，参数传数字即可，如‘1’，数字代表在下拉菜单中排第几的选项，
        修改后不报价，需要和后续方法一起调用"""
        try:
            driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_tab_css"])[4].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_toubaodiqu_css"])[9].click()
            time.sleep(1)
            if input_toubaodiqu == '1':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)').click()")
                time.sleep(1)
            elif input_toubaodiqu == '2':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)').click()")
                time.sleep(1)
            elif input_toubaodiqu == '3':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(3)').click()")
                time.sleep(1)
            elif input_toubaodiqu == '4':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(4)').click()")
                time.sleep(1)
            elif input_toubaodiqu == '5':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(5)').click()")
                time.sleep(1)
            elif input_toubaodiqu == '6':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(6)').click()")
                time.sleep(1)
            elif input_toubaodiqu == '7':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(7)').click()")
                time.sleep(1)
            elif input_toubaodiqu == '8':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(8)').click()")
                time.sleep(1)
            elif input_toubaodiqu == '9':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(9)').click()")
                time.sleep(1)
            elif input_toubaodiqu == '10':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(10)').click()")
                time.sleep(1)
            elif input_toubaodiqu == '11':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(11)').click()")
                time.sleep(1)
            elif input_toubaodiqu == '12':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(12)').click()")
                time.sleep(1)
            elif input_toubaodiqu == '13':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(13)').click()")
                time.sleep(1)
            elif input_toubaodiqu == '14':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(14)').click()")
                time.sleep(1)
            elif input_toubaodiqu == '15':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(15)').click()")
                time.sleep(1)
            elif input_toubaodiqu == '16':
                driver.execute_script(
                    "$('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(16)').click()")
                time.sleep(1)
            else:
                pass
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_toubaodiqu} 修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_toubaodiqu} 修改失败')

    def kehuxiangqing_baojiaxinxi_shangyexianqibao(driver, input_shangyexianqibaodate='2020-01-01', input_shangyexianqibaotime = '23:59:59'):
        """客户详情-报价信息-商业险起保修改，参数要传2个，前面是日期，格式如‘2019-01-01’，后面是时间，格式如：‘23：59：59’
        如果想选择‘此刻’，则日期参数要传‘此刻’，时间参数无需传递
        另：时间必须真实存在，且与业务要求吻合，不要输入不存在，不可选择的时间"""
        try:
            driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_tab_css"])[4].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_shangyexianqibao_css"])[32].click()
            time.sleep(1)
            if input_shangyexianqibaodate == '此刻':
                driver.find_element_by_css_selector(
                    elements["kehuxiangqing_baojiaxinxi_shangyexianqibao_cike_css"]).click()
                time.sleep(1)
            else:
                driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_shangyexianqibao_inputdate_css"])[0].clear()
                time.sleep(1)
                driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_shangyexianqibao_inputdate_css"])[0].send_keys(input_shangyexianqibaodate)
                time.sleep(1)
                driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_shangyexianqibao_inputtime_css"])[1].clear()
                time.sleep(1)
                driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_shangyexianqibao_inputtime_css"])[1].send_keys(input_shangyexianqibaotime)
                time.sleep(1)
                # 点一下确认，收回时间框
                driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_shangyexianqibao_inputtime_queding_css"]).click()
                time.sleep(1)
                driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_shangyexianqibao_queren_css"]).click()
                time.sleep(1)
                # 点一下确认，收回时间框
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_shangyexianqibaodate},{input_shangyexianqibaotime} 修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_shangyexianqibaodate},{input_shangyexianqibaotime} 修改失败')

    def kehuxiangqing_baojiaxinxi_jiaoqiangxianqibao(driver, input_jiaoqiangxianqibaodate='2019-01-01', input_jiaoqiangxianqibaotime = '23:59:59'):
        """客户详情-报价信息-交强险起保修改，参数要传2个，前面是日期，格式如‘2019-01-01’，后面是时间，格式如：‘23：59：59’
        如果想选择‘此刻’，则日期参数要传‘此刻’，时间参数无需传递
        另：时间必须真实存在，且与业务要求吻合，不要输入不存在，不可选择的时间"""
        try:
            driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_tab_css"])[4].click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_jiaoqiangxianqibao_css"])[33].click()
            time.sleep(1)
            if input_jiaoqiangxianqibaodate == '此刻':
                driver.find_element_by_css_selector(
                    elements["kehuxiangqing_baojiaxinxi_jiaoqiangxianqibao_cike_css"]).click()
                time.sleep(1)
            else:
                driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_jiaoqiangxianqibao_inputdate_css"])[0].clear()
                time.sleep(1)
                driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_jiaoqiangxianqibao_inputdate_css"])[0].send_keys(input_jiaoqiangxianqibaodate)
                time.sleep(1)
                driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_jiaoqiangxianqibao_inputtime_css"])[1].clear()
                time.sleep(1)
                driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_jiaoqiangxianqibao_inputtime_css"])[1].send_keys(input_jiaoqiangxianqibaotime)
                time.sleep(1)
                # 点一下确认，收回时间框
                driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_jiaoqiangxianqibao_inputtime_queding_css"]).click()
                time.sleep(1)
                driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_jiaoqiangxianqibao_queren_css"]).click()
                time.sleep(1)
                # 点一下确认，收回时间框
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_jiaoqiangxianqibaodate},{input_jiaoqiangxianqibaotime} 修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_jiaoqiangxianqibaodate},{input_jiaoqiangxianqibaotime} 修改失败')

    def kehuxiangqing_baojiaxinxi_baojiagongsi(driver, input_baojiagongsi = 11):
        """客户详情-报价信息-选择报价公司，参数传数字即可，1=太平洋，2=平安，4=人保，8=国寿财
        如需多家，则数字相加，如太平洋+平安 = 3"""
        try:
            driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_tab_css"])[4].click()
            time.sleep(1)

            # 取消勾选--------------
            for xuhao in range(0, len(driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"]))):
                if driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"])[xuhao].get_attribute('class') == elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checked_class"]:
                    driver.find_elements_by_css_selector(
                        elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"])[
                        xuhao].click()
                    time.sleep(1)
                else:
                    pass
            time.sleep(1)
            # 取消勾选--------------

            # 勾选保险公司--------------
            if input_baojiagongsi == 1: #太平洋
                for xuhao in range(0, len(driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"]))):
                    text_path = elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"] + ":nth-child(" + str(xuhao+1) + ")> span:nth-child(2)"
                    if driver.find_element_by_css_selector(text_path).text == '太平洋':
                        driver.find_elements_by_css_selector(
                            elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"])[xuhao].click()
                        time.sleep(1)
                        logger.info(f'{sys._getframe().f_code.co_name},{driver.find_element_by_css_selector(text_path).text}选择成功')
                    else:
                        pass

            elif input_baojiagongsi == 2:  # 平安
                for xuhao in range(0, len(driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"]))):
                    text_path = elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"] + ":nth-child(" + str(xuhao+1) + ")> span:nth-child(2)"
                    if driver.find_element_by_css_selector(text_path).text == '平安':
                        driver.find_elements_by_css_selector(
                            elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"])[xuhao].click()
                        time.sleep(1)
                        logger.info(f'{sys._getframe().f_code.co_name},{driver.find_element_by_css_selector(text_path).text}选择成功')
                    else:
                        pass

            elif input_baojiagongsi == 3:  # 平安 + 太平洋
                for xuhao in range(0, len(driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"]))):
                    text_path = elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"] + ":nth-child(" + str(xuhao+1) + ")> span:nth-child(2)"
                    # quoteInfo\.quoteSource > label:nth-child(1) > span:nth-child(2)
                    if driver.find_element_by_css_selector(text_path).text == '平安' or driver.find_element_by_css_selector(text_path).text == '太平洋':
                        driver.find_elements_by_css_selector(
                            elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"])[xuhao].click()
                        time.sleep(1)
                        logger.info(f'{sys._getframe().f_code.co_name},{driver.find_element_by_css_selector(text_path).text}选择成功')
                    else:
                        pass

            elif input_baojiagongsi == 4:  # 人保
                for xuhao in range(0, len(driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"]))):
                    text_path = elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"] + ":nth-child(" + str(xuhao+1) + ")> span:nth-child(2)"
                    # quoteInfo\.quoteSource > label:nth-child(1) > span:nth-child(2)
                    if driver.find_element_by_css_selector(text_path).text == '人保':
                        driver.find_elements_by_css_selector(
                            elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"])[xuhao].click()
                        time.sleep(1)
                        logger.info(f'{sys._getframe().f_code.co_name},{driver.find_element_by_css_selector(text_path).text}选择成功')
                    else:
                        pass

            elif input_baojiagongsi == 5:  # 人保 + 太平洋
                for xuhao in range(0, len(driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"]))):
                    text_path = elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"] + ":nth-child(" + str(xuhao+1) + ")> span:nth-child(2)"
                    # quoteInfo\.quoteSource > label:nth-child(1) > span:nth-child(2)
                    if driver.find_element_by_css_selector(text_path).text == '人保' or driver.find_element_by_css_selector(text_path).text == '太平洋':
                        driver.find_elements_by_css_selector(
                            elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"])[xuhao].click()
                        time.sleep(1)
                        logger.info(f'{sys._getframe().f_code.co_name},{driver.find_element_by_css_selector(text_path).text}选择成功')
                    else:
                        pass

            elif input_baojiagongsi == 6:  # 人保 + 平安
                for xuhao in range(0, len(driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"]))):
                    text_path = elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"] + ":nth-child(" + str(xuhao+1) + ")> span:nth-child(2)"
                    # quoteInfo\.quoteSource > label:nth-child(1) > span:nth-child(2)
                    if driver.find_element_by_css_selector(text_path).text == '人保' or driver.find_element_by_css_selector(text_path).text == '平安':
                        driver.find_elements_by_css_selector(
                            elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"])[xuhao].click()
                        time.sleep(1)
                        logger.info(f'{sys._getframe().f_code.co_name},{driver.find_element_by_css_selector(text_path).text}选择成功')
                    else:
                        pass

            elif input_baojiagongsi == 7:  # 人保 + 平安 + 太平洋
                for xuhao in range(0, len(driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"]))):
                    text_path = elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"] + ":nth-child(" + str(xuhao+1) + ")> span:nth-child(2)"
                    # quoteInfo\.quoteSource > label:nth-child(1) > span:nth-child(2)
                    if driver.find_element_by_css_selector(text_path).text == '人保' or driver.find_element_by_css_selector(text_path).text == '平安'or driver.find_element_by_css_selector(text_path).text == '太平洋':
                        driver.find_elements_by_css_selector(
                            elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"])[xuhao].click()
                        time.sleep(1)
                        logger.info(f'{sys._getframe().f_code.co_name},{driver.find_element_by_css_selector(text_path).text}选择成功')
                    else:
                        pass

            elif input_baojiagongsi == 8:  # 国寿财
                for xuhao in range(0, len(driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"]))):
                    text_path = elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"] + ":nth-child(" + str(xuhao+1) + ")> span:nth-child(2)"
                    # quoteInfo\.quoteSource > label:nth-child(1) > span:nth-child(2)
                    if driver.find_element_by_css_selector(text_path).text == '国寿财':
                        driver.find_elements_by_css_selector(
                            elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"])[xuhao].click()
                        time.sleep(1)
                        logger.info(f'{sys._getframe().f_code.co_name},{driver.find_element_by_css_selector(text_path).text}选择成功')
                    else:
                        pass


            elif input_baojiagongsi == 9:  # 国寿财 + 太平洋
                for xuhao in range(0, len(driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"]))):
                    text_path = elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"] + ":nth-child(" + str(xuhao+1) + ")> span:nth-child(2)"
                    # quoteInfo\.quoteSource > label:nth-child(1) > span:nth-child(2)
                    if driver.find_element_by_css_selector(text_path).text == '国寿财'or driver.find_element_by_css_selector(text_path).text == '太平洋':
                        driver.find_elements_by_css_selector(
                            elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"])[xuhao].click()
                        time.sleep(1)
                        logger.info(f'{sys._getframe().f_code.co_name},{driver.find_element_by_css_selector(text_path).text}选择成功')
                    else:
                        pass

            elif input_baojiagongsi == 10:  # 国寿财 + 平安
                for xuhao in range(0, len(driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"]))):
                    text_path = elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"] + ":nth-child(" + str(xuhao+1) + ")> span:nth-child(2)"
                    # quoteInfo\.quoteSource > label:nth-child(1) > span:nth-child(2)
                    if driver.find_element_by_css_selector(text_path).text == '国寿财' or driver.find_element_by_css_selector(text_path).text == '平安':
                        driver.find_elements_by_css_selector(
                            elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"])[xuhao].click()
                        time.sleep(1)
                        logger.info(f'{sys._getframe().f_code.co_name},{driver.find_element_by_css_selector(text_path).text}选择成功')
                    else:
                        pass

            elif input_baojiagongsi == 11:  # 国寿财 + 平安 + 太平洋
                for xuhao in range(0, len(driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"]))):
                    text_path = elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"] + ":nth-child(" + str(xuhao+1) + ")> span:nth-child(2)"
                    # quoteInfo\.quoteSource > label:nth-child(1) > span:nth-child(2)
                    if driver.find_element_by_css_selector(text_path).text == '国寿财' or driver.find_element_by_css_selector(text_path).text == '平安'or driver.find_element_by_css_selector(text_path).text == '太平洋':
                        driver.find_elements_by_css_selector(
                            elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"])[xuhao].click()
                        time.sleep(1)
                        logger.info(f'{sys._getframe().f_code.co_name},{driver.find_element_by_css_selector(text_path).text}选择成功')
                    else:
                        pass

            elif input_baojiagongsi == 12:  # 人保 + 国寿财
                for xuhao in range(0, len(driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"]))):
                    text_path = elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"] + ":nth-child(" + str(xuhao+1) + ")> span:nth-child(2)"
                    # quoteInfo\.quoteSource > label:nth-child(1) > span:nth-child(2)
                    if driver.find_element_by_css_selector(text_path).text == '人保' or driver.find_element_by_css_selector(text_path).text == '国寿财':
                        driver.find_elements_by_css_selector(
                            elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"])[xuhao].click()
                        time.sleep(1)
                        logger.info(f'{sys._getframe().f_code.co_name},{driver.find_element_by_css_selector(text_path).text}选择成功')
                    else:
                        pass

            elif input_baojiagongsi == 13:  # 人保 + 国寿财 + 太平洋
                for xuhao in range(0, len(driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"]))):
                    text_path = elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"] + ":nth-child(" + str(xuhao+1) + ")> span:nth-child(2)"
                    # quoteInfo\.quoteSource > label:nth-child(1) > span:nth-child(2)
                    if driver.find_element_by_css_selector(text_path).text == '人保' or driver.find_element_by_css_selector(text_path).text == '国寿财'or driver.find_element_by_css_selector(text_path).text == '太平洋':
                        driver.find_elements_by_css_selector(
                            elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"])[xuhao].click()
                        time.sleep(1)
                        logger.info(f'{sys._getframe().f_code.co_name},{driver.find_element_by_css_selector(text_path).text}选择成功')
                    else:
                        pass

            elif input_baojiagongsi == 14:  # 人保 + 国寿财 + 平安
                for xuhao in range(0, len(driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"]))):
                    text_path = elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"] + ":nth-child(" + str(xuhao+1) + ")> span:nth-child(2)"
                    # quoteInfo\.quoteSource > label:nth-child(1) > span:nth-child(2)
                    if driver.find_element_by_css_selector(text_path).text == '人保' or driver.find_element_by_css_selector(text_path).text == '平安'or driver.find_element_by_css_selector(text_path).text == '国寿财':
                        driver.find_elements_by_css_selector(
                            elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"])[xuhao].click()
                        time.sleep(1)
                        logger.info(f'{sys._getframe().f_code.co_name},{driver.find_element_by_css_selector(text_path).text}选择成功')
                    else:
                        pass

            elif input_baojiagongsi == 15:  # 人保 + 平安 + 太平洋 + 国寿财
                for xuhao in range(0, len(driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"]))):
                    text_path = elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"] + ":nth-child(" + str(xuhao+1) + ")> span:nth-child(2)"
                    # quoteInfo\.quoteSource > label:nth-child(1) > span:nth-child(2)
                    if driver.find_element_by_css_selector(text_path).text == '人保' or driver.find_element_by_css_selector(text_path).text == '平安' or driver.find_element_by_css_selector(text_path).text == '太平洋' or driver.find_element_by_css_selector(text_path).text == '国寿财':
                        driver.find_elements_by_css_selector(
                            elements["kehuxiangqing_baojiaxinxi_baojiagongsi_checkbox_css"])[xuhao].click()
                        time.sleep(1)
                        logger.info(f'{sys._getframe().f_code.co_name},{driver.find_element_by_css_selector(text_path).text}选择成功')
                    else:
                        pass
            else:
                pass
            # 勾选保险公司--------------
            logger.info(f'{sys._getframe().f_code.co_name}, {input_baojiagongsi}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}, {input_baojiagongsi} 修改失败')

    def kehuxiangqing_baojiaxinxi_hebaogongsi(driver, input_hebaogongsi = 11):
        """客户详情-报价信息-选择核保公司，参数传数字即可，1=太平洋，2=平安，4=人保，8=国寿财
        如需多家，则数字相加，如太平洋+平安 = 3
        另：核保公司最好和报价公司保持一致"""
        try:
            driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_tab_css"])[4].click()
            time.sleep(1)

            # 取消勾选--------------
            # for xuhao in range(0, len(driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"]))):
            #     if driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"])[xuhao].get_attribute('class') == elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checked_class"]:
            #         driver.find_elements_by_css_selector(
            #             elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"])[
            #             xuhao].click()
            #         time.sleep(1)
            #     else:
            #         pass
            # time.sleep(1)
            # 取消勾选--------------

            # 勾选核保公司--------------
            if input_hebaogongsi == 1: #太平洋
                for xuhao in range(0, len(driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"])[1])):
                    text_path = elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"] + ":nth-child(" + str(xuhao+1) + ")> span:nth-child(2)"
                    if driver.find_element_by_css_selector(text_path).text == '太平洋':
                        driver.find_elements_by_css_selector(
                            elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"])[xuhao].click()
                        time.sleep(1)
                        logger.info(f'{sys._getframe().f_code.co_name},{driver.find_element_by_css_selector(text_path).text}选择成功')
                    else:
                        pass

            elif input_hebaogongsi == 2:  # 平安
                for xuhao in range(0, len(driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"]))):
                    text_path = elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"] + ":nth-child(" + str(xuhao+1) + ")> span:nth-child(2)"
                    if driver.find_element_by_css_selector(text_path).text == '平安':
                        driver.find_elements_by_css_selector(
                            elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"])[xuhao].click()
                        time.sleep(1)
                        logger.info(f'{sys._getframe().f_code.co_name},{driver.find_element_by_css_selector(text_path).text}选择成功')
                    else:
                        pass

            elif input_hebaogongsi == 3:  # 平安 + 太平洋
                for xuhao in range(0, len(driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"]))):
                    text_path = elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"] + ":nth-child(" + str(xuhao+1) + ")> span:nth-child(2)"
                    # quoteInfo\.quoteSource > label:nth-child(1) > span:nth-child(2)
                    if driver.find_element_by_css_selector(text_path).text == '平安' or driver.find_element_by_css_selector(text_path).text == '太平洋':
                        driver.find_elements_by_css_selector(
                            elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"])[xuhao].click()
                        time.sleep(1)
                        logger.info(f'{sys._getframe().f_code.co_name},{driver.find_element_by_css_selector(text_path).text}选择成功')
                    else:
                        pass

            elif input_hebaogongsi == 4:  # 人保
                for xuhao in range(0, len(driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"]))):
                    text_path = elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"] + ":nth-child(" + str(xuhao+1) + ")> span:nth-child(2)"
                    # quoteInfo\.quoteSource > label:nth-child(1) > span:nth-child(2)
                    if driver.find_element_by_css_selector(text_path).text == '人保':
                        driver.find_elements_by_css_selector(
                            elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"])[xuhao].click()
                        time.sleep(1)
                        logger.info(f'{sys._getframe().f_code.co_name},{driver.find_element_by_css_selector(text_path).text}选择成功')
                    else:
                        pass

            elif input_hebaogongsi == 5:  # 人保 + 太平洋
                for xuhao in range(0, len(driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"]))):
                    text_path = elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"] + ":nth-child(" + str(xuhao+1) + ")> span:nth-child(2)"
                    # quoteInfo\.quoteSource > label:nth-child(1) > span:nth-child(2)
                    if driver.find_element_by_css_selector(text_path).text == '人保' or driver.find_element_by_css_selector(text_path).text == '太平洋':
                        driver.find_elements_by_css_selector(
                            elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"])[xuhao].click()
                        time.sleep(1)
                        logger.info(f'{sys._getframe().f_code.co_name},{driver.find_element_by_css_selector(text_path).text}选择成功')
                    else:
                        pass

            elif input_hebaogongsi == 6:  # 人保 + 平安
                for xuhao in range(0, len(driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"]))):
                    text_path = elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"] + ":nth-child(" + str(xuhao+1) + ")> span:nth-child(2)"
                    # quoteInfo\.quoteSource > label:nth-child(1) > span:nth-child(2)
                    if driver.find_element_by_css_selector(text_path).text == '人保' or driver.find_element_by_css_selector(text_path).text == '平安':
                        driver.find_elements_by_css_selector(
                            elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"])[xuhao].click()
                        time.sleep(1)
                        logger.info(f'{sys._getframe().f_code.co_name},{driver.find_element_by_css_selector(text_path).text}选择成功')
                    else:
                        pass

            elif input_hebaogongsi == 7:  # 人保 + 平安 + 太平洋
                for xuhao in range(0, len(driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"]))):
                    text_path = elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"] + ":nth-child(" + str(xuhao+1) + ")> span:nth-child(2)"
                    # quoteInfo\.quoteSource > label:nth-child(1) > span:nth-child(2)
                    if driver.find_element_by_css_selector(text_path).text == '人保' or driver.find_element_by_css_selector(text_path).text == '平安'or driver.find_element_by_css_selector(text_path).text == '太平洋':
                        driver.find_elements_by_css_selector(
                            elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"])[xuhao].click()
                        time.sleep(1)
                        logger.info(f'{sys._getframe().f_code.co_name},{driver.find_element_by_css_selector(text_path).text}选择成功')
                    else:
                        pass

            elif input_hebaogongsi == 8:  # 国寿财
                for xuhao in range(0, len(driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"]))):
                    text_path = elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"] + ":nth-child(" + str(xuhao+1) + ")> span:nth-child(2)"
                    # quoteInfo\.quoteSource > label:nth-child(1) > span:nth-child(2)
                    if driver.find_element_by_css_selector(text_path).text == '国寿财':
                        driver.find_elements_by_css_selector(
                            elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"])[xuhao].click()
                        time.sleep(1)
                        logger.info(f'{sys._getframe().f_code.co_name},{driver.find_element_by_css_selector(text_path).text}选择成功')
                    else:
                        pass


            elif input_hebaogongsi == 9:  # 国寿财 + 太平洋
                for xuhao in range(0, len(driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"]))):
                    text_path = elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"] + ":nth-child(" + str(xuhao+1) + ")> span:nth-child(2)"
                    # quoteInfo\.quoteSource > label:nth-child(1) > span:nth-child(2)
                    if driver.find_element_by_css_selector(text_path).text == '国寿财'or driver.find_element_by_css_selector(text_path).text == '太平洋':
                        driver.find_elements_by_css_selector(
                            elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"])[xuhao].click()
                        time.sleep(1)
                        logger.info(f'{sys._getframe().f_code.co_name},{driver.find_element_by_css_selector(text_path).text}选择成功')
                    else:
                        pass

            elif input_hebaogongsi == 10:  # 国寿财 + 平安
                for xuhao in range(0, len(driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"]))):
                    text_path = elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"] + ":nth-child(" + str(xuhao+1) + ")> span:nth-child(2)"
                    # quoteInfo\.quoteSource > label:nth-child(1) > span:nth-child(2)
                    if driver.find_element_by_css_selector(text_path).text == '国寿财' or driver.find_element_by_css_selector(text_path).text == '平安':
                        driver.find_elements_by_css_selector(
                            elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"])[xuhao].click()
                        time.sleep(1)
                        logger.info(f'{sys._getframe().f_code.co_name},{driver.find_element_by_css_selector(text_path).text}选择成功')
                    else:
                        pass

            elif input_hebaogongsi == 11:  # 国寿财 + 平安 + 太平洋
                for xuhao in range(0, len(driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"]))):
                    text_path = elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"] + ":nth-child(" + str(xuhao+1) + ")> span:nth-child(2)"
                    # quoteInfo\.quoteSource > label:nth-child(1) > span:nth-child(2)
                    if driver.find_element_by_css_selector(text_path).text == '国寿财' or driver.find_element_by_css_selector(text_path).text == '平安'or driver.find_element_by_css_selector(text_path).text == '太平洋':
                        driver.find_elements_by_css_selector(
                            elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"])[xuhao].click()
                        time.sleep(1)
                        logger.info(f'{sys._getframe().f_code.co_name},{driver.find_element_by_css_selector(text_path).text}选择成功')
                    else:
                        pass

            elif input_hebaogongsi == 12:  # 人保 + 国寿财
                for xuhao in range(0, len(driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"]))):
                    text_path = elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"] + ":nth-child(" + str(xuhao+1) + ")> span:nth-child(2)"
                    # quoteInfo\.quoteSource > label:nth-child(1) > span:nth-child(2)
                    if driver.find_element_by_css_selector(text_path).text == '人保' or driver.find_element_by_css_selector(text_path).text == '国寿财':
                        driver.find_elements_by_css_selector(
                            elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"])[xuhao].click()
                        time.sleep(1)
                        logger.info(f'{sys._getframe().f_code.co_name},{driver.find_element_by_css_selector(text_path).text}选择成功')
                    else:
                        pass

            elif input_hebaogongsi == 13:  # 人保 + 国寿财 + 太平洋
                for xuhao in range(0, len(driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"]))):
                    text_path = elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"] + ":nth-child(" + str(xuhao+1) + ")> span:nth-child(2)"
                    # quoteInfo\.quoteSource > label:nth-child(1) > span:nth-child(2)
                    if driver.find_element_by_css_selector(text_path).text == '人保' or driver.find_element_by_css_selector(text_path).text == '国寿财'or driver.find_element_by_css_selector(text_path).text == '太平洋':
                        driver.find_elements_by_css_selector(
                            elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"])[xuhao].click()
                        time.sleep(1)
                        logger.info(f'{sys._getframe().f_code.co_name},{driver.find_element_by_css_selector(text_path).text}选择成功')
                    else:
                        pass

            elif input_hebaogongsi == 14:  # 人保 + 国寿财 + 平安
                for xuhao in range(0, len(driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"]))):
                    text_path = elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"] + ":nth-child(" + str(xuhao+1) + ")> span:nth-child(2)"
                    # quoteInfo\.quoteSource > label:nth-child(1) > span:nth-child(2)
                    if driver.find_element_by_css_selector(text_path).text == '人保' or driver.find_element_by_css_selector(text_path).text == '平安'or driver.find_element_by_css_selector(text_path).text == '国寿财':
                        driver.find_elements_by_css_selector(
                            elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"])[xuhao].click()
                        time.sleep(1)
                        logger.info(f'{sys._getframe().f_code.co_name},{driver.find_element_by_css_selector(text_path).text}选择成功')
                    else:
                        pass

            elif input_hebaogongsi == 15:  # 人保 + 平安 + 太平洋 + 国寿财
                for xuhao in range(0, len(driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"]))):
                    text_path = elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"] + ":nth-child(" + str(xuhao+1) + ")> span:nth-child(2)"
                    # quoteInfo\.quoteSource > label:nth-child(1) > span:nth-child(2)
                    if driver.find_element_by_css_selector(text_path).text == '人保' or driver.find_element_by_css_selector(text_path).text == '平安' or driver.find_element_by_css_selector(text_path).text == '太平洋' or driver.find_element_by_css_selector(text_path).text == '国寿财':
                        driver.find_elements_by_css_selector(
                            elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"])[xuhao].click()
                        time.sleep(1)
                        logger.info(f'{sys._getframe().f_code.co_name},{driver.find_element_by_css_selector(text_path).text}选择成功')
                    else:
                        pass
            else:
                pass
            logger.info(f'{sys._getframe().f_code.co_name}, {input_hebaogongsi}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}, {input_hebaogongsi} 修改失败')

    def kehuxiangqing_baojiaxinxi_chesun(driver, is_zhuxian = 1, is_bujimian = 1):
        """客户详情-报价信息-车损，参数传数字即可，is_zhuxian为是否投保主险，1投0不投
        is_bujimian为是否投保附加险，1投0不投"""
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_tab_css"]).click()
            time.sleep(1)
            if is_zhuxian == 1 and is_bujimian == 1: #车损 + 不计免
                # 车损
                if driver.execute_script(elements["kehuxiangqing_baojiaxinxi_return车损险种"]) == elements["kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    pass
                else:
                    driver.execute_script(elements["kehuxiangqing_baojiaxinxi_点击车损险种"])
                time.sleep(1)
                # 不计免
                if driver.execute_script(elements["kehuxiangqing_baojiaxinxi_return车损不计免赔险种"]) == elements["kehuxiangqing_baojiaxinxi_bujimian_checked_class"]:
                    pass
                else:
                    driver.execute_script(elements["kehuxiangqing_baojiaxinxi_点击车损不计免赔险种"])

            elif is_zhuxian == 1 and is_bujimian == 0: #车损
                # 车损
                if driver.execute_script(elements["kehuxiangqing_baojiaxinxi_return车损险种"]) == elements[
                    "kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    pass
                else:
                    driver.execute_script(elements["kehuxiangqing_baojiaxinxi_点击车损险种"])
                time.sleep(1)

                # 不计免
                if driver.execute_script(elements["kehuxiangqing_baojiaxinxi_return车损不计免赔险种"]) == elements["kehuxiangqing_baojiaxinxi_bujimian_checked_class"]:
                    driver.execute_script(elements["kehuxiangqing_baojiaxinxi_点击车损不计免赔险种"])
                else:
                    pass

            elif is_zhuxian == 0 and is_bujimian == 0: #不上车损
                # 车损
                if driver.execute_script(elements["kehuxiangqing_baojiaxinxi_return车损险种"]) == elements[
                    "kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    driver.execute_script(elements["kehuxiangqing_baojiaxinxi_点击车损险种"])
                else:
                    pass
                time.sleep(1)

                # 不计免
                if driver.execute_script(elements=["kehuxiangqing_baojiaxinxi_return车损不计免赔险种"]) == elements[
                    "kehuxiangqing_baojiaxinxi_bujimian_checked_class"]:
                    driver.execute_script(elements=["kehuxiangqing_baojiaxinxi_点击车损不计免赔险种"])
                else:
                    pass

            else:
                pass
            #-----------------拖到可见
            target = driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baocun_button_css"])
            driver.execute_script("arguments[0].scrollIntoView();", target)
            # -----------------拖到可见
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name}, {is_zhuxian},{is_bujimian}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}, {is_zhuxian},{is_bujimian}修改失败')

    def kehuxiangqing_baojiaxinxi_sanzhe(driver, is_zhuxian = 1, is_bujimian = 1, bao_e = 5):
        """客户详情-报价信息-三者，参数传数字即可，is_zhuxian为是否投保主险，1投0不投
        is_bujimian为是否投保附加险，1投0不投
        bao_e为投保保额，参数要传数字，几万就传几，如5万就传5"""
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_tab_css"]).click()
            time.sleep(1)
            if is_zhuxian == 1 and is_bujimian == 1: #三者 + 不计免
                # 三者
                if driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sanzhe_css"]).get_attribute('class') == elements["kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    pass
                else:
                    driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sanzhe_css"]).click()
                time.sleep(1)

                # 保额
                driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_sanzhe_baoe_id"]).click()
                time.sleep(1)
                if bao_e == 5:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sanzhe_baoe_css"])[5].click()
                elif bao_e == 10:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sanzhe_baoe_css"])[
                        6].click()
                elif bao_e == 15:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sanzhe_baoe_css"])[
                        7].click()
                elif bao_e == 20:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sanzhe_baoe_css"])[
                        8].click()
                elif bao_e == 30:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sanzhe_baoe_css"])[
                        9].click()
                elif bao_e == 50:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sanzhe_baoe_css"])[
                        10].click()
                elif bao_e == 100:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sanzhe_baoe_css"])[
                        11].click()
                elif bao_e == 150:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sanzhe_baoe_css"])[
                        12].click()
                elif bao_e == 200:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sanzhe_baoe_css"])[
                        13].click()
                elif bao_e == 250:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sanzhe_baoe_css"])[
                        14].click()
                elif bao_e == 300:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sanzhe_baoe_css"])[
                        15].click()
                elif bao_e == 500:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sanzhe_baoe_css"])[
                        16].click()
                else:
                    pass
                time.sleep(1)

                # 不计免
                if driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_sanzhe_bujimian_id"]).get_attribute('class') == elements["kehuxiangqing_baojiaxinxi_bujimian_checked_class"]:
                    pass
                else:
                    driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_sanzhe_bujimian_id"]).click()


            elif is_zhuxian == 1 and is_bujimian == 0:  # 三者

                # 三者

                if driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sanzhe_css"]).get_attribute(

                        'class') == elements["kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:

                    pass

                else:

                    driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sanzhe_css"]).click()

                time.sleep(1)

                # 保额

                driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_sanzhe_baoe_id"]).click()

                time.sleep(1)

                if bao_e == 5:

                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sanzhe_baoe_css"])[

                        5].click()

                elif bao_e == 10:

                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sanzhe_baoe_css"])[

                        6].click()

                elif bao_e == 15:

                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sanzhe_baoe_css"])[

                        7].click()

                elif bao_e == 20:

                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sanzhe_baoe_css"])[

                        8].click()

                elif bao_e == 30:

                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sanzhe_baoe_css"])[

                        9].click()

                elif bao_e == 50:

                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sanzhe_baoe_css"])[

                        10].click()

                elif bao_e == 100:

                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sanzhe_baoe_css"])[

                        11].click()

                elif bao_e == 150:

                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sanzhe_baoe_css"])[

                        12].click()

                elif bao_e == 200:

                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sanzhe_baoe_css"])[

                        13].click()

                elif bao_e == 250:

                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sanzhe_baoe_css"])[

                        14].click()

                elif bao_e == 300:

                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sanzhe_baoe_css"])[

                        15].click()

                elif bao_e == 500:

                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sanzhe_baoe_css"])[

                        16].click()

                else:

                    pass

                time.sleep(1)

                # 不计免

                if driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_sanzhe_bujimian_id"]).get_attribute(

                        'class') == elements["kehuxiangqing_baojiaxinxi_bujimian_checked_class"]:

                    driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_sanzhe_bujimian_id"]).click()

                else:

                    pass

            elif is_zhuxian == 0 and is_bujimian == 0:  # 不上三者
                # 三者
                if driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sanzhe_css"]).get_attribute(
                        'class') == elements["kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sanzhe_css"]).click()
                else:
                    pass
                time.sleep(1)

                # 不计免
                if driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_sanzhe_bujimian_id"]).get_attribute(
                        'class') == elements["kehuxiangqing_baojiaxinxi_bujimian_checked_class"]:
                    driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_sanzhe_bujimian_id"]).click()
                else:
                    pass

            else:
                pass
            #-----------------拖到可见
            target = driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baocun_button_css"])
            driver.execute_script("arguments[0].scrollIntoView();", target)
            # -----------------拖到可见
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name}, {is_zhuxian},{bao_e},{is_bujimian}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}, {is_zhuxian},{bao_e},{is_bujimian}修改失败')

    def kehuxiangqing_baojiaxinxi_siji(driver, is_zhuxian = 1, is_bujimian = 1, bao_e = 5):
        """客户详情-报价信息-司机，参数传数字即可，is_zhuxian为是否投保主险，1投0不投
        is_bujimian为是否投保附加险，1投0不投
        bao_e为投保保额，参数要传数字，几万就传几，如5万就传5"""
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_tab_css"]).click()
            time.sleep(1)
            if is_zhuxian == 1 and is_bujimian == 1: #司机 + 不计免
                # 司机
                if driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_siji_css"]).get_attribute('class') == elements["kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    pass
                else:
                    driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_siji_css"]).click()
                time.sleep(1)

                # 保额
                driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_siji_baoe_id"]).click()
                time.sleep(1)
                if bao_e == 1:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_siji_baoe_css"])[5].click()
                elif bao_e == 2:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_siji_baoe_css"])[
                        6].click()
                elif bao_e == 3:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_siji_baoe_css"])[
                        7].click()
                elif bao_e == 4:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_siji_baoe_css"])[
                        8].click()
                elif bao_e == 5:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_siji_baoe_css"])[
                        9].click()
                elif bao_e == 10:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_siji_baoe_css"])[
                        10].click()
                elif bao_e == 20:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_siji_baoe_css"])[
                        11].click()
                elif bao_e == 50:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_siji_baoe_css"])[
                        12].click()
                elif bao_e == 100:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_siji_baoe_css"])[
                        13].click()
                else:
                    pass
                time.sleep(1)

                # 不计免
                if driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_siji_bujimian_id"]).get_attribute('class') == elements["kehuxiangqing_baojiaxinxi_bujimian_checked_class"]:
                    pass
                else:
                    driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_siji_bujimian_id"]).click()


            elif is_zhuxian == 1 and is_bujimian == 0:  # 司机

                # 司机
                if driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_siji_css"]).get_attribute('class') == elements["kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    pass
                else:
                    driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_siji_css"]).click()
                time.sleep(1)

                # 保额
                driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_siji_baoe_id"]).click()
                time.sleep(1)
                if bao_e == 1:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_siji_baoe_css"])[5].click()
                elif bao_e == 2:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_siji_baoe_css"])[
                        6].click()
                elif bao_e == 3:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_siji_baoe_css"])[
                        7].click()
                elif bao_e == 4:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_siji_baoe_css"])[
                        8].click()
                elif bao_e == 5:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_siji_baoe_css"])[
                        9].click()
                elif bao_e == 10:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_siji_baoe_css"])[
                        10].click()
                elif bao_e == 20:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_siji_baoe_css"])[
                        11].click()
                elif bao_e == 50:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_siji_baoe_css"])[
                        12].click()
                elif bao_e == 100:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_siji_baoe_css"])[
                        13].click()
                else:
                    pass

                time.sleep(1)

                # 不计免

                if driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_siji_bujimian_id"]).get_attribute(

                        'class') == elements["kehuxiangqing_baojiaxinxi_bujimian_checked_class"]:

                    driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_siji_bujimian_id"]).click()

                else:

                    pass

            elif is_zhuxian == 0 and is_bujimian == 0:  # 不上三者
                # 司机
                if driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_siji_css"]).get_attribute(
                        'class') == elements["kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_siji_css"]).click()
                else:
                    pass
                time.sleep(1)

                # 不计免
                if driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_siji_bujimian_id"]).get_attribute(
                        'class') == elements["kehuxiangqing_baojiaxinxi_bujimian_checked_class"]:
                    driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_siji_bujimian_id"]).click()
                else:
                    pass

            else:
                pass
            #-----------------拖到可见
            target = driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baocun_button_css"])
            driver.execute_script("arguments[0].scrollIntoView();", target)
            # -----------------拖到可见
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name}, {is_zhuxian},{bao_e},{is_bujimian}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}, {is_zhuxian},{bao_e},{is_bujimian}修改失败')

    def kehuxiangqing_baojiaxinxi_chengke(driver, is_zhuxian = 1, is_bujimian = 1, bao_e = 5):
        """客户详情-报价信息-乘客，参数传数字即可，is_zhuxian为是否投保主险，1投0不投
        is_bujimian为是否投保附加险，1投0不投
        bao_e为投保保额，参数要传数字，几万就传几，如5万就传5"""
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_tab_css"]).click()
            time.sleep(1)
            if is_zhuxian == 1 and is_bujimian == 1: #乘客 + 不计免
                # 乘客
                if driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_chengke_css"]).get_attribute('class') == elements["kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    pass
                else:
                    driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_chengke_css"]).click()
                time.sleep(1)

                # 保额
                driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_siji_baoe_id"]).click()
                time.sleep(1)
                if bao_e == 1:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_chengke_baoe_css"])[5].click()
                elif bao_e == 2:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_chengke_baoe_css"])[
                        6].click()
                elif bao_e == 3:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_chengke_baoe_css"])[
                        7].click()
                elif bao_e == 4:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_chengke_baoe_css"])[
                        8].click()
                elif bao_e == 5:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_chengke_baoe_css"])[
                        9].click()
                elif bao_e == 10:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_chengke_baoe_css"])[
                        10].click()
                elif bao_e == 20:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_chengke_baoe_css"])[
                        11].click()
                elif bao_e == 50:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_chengke_baoe_css"])[
                        12].click()
                elif bao_e == 100:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_chengke_baoe_css"])[
                        13].click()
                else:
                    pass
                time.sleep(1)

                # 不计免
                if driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_chengke_bujimian_id"]).get_attribute('class') == elements["kehuxiangqing_baojiaxinxi_bujimian_checked_class"]:
                    pass
                else:
                    driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_chengke_bujimian_id"]).click()


            elif is_zhuxian == 1 and is_bujimian == 0:  # 乘客

                # 乘客
                if driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_chengke_css"]).get_attribute('class') == elements["kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    pass
                else:
                    driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_chengke_css"]).click()
                time.sleep(1)

                # 保额
                driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_chengke_baoe_id"]).click()
                time.sleep(1)
                if bao_e == 1:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_chengke_baoe_css"])[5].click()
                elif bao_e == 2:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_chengke_baoe_css"])[
                        6].click()
                elif bao_e == 3:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_chengke_baoe_css"])[
                        7].click()
                elif bao_e == 4:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_chengke_baoe_css"])[
                        8].click()
                elif bao_e == 5:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_chengke_baoe_css"])[
                        9].click()
                elif bao_e == 10:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_chengke_baoe_css"])[
                        10].click()
                elif bao_e == 20:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_chengke_baoe_css"])[
                        11].click()
                elif bao_e == 50:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_chengke_baoe_css"])[
                        12].click()
                elif bao_e == 100:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_chengke_baoe_css"])[
                        13].click()
                else:
                    pass

                time.sleep(1)

                # 不计免

                if driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_chengke_bujimian_id"]).get_attribute(

                        'class') == elements["kehuxiangqing_baojiaxinxi_bujimian_checked_class"]:

                    driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_chengke_bujimian_id"]).click()

                else:

                    pass

            elif is_zhuxian == 0 and is_bujimian == 0:  # 不上乘客
                # 乘客
                if driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_chengke_css"]).get_attribute(
                        'class') == elements["kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_chengke_css"]).click()
                else:
                    pass
                time.sleep(1)

                # 不计免
                if driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_chengke_bujimian_id"]).get_attribute(
                        'class') == elements["kehuxiangqing_baojiaxinxi_bujimian_checked_class"]:
                    driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_chengke_bujimian_id"]).click()
                else:
                    pass

            else:
                pass
            #-----------------拖到可见
            target = driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baocun_button_css"])
            driver.execute_script("arguments[0].scrollIntoView();", target)
            # -----------------拖到可见
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name}, {is_zhuxian},{bao_e},{is_bujimian}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}, {is_zhuxian},{bao_e},{is_bujimian}修改失败')

    def kehuxiangqing_baojiaxinxi_daoqiang(driver, is_zhuxian = 1, is_bujimian = 1):
        """客户详情-报价信息-盗抢，参数传数字即可，is_zhuxian为是否投保主险，1投0不投
        is_bujimian为是否投保附加险，1投0不投"""
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_tab_css"]).click()
            time.sleep(1)
            if is_zhuxian == 1 and is_bujimian == 1: #盗抢 + 不计免
                # 盗抢
                if driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_daoqiang_css"]).get_attribute('class') == elements["kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    pass
                else:
                    driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_daoqiang_css"]).click()
                time.sleep(1)

                # 不计免
                if driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_daoqiang_bujimian_id"]).get_attribute('class') == elements["kehuxiangqing_baojiaxinxi_bujimian_checked_class"]:
                    pass
                else:
                    driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_daoqiang_bujimian_id"]).click()

            elif is_zhuxian == 1 and is_bujimian == 0: #盗抢
                # 盗抢
                if driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_daoqiang_css"]).get_attribute(
                        'class') == elements["kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    pass
                else:
                    driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_daoqiang_css"]).click()
                time.sleep(1)

                # 不计免
                if driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_daoqiang_bujimian_id"]).get_attribute(
                        'class') == elements["kehuxiangqing_baojiaxinxi_bujimian_checked_class"]:
                    driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_daoqiang_bujimian_id"]).click()
                else:
                    pass

            elif is_zhuxian == 0 and is_bujimian == 0: #不上盗抢
                # 盗抢
                if driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_daoqiang_css"]).get_attribute(
                        'class') == elements["kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_daoqiang_css"]).click()
                else:
                    pass

                time.sleep(1)

                # 不计免
                if driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_daoqiang_bujimian_id"]).get_attribute(
                        'class') == elements["kehuxiangqing_baojiaxinxi_bujimian_checked_class"]:
                    driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_daoqiang_bujimian_id"]).click()
                else:
                    pass

            else:
                pass
            #-----------------拖到可见
            target = driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baocun_button_css"])
            driver.execute_script("arguments[0].scrollIntoView();", target)
            # -----------------拖到可见
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name}, {is_zhuxian},{is_bujimian}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}, {is_zhuxian},{is_bujimian}修改失败')

    def kehuxiangqing_baojiaxinxi_huahen(driver, is_zhuxian = 1, is_bujimian = 1, bao_e = 2000):
        """客户详情-报价信息-划痕，参数传数字即可，is_zhuxian为是否投保主险，1投0不投
        is_bujimian为是否投保附加险，1投0不投
        bao_e为投保保额，参数要传数字，要传具体价格，如2000，5000，10000"""
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_tab_css"]).click()
            time.sleep(1)
            if is_zhuxian == 1 and is_bujimian == 1: #划痕 + 不计免
                # 划痕
                if driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_huahen_css"]).get_attribute('class') == elements["kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    pass
                else:
                    driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_huahen_css"]).click()
                time.sleep(1)

                # 保额
                driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_huahen_baoe_id"]).click()
                time.sleep(1)
                if bao_e == 2000:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_huahen_baoe_css"])[5].click()
                elif bao_e == 5000:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_huahen_baoe_css"])[
                        6].click()
                elif bao_e == 10000:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_huahen_baoe_css"])[
                        7].click()
                elif bao_e == 20000:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_huahen_baoe_css"])[
                        8].click()
                else:
                    pass
                time.sleep(1)

                # 不计免
                if driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_huahen_bujimian_id"]).get_attribute('class') == elements["kehuxiangqing_baojiaxinxi_bujimian_checked_class"]:
                    pass
                else:
                    driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_huahen_bujimian_id"]).click()


            elif is_zhuxian == 1 and is_bujimian == 0:  # 划痕

                # 划痕
                if driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_huahen_css"]).get_attribute('class') == elements["kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    pass
                else:
                    driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_huahen_css"]).click()
                time.sleep(1)

                # 保额
                driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_huahen_baoe_id"]).click()
                time.sleep(1)
                if bao_e == 2000:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_huahen_baoe_css"])[
                        5].click()
                elif bao_e == 5000:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_huahen_baoe_css"])[
                        6].click()
                elif bao_e == 10000:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_huahen_baoe_css"])[
                        7].click()
                elif bao_e == 20000:
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_huahen_baoe_css"])[
                        8].click()
                else:
                    pass

                time.sleep(1)

                # 不计免

                if driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_huahen_bujimian_id"]).get_attribute(

                        'class') == elements["kehuxiangqing_baojiaxinxi_bujimian_checked_class"]:

                    driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_huahen_bujimian_id"]).click()

                else:

                    pass

            elif is_zhuxian == 0 and is_bujimian == 0:  # 不上划痕
                # 划痕
                if driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_huahen_css"]).get_attribute(
                        'class') == elements["kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_huahen_css"]).click()
                else:
                    pass
                time.sleep(1)

                # 不计免
                if driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_huahen_bujimian_id"]).get_attribute(
                        'class') == elements["kehuxiangqing_baojiaxinxi_bujimian_checked_class"]:
                    driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_huahen_bujimian_id"]).click()
                else:
                    pass

            else:
                pass
            #-----------------拖到可见
            target = driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baocun_button_css"])
            driver.execute_script("arguments[0].scrollIntoView();", target)
            # -----------------拖到可见
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name}, {is_zhuxian},{bao_e},{is_bujimian}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}, {is_zhuxian},{bao_e},{is_bujimian}修改失败')

    def kehuxiangqing_baojiaxinxi_boli(driver, is_zhuxian = 1, bao_e = '国产'):
        """客户详情-报价信息-玻璃，参数传数字即可，is_zhuxian为是否投保主险，1投0不投
        is_bujimian为是否投保附加险，1投0不投
        bao_e为投保保额，参数要传‘国产’或‘进口’"""
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_tab_css"]).click()
            time.sleep(1)
            if is_zhuxian == 1: #玻璃
                # 玻璃
                if driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_boli_css"]).get_attribute('class') == elements["kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    pass
                else:
                    driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_boli_css"]).click()
                time.sleep(1)

                # 保额
                driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_boli_baoe_id"]).click()
                time.sleep(1)
                if bao_e == '国产':
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_huahen_baoe_css"])[5].click()
                elif bao_e == '进口':
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_huahen_baoe_css"])[
                        6].click()
                else:
                    pass
                time.sleep(1)


            elif is_zhuxian == 0:  # 不上玻璃

                # 玻璃
                if driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_huahen_css"]).get_attribute('class') == elements["kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_huahen_css"]).click()
                else:
                    pass
                time.sleep(1)

            else:
                pass
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name}, {is_zhuxian},{bao_e},修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}, {is_zhuxian},{bao_e},修改失败')

    def kehuxiangqing_baojiaxinxi_ziran(driver, is_zhuxian = 1, is_bujimian = 1):
        """客户详情-报价信息-自燃，参数传数字即可，is_zhuxian为是否投保主险，1投0不投
        is_bujimian为是否投保附加险，1投0不投"""
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_tab_css"]).click()
            time.sleep(1)
            if is_zhuxian == 1 and is_bujimian == 1: #自燃 + 不计免
                # 自燃
                if driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_ziran_css"]).get_attribute('class') == elements["kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    pass
                else:
                    driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_ziran_css"]).click()
                time.sleep(1)

                # 不计免
                if driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_ziran_bujimian_id"]).get_attribute('class') == elements["kehuxiangqing_baojiaxinxi_bujimian_checked_class"]:
                    pass
                else:
                    driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_ziran_bujimian_id"]).click()

            elif is_zhuxian == 1 and is_bujimian == 0: #自燃
                # 自燃
                if driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_ziran_css"]).get_attribute(
                        'class') == elements["kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    pass
                else:
                    driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_ziran_css"]).click()
                time.sleep(1)

                # 不计免
                if driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_ziran_bujimian_id"]).get_attribute(
                        'class') == elements["kehuxiangqing_baojiaxinxi_bujimian_checked_class"]:
                    driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_ziran_bujimian_id"]).click()
                else:
                    pass

            elif is_zhuxian == 0 and is_bujimian == 0: #不上自燃
                # 自燃
                if driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_ziran_css"]).get_attribute(
                        'class') == elements["kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_ziran_css"]).click()
                else:
                    pass

                time.sleep(1)

                # 不计免
                if driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_ziran_bujimian_id"]).get_attribute(
                        'class') == elements["kehuxiangqing_baojiaxinxi_bujimian_checked_class"]:
                    driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_ziran_bujimian_id"]).click()
                else:
                    pass

            else:
                pass
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name}, {is_zhuxian},{is_bujimian}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}, {is_zhuxian},{is_bujimian}修改失败')

    def kehuxiangqing_baojiaxinxi_sheshui(driver, is_zhuxian = 1, is_bujimian = 1):
        """客户详情-报价信息-涉水，参数传数字即可，is_zhuxian为是否投保主险，1投0不投
        is_bujimian为是否投保附加险，1投0不投"""
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_tab_css"]).click()
            time.sleep(1)
            if is_zhuxian == 1 and is_bujimian == 1: #涉水 + 不计免
                # 涉水
                if driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sheshui_css"]).get_attribute('class') == elements["kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    pass
                else:
                    driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sheshui_css"]).click()
                time.sleep(1)

                # 不计免
                if driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_sheshui_bujimian_id"]).get_attribute('class') == elements["kehuxiangqing_baojiaxinxi_bujimian_checked_class"]:
                    pass
                else:
                    driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_sheshui_bujimian_id"]).click()

            elif is_zhuxian == 1 and is_bujimian == 0: #涉水
                # 涉水
                if driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sheshui_css"]).get_attribute(
                        'class') == elements["kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    pass
                else:
                    driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sheshui_css"]).click()
                time.sleep(1)

                # 不计免
                if driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_sheshui_bujimian_id"]).get_attribute(
                        'class') == elements["kehuxiangqing_baojiaxinxi_bujimian_checked_class"]:
                    driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_sheshui_bujimian_id"]).click()
                else:
                    pass

            elif is_zhuxian == 0 and is_bujimian == 0: #不上涉水
                # 涉水
                if driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sheshui_css"]).get_attribute(
                        'class') == elements["kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sheshui_css"]).click()
                else:
                    pass

                time.sleep(1)

                # 不计免
                if driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_sheshui_bujimian_id"]).get_attribute(
                        'class') == elements["kehuxiangqing_baojiaxinxi_bujimian_checked_class"]:
                    driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_sheshui_bujimian_id"]).click()
                else:
                    pass

            else:
                pass
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name}, {is_zhuxian},{is_bujimian}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}, {is_zhuxian},{is_bujimian}修改失败')

    def kehuxiangqing_baojiaxinxi_chesunwufazhaodaodisanfang(driver, is_zhuxian = 1):
        """客户详情-报价信息-车损无法找到第三方，参数传数字即可，is_zhuxian为是否投保主险，1投0不投"""
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_tab_css"]).click()
            time.sleep(1)
            if is_zhuxian == 1: #车损无法找到第三方
                # 车损无法找到第三方
                if driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_chesunwufazhaodaodisanfang_css"]).get_attribute('class') == elements["kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    pass
                else:
                    driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_chesunwufazhaodaodisanfang_css"]).click()
                time.sleep(1)


            elif is_zhuxian == 0: #不上车损无法找到第三方
                # 车损无法找到第三方
                if driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_chesunwufazhaodaodisanfang_css"]).get_attribute(
                        'class') == elements["kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_chesunwufazhaodaodisanfang_css"]).click()
                else:
                    pass

                time.sleep(1)

            else:
                pass
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name}, {is_zhuxian},修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}, {is_zhuxian},修改失败')

    def kehuxiangqing_baojiaxinxi_zhidingxiulichang(driver, is_zhuxian = 1, bao_e = '国产'):
        """客户详情-报价信息-指定修理厂，参数传数字即可，is_zhuxian为是否投保主险，1投0不投
        bao_e为投保保额，参数要传‘国产’或‘进口’"""
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_tab_css"]).click()
            time.sleep(1)
            if is_zhuxian == 1: #指定修理厂
                # 玻璃
                if driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_zhidingxiulichang_css"]).get_attribute('class') == elements["kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    pass
                else:
                    driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_zhidingxiulichang_css"]).click()
                time.sleep(1)

                # 保额
                driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_zhidingxiulichang_baoe_id"]).click()
                time.sleep(1)
                if bao_e == '国产':
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_zhidingxiulichang_baoe_css"])[5].click()
                elif bao_e == '进口':
                    driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_zhidingxiulichang_baoe_css"])[
                        6].click()
                else:
                    pass
                time.sleep(1)


            elif is_zhuxian == 0:  # 不上指定修理厂

                # 玻璃
                if driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_zhidingxiulichang_css"]).get_attribute('class') == elements["kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_zhidingxiulichang_css"]).click()
                else:
                    pass
                time.sleep(1)

            else:
                pass
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name}, {is_zhuxian},{bao_e},修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}, {is_zhuxian},{bao_e},修改失败')

    def kehuxiangqing_baojiaxinxi_xinzengshebeisunshi(driver, is_zhuxian = 1, is_bujimian = 1):
        """客户详情-报价信息-新增设备损失，参数传数字即可，is_zhuxian为是否投保主险，1投0不投
        is_bujimian为是否投保附加险，1投0不投"""
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_tab_css"]).click()
            time.sleep(1)
            #-----------------拖到可见
            target = driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_xinzengshebeisunshi_css"])
            driver.execute_script("arguments[0].scrollIntoView();", target)
            # -----------------拖到可见
            time.sleep(1)

            if is_zhuxian == 1 and is_bujimian == 1: #新增设备损失 + 不计免
                # 新增设备损失
                if driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_xinzengshebeisunshi_css"]).get_attribute('class') == elements["kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    pass
                else:
                    driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_xinzengshebeisunshi_css"]).click()
                time.sleep(1)

                # 不计免
                if driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_xinzengshebeisunshi_bujimian_id"]).get_attribute('class') == elements["kehuxiangqing_baojiaxinxi_bujimian_checked_class"]:
                    pass
                else:
                    driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_xinzengshebeisunshi_bujimian_id"]).click()

            elif is_zhuxian == 1 and is_bujimian == 0: #新增设备损失
                # 新增设备损失
                if driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_xinzengshebeisunshi_css"]).get_attribute(
                        'class') == elements["kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    pass
                else:
                    driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_xinzengshebeisunshi_css"]).click()
                time.sleep(1)

                # 不计免
                if driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_xinzengshebeisunshi_bujimian_id"]).get_attribute(
                        'class') == elements["kehuxiangqing_baojiaxinxi_bujimian_checked_class"]:
                    driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_xinzengshebeisunshi_bujimian_id"]).click()
                else:
                    pass

            elif is_zhuxian == 0 and is_bujimian == 0: #不上新增设备损失
                # 新增设备损失
                if driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_xinzengshebeisunshi_css"]).get_attribute(
                        'class') == elements["kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_xinzengshebeisunshi_css"]).click()
                else:
                    pass

                time.sleep(1)

                # 不计免
                if driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_xinzengshebeisunshi_bujimian_id"]).get_attribute(
                        'class') == elements["kehuxiangqing_baojiaxinxi_bujimian_checked_class"]:
                    driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_xinzengshebeisunshi_bujimian_id"]).click()
                else:
                    pass

            else:
                pass
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name}, {is_zhuxian},{is_bujimian}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}, {is_zhuxian},{is_bujimian}修改失败')

    def kehuxiangqing_baojiaxinxi_sanzexianfujiafadingjiejiarixianefanbei(driver, is_zhuxian = 1):
        """客户详情-报价信息-三责险附加法定节假日限额翻倍险，参数传数字即可，is_zhuxian为是否投保主险，1投0不投"""
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_tab_css"]).click()
            time.sleep(1)
            #-----------------拖到可见
            target = driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sanzexianfujiafadingjiajiarixianefanbei_css"])
            driver.execute_script("arguments[0].scrollIntoView();", target)
            # -----------------拖到可见
            time.sleep(1)

            if is_zhuxian == 1: #三责险附加法定节假日险翻倍险
                # 三责险附加法定节假日险翻倍险
                if driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sanzexianfujiafadingjiajiarixianefanbei_css"]).get_attribute('class') == elements["kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    pass
                else:
                    driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sanzexianfujiafadingjiajiarixianefanbei_css"]).click()
                time.sleep(1)


            elif is_zhuxian == 0: #不上三责险附加法定节假日险翻倍险
                # 三责险附加法定节假日险翻倍险
                if driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sanzexianfujiafadingjiajiarixianefanbei_css"]).get_attribute(
                        'class') == elements["kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_sanzexianfujiafadingjiajiarixianefanbei_css"]).click()
                else:
                    pass

                time.sleep(1)

            else:
                pass
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name}, {is_zhuxian},修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}, {is_zhuxian},修改失败')

    def kehuxiangqing_baojiaxinxi_xiuliqijianfeiyongbuchang(driver, is_zhuxian = 1, bao_e = 100, xishu = 1):
        """客户详情-报价信息-修理期间费用补偿险，参数传数字即可，is_zhuxian为是否投保主险，1投0不投
        bao_e为投保保额，参数要传具体保额，如100，200，300，与下拉菜单选项文字保持一致
        系数为天数，要传具体天数，如1，2"""
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_tab_css"]).click()
            time.sleep(1)
            #-----------------拖到可见
            target = driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_xiuliqijianfeiyongbuchang_css"])
            driver.execute_script("arguments[0].scrollIntoView();", target)
            # -----------------拖到可见
            time.sleep(1)

            if is_zhuxian == 1: #修理期间费用补偿险
                # 修理期间费用补偿险
                if driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_xiuliqijianfeiyongbuchang_css"]).get_attribute('class') == elements["kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    pass
                else:
                    driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_xiuliqijianfeiyongbuchang_css"]).click()
                time.sleep(1)

                # 保额
                # driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_xiuliqijianfeiyongbuchang_baoe_id"]).click()
                # time.sleep(1)
                # if bao_e == 100:
                #     driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_xiuliqijianfeiyongbuchang_baoe_css"])[
                #         5].click()
                # elif bao_e == 200:
                #     driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_xiuliqijianfeiyongbuchang_baoe_css"])[
                #         6].click()
                # elif bao_e == 300:
                #     driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_xiuliqijianfeiyongbuchang_baoe_css"])[
                #         7].click()
                # else:
                #     pass
                #
                # time.sleep(1)

                # 系数
                driver.find_element_by_id(
                    elements["kehuxiangqing_baojiaxinxi_xiuliqijianfeiyongbuchang_xishu_id"]).clear()
                time.sleep(1)
                driver.find_element_by_id(
                    elements["kehuxiangqing_baojiaxinxi_xiuliqijianfeiyongbuchang_xishu_id"]).send_keys(xishu)
                time.sleep(1)




            elif is_zhuxian == 0: #不上修理期间费用补偿险
                # 修理期间费用补偿险
                if driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_xiuliqijianfeiyongbuchang_css"]).get_attribute(
                        'class') == elements["kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_xiuliqijianfeiyongbuchang_css"]).click()
                else:
                    pass

                time.sleep(1)

            else:
                pass
            time.sleep(1)
            #-----------------拖到可见
            target = driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baocun_button_css"])
            driver.execute_script("arguments[0].scrollIntoView();", target)
            # -----------------拖到可见
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name}, {is_zhuxian},修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}, {is_zhuxian},修改失败')


