import unittest,os,json,sys
from time import sleep
from utils.Logbug import LogBug
from utils.Log import Log
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
    #车牌号-新增报价车牌号输入
    def quotation_license_input(driver, license1):
        try:
            #driver.find_element_by_css_selector("#licenseNo > input").send_keys(license1)
            driver.find_element_by_class_name(elements["chepairukou_class"]).send_keys(license1)
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},中断执行--新增报价车牌号输入异常')

    #车牌号-新增报价页面点击下一步
    def quotation_license_click(driver):
        try:
            driver.find_element_by_css_selector(elements["xiayibu_css"]).click()
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},中断执行--新增报价页面点击下一步按钮异常')

    #车牌号-新增报价页面车牌号清空
    def quotation_license_claer(driver):
        try:
            driver.find_element_by_class_name(elements["chepairukou_class"]).clear()
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},继续执行--新增报价页面车牌号清空异常')
        finally:
            sleep(1)
            pass

    #车牌号-新增报价页面点击下一步所有返回提示
    def All_the_tips(driver):
        try:
            global tishi
            tishi = driver.find_element_by_class_name(elements["ant-modal-body"]).text
        except Exception:
            logger.info(f'{sys._getframe().f_code.co_name},{tishi} 弹窗不存在')
        else:
            if tishi in "您的账户余额不足，请联系管理员充值！":
                logger.info(f'{sys._getframe().f_code.co_name},{tishi} 弹窗内容')
            elif tishi in "账号待审核":
                logger.info(f'{sys._getframe().f_code.co_name},{tishi} 弹窗内容')
            else:
                logger.info(f'{sys._getframe().f_code.co_name},{tishi} 弹窗内容')

    #车牌号-新增报价页面点击下一步所有返回提示点击好的
    def All_the_tips_click(driver):
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
            sleep(2)
            pass

    # 车牌号-投保城市
    def license_cityCode(driver, license_cityCode):
        try:
            dict1 = driver.find_elements_by_css_selector(elements['idcityCode'])[0].click()
            dict2 = driver.find_elements_by_css_selector(elements['chepaihao_toubaochengshi'])[2]
            if license_cityCode == '北京':
                dict3 = dict2.find_element_by_css_selector(elements['chepaihao_toubaochengshi1']).click()
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name},继续执行--新增报价选择投保城市暂未开发')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},继续执行--新增报价选择城市名异常')
        finally:
            sleep(2)
            pass

    # 车牌号-城市名
    def license_cityCode_ming(driver, license_cityCode_ming):
        try:
            dict1 = driver.find_element_by_css_selector(elements['chepaihao_城市']).text
            if license_cityCode_ming == '京':
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
        try:
            dict1 = driver.find_elements_by_css_selector(elements["chepaihao_shangniantoubaogongsi"])[0]
            ActionChains(driver).move_to_element(dict1).perform()
            dict1.click()
            sleep(1)
            if insurance == '太平洋车险':
                ct2 = driver.find_element_by_css_selector(elements["chepaihao_shangniantoubaogongsi1"])
                ct3 = ct2.find_element_by_css_selector(elements["chepaihao_TPY_shangniantoubaogongsi12"])
                ct3.click()
            elif insurance == '平安车险':
                ct2 = driver.find_element_by_css_selector(elements["chepaihao_shangniantoubaogongsi1"])
                ct3 = ct2.find_element_by_css_selector(elements["chepaihao_PA_shangniantoubaogongsi12"])
                ct3.click()
            elif insurance == '人保车险':
                ct2 = driver.find_element_by_css_selector(elements["chepaihao_shangniantoubaogongsi1"])
                ct3 = ct2.find_element_by_css_selector(elements["chepaihao_RB_shangniantoubaogongsi12"])
                ct3.click()
            elif insurance == '中国人寿财险':
                ct2 = driver.find_element_by_css_selector(elements["chepaihao_shangniantoubaogongsi1"])
                ct3 = ct2.find_element_by_css_selector(elements["chepaihao_GSC_shangniantoubaogongsi12"])
                ct3.click()
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name},继续执行--新增报价上年投保公司未选择')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},继续执行--新增报价选择上年投保公司选择异常')
        finally:
            sleep(2)
            pass

    #选择车架号title
    def title_VIN_click(driver):
        try:
            driver.find_element_by_css_selector(elements["chejiahao_titel"]).click()
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},继续执行--新增报价选择上年投保公司输入异常')
        finally:
            sleep(2)
            pass

    # 车架号输入
    def VIN_input(driver, vin):
        try:
            driver.find_element_by_id(elements["chejiahao_input"]).send_keys(vin)
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},继续执行--新增报价选择上年投保公司输入异常')
        finally:
            sleep(2)
            pass
    # 车架号提示
    def VIN_input_hint(driver, hint):
        try:
            hinttishi = driver.find_element_by_css_selector(elements["chejiahao_input_vin_hint"]).text
            if hint == '车架号必填':
                logger.info("输入车架号提示，预期为:'车架号必填'实际为:{}".format(hinttishi))
            else:
                logbug.debug("输入车架号提示，预期为:'请输入正确的车架号'实际为:{}".format(hinttishi))
        except Exception:
            logbug.debug("车架号提示不存在")
        finally:
            sleep(2)
            pass
    #车架号提示
    def VIN_input_hint_title(driver, hint):
        try:
            hinttishi = driver.find_element_by_css_selector("body > div.ant-message").text
            if hint == '请正确填写车架号':
                logger.info("输入车架号提示，预期为:'车架号必填'实际为:{}".format(hinttishi))
            else:
                logbug.debug("输入车架号提示，预期为:'请输入正确的车架号'实际为:{}".format(hinttishi))
        except Exception:
            logbug.debug("车架号提示不存在")
        finally:
            sleep(2)
            pass

    # 发动机号输入
    def engine_input(driver, engine):
        try:
            driver.find_element_by_id(elements["chejiahao_input_fadongjihao"]).send_keys(engine)
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},继续执行--新增报价选择上年投保公司输入异常')
        finally:
            sleep(2)
            pass

    # 车架号-上年投保公司输入
    def VIN_Last_year_insurance(driver, insurance2):
        try:
            dict1 = driver.find_elements_by_css_selector(elements["chejiahao_shangniantoubaogongsi"])[1]
            ActionChains(driver).move_to_element(dict1).perform()
            dict1.click()
            if insurance2 == '太平洋车险':
                ct2 = driver.find_element_by_css_selector(elements["chejiahao_shangniantoubaogongsi1"])
                ct3 = ct2.find_element_by_css_selector(elements["chejiahao_shangniantoubaogongsi_TPY"])
                ct3.click()
            elif insurance2 == '平安车险':
                ct2 = driver.find_element_by_css_selector(elements["chepaihao_shangniantoubaogongsi1"])
                ct3 = ct2.find_element_by_css_selector(elements["chejiahao_shangniantoubaogongsi_PA"])
                ct3.click()
            elif insurance2 == '人保车险':
                ct2 = driver.find_element_by_css_selector(elements["chepaihao_shangniantoubaogongsi1"])
                ct3 = ct2.find_element_by_css_selector(elements["chejiahao_shangniantoubaogongsi_RB"])
                ct3.click()
            elif insurance2 == '中国人寿财险':
                ct2 = driver.find_element_by_css_selector(elements["chepaihao_shangniantoubaogongsi1"])
                ct3 = ct2.find_element_by_css_selector(elements["chejiahao_shangniantoubaogongsi_GSC"])
                ct3.click()
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name},继续执行--新增报价选择上年投保公司暂未开发')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},继续执行--新增报价选择上年投保公司选择异常')
        finally:
            sleep(2)
            pass

    # 车架号-投保城市
    def VIN_cityCode(driver, vin_cityCode):
        try:
            dict1 = driver.find_elements_by_css_selector(elements["chejiahao_toubaochengshi"])[1].click()
            dict2 = driver.find_element_by_css_selector(elements["chejiahao_toubaochengshi1"])
            if vin_cityCode == '北京':
                dict3 = dict2.find_elements_by_css_selector(elements["chejiahao_toubaochengshi_BEIJING"]).click()
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name},继续执行--新增报价选择投保城市暂未开发')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},继续执行--新增报价选择上年投保公司输入异常')
        finally:
            sleep(2)
            pass












if __name__ == '__main__':
    unittest.main()
