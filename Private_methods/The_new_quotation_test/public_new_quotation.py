import unittest,os,json
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
    #车牌号
    def quotation_license_input(driver, license):
        try:
            chepai1 = driver.find_element_by_class_name(elements["chepairukou_class"]).send_keys(license)
            logger.info("新增报价车牌正常操作")
        except Exception:
            logbug.debug("新增报价车牌未找到")
        finally:
            pass
        return license

    def quotation_license_click(driver):
        try:
            xiayibu = driver.find_elements_by_css_selector(elements["xiayibu_css"])[0].click()
            logger.info("新增报价下一步正常操作")
        except Exception:
            logbug.debug("新增报价下一步未找到")
        finally:
            pass

    def quotation_license_claer(driver):
        try:
            chepai1 = driver.find_element_by_class_name(elements["chepairukou_class"]).clear()
            logger.info("车牌号文本清空正常操作")
        except Exception:
            logbug.debug("车牌号文本清空正常操作")
        finally:
            pass

if __name__ == '__main__':
    unittest.main()
