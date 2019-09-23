import unittest,os,json,sys
from time import sleep
from utils.Logbug import LogBug
from utils.Log import Log
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
logger = Log()
logbug = LogBug()
log_path = os.path.dirname(os.path.abspath('.')) + "\\Element_methods\quotation.json"
element = open(log_path, encoding='utf-8')
elements = json.load(element)

#菜单
class quotation_license:

    def kehuxiangqiang_xinzengbaojia(driver):
        try:
            driver.execute_script(elements['客户列表_新增报价按钮'])
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},中断执行--客户列表_新增报价按钮点击异常')


    '''车牌号-新增报价车牌号输入'''
    def quotation_license_input(driver, license1):
        sleep(2)
        try:
            dict1 = driver.find_element_by_class_name(elements["chepairukou_class"])
            ActionChains(driver).move_to_element(dict1).perform()
            dict1.click()
            dict1.send_keys(license1)

            #driver.find_element_by_class_name(elements["chepairukou_class"]).send_keys(license1)
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},中断执行--新增报价车牌号输入异常')

    '''车牌号-新增报价页面点击下一步'''
    def quotation_license_click(driver):
        sleep(2)
        try:
            dict1 = driver.find_element_by_css_selector(elements["新增报价_下一步模拟"])
            ActionChains(driver).move_to_element(dict1).perform()
            dict1.click()
            #new_js = driver.execute_script(elements["新增报价_下一步"])
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},中断执行--新增报价弹窗点击下一步按钮异常')

    #车牌号-新增报价页面车牌号清空
    def quotation_license_claer(driver):
        sleep(2)
        try:
            driver.find_element_by_class_name(elements["chepairukou_class"]).clear()
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},继续执行--新增报价页面车牌号清空异常')
        finally:
            sleep(1)
            pass

    #车牌号-新增报价页面直接报价按钮
    def quotation_license_direct_quotation(driver):
        sleep(2)
        try:
            driver.execute_script(elements['车牌号-新增报价页面直接报价按钮'])
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},继续执行--车牌号-新增报价页面直接报价按钮未点击')
        finally:
            sleep(1)
            pass



    #车牌号-新增报价页面点击下一步所有返回提示
    def All_the_tips(driver):
        sleep(2)
        try:
            global tishi
            tishi = driver.execute_script(elements["ant-modal-body"])
        except Exception:
            logger.info(f'{sys._getframe().f_code.co_name},{tishi} 弹窗不存在')
        else:
            if tishi == "您的账户余额不足，请联系管理员充值！":
                tishihaode = driver.execute_script(elements["好的"])
                logger.info(f'{sys._getframe().f_code.co_name},{tishi} 弹窗内容')
            elif tishi == "账号待审核":
                logger.info(f'{sys._getframe().f_code.co_name},{tishi} 弹窗内容')
            else:
                logger.info(f'{sys._getframe().f_code.co_name},{tishi} 弹窗内容')

    #车牌号-新增报价页面点击下一步所有返回提示点击好的
    def All_the_tips_click(driver):
        sleep(2)
        try:
            driver.find_element_by_class_name(elements["ant-modal-confirm-btns"]).click()
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},中断执行--新增报价页面点击下一步所有返回提示点击确定按钮异常')

    #车牌号-新增报价平安证件号
    def Safety_Certificate_Number(driver, safety):
        try:
            
            driver.find_element_by_id(elements["sixDigitsAfterIdCard"]).send_keys(safety)
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},继续执行--新增报价页面新增报价平安证件号输入异常')
        finally:
            
            pass

    # 车牌号-投保城市
    def license_cityCode(driver, license_cityCode):
        sleep(2)
        try:
            dict1 = driver.execute_script(elements['车牌号_投保地区点击'])
            beijiing = driver.execute_script(elements["车牌号_投保地区文本"])
            if license_cityCode in beijiing:
                for i in range(len(beijiing)):
                    ing = driver.execute_script("return $('.ant-select-dropdown-content').find('li').eq(" + str(i) +").text()")
                    if ing == '北京' and ing == license_cityCode:
                        ing = driver.execute_script("$('.ant-select-dropdown-content').find('li').eq(" + str(i) +").click()")
                        break
                    elif ing == '南京'and ing == license_cityCode:
                        ing = driver.execute_script("$('.ant-select-dropdown-content').find('li').eq(" + str(i) +").click()")
                        break
                    else:
                        logbug.debug(f'{sys._getframe().f_code.co_name},继续执行--新增报价选择上年投保公司输入异常')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},继续执行--新增报价选择上年投保公司输入异常')
        finally:
            pass
    # 车牌号-城市名
    def license_cityCode_ming(driver, license_cityCode_ming):
        try:
            dict1 = driver.execute_script(elements['新增报价_选择城市名'])
            if license_cityCode_ming == '京' and dict1 == '京':
                logger.info(f'{sys._getframe().f_code.co_name},继续执行--新增报价选择城市名正确')
            elif license_cityCode_ming == '苏' and dict1 == '苏':
                logger.info(f'{sys._getframe().f_code.co_name},继续执行--新增报价选择城市名正确')
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name},继续执行--新增报价选择城市名暂未开发')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},继续执行--新增报价选择城市名异常')
        finally:
            sleep(2)
            pass

    #车牌号-新增报价车牌选择上年投保公司
    def Last_year_insurance(driver, insurance):
        sleep(2)
        try:
            dict1 = driver.find_elements_by_css_selector(elements["chepaihao_shangniantoubaogongsi"])[0]
            ActionChains(driver).move_to_element(dict1).perform()
            dict1.click()
            sleep(1)
            if insurance == '太平洋车险':
                driver.execute_script(elements["chepaihao_TPY_shangniantoubaogongsi12"])
            elif insurance == '平安车险':
                driver.execute_script(elements["chepaihao_PA_shangniantoubaogongsi12"])
            elif insurance == '人保车险':
                driver.execute_script(elements["chepaihao_RB_shangniantoubaogongsi12"])
            elif insurance == '中国人寿财险':
                driver.execute_script(elements["chepaihao_GSC_shangniantoubaogongsi12"])
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name},继续执行--新增报价上年投保公司未选择')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},继续执行--新增报价选择上年投保公司选择异常')
        finally:
            
            pass

    #选择车架号title
    def title_VIN_click(driver):
        sleep(2)
        try:
            driver.find_elements_by_css_selector(elements["chejiahao_titel"])[1].click()
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},继续执行--新增报价选择车架号title异常')
        finally:
            pass


    def VIN_table_assert(driver,):
        try:
            vin = "$('.ant-tabs-nav-animated>div>div:nth-child(2)').eq(1).attr('class')"
            vin_ne = driver.execute_script(vin)
            if vin_ne == "ant-tabs-tab-active ant-tabs-tab":
                logger.info(f'{sys._getframe().f_code.co_name},继续执行--测试车架号切换正常')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},继续执行--测试车架号是否切换异常')
        finally:
            pass



    # 车架号输入
    def VIN_input(driver, vin):
        sleep(2)
        try:
            driver.find_element_by_id(elements["chejiahao_input"]).send_keys(vin)
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},继续执行--新增报价选择上年投保公司输入异常')
        finally:
            pass
    # 车架号提示
    def VIN_input_hint(driver, hint):
        sleep(2)
        try:
            hinttishi = driver.execute_script(elements['chejiahao_input_vin_hint'])
            if hint == '车架号必填' and hinttishi == "车架号必填":
                logger.info(f'{sys._getframe().f_code.co_name}{hinttishi},继续执行--车架号必填-返回与实际相符')
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name}{hinttishi},继续执行--车架号必填-返回与实际不符')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},继续执行--车架号必填--提示不存在')
        finally:
            pass
    #车架号提示
    def VIN_input_hint_title(driver, hint):
        sleep(2)
        try:
            hinttishi = driver.find_element_by_css_selector("body > div.ant-message").text
            if hint == '请正确填写车架号':
                logger.info(f'{sys._getframe().f_code.co_name}{hinttishi},继续执行--车架号必填-返回与实际相符')
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name}{hinttishi},继续执行--车架号必填-返回与实际不符')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},继续执行--车架号必填--提示不存在')
        finally:
            
            pass

    # 发动机号输入
    def engine_input(driver, engine):
        sleep(2)
        try:
            driver.find_element_by_id(elements["chejiahao_input_fadongjihao"]).send_keys(engine)
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},继续执行--新增报价选择上年投保公司输入异常')
        finally:
            
            pass

    # 车架号-上年投保公司输入
    def VIN_Last_year_insurance(driver, insurance2):
        sleep(2)
        try:
            dict1 = driver.find_elements_by_css_selector(elements["chejiahao_shangniantoubaogongsi"])[1]
            ActionChains(driver).move_to_element(dict1).perform()
            dict1.click()
            if insurance2 == '太平洋车险':
                driver.execute_script(elements["chejiahao_shangniantoubaogongsi_TPY"])
            elif insurance2 == '平安车险':
                driver.execute_script(elements["chejiahao_shangniantoubaogongsi_PA"])
            elif insurance2 == '人保车险':
                driver.execute_script(elements["chejiahao_shangniantoubaogongsi_RB"])
            elif insurance2 == '中国人寿财险':
                driver.execute_script(elements["chejiahao_shangniantoubaogongsi_GSC"])
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name},继续执行--新增报价选择上年投保公司暂未开发')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},继续执行--新增报价选择上年投保公司选择异常')
        finally:
            
            pass

    # 车架号-投保城市
    def VIN_cityCode(driver, vin_cityCode):
        sleep(2)
        #driver = webdriver.Chrome()
        try:
            dict1 = driver.execute_script(elements['车架号_投保地区点击'])
            beijiing = driver.execute_script(elements["chejiahao_toubaochengshitext"])
            if vin_cityCode in beijiing:
                for i in range(len(driver.execute_script(elements["chejiahao_toubaochengshi1"]))):
                    ing = driver.execute_script("$('.ant-select-dropdown-content').find('li').eq(" + str(i + 1) + ").text()")
                    if ing == '北京':
                        ing = driver.execute_script("$('.ant-select-dropdown-content').find('li').eq(" + str(i + 1) + ").click()")
                        break
                    elif ing == '南京':
                        ing = driver.execute_script("$('.ant-select-dropdown-content').find('li').eq(" + str(i + 1) + ").click()")
                        break
                    else:
                        logbug.debug(f'{sys._getframe().f_code.co_name},继续执行--新增报价选择上年投保公司输入异常')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},继续执行--新增报价选择上年投保公司输入异常')
        finally:
            pass

    #新增报价_新车报价tab
    def title_new_car_click(driver):
        sleep(2)
        try:
            driver.find_elements_by_css_selector(elements["新增报价_新车报价tab"])[1].click()
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},继续执行--新增报价选择车架号title异常')
        finally:
            pass










if __name__ == '__main__':
    unittest.main()
