import unittest, os, json, sys
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
        # 车牌提示
        try:
            js = "return $('.ant-message').text()"
            hinttishi = driver.execute_script(js)
            if hint == '请正确填写车牌号' and hinttishi == "请正确填写车牌号":
                logger.info(f'{sys._getframe().f_code.co_name},{hint},继续执行--新增报价车牌号提示正确')
            else:
                logbug.debug(f'{sys._getframe().f_code.co_name},预期结果{hint},实际结果{hinttishi},继续执行--新增报价车牌号提示异常')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},except继续执行--新增报价车牌号提示异常')
        finally:
            sleep(2)
            pass
    #fuchuang_tishi_return
    def fuchuang_tishi_return(self, driver):
        try:
            global hint
            hint = driver.execupt_script(elements['fuchuang_tishi_return'])
            logbug.debug(f'{sys._getframe().f_code.co_name},{hint}继续执行--查看提示信息')
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},{hint}except继续执行--查看提示信息')
        finally:
            sleep(2)
            pass
if __name__ == '__main__':
    unittest.main()
