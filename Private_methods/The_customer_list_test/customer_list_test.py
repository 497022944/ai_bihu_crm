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
    # 选择客户列表tab
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


    def kehuxiangqing_shangniantoubaoxinxi_toubaogongsi(driver, input_toubaogongsi=elements["test_vin"]):
        try:

            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_id"]).click()
            time.sleep(1)
            if input_toubaogongsi == '太平洋车险':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_css"])[4].click()
                time.sleep(1)
            elif input_toubaogongsi == '平安车险':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_css"])[5].click()
                time.sleep(1)
            elif input_toubaogongsi == '人保车险':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_css"])[6].click()
                time.sleep(1)
            elif input_toubaogongsi == '中国人寿财险':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_css"])[7].click()
                time.sleep(1)
            elif input_toubaogongsi == '中华联合车险':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_css"])[8].click()
                time.sleep(1)
            elif input_toubaogongsi == '大地车险':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_css"])[9].click()
                time.sleep(1)
            elif input_toubaogongsi == '阳光车险':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_css"])[10].click()
                time.sleep(1)
            elif input_toubaogongsi == '太平车险':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_css"])[11].click()
                time.sleep(1)
            elif input_toubaogongsi == '华安车险':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_css"])[12].click()
                time.sleep(1)
            elif input_toubaogongsi == '天安车险':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_css"])[13].click()
                time.sleep(1)
            elif input_toubaogongsi == '英大泰和车险':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_css"])[14].click()
                time.sleep(1)
            elif input_toubaogongsi == '安盛天平车险':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_css"])[15].click()
                time.sleep(1)
            elif input_toubaogongsi == '安心车险':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_css"])[16].click()
                time.sleep(1)
            elif input_toubaogongsi == '亚太车险':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_css"])[17].click()
                time.sleep(1)
            elif input_toubaogongsi == '合众车险':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_css"])[18].click()
                time.sleep(1)
            elif input_toubaogongsi == '利宝车险':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_css"])[19].click()
                time.sleep(1)
            elif input_toubaogongsi == '永安车险':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_css"])[20].click()
                time.sleep(1)
            elif input_toubaogongsi == '安诚车险':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_css"])[21].click()
                time.sleep(1)
            elif input_toubaogongsi == '锦泰车险':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_css"])[22].click()
                time.sleep(1)
            elif input_toubaogongsi == '安邦车险':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_css"])[23].click()
                time.sleep(1)
            elif input_toubaogongsi == '永诚车险':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_css"])[24].click()
                time.sleep(1)
            elif input_toubaogongsi == '华泰车险':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_css"])[25].click()
                time.sleep(1)
            elif input_toubaogongsi == '渤海车险':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_css"])[26].click()
                time.sleep(1)
            elif input_toubaogongsi == '信达车险':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_css"])[27].click()
                time.sleep(1)
            elif input_toubaogongsi == '安华农业车险':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_css"])[28].click()
                time.sleep(1)
            elif input_toubaogongsi == '鼎和车险':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_css"])[29].click()
                time.sleep(1)
            elif input_toubaogongsi == '中煤车险':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_css"])[30].click()
                time.sleep(1)
            elif input_toubaogongsi == '诚泰车险':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_css"])[31].click()
                time.sleep(1)
            elif input_toubaogongsi == '长江车险':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_css"])[32].click()
                time.sleep(1)
            elif input_toubaogongsi == '北部湾车险':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_css"])[33].click()
                time.sleep(1)
            elif input_toubaogongsi == '恒邦车险':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_css"])[34].click()
                time.sleep(1)
            elif input_toubaogongsi == '中铁车险':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_css"])[35].click()
                time.sleep(1)
            elif input_toubaogongsi == '美亚车险':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_css"])[36].click()
                time.sleep(1)
            elif input_toubaogongsi == '富邦车险':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_css"])[37].click()
                time.sleep(1)
            elif input_toubaogongsi == '众诚车险':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_css"])[38].click()
                time.sleep(1)
            elif input_toubaogongsi == '东京海上车险':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_css"])[39].click()
                time.sleep(1)
            elif input_toubaogongsi == '其他':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_toubaogongsi_css"])[40].click()
                time.sleep(1)
            else:
                pass
            # driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_fadongjihao_id"]).send_keys(input_zhuceriqi)
            # time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_toubaogongsi}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_toubaogongsi} 修改失败')

    def kehuxiangqing_shangniantoubaoxinxi_shangyedaoqi(driver, input_shangyedaoqi=elements["test_vin"]):
        try:

            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_shangniantoubaoxinxi_shangyedaoqi_id"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_shangyedaoqi}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_shangyedaoqi}修改失败')

    def kehuxiangqing_shangniantoubaoxinxi_jiaoqiangdaoqi(driver, input_jiaoqiangdaoqi=elements["test_vin"]):
        try:

            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_shangniantoubaoxinxi_jiaoqiangdaoqi_id"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_jiaoqiangdaoqi}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_jiaoqiangdaoqi}修改失败')

    def kehuxiangqing_shangniantoubaoxinxi_beibaoxianren(driver, input_beibaoxianren=elements["test_vin"]):
        try:

            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_shangniantoubaoxinxi_beibaoxianren_id"]).clear()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_shangniantoubaoxinxi_beibaoxianren_id"]).send_keys(input_beibaoxianren)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_beibaoxianren}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_beibaoxianren}修改失败')


    def kehuxiangqing_shangniantoubaoxinxi_zhengjianleixing(driver,input_zhengjianleixing, input_zhengjianhaoma=elements["test_vin"]):
        try:

            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_shangniantoubaoxinxi_zhengjianleixing_id"]).click()
            time.sleep(1)
            if input_zhengjianleixing == '身份证':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_zhengjianleixing_css"])[4].click()
                time.sleep(1)
                driver.find_element_by_id(elements["kehuxiangqing_shangniantoubaoxinxi_zhengjianhaoma_id"]).clear()
                time.sleep(1)
                driver.find_element_by_id(elements["kehuxiangqing_shangniantoubaoxinxi_zhengjianhaoma_id"]).send_keys(input_zhengjianhaoma)
                time.sleep(1)
            elif input_zhengjianleixing == '组织机构代码证':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_zhengjianleixing_css"])[5].click()
                time.sleep(1)
                driver.find_element_by_id(elements["kehuxiangqing_shangniantoubaoxinxi_zhengjianhaoma_id"]).clear()
                time.sleep(1)
                driver.find_element_by_id(elements["kehuxiangqing_shangniantoubaoxinxi_zhengjianhaoma_id"]).send_keys(input_zhengjianhaoma)
                time.sleep(1)
            elif input_zhengjianleixing == '营业执照/统一社会信用代码':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_zhengjianleixing_css"])[6].click()
                time.sleep(1)
                driver.find_element_by_id(elements["kehuxiangqing_shangniantoubaoxinxi_zhengjianhaoma_id"]).clear()
                time.sleep(1)
                driver.find_element_by_id(elements["kehuxiangqing_shangniantoubaoxinxi_zhengjianhaoma_id"]).send_keys(input_zhengjianhaoma)
                time.sleep(1)
            elif input_zhengjianleixing == '港澳居民来往内地通行证':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_zhengjianleixing_css"])[7].click()
                time.sleep(1)
                driver.find_element_by_id(elements["kehuxiangqing_shangniantoubaoxinxi_zhengjianhaoma_id"]).clear()
                time.sleep(1)
                driver.find_element_by_id(elements["kehuxiangqing_shangniantoubaoxinxi_zhengjianhaoma_id"]).send_keys(input_zhengjianhaoma)
                time.sleep(1)
            elif input_zhengjianleixing == '港澳身份证':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_zhengjianleixing_css"])[8].click()
                time.sleep(1)
                driver.find_element_by_id(elements["kehuxiangqing_shangniantoubaoxinxi_zhengjianhaoma_id"]).clear()
                time.sleep(1)
                driver.find_element_by_id(elements["kehuxiangqing_shangniantoubaoxinxi_zhengjianhaoma_id"]).send_keys(input_zhengjianhaoma)
                time.sleep(1)
            else:
                pass
            driver.find_element_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_zhengjianleixing}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_zhengjianleixing}修改失败')


    def kehuxiangqing_shangniantoubaoxinxi_jigoumingcheng(driver,input_jigoumingcheng=elements["test_vin"]):
        try:

            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_shangniantoubaoxinxi_jigoumingcheng_id"]).clear()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_shangniantoubaoxinxi_jigoumingcheng_id"]).send_keys(input_jigoumingcheng)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_jigoumingcheng}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_jigoumingcheng}修改失败')

    def kehuxiangqing_shangniantoubaoxinxi_shangyexianbaodanhao(driver,input_shangyexianbaodanhao=elements["test_vin"]):
        try:

            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_shangniantoubaoxinxi_shangyexianbaodanhao_id"]).clear()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_shangniantoubaoxinxi_shangyexianbaodanhao_id"]).send_keys(input_shangyexianbaodanhao)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_shangyexianbaodanhao}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_shangyexianbaodanhao}修改失败')

    def kehuxiangqing_shangniantoubaoxinxi_jiaoqiangxianbaodanhao(driver,input_jiaoqiangxianbaodanhao=elements["test_vin"]):
        # 客户详情-上年投保信息-交强险保单号
        try:

            driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_zhankai_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_shangniantoubaoxinxi_jiaoqiangxianbaodanhao_id"]).clear()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_shangniantoubaoxinxi_jiaoqiangxianbaodanhao_id"]).send_keys(input_jiaoqiangxianbaodanhao)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_shangniantoubaoxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_jiaoqiangxianbaodanhao}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_jiaoqiangxianbaodanhao}修改失败')

    def kehuxiangqing_guanxirenxinxi_shezhilinshiguanxiren(driver):
        # 客户详情-关系人信息-设置临时关系人
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(
                elements["kehuxiangqing_guanxirenxinxi_shezhilinshiguanxiren_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},修改失败')



    def kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_gonghu(driver):
        # 客户详情-关系人信息-被保人信息-公户
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(
                elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_quickselect_gonghu_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},修改失败')


    def kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_geren(driver):
        # 客户详情-关系人信息-被保人信息-个人
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(
                elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_quickselect_geren_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},修改失败')


    def kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_beibaoxianrenxingming(driver, input_beibaoxianrenxingming=elements["test_vin"]):
        # 客户详情-关系人信息-被保人信息-被保险人姓名
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
        # 客户详情-关系人信息-被保人信息-证件类型
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianleixing_id"]).click()
            time.sleep(1)
            if input_zhengjianleixing == '身份证':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianleixing_css"])[4].click()
                time.sleep(1)
                driver.find_element_by_id(
                    elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianhaoma_id"]).clear()
                time.sleep(1)
                driver.find_element_by_id(
                    elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianhaoma_id"]).send_keys(input_zhengjianhaoma)
                time.sleep(1)
            elif input_zhengjianleixing == '组织机构代码证':
                driver.find_elements_by_css_selector(
                    elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianleixing_css"])[5].click()
                time.sleep(1)
                driver.find_element_by_id(
                    elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianhaoma_id"]).clear()
                time.sleep(1)
                driver.find_element_by_id(
                    elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianhaoma_id"]).send_keys(input_zhengjianhaoma)
                time.sleep(1)
            elif input_zhengjianleixing == '营业执照/统一社会信用代码':
                driver.find_elements_by_css_selector(
                    elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianleixing_css"])[6].click()
                time.sleep(1)
                driver.find_element_by_id(
                    elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianhaoma_id"]).clear()
                time.sleep(1)
                driver.find_element_by_id(
                    elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianhaoma_id"]).send_keys(input_zhengjianhaoma)
                time.sleep(1)
            elif input_zhengjianleixing == '港澳居民来往内地通行证':
                driver.find_elements_by_css_selector(
                    elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianleixing_css"])[7].click()
                time.sleep(1)
                driver.find_element_by_id(
                    elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianhaoma_id"]).clear()
                time.sleep(1)
                driver.find_element_by_id(
                    elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianhaoma_id"]).send_keys(input_zhengjianhaoma)
                time.sleep(1)
            elif input_zhengjianleixing == '港澳身份证':
                driver.find_elements_by_css_selector(
                    elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianleixing_css"])[8].click()
                time.sleep(1)
                driver.find_element_by_id(
                    elements["kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianhaoma_id"]).clear()
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
        #客户详情-关系人信息-被保人信息-被保险人电话
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
        #客户详情-关系人信息-被保人信息-被保险人邮箱
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
        #客户详情-关系人信息-被保人信息-住址
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
        # 客户详情-关系人信息-被保人信息-民族
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
        # 客户详情-关系人信息-被保人信息-签发机关
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


    def kehuxiangqing_guanxirenxinxi_toubaorenxinxi_gonghu(driver):
        # 客户详情-关系人信息-投保人信息-公户
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(
                elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_quickselect_gonghu_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},修改失败')


    def kehuxiangqing_guanxirenxinxi_toubaorenxinxi_geren(driver):
        # 客户详情-关系人信息-投保人信息-个人
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(
                elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_quickselect_geren_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},修改失败')

    def kehuxiangqing_guanxirenxinxi_toubaorenxinxi_toubaorenxingming(driver, input_toubaorenxingming=elements["test_vin"]):
        # 客户详情-关系人信息-投保人信息-投保人姓名
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_toubaorenxingming_id"]).clear()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_toubaorenxingming_id"]).send_keys(
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

    def kehuxiangqing_guanxirenxinxi_toubaorenxinxi_zhengjianleixing(driver, input_zhengjianleixing, input_zhengjianhaoma=elements["test_vin"]):
        # 客户详情-关系人信息-投保人信息-证件类型
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_zhengjianleixing_id"]).click()
            time.sleep(1)
            if input_zhengjianleixing == '身份证':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_zhengjianleixing_css"])[4].click()
                time.sleep(1)
                driver.find_element_by_id(
                    elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_zhengjianhaoma_id"]).send_keys(input_zhengjianhaoma)
                time.sleep(1)
            elif input_zhengjianleixing == '组织机构代码证':
                driver.find_elements_by_css_selector(
                    elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_zhengjianleixing_css"])[5].click()
                time.sleep(1)
                driver.find_element_by_id(
                    elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_zhengjianhaoma_id"]).send_keys(input_zhengjianhaoma)
                time.sleep(1)
            elif input_zhengjianleixing == '营业执照/统一社会信用代码':
                driver.find_elements_by_css_selector(
                    elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_zhengjianleixing_css"])[6].click()
                time.sleep(1)
                driver.find_element_by_id(
                    elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_zhengjianhaoma_id"]).send_keys(input_zhengjianhaoma)
                time.sleep(1)
            elif input_zhengjianleixing == '港澳居民来往内地通行证':
                driver.find_elements_by_css_selector(
                    elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_zhengjianleixing_css"])[7].click()
                time.sleep(1)
                driver.find_element_by_id(
                    elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_zhengjianhaoma_id"]).send_keys(input_zhengjianhaoma)
                time.sleep(1)
            elif input_zhengjianleixing == '港澳身份证':
                driver.find_elements_by_css_selector(
                    elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_zhengjianleixing_css"])[8].click()
                time.sleep(1)
                driver.find_element_by_id(
                    elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_zhengjianhaoma_id"]).send_keys(input_zhengjianhaoma)
                time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_zhengjianleixing}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_zhengjianleixing} 修改失败')


    def kehuxiangqing_guanxirenxinxi_toubaorenxinxi_toubaorendianhua(driver, input_toubaorendianhua=elements["test_vin"]):
        # 客户详情-关系人信息-投保人信息-投保人电话
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(
                elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_toubaorendianhua_id"]).clear()
            time.sleep(1)
            driver.find_element_by_id(
                elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_toubaorendianhua_id"]).send_keys(
                input_toubaorendianhua)
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

    def kehuxiangqing_guanxirenxinxi_toubaorenxinxi_toubaorenyouxiang(driver, input_toubaorenyouxiang=elements["test_vin"]):
        # 客户详情-关系人信息-投保人信息-投保人邮箱
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(
                elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_toubaorenyouxiang_id"]).clear()
            time.sleep(1)
            driver.find_element_by_id(
                elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_toubaorenyouxiang_id"]).send_keys(
                input_toubaorenyouxiang)
            time.sleep(1)
            # driver.find_element_by_id(elements["kehuxiangqing_cheliangxinxi_fadongjihao_id"]).send_keys(input_zhuceriqi)
            # time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_toubaorenyouxiang}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_toubaorenyouxiang} 修改失败')


    def kehuxiangqing_guanxirenxinxi_toubaorenxinxi_zhuzhi(driver, input_zhuzhi=elements["test_vin"]):
        # 客户详情-关系人信息-投保人信息-住址
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(
                elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_zhuzhi_id"]).clear()
            time.sleep(1)
            driver.find_element_by_id(
                elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_zhuzhi_id"]).send_keys(
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

    def kehuxiangqing_guanxirenxinxi_toubaorenxinxi_minzu(driver, input_minzu=elements["test_vin"]):
        # 客户详情-关系人信息-投保人信息-民族
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(
                elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_minzu_id"]).clear()
            time.sleep(1)
            driver.find_element_by_id(
                elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_minzu_id"]).send_keys(
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


    def kehuxiangqing_guanxirenxinxi_toubaorenxinxi_qianfajiguan(driver, input_qianfajiguan=elements["test_vin"]):
        # 客户详情-关系人信息-投保人信息-签发机关
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(
                elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_qianfajiguan_id"]).clear()
            time.sleep(1)
            driver.find_element_by_id(
                elements["kehuxiangqing_guanxirenxinxi_toubaorenxinxi_qianfajiguan_id"]).send_keys(
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



    def kehuxiangqing_guanxirenxinxi_chezhuxinxi_gonghu(driver):
        # 客户详情-关系人信息-车主信息-公户
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"]).click()
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
        # 客户详情-关系人信息-车主信息-个人
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(
                elements["kehuxiangqing_guanxirenxinxi_chezhuxinxi_quickselect_geren_css"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},修改失败')


    def kehuxiangqing_guanxirenxinxi_chezhuxinxi_chezhuxingming(driver, input_chezhuxingming=elements["test_vin"]):
        #客户详情-关系人信息-车主信息-车主姓名
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_guanxirenxinxi_chezhuxinxi_chezhuxingming_id"]).clear()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_guanxirenxinxi_chezhuxinxi_chezhuxingming_id"]).send_keys(input_chezhuxingming)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_chezhuxingming} 修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_chezhuxingming} 修改失败')

    def kehuxiangqing_guanxirenxinxi_chezhuxinxi_zhengjianleixing(driver, input_zhengjianleixing, input_zhengjianhaoma=elements["test_vin"]):
        #客户详情-关系人信息-车主信息-证件类型
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_guanxirenxinxi_chezhuxinxi_zhengjianleixing_id"]).click()
            time.sleep(1)
            if input_zhengjianleixing == '身份证':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_chezhuxinxi_zhengjianleixing_css"])[4].click()
                time.sleep(1)
            elif input_zhengjianleixing == '组织机构代码证':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_chezhuxinxi_zhengjianleixing_css"])[5].click()
                time.sleep(1)
            elif input_zhengjianleixing == '营业执照/统一社会信用代码':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_chezhuxinxi_zhengjianleixing_css"])[6].click()
                time.sleep(1)
            elif input_zhengjianleixing == '港澳居民来往内地通行证':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_chezhuxinxi_zhengjianleixing_css"])[7].click()
                time.sleep(1)
            elif input_zhengjianleixing == '港澳身份证':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_chezhuxinxi_zhengjianleixing_css"])[8].click()
                time.sleep(1)
            else:
                pass
            driver.find_element_by_id(elements["kehuxiangqing_guanxirenxinxi_chezhuxinxi_zhengjianhaoma_id"]).clear()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_guanxirenxinxi_chezhuxinxi_zhengjianhaoma_id"]).send_keys(input_zhengjianhaoma)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_guanxirenxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_zhengjianleixing} 修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_zhengjianleixing} 修改失败')


    def kehuxiangqing_baojiaxinxi_toubaodiqu(driver, input_toubaodiqu=elements["test_vin"]):
        #客户详情-报价信息-投保地区
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_toubaodiqu_id"]).click()
            time.sleep(1)
            if input_toubaodiqu == '北京':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_toubaodiqu_css"])[4].click()
                time.sleep(1)
            elif input_toubaodiqu == '成都':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_toubaodiqu_css"])[5].click()
                time.sleep(1)
            elif input_toubaodiqu == '昆明':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_toubaodiqu_css"])[6].click()
                time.sleep(1)
            elif input_toubaodiqu == '上海':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_toubaodiqu_css"])[7].click()
                time.sleep(1)
            elif input_toubaodiqu == '南京':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_toubaodiqu_css"])[8].click()
                time.sleep(1)
            elif input_toubaodiqu == '杭州':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_toubaodiqu_css"])[9].click()
                time.sleep(1)
            elif input_toubaodiqu == '深圳':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_toubaodiqu_css"])[10].click()
                time.sleep(1)
            elif input_toubaodiqu == '东莞':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_toubaodiqu_css"])[11].click()
                time.sleep(1)
            elif input_toubaodiqu == '济南':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_toubaodiqu_css"])[12].click()
                time.sleep(1)
            elif input_toubaodiqu == '佛山':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_toubaodiqu_css"])[13].click()
                time.sleep(1)
            elif input_toubaodiqu == '长春':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_toubaodiqu_css"])[14].click()
                time.sleep(1)
            elif input_toubaodiqu == '青岛':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_toubaodiqu_css"])[15].click()
                time.sleep(1)
            elif input_toubaodiqu == '合肥':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_toubaodiqu_css"])[16].click()
                time.sleep(1)
            elif input_toubaodiqu == '宁波':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_toubaodiqu_css"])[17].click()
                time.sleep(1)
            elif input_toubaodiqu == '呼和浩特':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_toubaodiqu_css"])[18].click()
                time.sleep(1)
            elif input_toubaodiqu == '南宁':
                driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_toubaodiqu_css"])[19].click()
                time.sleep(1)
            else:
                pass
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baocun_button_css"]).click()
            time.sleep(1)
            # driver.find_element_by_css_selector(elements["kehuxiangqing_cheliangxinxi_baocun_button_css"]).click()
            # time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_toubaodiqu} 修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_toubaodiqu} 修改失败')


    def kehuxiangqing_baojiaxinxi_shangyeqibao(driver, input_shangyeqibao=elements["test_vin"]):
        #客户详情-报价信息-商业起保
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_shangyeqibao_id"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_shangyeqibao} 修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_shangyeqibao} 修改失败')

    def kehuxiangqing_baojiaxinxi_jiaoqiangqibao(driver, input_jiaoqiangqibao=elements["test_vin"]):
        #客户详情-报价信息-交强起保
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_tab_css"]).click()
            time.sleep(1)
            driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_jiaoqiangqibao_id"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name},{input_jiaoqiangqibao} 修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{input_jiaoqiangqibao} 修改失败')

    def kehuxiangqing_baojiaxinxi_baojiagongsi(driver, input_baojiagongsi):
        #客户详情-报价信息-选择报价公司
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_tab_css"]).click()
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

            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name}, {input_baojiagongsi}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}, {input_baojiagongsi} 修改失败')


    def kehuxiangqing_baojiaxinxi_hebaogongsi(driver, input_hebaogongsi):
        #客户详情-报价信息-选择核保公司
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_tab_css"]).click()
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
                for xuhao in range(0, len(driver.find_elements_by_css_selector(elements["kehuxiangqing_baojiaxinxi_hebaogongsi_checkbox_css"]))):
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
            # 勾选核保公司--------------

            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name}, {input_hebaogongsi}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}, {input_hebaogongsi} 修改失败')



    def kehuxiangqing_baojiaxinxi_chesun(driver, is_zhuxian = 1, is_bujimian = 1):
        #客户详情-报价信息-车损
        try:
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_tab_css"]).click()
            time.sleep(1)
            if is_zhuxian == 1 and is_bujimian == 1: #车损 + 不计免
                # 车损
                if driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_chesun_css"]).get_attribute('class') == elements["kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    pass
                else:
                    driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_chesun_css"]).click()
                time.sleep(1)

                # 不计免
                if driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_chesun_bujimian_id"]).get_attribute('class') == elements["kehuxiangqing_baojiaxinxi_bujimian_checked_class"]:
                    pass
                else:
                    driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_chesun_bujimian_id"]).click()

            elif is_zhuxian == 1 and is_bujimian == 0: #车损
                # 车损
                if driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_chesun_css"]).get_attribute(
                        'class') == elements["kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    pass
                else:
                    driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_chesun_css"]).click()
                time.sleep(1)

                # 不计免
                if driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_chesun_bujimian_id"]).get_attribute(
                        'class') == elements["kehuxiangqing_baojiaxinxi_bujimian_checked_class"]:
                    driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_chesun_bujimian_id"]).click()
                else:
                    pass

            elif is_zhuxian == 0 and is_bujimian == 0: #不上车损
                # 车损
                if driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_chesun_css"]).get_attribute(
                        'class') == elements["kehuxiangqing_baojiaxinxi_xianzhong_checked_class"]:
                    driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_chesun_css"]).click()
                else:
                    pass

                time.sleep(1)

                # 不计免
                if driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_chesun_bujimian_id"]).get_attribute(
                        'class') == elements["kehuxiangqing_baojiaxinxi_bujimian_checked_class"]:
                    driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_chesun_bujimian_id"]).click()
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


    def kehuxiangqing_baojiaxinxi_sanzhe(driver, is_zhuxian = 1, is_bujimian = 1, bao_e = 5):
        #客户详情-报价信息-三者
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
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name}, {is_zhuxian},{bao_e},{is_bujimian}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}, {is_zhuxian},{bao_e},{is_bujimian}修改失败')


    def kehuxiangqing_baojiaxinxi_siji(driver, is_zhuxian = 1, is_bujimian = 1, bao_e = 5):
        #客户详情-报价信息-司机
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
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name}, {is_zhuxian},{bao_e},{is_bujimian}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}, {is_zhuxian},{bao_e},{is_bujimian}修改失败')


    def kehuxiangqing_baojiaxinxi_chengke(driver, is_zhuxian = 1, is_bujimian = 1, bao_e = 5):
        #客户详情-报价信息-乘客
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
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name}, {is_zhuxian},{bao_e},{is_bujimian}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}, {is_zhuxian},{bao_e},{is_bujimian}修改失败')


    def kehuxiangqing_baojiaxinxi_daoqiang(driver, is_zhuxian = 1, is_bujimian = 1):
        #客户详情-报价信息-盗抢
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
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name}, {is_zhuxian},{is_bujimian}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}, {is_zhuxian},{is_bujimian}修改失败')


    def kehuxiangqing_baojiaxinxi_huahen(driver, is_zhuxian = 1, is_bujimian = 1, bao_e = 2000):
        #客户详情-报价信息-划痕
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
            time.sleep(1)
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name}, {is_zhuxian},{bao_e},{is_bujimian}修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}, {is_zhuxian},{bao_e},{is_bujimian}修改失败')


    def kehuxiangqing_baojiaxinxi_boli(driver, is_zhuxian = 1, bao_e = '国产'):
        #客户详情-报价信息-玻璃
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
        #客户详情-报价信息-自燃
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
        #客户详情-报价信息-涉水
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
        #客户详情-报价信息-车损无法找到第三方
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
        #客户详情-报价信息-指定修理厂
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
        #客户详情-报价信息-新增设备损失
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


    def kehuxiangqing_baojiaxinxi_sanzexianfujiafadingjiajiarixianefanbei(driver, is_zhuxian = 1):
        #客户详情-报价信息-三责险附加法定节假日险翻倍险
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
        #客户详情-报价信息-修理期间费用补偿险
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
                driver.find_element_by_id(elements["kehuxiangqing_baojiaxinxi_xiuliqijianfeiyongbuchang_baoe_id"]).click()
                time.sleep(1)
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
            driver.find_element_by_css_selector(elements["kehuxiangqing_baojiaxinxi_baocun_button_css"]).click()
            time.sleep(1)
            logger.info(f'{sys._getframe().f_code.co_name}, {is_zhuxian},修改成功')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name}, {is_zhuxian},修改失败')
