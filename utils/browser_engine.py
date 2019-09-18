# -*- coding: utf-8 -*-
from selenium import webdriver
import configparser
import os
import time
from utils.Log import Log
from configparser import ConfigParser



logger = Log()
class BrowserEngin(object):

    driver_dir = os.path.dirname(os.path.abspath('.'))
    chrome_driver_full_path = driver_dir + '\\tools\chromedriver.exe'
    firefox_driver_full_path = driver_dir + '\\tools\geckodriver.exe'
    def open_browser(self):
# 创建一个引用对�?
        config = ConfigParser()
# 获取配置文件的全路径
        config_full_path = os.path.dirname(os.path.abspath('.')) + "\\configs\config.ini"


# 通过�?read(一个参数是全路�? 方法 ---> 读取�?ini配置文件的内�?
        config.read(config_full_path)
        browser = config.get("browserType","browserName")
        logger.info("You had select %s browser."% browser)
#得到初始化打开的URL页面
        url = config.get("testServer","URL")
        logger.info("The test server url is: %s "% url)

#添加cookie

        # cookie1=config.get("testCookie","Cookie")
        # print(cookie1)
        # print(type(cookie1))
        # logger.info("The test server url is: %s "% cookie1)
        if browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_driver_full_path)
            logger.info("Starting Chrome browser.")
        elif browser == "FireFox":
            profile = webdriver.FirefoxProfile(self.firefox_driver_full_path)
            driver = webdriver.Firefox(profile)
            logger.info("Starting  Firefox browser.")
        elif browser == "IE":
            driver=webdriver.Edge("...没有 IE=Edge 驱动文件...")
            logger.info("No IE driver.")

        driver.get(url)
        logger.info("open url %s" % url)
        # driver.add_cookie({'name': 'pgv_pvi', 'value': '1115555840'})
        # driver.add_cookie({'name': 'ASP.NET_SessionId', 'value': 'o5fwpaswot342jdd34ymbikr'})
        logger.info("open cookie")
        driver.refresh()
        driver.maximize_window()
        logger.info("Maximize the current window.")
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds.")
        return driver



    def quit_browser(self):
        logger.info("Now,Close and quit the browser.")
        self.driver.quit()

    def Read_ini_loading(self):
        root_dir = os.path.dirname(os.path.abspath('.'))  # 获取当前文件所在目录的上一级目录，即项目所在目录E:\Crawler
        cf = configparser.ConfigParser()
        cf.read(root_dir+"/Configs/config.ini", encoding='utf-8-sig')  # 拼接得到config.ini文件的路径，直接使用
        return cf