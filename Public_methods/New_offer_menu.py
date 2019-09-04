import unittest,os,json
from utils.Logbug import LogBug
from utils.Log import Log
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Public_methods.PublicMethod import BasePage
logger = Log()
logbug = LogBug()
log_path = os.path.dirname(os.path.abspath('.')) + "\\Element_methods\menu.json"
element = open(log_path, encoding='utf-8')
elements = json.load(element)

#菜单
class menu:
    #新增报价菜单

    def quotation_Menu_case(self, driver):
        #driver = webdriver.Chrome()

        #选择菜单
        try:
            global xinzengbaojia
            xinzengbaojia = BasePage.isElementExistlinktext(driver, '新增报价')
            if xinzengbaojia == True:
                logger.info("新增报价菜单已选中，选中状态为:{}".format(xinzengbaojia))
            else:
                xinzengbaojia = driver.find_element_by_class_name(".ant-menu-submenu-selecte").click()
                xinzengbaojia = driver.find_element_by_link_text("新增报价").click()
                logger.info("新增报价菜单未选中已重新选择，选中状态为:{}".format(xinzengbaojia))
        except Exception:
            logbug.debug("新增报价菜单已选中，选中状态为:{}".format(xinzengbaojia))
        finally:
            pass



if __name__ == '__main__':
    unittest.main()
