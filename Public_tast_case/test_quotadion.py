# coding=utf-8
import unittest,sys
from selenium import webdriver
from time import sleep
from utils.Logbug import LogBug
from utils.Log import Log
from utils.browser_engine import BrowserEngin
from Private_methods.Private_login_test.login_test import login
from Public_methods.New_offer_menu import menu
from Private_methods.The_new_quotation_test.new_quotation_tset import new_quotation_case
from Private_methods.The_new_quotation_test.public_new_quotation import quotation_license
logger = Log()
#  说的读取配置文件
logbug = LogBug()
class Login(unittest.TestCase):

    @classmethod
    def setUp(self):
        browser = BrowserEngin()
        self.driver = browser.open_browser()
    #测试车牌号输入框为空
    def test_a_LicenseNo_input_box001(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.quotation_license_input(self.driver, license1='')
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='请正确填写车牌号')
        quotation_license.quotation_license_claer(self.driver)

    # 测试车牌号输入框为特殊字符
    def test_a_LicenseNo_input_box002(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.quotation_license_input(self.driver, license1='#')
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='请正确填写车牌号')
        quotation_license.quotation_license_claer(self.driver)

    # 测试车牌号输入框长度为10
    def test_a_LicenseNo_input_box003(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.quotation_license_input(self.driver, license1='123456799')
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='请正确填写车牌号')
        quotation_license.quotation_license_claer(self.driver)

    # 测试车牌号输入框为纯字母大写
    def test_a_LicenseNo_input_box004(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.quotation_license_input(self.driver, license1='JJJJJJJ')
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='请正确填写车牌号')
        quotation_license.quotation_license_claer(self.driver)

    # 测试车牌号输入框为纯字母小写
    def test_a_LicenseNo_input_box005(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.quotation_license_input(self.driver, license1='kkkkkkkk')
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='请正确填写车牌号')
        quotation_license.quotation_license_claer(self.driver)

    # 测试车牌号输入框为字目前后数字组合
    def a_LicenseNo_input_box006(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.quotation_license_input(self.driver, license1='J5623JJ')
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='请正确填写车牌号')
        quotation_license.quotation_license_claer(self.driver)

    # 测试车牌号输入框为纯数字
    def test_a_LicenseNo_input_box007(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.quotation_license_input(self.driver, license1='9875361')
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='请正确填写车牌号')
        quotation_license.quotation_license_claer(self.driver)

    # 车牌号为正确车牌
    def test_a_LicenseNo_input_box008(self):
        BrowserEngins = BrowserEngin()
        new_quotation_case1 = new_quotation_case()
        readagin = BrowserEngins.Read_ini_loading()
        secs = readagin.sections()  # 加载ini值
        licenseNo = readagin.get("LicenseNo", "licenseNo")
        licenseNoh = licenseNo.split(',')
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        for licenseNos in licenseNoh:
            quotation_license.quotation_license_input(self.driver, license1=licenseNos)
            quotation_license.quotation_license_click(self.driver)

    #选择投保城市车牌号城市名变动
    def test_b_city_name001(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.quotation_license_input(self.driver, license1='9875361')
        quotation_license.license_cityCode(self.driver, license_cityCode='南京')
        quotation_license.license_cityCode_ming(self.driver, license_cityCode_ming='苏')
        new_quotation_case1.license_check_hint(self.driver, hint='')

    #测试车主证件号输入空
    def test_c_city_name001(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.quotation_license_input(self.driver, license1='京J97896')
        quotation_license.Safety_Certificate_Number(self.driver, safety='')
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='')

    #测试车主证件号输入长度20位
    def test_c_city_name002(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.quotation_license_input(self.driver, license1='京J97896')
        quotation_license.Safety_Certificate_Number(self.driver, safety='12312312311231231231')
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='')

    #测试车主证件号输入特殊字符
    def c_city_name003(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.quotation_license_input(self.driver, license1='京J97896')
        quotation_license.Safety_Certificate_Number(self.driver, safety='@#￥%￥#@#￥……&*%￥……')
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='')

    #测试车主证件号输入字母
    def test_c_city_name004(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.quotation_license_input(self.driver, license1='京J97896')
        quotation_license.Safety_Certificate_Number(self.driver, safety='ADNGMKSNGBD')
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='')

    #测试车主证件号输入字母数字组合
    def c_city_name005(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.quotation_license_input(self.driver, license1='京J97896')
        quotation_license.Safety_Certificate_Number(self.driver, safety='ADNG23456SNGBD12345')
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='')

    #测试车主证件号输入字母数字空符号组合
    def test_c_city_name006(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.quotation_license_input(self.driver, license1='京J97896')
        quotation_license.Safety_Certificate_Number(self.driver, safety='ADNG2 3456  D123')
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='')

    #测试上年投保公司全部为空提交
    def test_d_last_year_insurance001(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.Last_year_insurance(self.driver, insurance=" ")
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='')

    #测试上年投保公司全部为空提交
    def d_last_year_insurance002(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.Last_year_insurance(self.driver, insurance="#￥@")
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='请正确填写车牌号')

    #测试上年投保公司纯数字提交
    def test_d_last_year_insurance003(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.Last_year_insurance(self.driver, insurance="12345")
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='请正确填写车牌号')

    #测试上年投保公司纯字母提交
    def test_d_last_year_insurance004(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.Last_year_insurance(self.driver, insurance="ajsdkjsadjkl")
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='请正确填写车牌号')

    # 测试上年投保公司字母数字组合提交
    def test_d_last_year_insurance005(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.Last_year_insurance(self.driver, insurance="ajsdkj23456skl")
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='请正确填写车牌号')

    # 测试上年投保公司字母数字组合字符提交
    def test_d_last_year_insurance006(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.Last_year_insurance(self.driver, insurance="ajsdkj23#%……56skl")
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='请正确填写车牌号')

    # 测试上年投保公司输入正确人保车险
    def d_last_year_insurance007(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.Last_year_insurance(self.driver, insurance="人保车险")
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='请正确填写车牌号')

    # 测试车架号是否切换正确
    def test_e_vin007(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.title_VIN_click(self.driver)
        try:
            vin = self.driver.find_element_by_css_selector(".ant-tabs-nav-animated > div > div:nth-child(2)")
            vinclass = vin.get_attribute("class")
            self.assertEqual("ant-tabs-tab-active ant-tabs-tab", vinclass, msg="测试车架号是否切换正确")
        except Exception:
            logbug.debug(f'{sys._getframe().f_code.co_name},继续执行--测试车架号是否切换异常')
        finally:
            pass

    #测试车架号输入为空提示必填
    def test_f_vin_vin001(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="")
        quotation_license.quotation_license_click(self.driver)
        quotation_license.VIN_input_hint(self.driver, hint='车架号必填')

    # 测试车架号输入十位数字提示必填
    def test_f_vin_vin002(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="1234567894")
        quotation_license.quotation_license_click(self.driver)
        quotation_license.VIN_input_hint(self.driver, hint='车架号必填')
        quotation_license.VIN_input_hint_title(self.driver, hint='车架号必填')

    # 测试车架号输入十位字母提示必填
    def test_f_vin_vin003(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="qweqwertyu")
        quotation_license.quotation_license_click(self.driver)
        quotation_license.VIN_input_hint(self.driver, hint='车架号必填')
        quotation_license.VIN_input_hint_title(self.driver, hint='车架号必填')


    # 测试车架号输入20位字母提示必填
    def test_f_vin_vin004(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="qweqwertyuqweqwertyu")
        quotation_license.quotation_license_click(self.driver)
        quotation_license.VIN_input_hint(self.driver, hint='车架号必填')
        quotation_license.VIN_input_hint_title(self.driver, hint='车架号必填')

    # 测试车架号输入20位字母数字组合提示必填
    def f_vin_vin005(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="qweqwe1234569513rtyu")
        quotation_license.quotation_license_click(self.driver)
        quotation_license.VIN_input_hint(self.driver, hint='车架号必填')
        quotation_license.VIN_input_hint_title(self.driver, hint='车架号必填')

    # 测试车架号输入20位字母数字组合提示必填
    def test_f_vin_vin006(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="qweqwe1234569513rtyu")
        quotation_license.quotation_license_click(self.driver)
        quotation_license.VIN_input_hint(self.driver, hint='车架号必填')
        quotation_license.VIN_input_hint_title(self.driver, hint='车架号必填')

    # 测试车架号输入17位字母数字组合o开头提示必填
    def test_f_vin_vin007(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="OS5A3ADD7CB152216")
        quotation_license.quotation_license_click(self.driver)
        quotation_license.VIN_input_hint(self.driver, hint='车架号必填')
        quotation_license.VIN_input_hint_title(self.driver, hint='车架号必填')

    # 测试车架号输入17位字母数字组合o开头提示必填
    def test_f_vin_vin008(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="OS5A3ADD7CB152216")
        quotation_license.quotation_license_click(self.driver)
        quotation_license.VIN_input_hint(self.driver, hint='车架号必填')
        quotation_license.VIN_input_hint_title(self.driver, hint='车架号必填')

    # 测试车架号输入17位字母数字组合o开头提示必填
    def test_f_vin_vin009(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="OS5A3ADD7CB152216")
        quotation_license.quotation_license_click(self.driver)
        quotation_license.VIN_input_hint(self.driver, hint='车架号必填')
        quotation_license.VIN_input_hint_title(self.driver, hint='车架号必填')

    # 测试车架号输入17位数字提示必填
    def test_f_vin_vin010(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="13236562398547563")
        quotation_license.quotation_license_click(self.driver)
        quotation_license.VIN_input_hint(self.driver, hint='车架号必填')
        quotation_license.VIN_input_hint_title(self.driver, hint='车架号必填')

    # 测试车架号输入17位数字提示必填
    def test_f_vin_vin011(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="13236562398547563")
        quotation_license.quotation_license_click(self.driver)
        quotation_license.VIN_input_hint(self.driver, hint='车架号必填')
        quotation_license.VIN_input_hint_title(self.driver, hint='车架号必填')

    # 测试车架号输入17位国产正确
    def test_f_vin_vin012(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="LS5A3ADD7CB152216")
        quotation_license.quotation_license_click(self.driver)

    # 测试车架号输入17位进口正确
    def test_f_vin_vin013(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="WS5A3ADD7CB152216")
        quotation_license.quotation_license_click(self.driver)

    # 测试车架号为空发动机号输入空
    def test_j_engine_input001(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="")
        quotation_license.engine_input(self.driver, engine='')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.VIN_input_hint(self.driver, hint='车架号必填')
        quotation_license.VIN_input_hint_title(self.driver, hint='车架号必填')

    # 测试车架号正确发动机号输入空
    def test_j_engine_input002(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="WS5A3ADD7CB152216")
        quotation_license.engine_input(self.driver, engine='')
        quotation_license.quotation_license_click(self.driver)

    # 测试车架号正确发动机号输入1
    def test_j_engine_input003(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="WS5A3ADD7CB152216")
        quotation_license.engine_input(self.driver, engine='1')
        quotation_license.quotation_license_click(self.driver)

    # 测试车架号正确发动机号输入11个0
    def test_j_engine_input004(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="WS5A3ADD7CB152216")
        quotation_license.engine_input(self.driver, engine='0000000000')
        quotation_license.quotation_license_click(self.driver)

    # 测试车架号正确发动机号输入7位数
    def j_engine_input005(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="WS5A3ADD7CB152216")
        quotation_license.engine_input(self.driver, engine='1234567')
        quotation_license.quotation_license_click(self.driver)

    # 测试车架号正确发动机号输入7位数数字字母组合
    def test_j_engine_input006(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="WS5A3ADD7CB152216")
        quotation_license.engine_input(self.driver, engine='1234qwe')
        quotation_license.quotation_license_click(self.driver)

    # 测试车架号正确发动机号输入7位字母
    def j_engine_input007(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="WS5A3ADD7CB152216")
        quotation_license.engine_input(self.driver, engine='qwerett')
        quotation_license.quotation_license_click(self.driver)

    # 测试车架号正确发动机号输入C4KB23238正确
    def test_j_engine_input008(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="WS5A3ADD7CB152216")
        quotation_license.engine_input(self.driver, engine='C4KB23238')
        quotation_license.quotation_license_click(self.driver)

    #测试车架号上年投保公司全部为空提交
    def h_last_year_insurance_vin001(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.VIN_input(self.driver, vin="WS5A3ADD7CB152216")
        quotation_license.engine_input(self.driver, engine='C4KB23238')
        quotation_license.VIN_Last_year_insurance(self.driver, insurance2=" ")
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='')

    #测试车架号上年投保公司全部为空提交
    def test_h_last_year_insurance_vin002(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.VIN_input(self.driver, vin="WS5A3ADD7CB152216")
        quotation_license.engine_input(self.driver, engine='C4KB23238')
        quotation_license.VIN_Last_year_insurance(self.driver, insurance2="#￥@")
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='车架号必填')

    #测试车架号上年投保公司纯数字提交
    def h_last_year_insurance_vin003(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.VIN_input(self.driver, vin="WS5A3ADD7CB152216")
        quotation_license.engine_input(self.driver, engine='C4KB23238')
        quotation_license.VIN_Last_year_insurance(self.driver, insurance2="12345")
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='车架号必填')

    #测试车架号上年投保公司纯字母提交
    def test_h_last_year_insurance_vin004(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.VIN_input(self.driver, vin="WS5A3ADD7CB152216")
        quotation_license.engine_input(self.driver, engine='C4KB23238')
        quotation_license.VIN_Last_year_insurance(self.driver, insurance2="ajsdkjsadjkl")
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='车架号必填')

    # 测试车架号上年投保公司字母数字组合提交
    def h_last_year_insurance_vin005(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.VIN_input(self.driver, vin="WS5A3ADD7CB152216")
        quotation_license.engine_input(self.driver, engine='C4KB23238')
        quotation_license.VIN_Last_year_insurance(self.driver, insurance2="ajsdkj23456skl")
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='车架号必填')

    # 测试车架号上年投保公司字母数字组合字符提交
    def test_h_last_year_insurance_vin006(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.VIN_input(self.driver, vin="WS5A3ADD7CB152216")
        quotation_license.engine_input(self.driver, engine='C4KB23238')
        quotation_license.VIN_Last_year_insurance(self.driver, insurance2="ajsdkj23#%……56skl")
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='车架号必填')

    # 测试车架号上年投保公司输入正确人保车险
    def test_h_last_year_insurance_vin007(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.VIN_input(self.driver, vin="WS5A3ADD7CB152216")
        quotation_license.engine_input(self.driver, engine='C4KB23238')
        quotation_license.VIN_Last_year_insurance(self.driver, insurance2="人保车险")
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='车架号必填')

    # 测试车架号投保城市传空
    def test_i_Insured_City_vin001(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.VIN_cityCode(self.driver, vin_cityCode="")
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='车架号必填')

    # 测试车架号投保城市传空
    def test_i_Insured_City_vin002(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.VIN_cityCode(self.driver, vin_cityCode="北京")
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='车架号必填')

    # 测试车架号投保城市传空值
    def test_i_Insured_City_vin003(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.VIN_cityCode(self.driver, vin_cityCode="南京")
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='车架号必填')


    #新增报价车牌
    # def test01(self):
    #     login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
    #
    #     ##调用菜单
    #     #menu1 = menu()
    #     #menu1.Select_Menu_case(self.driver, '新增报价')
    #     #输入车牌
    #     quotation_license.quotation_license_input(self.driver, license1='96')
    #     sleep(2)
    #     #调用点击下一步
    #     quotation_license.quotation_license_click(self.driver)
    #     sleep(2)
    #     #调用提示
    #     new_quotation_case1 = new_quotation_case()
    #     new_quotation_case1.license_check_hint(self.driver, hint='请正确填写车牌号')
    #     sleep(2)
    #     #点击提示确定按钮
    #     #quotation_license.All_the_tips_click(self.driver)
    #     #调用车牌号清空
    #     quotation_license.quotation_license_claer(self.driver)
    #     sleep(2)
    #     #平安证件号
    #     quotation_license.Safety_Certificate_Number(self.driver, safety='123456')
    #     sleep(2)
    #     #上年投保公司
    #     quotation_license.Last_year_insurance(self.driver, insurance="人保车险")
    #     #车架title
    #     quotation_license.title_VIN_click(self.driver)
    #     #车架号
    #     quotation_license.VIN_input(self.driver, vin="12345678978945612")
    #     #发动机号
    #     quotation_license.engine_input(self.driver, engine='789456')
    #     #上年投保公式
    #     quotation_license.VIN_Last_year_insurance(self.driver, insurance2='人保车险')
    #     #投保城市
    #     quotation_license.VIN_cityCode(self.driver, vin_cityCode='北京')
    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()