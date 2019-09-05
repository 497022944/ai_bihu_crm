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


class customerlist:
    def customer_list_tab_select(driver,select_tab):
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
            logger.info(f'{sys._getframe().f_code.co_name},{input_chepai} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_chepai} 搜索失败')

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
            logger.info(f'{sys._getframe().f_code.co_name},{input_chejia} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_chejia} 搜索失败')


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
            logger.info(f'{sys._getframe().f_code.co_name},{input_chezhuxingming} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_chezhuxingming} 搜索失败')

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
            logger.info(f'{sys._getframe().f_code.co_name},{input_kehumingcheng} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_kehumingcheng} 搜索失败')

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
            logger.info(f'{sys._getframe().f_code.co_name},{input_kehudianhua} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_kehudianhua} 搜索失败')



    def search_daoqishijian(driver, input_daoqishijian=elements["test_kehudianhua1"]):
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuliebiao_sousuo2_daoqishijian_id"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_daoqishijian} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_daoqishijian} 搜索失败')


    def search_kehuleibie(driver, input_kehuleibie=elements["test_kehudianhua1"]):
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuliebiao_sousuo3_kehuleibie_css"]).click()
            driver.find_element_by_id(elements["kehuliebiao_sousuo3_kehuleibie_id"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo3_kehuleibie_dropdown_input_css"]).send_keys(input_kehuleibie)
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_kehuleibie} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_kehuleibie} 搜索失败')


    def search_pinpaixinghao(driver, input_pinpaixinghao=elements["test_kehudianhua1"]):
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuliebiao_sousuo3_kehuleibie_css"]).click()
            driver.find_element_by_id(elements["kehuliebiao_sousuo4_pinpaixinghao_id"]).send_keys(input_pinpaixinghao)
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_pinpaixinghao} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_pinpaixinghao} 搜索失败')

    def search_shangniantoubaogongsi(driver, input_shangniantoubaogongsi=elements["test_kehudianhua1"]):
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuliebiao_sousuo5_shangniantoubaogongsi_id"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo5_shangniantoubaogongsi_input_css"]).send_keys(input_shangniantoubaogongsi)
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_shangniantoubaogongsi} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_shangniantoubaogongsi} 搜索失败')

    def search_shangchuanpici(driver, input_shangchuanpici=elements["test_kehudianhua1"]):
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuliebiao_sousuo6_shangchuanpici_id"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo6_shangchuanpici_input_css"]).send_keys(input_shangchuanpici)
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_shangchuanpici} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_shangchuanpici} 搜索失败')


    def search_shangyedaoqishijian(driver, input_shangyedaoqishijian=elements["test_kehudianhua1"]):
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuliebiao_sousuo7_shangyedaoqishijian_id"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuliebiao_sousuo6_shangchuanpici_input_css"]).send_keys(input_shangyedaoqishijian)
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_shangyedaoqishijian} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_shangyedaoqishijian} 搜索失败')


    def search_jiaoqiangdaoqishijian(driver, input_jiaoqiangdaoqishijian=elements["test_kehudianhua1"]):
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuliebiao_sousuo8_jiaoqiangdaoqishijian_id"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuliebiao_sousuo6_shangchuanpici_input_css"]).send_keys(input_shangyedaoqishijian)
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_jiaoqiangdaoqishijian} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_jiaoqiangdaoqishijian} 搜索失败')

    def search_shangyedaoqiyuefen(driver, input_shangyedaoqiyuefen=elements["test_kehudianhua1"]):
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuliebiao_sousuo9_shangyedaoqiyuefen_id"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuliebiao_sousuo6_shangchuanpici_input_css"]).send_keys(input_shangyedaoqishijian)
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_shangyedaoqiyuefen} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_shangyedaoqiyuefen} 搜索失败')

    def search_jiaoqiangdaoqiyuefen(driver, input_jiaoqiangdaoqiyuefen=elements["test_kehudianhua1"]):
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuliebiao_sousuo10_jiaoqiangdaoqiyuefen_id"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuliebiao_sousuo6_shangchuanpici_input_css"]).send_keys(input_shangyedaoqishijian)
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_jiaoqiangdaoqiyuefen} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_jiaoqiangdaoqiyuefen} 搜索失败')


    def search_zhuceshijian(driver, input_zhuceshijian=elements["test_kehudianhua1"]):
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuliebiao_sousuo11_zhuceshijian_id"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuliebiao_sousuo6_shangchuanpici_input_css"]).send_keys(input_shangyedaoqishijian)
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_zhuceshijian} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_zhuceshijian} 搜索失败')



    def search_zhuceyuefen(driver, input_zhuceyuefen=elements["test_kehudianhua1"]):
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuliebiao_sousuo12_zhuceyuefen_id"]).click()
            time.sleep(1)
            if input_zhuceyuefen == '01月份':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo12_zhuceyuefen_dropdown_css"])[0].click()
                time.sleep(1)
                logger.info(f'{sys._getframe().f_code.co_name},{input_zhuceyuefen} 搜索成功')
            elif input_zhuceyuefen == '02月份':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo12_zhuceyuefen_dropdown_css"])[1].click()
                time.sleep(1)
                logger.info(f'{sys._getframe().f_code.co_name},{input_zhuceyuefen} 搜索成功')
            elif input_zhuceyuefen == '03月份':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo12_zhuceyuefen_dropdown_css"])[2].click()
                time.sleep(1)
                logger.info(f'{sys._getframe().f_code.co_name},{input_zhuceyuefen} 搜索成功')
            elif input_zhuceyuefen == '04月份':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo12_zhuceyuefen_dropdown_css"])[3].click()
                time.sleep(1)
                logger.info(f'{sys._getframe().f_code.co_name},{input_zhuceyuefen} 搜索成功')
            elif input_zhuceyuefen == '05月份':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo12_zhuceyuefen_dropdown_css"])[4].click()
                time.sleep(1)
                logger.info(f'{sys._getframe().f_code.co_name},{input_zhuceyuefen} 搜索成功')
            elif input_zhuceyuefen == '06月份':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo12_zhuceyuefen_dropdown_css"])[5].click()
                time.sleep(1)
                logger.info(f'{sys._getframe().f_code.co_name},{input_zhuceyuefen} 搜索成功')
            elif input_zhuceyuefen == '07月份':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo12_zhuceyuefen_dropdown_css"])[6].click()
                time.sleep(1)
                logger.info(f'{sys._getframe().f_code.co_name},{input_zhuceyuefen} 搜索成功')
            elif input_zhuceyuefen == '08月份':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo12_zhuceyuefen_dropdown_css"])[7].click()
                time.sleep(1)
                logger.info(f'{sys._getframe().f_code.co_name},{input_zhuceyuefen} 搜索成功')
            elif input_zhuceyuefen == '09月份':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo12_zhuceyuefen_dropdown_css"])[8].click()
                time.sleep(1)
                logger.info(f'{sys._getframe().f_code.co_name},{input_zhuceyuefen} 搜索成功')
            elif input_zhuceyuefen == '10月份':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo12_zhuceyuefen_dropdown_css"])[9].click()
                time.sleep(1)
                logger.info(f'{sys._getframe().f_code.co_name},{input_zhuceyuefen} 搜索成功')
            elif input_zhuceyuefen == '11月份':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo12_zhuceyuefen_dropdown_css"])[10].click()
                time.sleep(1)
                logger.info(f'{sys._getframe().f_code.co_name},{input_zhuceyuefen} 搜索成功')
            elif input_zhuceyuefen == '12月份':
                driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo12_zhuceyuefen_dropdown_css"])[11].click()
                time.sleep(1)
                logger.info(f'{sys._getframe().f_code.co_name},{input_zhuceyuefen} 搜索成功')
            else:
                pass
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_zhuceyuefen} 搜索失败')


    def search_baojiazhuangtai(driver, input_baojiazhuangtai=elements["test_kehudianhua1"]):
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuliebiao_sousuo15_baojiazhuangtai_id"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo15_baojiazhuangtai_input_css"]).send_keys(input_baojiazhuangtai)
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_baojiazhuangtai} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_baojiazhuangtai} 搜索失败')

    def search_xubaozhuangtai(driver, input_xubaozhuangtai=elements["test_kehudianhua1"]):
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuliebiao_sousuo14_xubaozhuangtai_id"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo14_xubaozhuangtai_input_css"]).send_keys(input_xubaozhuangtai)
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_xubaozhuangtai} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_xubaozhuangtai} 搜索失败')