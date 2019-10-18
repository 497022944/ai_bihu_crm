import os,time,re
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from time import sleep


#浏览器选择方法
class BasePage(object):
    def __init__(self, driver):

        "一个构造函数，param参数driver"

        self.driver = driver
    # def Browser(self, driver):
    #     self.driver = driver
    #
    # def get_browser(self):
    #     """
    #     通过if语句，来控制初始化不同浏览器的启动，默认是启动Chrome
    #     :return: driver
    #     """
    #     if self.driver == 'Firefox':
    #         driver = webdriver.Firefox()
    #     elif self.driver == 'Chrome':
    #         driver = webdriver.Chrome()
    #     elif self.driver == 'IE':
    #         driver = webdriver.Ie()
    #     else:
    #         driver = webdriver.Chrome()
    #     driver.maximize_window()
    #     driver.implicitly_wait(10)
    #     return driver
    @staticmethod
#Toast方法判断耗时3秒最大化，寻找页面存在元素 XPATH
    def Toast(self,driver,text,timeout=2,poll_frequency=0.1,waitTimes=3):
        try:
            toast_loc = ("xpath", ".//*[contains(text(),'%s')]" % text)
            for t in range(waitTimes-1):
                t1 = WebDriverWait(driver, timeout, poll_frequency).until(expected_conditions.presence_of_element_located(toast_loc))
                if t1.is_displayed():
                    return True
                else:
                    sleep(0.2)
        except:
            return False
    @staticmethod
#Toast方法判断耗时3秒最大化，寻找页面存在元素 ID
    def ToastId(self,driver,text,timeout=2,poll_frequency=0.1,waitTimes=3):
        try:
            toast_loc = ("id", "id" % text)
            for t in range(waitTimes-1):
                t1 = WebDriverWait(driver, timeout, poll_frequency).until(expected_conditions.presence_of_element_located(toast_loc))
                if t1.is_displayed():
                    return True
                else:
                    sleep(0.2)
        except:
            return False
    @staticmethod
#Toast方法判断耗时3秒最大化，寻找页面存在元素 classname
    def ToastClassname(self,driver,text,timeout=2,poll_frequency=0.1,waitTimes=3):
        try:
            toast_loc = ("class_name", "class_name" % text)
            for t in range(waitTimes-1):
                t1 = WebDriverWait(driver, timeout, poll_frequency).until(expected_conditions.presence_of_element_located(toast_loc))
                if t1.is_displayed():
                    return True
                else:
                    sleep(0.2)
        except:
            return False
    @staticmethod
#Toast方法判断耗时3秒最大化，寻找页面存在元素 name
    def ToastName(self,driver,text,timeout=2,poll_frequency=0.1,waitTimes=3):
        try:
            toast_loc = ("name", "name" % text)
            for t in range(waitTimes-1):
                t1 = WebDriverWait(driver, timeout, poll_frequency).until(expected_conditions.presence_of_element_located(toast_loc))
                if t1.is_displayed():
                    return True
                else:
                    sleep(0.2)
        except:
            return False
    @staticmethod
#Toast方法判断耗时3秒最大化，寻找页面存在元素 Css
    def ToastCss(self,driver,text,timeout=2,poll_frequency=0.1,waitTimes=3):
        try:
            toast_loc = ("css_selector", "css_selector" % text)
            for t in range(waitTimes-1):
                t1 = WebDriverWait(driver, timeout, poll_frequency).until(expected_conditions.presence_of_element_located(toast_loc))
                if t1.is_displayed():
                    return True
                else:
                    sleep(0.2)
        except:
            return False
    @staticmethod
    def Toastxpath(driver,text,timeout=1,poll_frequency=0.1,waitTimes=2):
        try:
            toast_loc = ("xpath", ".//*[contains(text(),'%s')]" % text)
            for t in range(waitTimes-1):
                t1 = WebDriverWait(driver, timeout, poll_frequency).until(expected_conditions.presence_of_element_located(toast_loc))
                if t1.is_displayed():
                    return True
                else:
                    sleep(0.2)
        except:
            return False
