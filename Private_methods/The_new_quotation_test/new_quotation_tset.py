import unittest, os, json
from time import sleep
from utils.Logbug import LogBug
from utils.Log import Log
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Public_methods.New_offer_menu import menu
logger = Log()
logbug = LogBug()
log_path = os.path.dirname(os.path.abspath('.')) + "\\Element_methods\quotation.json"
element = open(log_path, encoding='utf-8')
elements = json.load(element)
yongli_path = os.path.dirname(os.path.abspath('.')) + "\\configs\yongli.txt"
ele = open(yongli_path, 'r',encoding='utf-8-sig')
c = ele.readlines()

class new_quotation_case(unittest.TestCase):

    #新增报价菜单
    def license_check(self, driver):
        #driver = webdriver.Chrome()
        try:
            #title新增报价
            xinzhengtitle = driver.find_element_by_class_name(elements['xinzhengtitle']).text
            if xinzhengtitle == '新增报价':
                logger.info("新增报价页面title正确，预期为:'新增报价'实际为:{}".format(xinzhengtitle))
            else:
                logbug.debug("新增报价页面title异常，预期为:'新增报价'实际为:{}".format(xinzhengtitle))
        except Exception:
            logbug.debug("新增报价title未找到")
        finally:
            sleep(2)
            pass

        try:
            chepaihaotitle = driver.find_element_by_css_selector(elements['chepaihaotitle']).text
            if chepaihaotitle == '车牌':
                logger.info("新增报价页面车牌title正确，预期为:'车牌号'实际为:{}".format(chepaihaotitle))
            else:
                logbug.debug("新增报价页面车牌title正确，预期为:'车牌号'实际为:{}".format(chepaihaotitle))
        except Exception:
            logbug.debug("车牌号title未找到")
        finally:
            sleep(2)
            pass
    def license_check_hint(self, driver, hint):
        #车牌提示
        try:
            #cphint = driver.find_element_by_class_name(elements['chepaihint']).text()
            hinttishi = driver.find_element_by_css_selector("body > div.ant-message").text
            # js = '$(".ant-message").text()'
            # js1 = driver.execute_script(js)
            #logger.info("输入车牌提示，预期为:'车牌号必填'实际为:{}".format(hinttishi))
            if hint == '请正确填写车牌号':
                    logger.info("输入车牌提示，预期为:'车牌号必填'实际为:{}".format(hinttishi))
            else:
                logbug.debug("输入车牌提示，预期为:'请输入正确的车牌号'实际为:{}".format(hinttishi))
        except Exception:
            logbug.debug("车牌号提示不存在")
        finally:
            sleep(2)
            pass




if __name__ == '__main__':
    unittest.main()
