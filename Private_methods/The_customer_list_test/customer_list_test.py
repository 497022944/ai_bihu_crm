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


    def search_1_0_chepai(driver,input_chepai = elements["test_licenseno"]):
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

    def search_1_0_chepai_gotofirst_detail(driver,input_chepai = elements["test_licenseno"]):
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_dropdown_css"]).click()
            time.sleep(1)
            driver.find_elements_by_css_selector(elements["kehuliebiao_sousuo1_dropdown_selection_css"])[0].click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo1_textbox_css"]).send_keys(input_chepai)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_button_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo_result_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},进入{input_chepai} 详情成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},进入{input_chepai} 详情失败')

    def search_1_1_chejia(driver,input_chejia = elements["test_vin"]):
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


    def search_1_2_chezhuxingming(driver,input_chezhuxingming = elements["test_chezhuxingming"]):
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

    def search_1_3_kehumingcheng(driver,input_kehumingcheng = elements["test_kehumingcheng"]):
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

    def search_1_4_kehudianhua(driver, input_kehudianhua=elements["test_kehudianhua1"]):
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



    def search_2_daoqishijian(driver, input_daoqishijian=elements["test_kehudianhua1"]):
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuliebiao_sousuo2_daoqishijian_id"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_daoqishijian} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_daoqishijian} 搜索失败')


    def search_3_kehuleibie(driver, input_kehuleibie=elements["test_kehudianhua1"]):
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


    def search_4_pinpaixinghao(driver, input_pinpaixinghao=elements["test_kehudianhua1"]):
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuliebiao_sousuo3_kehuleibie_css"]).click()
            driver.find_element_by_id(elements["kehuliebiao_sousuo4_pinpaixinghao_id"]).send_keys(input_pinpaixinghao)
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_pinpaixinghao} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_pinpaixinghao} 搜索失败')

    def search_5_shangniantoubaogongsi(driver, input_shangniantoubaogongsi=elements["test_kehudianhua1"]):
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

    def search_6_shangchuanpici(driver, input_shangchuanpici=elements["test_kehudianhua1"]):
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


    def search_7_shangyedaoqishijian(driver, input_shangyedaoqishijian=elements["test_kehudianhua1"]):
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


    def search_8_jiaoqiangdaoqishijian(driver, input_jiaoqiangdaoqishijian=elements["test_kehudianhua1"]):
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

    def search_9_shangyedaoqiyuefen(driver, input_shangyedaoqiyuefen=elements["test_kehudianhua1"]):
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

    def search_10_jiaoqiangdaoqiyuefen(driver, input_jiaoqiangdaoqiyuefen=elements["test_kehudianhua1"]):
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


    def search_11_zhuceshijian(driver, input_zhuceshijian=elements["test_kehudianhua1"]):
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



    def search_12_zhuceyuefen(driver, input_zhuceyuefen=elements["test_kehudianhua1"]):
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


    def search_13_kehuzhuangtai(driver, input_kehuzhuangtai=elements["test_kehudianhua1"]):
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuliebiao_sousuo13_kehuzhuangtai_id"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo13_kehuzhuangtai_input_css"]).send_keys(
                input_kehuzhuangtai)
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_kehuzhuangtai} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_kehuzhuangtai} 搜索失败')


    def search_14_xubaozhuangtai(driver, input_xubaozhuangtai=elements["test_kehudianhua1"]):
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

    def search_15_baojiazhuangtai(driver, input_baojiazhuangtai=elements["test_kehudianhua1"]):
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


    def search_16_fenpeizhuangtai(driver, input_fenpeizhuangtai=elements["test_kehudianhua1"]):
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            if input_fenpeizhuangtai == '未分配':
                driver.find_element_by_css_selector(elements["kehuliebiao_sousuo16_fenpeizhuangtai_weifenpei_css"]).click()
                time.sleep(1)
            elif input_fenpeizhuangtai == '已分配':
                driver.find_element_by_css_selector(elements["kehuliebiao_sousuo16_fenpeizhuangtai_yifenpei_css"]).click()
                time.sleep(1)
            else:
                pass
            logger.info(f'{sys._getframe().f_code.co_name},{input_fenpeizhuangtai} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_fenpeizhuangtai} 搜索失败')



    def search_17_fenpeishijian(driver, input_fenpeishijian=elements["test_kehudianhua1"]):
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuliebiao_sousuo17_fenpeishijian_id"]).click()
            time.sleep(1)

            # driver.find_element_by_css_selector(elements["kehuliebiao_sousuo16_fenpeizhuangtai_yifenpei_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_fenpeishijian} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_fenpeishijian} 搜索失败')


    def search_18_yuyueshijian(driver, input_yuyueshijian=elements["test_kehudianhua1"]):
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuliebiao_sousuo18_yuyueshijian_id"]).click()
            time.sleep(1)

            # driver.find_element_by_css_selector(elements["kehuliebiao_sousuo16_fenpeizhuangtai_yifenpei_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_yuyueshijian} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_yuyueshijian} 搜索失败')


    def search_19_huifangshijian(driver, input_huifangshijian=elements["test_kehudianhua1"]):
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuliebiao_sousuo19_huifangshijian_id"]).click()
            time.sleep(1)

            # driver.find_element_by_css_selector(elements["kehuliebiao_sousuo16_fenpeizhuangtai_yifenpei_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_huifangshijian} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_huifangshijian} 搜索失败')


    def search_20_lurufangshi(driver, input_lurufangshi=elements["test_kehudianhua1"]):
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuliebiao_sousuo20_lurufangshi_id"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo20_lurufangshi_input_css"]).send_keys(input_lurufangshi)
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_lurufangshi} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_lurufangshi} 搜索失败')


    def search_21_jindianshijian(driver, input_jindianshijian=elements["test_kehudianhua1"]):
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuliebiao_sousuo21_jindianshijian_id"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuliebiao_sousuo20_lurufangshi_input_css"]).send_keys(input_lurufangshi)
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_jindianshijian} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_jindianshijian} 搜索失败')


    def search_22_kehudianhua(driver, input_kehudianhua=elements["test_kehudianhua1"]):
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuliebiao_sousuo21_jindianshijian_id"]).click()
            time.sleep(1)
            if input_kehudianhua == '有':
                driver.find_element_by_css_selector(elements["kehuliebiao_sousuo22_kehudianhua_you_css"]).click()
                time.sleep(1)
            elif input_kehudianhua == '无':
                driver.find_element_by_css_selector(elements["kehuliebiao_sousuo22_kehehudianhua_wu_css"]).click()
                time.sleep(1)
            else:
                pass
            logger.info(f'{sys._getframe().f_code.co_name},{input_kehudianhua} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_kehudianhua} 搜索失败')



    def search_23_yewuyuan(driver, input_yewuyuan=elements["test_kehudianhua1"]):
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuliebiao_sousuo23_yewuyuan_id"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo23_yewuyuan_input_css"]).send_keys(input_yewuyuan)
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_yewuyuan} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_yewuyuan} 搜索失败')


    def search_24_bumenmingcheng(driver, input_bumenmingcheng=elements["test_kehudianhua1"]):
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuliebiao_sousuo24_bumenmingcheng_id"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuliebiao_sousuo24_bumenmingcheng_input_css"]).send_keys(input_bumenmingcheng)
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_bumenmingcheng} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_bumenmingcheng} 搜索失败')

    def search_25_gengxinshijian(driver, input_gengxinshijian=elements["test_kehudianhua1"]):
        try:
            driver.find_element_by_css_selector(elements["kehuliebiao_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuliebiao_sousuo25_gengxinshijian_id"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuliebiao_sousuo24_bumenmingcheng_input_css"]).send_keys(input_bumenmingcheng)
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_gengxinshijian} 搜索成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_gengxinshijian} 搜索失败')


    def kehuxiangqing_kehuxinxi_kehuxingming(driver,input_kehuxingming = elements["test_chezhuxingming"]):
        try:
            # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
            # time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_kehuxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"]).clear()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"]).send_keys(input_kehuxingming)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_kehuxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_kehuxingming}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_kehuxingming} 修改失败')


    def kehuxiangqing_kehuxinxi_dianhua1(driver, input_dianhua1=elements["test_kehudianhua1"]):
        try:
            # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
            # time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_kehuxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_dianhua1_id"]).clear()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_dianhua1_id"]).send_keys(input_dianhua1)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_kehuxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_dianhua1}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_dianhua1} 修改失败')

    def kehuxiangqing_kehuxinxi_dianhua2(driver, input_dianhua1=elements["test_kehudianhua2"]):
        try:
            # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
            # time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_kehuxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_dianhua2_id"]).clear()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_dianhua2_id"]).send_keys(input_dianhua1)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_kehuxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_dianhua1}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_dianhua1} 修改失败')

    def kehuxiangqing_kehuxinxi_leibie(driver, input_leibie=elements["test_kehudianhua2"]):
        try:
            # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
            # time.sleep(1)
            # driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_leibie_id"]).clear()
            # time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_kehuxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_leibie_id"]).send_keys(input_leibie)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_kehuxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_leibie}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_leibie} 修改失败')

    def kehuxiangqing_kehuxinxi_dizhi(driver, input_dizhi=elements["test_kehudianhua2"]):
        try:
            # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
            # time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_kehuxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_dizhi_id"]).clear()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_dizhi_id"]).send_keys(input_dizhi)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_kehuxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_dizhi}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_dizhi} 修改失败')

    def kehuxiangqing_kehuxinxi_beizhu1(driver, input_beizhu1=elements["test_kehudianhua2"]):
        try:
            # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
            # time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_kehuxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_beizhu1_id"]).clear()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_beizhu1_id"]).send_keys(input_beizhu1)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_kehuxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_beizhu1}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_beizhu1} 修改失败')

    def kehuxiangqing_kehuxinxi_beizhu2(driver, input_beizhu2=elements["test_kehudianhua2"]):
        try:
            # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
            # time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_kehuxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_beizhu2_id"]).clear()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_beizhu2_id"]).send_keys(input_beizhu2)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_kehuxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_beizhu2}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_beizhu2} 修改失败')

    def kehuxiangqing_cheliangxinxi_chepaihao(driver, input_chepaihao=elements["test_licenseno"]):
        try:
            # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
            # time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_chepaihao_id"]).clear()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_chepaihao_id"]).send_keys(input_chepaihao)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_chepaihao}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_chepaihao} 修改失败')


    def kehuxiangqing_cheliangxinxi_chepaihaoleixing(driver, input_chepaihaoleixing=elements["test_licenseno"]):
        try:
            # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
            # time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_chepaihaoleixing_id"]).clear()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_chepaihaoleixing_id"]).send_keys(input_chepaihaoleixing)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_chepaihaoleixing}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_chepaihaoleixing} 修改失败')


    def kehuxiangqing_cheliangxinxi_chejiahao(driver, input_chejiahao=elements["test_vin"]):
        try:
            # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
            # time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_chejiahao_input_css"]).clear()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_chejiahao_input_css"]).send_keys(input_chejiahao)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_chejiahao_sousuo_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_chejiahao}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_chejiahao} 修改失败')


    def kehuxiangqing_cheliangxinxi_fadongjihao(driver, input_fadongjihao=elements["test_vin"]):
        try:
            # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
            # time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_fadongjihao_id"]).clear()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_fadongjihao_id"]).send_keys(input_fadongjihao)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_fadongjihao}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_fadongjihao} 修改失败')


    def kehuxiangqing_cheliangxinxi_zhuceriqi(driver, input_zhuceriqi=elements["test_vin"]):
        try:
            # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
            # time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_zhuceriqi_id"]).click()
            time.sleep(1)
            # driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_fadongjihao_id"]).send_keys(input_zhuceriqi)
            # time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_zhuceriqi}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_zhuceriqi} 修改失败')

    def kehuxiangqing_cheliangxinxi_pinpaixinghao(driver, input_pinpaixinghao=elements["test_vin"]):
        try:
            # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
            # time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(
                elements["kehuxiangqing_cheliangxinxi_pinpaixinghao_input_css"]).clear()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_pinpaixinghao_input_css"]).send_keys(
                input_pinpaixinghao)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_pinpaixinghao_sousuo_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_pinpaixinghao}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_pinpaixinghao} 修改失败')


    def kehuxiangqing_cheliangxinxi_chexing(driver, input_chexing=elements["test_vin"]):
        try:
            # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
            # time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_chexing_id"]).click()
            time.sleep(1)
            # driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_fadongjihao_id"]).send_keys(input_zhuceriqi)
            # time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_chexing}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_chexing} 修改失败')

    def kehuxiangqing_cheliangxinxi_xinchegouzhijia(driver, input_xinchegouzhijia=elements["test_vin"]):
        try:
            # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
            # time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_xinchegouzhijia_id"]).clear()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_xinchegouzhijia_id"]).send_keys(input_xinchegouzhijia)
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

    def kehuxiangqing_cheliangxinxi_zuoweishu(driver, input_zuoweishu=elements["test_vin"]):
        try:
            # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
            # time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_zuoweishu_id"]).click()
            time.sleep(2)
            if input_zuoweishu == '3座':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_zuoweishu_css"])[4].click()
                time.sleep(1)
            elif input_zuoweishu == '4座':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_zuoweishu_css"])[5].click()
                time.sleep(1)
            elif input_zuoweishu == '5座':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_zuoweishu_css"])[6].click()
                time.sleep(1)
            elif input_zuoweishu == '6座':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_zuoweishu_css"])[7].click()
                time.sleep(1)
            elif input_zuoweishu == '7座':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_zuoweishu_css"])[8].click()
                time.sleep(1)
            elif input_zuoweishu == '8座':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_zuoweishu_css"])[9].click()
                time.sleep(1)
            elif input_zuoweishu == '9座':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_zuoweishu_css"])[10].click()
                time.sleep(1)
            elif input_zuoweishu == '10座':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_cheliangxinxi_zuoweishu_css"])[11].click()
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

    def kehuxiangqing_cheliangxinxi_pailiang(driver, input_pailiang=elements["test_vin"]):
        try:
            # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
            # time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_pailiang_id"]).send_keys(
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


    def kehuxiangqing_cheliangxinxi_guohuche(driver , input_shifou, input_guohuriqi=elements["test_vin"]):
        try:
            # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
            # time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"]).click()
            time.sleep(1)
            if input_shifou == '是':
                driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_guohuche_shi_css"]).click()
                time.sleep(1)
                driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_guohuriqi_id"]).click()
                time.sleep(1)
            elif input_shifou == '否':
                driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_guohuche_fou_css"]).click()
                time.sleep(1)
            else:
                pass
            # driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_fadongjihao_id"]).send_keys(input_zhuceriqi)
            # time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_guohuriqi_id"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_shifou}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_shifou} 修改失败')




    def kehuxiangqing_cheliangxinxi_daikuanche(driver, input_shifou, input_diyishouyiren=elements["test_vin"]):
        try:
            # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
            # time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"]).click()
            time.sleep(1)
            if input_shifou == '是':
                driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_daikuanche_shi_css"]).click()
                time.sleep(1)
                driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_diyishouyiren_id"]).send_keys(input_diyishouyiren)
                time.sleep(1)
            elif input_shifou == '否':
                driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_daikuanche_fou_css"]).click()
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


    def kehuxiangqing_cheliangxinxi_beizhuxinxi(driver, input_beizhuxinxi=elements["test_vin"]):
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_beizhuxinxi_id"]).send_keys(
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


    # def kehuxiangqing_shangniantoubaoxinxi_toubaogongsi(driver, input_toubaogongsi=elements["test_vin"]):
    #     try:
    #         # ActionChains(driver).double_click(driver.find_element_by_id(elements["kehuxiangqing_kehuxinxi_kehuxingming_id"])).perform()
    #         # time.sleep(1)
    #         # target = driver.find_element_by_id(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_id"])
    #         # time.sleep(1)
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_tab_css"]).click()
    #         time.sleep(1)
    #         driver.find_element_by_id(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_id"]).send_keys(
    #             input_toubaogongsi)
    #         time.sleep(1)
    #         # driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_fadongjihao_id"]).send_keys(input_zhuceriqi)
    #         # time.sleep(1)
    #         driver.find_element_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_baocun_button_css"]).click()
    #         time.sleep(1)
    #         # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
    #         # time.sleep(1)
    #         logger.info(f'{sys._getframe().f_code.co_name},{input_toubaogongsi}修改成功')
    #     except Exception:
    #         logbug.debug(f'{sys._getframe().f_code.co_name},{input_toubaogongsi} 修改失败')


    def kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_beibaoxianrenxingming(driver, input_beibaoxianrenxingming=elements["test_vin"]):
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_beibaoxianrenxingming_id"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_beibaoxianrenxingming_id"]).send_keys(input_beibaoxianrenxingming)
            time.sleep(1)
            # driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_fadongjihao_id"]).send_keys(input_zhuceriqi)
            # time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_beibaoxianrenxingming}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_beibaoxianrenxingming} 修改失败')


    def kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianleixing(driver, input_zhengjianleixing, input_zhengjianhaoma=elements["test_vin"]):
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianleixing_id"]).click()
            time.sleep(1)
            if input_zhengjianleixing == '身份证':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianleixing_css"])[4].click()
                time.sleep(1)
                driver.find_element_by_id(
                    elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianhaoma_id"]).send_keys(input_zhengjianhaoma)
                time.sleep(1)
            elif input_zhengjianleixing == '组织机构代码证':
                driver.find_elements_by_css_selector(
                    elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianleixing_css"])[5].click()
                time.sleep(1)
                driver.find_element_by_id(
                    elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianhaoma_id"]).send_keys(input_zhengjianhaoma)
                time.sleep(1)
            elif input_zhengjianleixing == '营业执照/统一社会信用代码':
                driver.find_elements_by_css_selector(
                    elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianleixing_css"])[6].click()
                time.sleep(1)
                driver.find_element_by_id(
                    elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianhaoma_id"]).send_keys(input_zhengjianhaoma)
                time.sleep(1)
            elif input_zhengjianleixing == '港澳居民来往内地通行证':
                driver.find_elements_by_css_selector(
                    elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianleixing_css"])[7].click()
                time.sleep(1)
                driver.find_element_by_id(
                    elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianhaoma_id"]).send_keys(input_zhengjianhaoma)
                time.sleep(1)
            elif input_zhengjianleixing == '港澳身份证':
                driver.find_elements_by_css_selector(
                    elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianleixing_css"])[8].click()
                time.sleep(1)
                driver.find_element_by_id(
                    elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianhaoma_id"]).send_keys(input_zhengjianhaoma)
                time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_zhengjianleixing}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_zhengjianleixing} 修改失败')

    def kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_beibaoxianrendianhua(driver,
                                                                              input_beibaoxianrendianhua=elements[
                                                                                  "test_vin"]):
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(
                elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_beibaoxianrendianhua_id"]).clear()
            time.sleep(1)
            driver.find_element_by_id(
                elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_beibaoxianrendianhua_id"]).send_keys(
                input_beibaoxianrendianhua)
            time.sleep(1)
            # driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_fadongjihao_id"]).send_keys(input_zhuceriqi)
            # time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_beibaoxianrendianhua}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_beibaoxianrendianhua} 修改失败')


    def kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_beibaoxianrenyouxiang(driver,
                                                                              input_beibaoxianrenyouxiang=elements[
                                                                                  "test_vin"]):
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(
                elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_beibaoxianrenyouxiang_id"]).clear()
            time.sleep(1)
            driver.find_element_by_id(
                elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_beibaoxianrenyouxiang_id"]).send_keys(
                input_beibaoxianrenyouxiang)
            time.sleep(1)
            # driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_fadongjihao_id"]).send_keys(input_zhuceriqi)
            # time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_beibaoxianrenyouxiang}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_beibaoxianrenyouxiang} 修改失败')


    def kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhuzhi(driver, input_zhuzhi=elements["test_vin"]):
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhuzhi_id"]).clear()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhuzhi_id"]).send_keys(
                input_zhuzhi)
            time.sleep(1)
            # driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_fadongjihao_id"]).send_keys(input_zhuceriqi)
            # time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_zhuzhi}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_zhuzhi} 修改失败')


    def kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_minzu(driver, input_minzu=elements["test_vin"]):
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_minzu_id"]).clear()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_minzu_id"]).send_keys(
                input_minzu)
            time.sleep(1)
            # driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_fadongjihao_id"]).send_keys(input_zhuceriqi)
            # time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_minzu}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_minzu} 修改失败')

    def kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_qianfajiguan(driver, input_qianfajiguan=elements["test_vin"]):
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_qianfajiguan_id"]).clear()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_qianfajiguan_id"]).send_keys(
                input_qianfajiguan)
            time.sleep(1)
            # driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_fadongjihao_id"]).send_keys(input_zhuceriqi)
            # time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_qianfajiguan}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_qianfajiguan} 修改失败')