#判断try中内容是否存在，true或false
    @staticmethod#静态方法
    #css
    def isElementExistcss(driver, element):
        flag = True
        try:
            driver.find_element_by_css_selector(element)
            return flag
        except:
            flag = False
            return flag
    @staticmethod
    #id
    def isElementExistid(driver, element):
        flag = True
        try:
            driver.find_element_by_id(element)
            return flag
        except:
            flag = False
            return flag
    @staticmethod
    #name
    def isElementExistname(driver, element):
        flag = True
        try:
            driver.find_element_by_name(element)
            return flag
        except:
            flag = False
            return flag
    @staticmethod
    #class_name
    def isElementExistclassname(driver, element):
        flag = True
        try:
            driver.find_element_by_class_name(element)
            return flag
        except:
            return False
    #link_text
    @staticmethod
    def isElementExistlinktext(driver, element):
        try:
            driver.find_element_by_link_text(element)
            return True
        except:
            return False
    #创建文件夹用于图片存储
    @staticmethod
    def Cjwenjian():
        directory_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        try:
            File_Path = os.getcwd() + '\\' + directory_time + '\\'
            if not os.path.exists(File_Path):
                os.makedirs(File_Path)
                print("目录新建成功：%s" % File_Path)
            else:
                print("目录已存在！！！")
        except BaseException as msg:
            print("新建目录失败：%s" % msg)

    def is_element_visible(self, element):
        driver = self.driver
        try:
            the_element = EC.visibility_of_element_located(element)
            assert the_element(driver)
            flag = True
        except:
            flag = False
        return flag
    @staticmethod
    def Zhengze(element, strrings,s):
        fo = 1
        f = 2
        try:
            resa = re.findall(element,strrings,s)
            a= str(resa)
            # print(type(a))
            # print(a)
            # print(len(a))
            if a.__str__() == '[]':
                return f
            else:
                return a
        except:
            return f

    @staticmethod
    def element_WebDriverWait(driver, locator):
        '''
        结合WebDriverWait和expected_conditions判断元素是否存在,
        每间隔0.5秒判断一次，30s超时，存在返回True,不存返回False
        :param locator: locator为元组类型，如("id", "yoyo")
        :return: bool值，True or False
        使用方法：locator = (By.ID, 'name')
        is_element_exsist2(self.driver, (By.ID, 'name'))
        '''
        try:
            WebDriverWait(driver, 30, 0.5).until(EC.presence_of_element_located(locator))
            return True
        except:
            return False

    @staticmethod
    def Regular_Designation(driver, element):
        '''
        正则筛选字符串内容去掉符号
        :param driver:
        :param element:
        :return
        '''
        r = '[’!"#$%&\'()*+,-/:;<=>?@[\\]^_`【】{|}~]+'# 英文逗号未添加
        line = re.sub(r, '', element)
        return line

    @staticmethod
    def monishijian(driver, typenew, element, numbers):
        '''
        鼠标模拟事件
        需要值typenew = type
        element
        '''
        try:
            if typenew == 'id':
                elements = driver.find_element_by_id(element)
                webdriver.ActionChains(driver).move_to_element(elements)
                elements.click()
            elif typenew == 'class':
                elements = driver.find_element_by_class_name(element)
                webdriver.ActionChains(driver).move_to_element(elements)
                elements.click()
            elif typenew == 'sclass':
                elements = driver.find_elements_by_class_name(element)[numbers]
                webdriver.ActionChains(driver).move_to_element(elements)
                elements.click()
            elif typenew == 'name':
                elements = driver.find_element_by_name(element)
                webdriver.ActionChains(driver).move_to_element(elements)
                elements.click()
            elif typenew == 'css':
                elements = driver.find_element_by_css_selector(element)
                webdriver.ActionChains(driver).move_to_element(elements)
                elements.click()
            else:
                pass
        except Exception:
            pass









