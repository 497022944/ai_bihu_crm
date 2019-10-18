import unittest,os,json
from time import sleep
import sys
from utils.Logbug import LogBug
from utils.Log import Log
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Public_methods.PublicMethod import BasePage
from utils.browser_engine import BrowserEngin
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
logger = Log()
logbug = LogBug()
log_path = os.path.dirname(os.path.abspath('.')) + "\\Element_methods\chandao.json"
element = open(log_path, encoding='utf-8')
elements = json.load(element)
from configparser import ConfigParser
config = ConfigParser()
config_full_path = os.path.dirname(os.path.abspath('.')) + "\\configs\config.ini"
config.read(config_full_path)
url = config.get("testServer","ChandaoURL")
driver_dir = os.path.dirname(os.path.abspath('.'))
chrome_driver_full_path = driver_dir + '\\tools\chromedriver.exe'





"""注意"""
"""注意"""
"""注意"""
"""注意"""
"""注意"""
"""注意"""
"""提bug，需要调用3个方法，
1.chandao_login用来登录，
2.chandao_goto_project_bug进入对应项目bug页面，
3.chandao_create_bug提bug
每个方法需要传递的参数，进入对应方法查找
"""



#禅道
class chandao:

    #登录
    def chandao_login(driver, account = elements["禅道登录账号"], password = elements["禅道登录密码"]):
        """禅道登录方法，参数要传用户名和密码，默认为testaccount"""
        # 浏览器开启新窗口
        time.sleep(1)

        # driver = webdriver.Chrome(chrome_driver_full_path)
        js = "window.open('"+ url +"')"
        driver.execute_script(js)
        time.sleep(1)
        windows = driver.window_handles
        driver.switch_to.window(windows[-1])
        #
        # driver.get(url)
        # time.sleep(1)
        # # # 最大化浏览器
        # # driver.maximize_window()
        # time.sleep(1)
        # 输入账号密码，点击登录
        try:
            driver.find_element_by_id(elements["禅道登录页_用户名输入框id"]).send_keys(account)
            time.sleep(1)
            driver.find_element_by_name(elements["禅道登录页_密码输入框name"]).send_keys(password)
            time.sleep(1)
            driver.find_element_by_id(elements["禅道登录页_登录按钮id"]).click()
            time.sleep(5)
            logger.info("{},{}账号已登录".format(sys._getframe().f_code.co_name,account))
        except Exception:
            logbug.debug("{},{}账号登录错误".format(sys._getframe().f_code.co_name,account))

    # 进入对应项目任务页面
    def chandao_goto_project_task(driver, projectid = elements["禅道默认项目id"]):
        """禅道进入对应项目任务方法，参数要传项目id，默认为61（测试项目）"""
        try:
            # windows = driver.window_handles

            # driver.switch_to_window(windows[-2])
            # time.sleep(1)
            project_url = url+ 'project-task-'+str(projectid)+ '.html'
            driver.get(project_url)
            time.sleep(1)
            logger.info("{},{}项目任务页面进入成功".format(sys._getframe().f_code.co_name, projectid))
        except Exception:
            logger.info("{},{}项目任务页面进入失败".format(sys._getframe().f_code.co_name, projectid))

    # 进入对应项目bug页面
    def chandao_goto_project_bug(driver, projectid = elements["禅道默认项目id"]):
        """禅道进入对应项目bug方法，参数要传项目id，默认为61（测试项目）"""
        try:
            # windows = driver.window_handles

            # driver.switch_to_window(windows[-2])
            # time.sleep(1)
            project_url = url+ 'project-bug-'+str(projectid)+ '.html'
            driver.get(project_url)
            time.sleep(1)
            logger.info("{},{}项目进入成功".format(sys._getframe().f_code.co_name, projectid))
        except Exception:
            logger.info("{},{}项目进入失败".format(sys._getframe().f_code.co_name, projectid))

    # 提交bug页面
    def chandao_create_bug(driver, input_biaoti, input_zhipairen, input_yanzhongchengdu = '严重', input_youxianji = '中',input_xiangguanrenwu= '0000'):
        """禅道提交bug方法，需要先调用chandao_goto_project_bug方法，进入对应项目，参数要传"""
        try:
            # driver = webdriver.Chrome(chrome_driver_full_path)

            driver.find_element_by_css_selector(elements["禅道提bug按钮css"]).click()
            time.sleep(1)

            # # 影响版本，选择主干
            # driver.find_element_by_id(elements["禅道提bug页面_影响版本id"]).click()
            # time.sleep(1)
            # driver.find_element_by_css_selector(elements["禅道提bug页面_影响版本_主干_css"]).click()
            # time.sleep(1)
            # # 影响版本，选择主干
            #
            # # 输入bug标题
            # driver.find_element_by_id(elements["禅道提bug页面_标题id"]).send_keys(input_biaoti)
            # time.sleep(1)
            # # 输入bug标题
            #
            # # 输入指派人
            # driver.find_element_by_id(elements["禅道提bug页面_指派人id"]).click()
            # time.sleep(1)
            # driver.find_element_by_css_selector(elements["禅道提bug页面_指派人id_输入css"]).send_keys(input_zhipairen)
            # time.sleep(1)
            # driver.find_element_by_css_selector(elements["禅道提bug页面_指派人id_输入css_搜索结果css"]).click()
            # time.sleep(1)
            # # 输入指派人
            #
            #
            #
            #
            # # 选择严重程度（默认为严重如果输入有误，则均按照‘严重’选择）
            # driver.find_element_by_id(elements["禅道提bug页面_严重程度id"]).click()
            # time.sleep(1)
            # if input_yanzhongchengdu == '严重':
            #     Select(driver.find_element_by_id(elements["禅道提bug页面_严重程度id"])).select_by_value('2')
            # elif input_yanzhongchengdu == '一般':
            #     Select(driver.find_element_by_id(elements["禅道提bug页面_严重程度id"])).select_by_value('3')
            # elif input_yanzhongchengdu == '非常严重':
            #     Select(driver.find_element_by_id(elements["禅道提bug页面_严重程度id"])).select_by_value('1')
            # elif input_yanzhongchengdu == '轻微':
            #     Select(driver.find_element_by_id(elements["禅道提bug页面_严重程度id"])).select_by_value('4')
            # else:
            #     Select(driver.find_element_by_id(elements["禅道提bug页面_严重程度id"])).select_by_value('2')
            # time.sleep(1)
            # # 选择严重程度（默认为‘严重’，如果输入有误，则均按照‘严重’选择）
            #
            # # 选择优先级（默认为‘中’，如果输入有误，则均按照‘中’选择）
            # driver.find_element_by_id(elements["禅道提bug页面_优先级id"]).click()
            # time.sleep(1)
            # if input_youxianji == '中':
            #     Select(driver.find_element_by_id(elements["禅道提bug页面_优先级id"])).select_by_value('2')
            # elif input_youxianji == '高':
            #     Select(driver.find_element_by_id(elements["禅道提bug页面_优先级id"])).select_by_value('1')
            # elif input_youxianji == '低':
            #     Select(driver.find_element_by_id(elements["禅道提bug页面_优先级id"])).select_by_value('3')
            # else:
            #     Select(driver.find_element_by_id(elements["禅道提bug页面_优先级id"])).select_by_value('2')
            # time.sleep(1)
            # # 选择优先级（默认为‘中’，如果输入有误，则均按照‘中’选择）


            # # 输入重现步骤（未完成，无法定位到输入框）
            # driver.find_element_by_css_selector(elements["禅道提bug页面_重现步骤css"]).click()
            # time.sleep(1)
            # driver.find_element_by_xpath(elements["禅道提bug页面_重现步骤_步骤css"]).send_keys('buzhrwerwerwerwerwerwerwerwerwerweou')
            # time.sleep(5)
            # # 输入重现步骤（未完成，无法定位到输入框）



            # 输入相关任务
            #-----------------拖到可见
            target = driver.find_element_by_id(elements["禅道提bug页面_相关任务id"])
            driver.execute_script("arguments[0].scrollIntoView();", target)
            # -----------------拖到可见

            driver.find_element_by_id(elements["禅道提bug页面_相关任务id"]).click()
            time.sleep(1)
            driver.find_element_by_css_selector(elements["禅道提bug页面_相关任务id_输入css"]).send_keys(input_xiangguanrenwu)
            time.sleep(1)
            driver.find_element_by_css_selector(elements["禅道提bug页面_相关任务id_输入css_搜索结果css"]).click()
            time.sleep(1)
            # 输入相关任务




            logger.info("{},{}bug提交成功".format(sys._getframe().f_code.co_name, input_biaoti))
        except Exception:
            logger.info("{},{}bug提交失败".format(sys._getframe().f_code.co_name, input_biaoti))












if __name__ == '__main__':
    unittest.main()
