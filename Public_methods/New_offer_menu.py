import unittest,os,json
from time import sleep
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
from configparser import ConfigParser
config = ConfigParser()
config_full_path = os.path.dirname(os.path.abspath('.')) + "\\configs\config.ini"
config.read(config_full_path)
url = config.get("testServer","URL")


#菜单
class menu:
    #选择菜单

    def Select_Menu_case(self, driver, select_menu):
        #driver = webdriver.Chrome()
        sleep(2)
        #选择菜单
        if select_menu == '新增报价':
            try:
                driver.get(url + elements["kehuguanli_xinzengbaojia_url"])
                logger.info("{}菜单已选中".format(select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{}菜单选中错误".format(select_menu))

        elif select_menu == '客户列表':
            try:
                driver.get(url + elements["kehuguanli_kehuliebiao_url"])
                logger.info("{}菜单已选中".format(select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{}菜单选中错误".format(select_menu))

        elif select_menu == '摄像头进店':
            try:
                driver.get(url + elements["kehuguanli_shexiangtoujindian_url"])
                logger.info("{}菜单已选中".format(select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{}菜单选中错误".format(select_menu))

        elif select_menu == '批量续保':
            try:
                driver.get(url + elements["kehuguanli_piliangxubao_url"])
                logger.info("{}菜单已选中".format(select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{}菜单选中错误".format(select_menu))

        elif select_menu == '车险订单':
            try:
                driver.get(url + elements["kehuguanli_chexiandingdan_url"])
                logger.info("{}菜单已选中".format(select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{}菜单选中错误".format(select_menu))

        elif select_menu == '非车订单':
            try:
                driver.get(url + elements["kehuguanli_feichedingdan_url"])
                logger.info("{}菜单已选中".format(select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{}菜单选中错误".format(select_menu))
        else:
            pass

        # try:
        #     global xinzengbaojia
        #     xinzengbaojia = BasePage.isElementExistlinktext(driver, '新增报价')
        #     if xinzengbaojia == True:
        #         logger.info("新增报价菜单已选中，选中状态为:{}".format(xinzengbaojia))
        #     else:
        #         xinzengbaojia = driver.find_element_by_class_name(".ant-menu-submenu-selecte").click()
        #         xinzengbaojia = driver.find_element_by_link_text("新增报价").click()
        #         logger.info("新增报价菜单未选中已重新选择，选中状态为:{}".format(xinzengbaojia))
        # except Exception:
        #     logbug.debug("新增报价菜单已选中，选中状态为:{}".format(xinzengbaojia))
        # finally:
        #     pass




if __name__ == '__main__':
    unittest.main()
