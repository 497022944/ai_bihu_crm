#  coding=utf-8
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
from Private_methods.The_customer_list_test.customer_list_test import customerlist

logger = Log()
#   说的读取配置文件
logbug = LogBug()
class Login(unittest.TestCase):

    @classmethod
    def setUp(self):
        browser = BrowserEngin()
        self.driver = browser.open_browser()
    # 测试车牌号输入框为空
    def test_a_LicenseNo_input_box001(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='')
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='请正确填写车牌号')
        quotation_license.quotation_license_claer(self.driver)

    #  测试车牌号输入框为特殊字符
    def test_a_LicenseNo_input_box002(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='# ')
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='请正确填写车牌号')
        quotation_license.quotation_license_claer(self.driver)

    #  测试车牌号输入框长度为10
    def test_a_LicenseNo_input_box003(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='123456799')
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='请正确填写车牌号')
        quotation_license.quotation_license_claer(self.driver)

    #  测试车牌号输入框为纯字母大写
    def test_a_LicenseNo_input_box004(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='JJJJJJJ')
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='请正确填写车牌号')
        quotation_license.quotation_license_claer(self.driver)

    #  测试车牌号输入框为纯字母小写
    def test_a_LicenseNo_input_box005(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='kkkkkkkk')
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='请正确填写车牌号')
        quotation_license.quotation_license_claer(self.driver)

    #  测试车牌号输入框为字目前后数字组合
    def a_LicenseNo_input_box006(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J5623JJ')
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='请正确填写车牌号')
        quotation_license.quotation_license_claer(self.driver)

    #  测试车牌号输入框为纯数字
    def test_a_LicenseNo_input_box007(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='9875361')
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='请正确填写车牌号')
        quotation_license.quotation_license_claer(self.driver)

    #  车牌号为正确车牌
    def test_a_LicenseNo_input_box008(self):
        BrowserEngins = BrowserEngin()
        new_quotation_case1 = new_quotation_case()
        readagin = BrowserEngins.Read_ini_loading()
        secs = readagin.sections()  #  加载ini值
        licenseNo = readagin.get("LicenseNo", "licenseNo")
        licenseNoh = licenseNo.split(',')
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        for licenseNos in licenseNoh:
            customerlist1 = customerlist
            menu1 = menu()
            menu1.Select_Menu_case(self.driver, '客户列表')
            quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
            quotation_license.quotation_license_input(self.driver, license1=licenseNos)# 缺少清空车牌输入框
            quotation_license.quotation_license_click(self.driver)

    # 选择投保城市车牌号城市名变动
    def test_b_city_name001(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.license_cityCode(self.driver, license_cityCode='南京')
        quotation_license.license_cityCode_ming(self.driver, license_cityCode_ming='苏')
        new_quotation_case1.license_check_hint(self.driver, hint='请正确填写车牌号')
        quotation_license.All_the_tips(self.driver)

    # 测试车主证件号输入空
    def test_c_city_name001(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.Safety_Certificate_Number(self.driver, safety='')
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='请正确填写车牌号')
        quotation_license.All_the_tips(self.driver)

    # 测试车主证件号输入长度20位
    def test_c_city_name002(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.Safety_Certificate_Number(self.driver, safety='12312312311231231231')
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='请正确填写车牌号')
        quotation_license.All_the_tips(self.driver)

    # 测试车主证件号输入特殊字符
    def c_city_name003(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.Safety_Certificate_Number(self.driver, safety='@# ￥%￥# @# ￥……&*%￥……')
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='请正确填写车牌号')
        quotation_license.All_the_tips(self.driver)

    # 测试车主证件号输入字母
    def test_c_city_name004(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.Safety_Certificate_Number(self.driver, safety='ADNGMKSNGBD')
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='请正确填写车牌号')
        quotation_license.All_the_tips(self.driver)

    # 测试车主证件号输入字母数字组合
    def test_c_city_name005(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.Safety_Certificate_Number(self.driver, safety='ADNG23456SNGBD12345')
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='请正确填写车牌号')
        quotation_license.All_the_tips(self.driver)
    # 测试车主证件号输入字母数字空符号组合
    def test_c_city_name006(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.Safety_Certificate_Number(self.driver, safety='ADNG2 3456  D123')
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='请正确填写车牌号')
        quotation_license.All_the_tips(self.driver)

    # 测试上年投保公司全部为空提交
    def test_d_last_year_insurance001(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.Last_year_insurance(self.driver, insurance=" ")
        new_quotation_case1.license_check_hint(self.driver, hint='请正确填写车牌号')
        quotation_license.All_the_tips(self.driver)

    # 测试上年投保公司为字符提交
    def d_last_year_insurance002(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.Last_year_insurance(self.driver, insurance="# ￥@")
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='请正确填写车牌号')
        quotation_license.All_the_tips(self.driver)

    # 测试上年投保公司纯数字提交
    def test_d_last_year_insurance003(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.Last_year_insurance(self.driver, insurance="123456789")
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='请正确填写车牌号')
        quotation_license.All_the_tips(self.driver)

    # 测试上年投保公司纯字母提交
    def test_d_last_year_insurance004(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.Last_year_insurance(self.driver, insurance="ajsdkjsadjkl")
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='请正确填写车牌号')
        quotation_license.All_the_tips(self.driver)

    #  测试上年投保公司字母数字组合提交
    def test_d_last_year_insurance005(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        quotation_license.Last_year_insurance(self.driver, insurance="ajsdkj23456skl")
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='请正确填写车牌号')
        quotation_license.All_the_tips(self.driver)

    #  测试上年投保公司字母数字组合字符提交
    def test_d_last_year_insurance006(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.Last_year_insurance(self.driver, insurance="ajsdkj23# %……56skl")
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='请正确填写车牌号')
        quotation_license.All_the_tips(self.driver)

    #  测试上年投保公司输入正确人保车险
    def test_d_last_year_insurance007(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.Last_year_insurance(self.driver, insurance="人保车险")
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='请正确填写车牌号')
        quotation_license.All_the_tips(self.driver)

    #  测试车架号是否切换正确
    def test_e_vin007(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_table_assert(self.driver)

    # 测试车架号输入为空提示必填
    def test_f_vin_vin001(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="")
        quotation_license.quotation_license_click(self.driver)
        quotation_license.VIN_input_hint(self.driver, hint='车架号必填')

    #  测试车架号输入十位数字提示必填
    def test_f_vin_vin002(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="1234567894")
        quotation_license.quotation_license_click(self.driver)
        quotation_license.VIN_input_hint(self.driver, hint='车架号必填')
        quotation_license.VIN_input_hint_title(self.driver, hint='车架号必填')
        new_quotation_case1.fuchuang_tishi_return(self.driver)

    #  测试车架号输入十位字母提示必填
    def test_f_vin_vin003(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="qweqwertyu")
        quotation_license.quotation_license_click(self.driver)
        quotation_license.VIN_input_hint(self.driver, hint='车架号必填')
        quotation_license.VIN_input_hint_title(self.driver, hint='车架号必填')
        new_quotation_case1.fuchuang_tishi_return(self.driver)


    #  测试车架号输入20位字母提示必填
    def test_f_vin_vin004(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="qweqwertyuqweqwertyu")
        quotation_license.quotation_license_click(self.driver)
        quotation_license.VIN_input_hint(self.driver, hint='车架号必填')
        quotation_license.VIN_input_hint_title(self.driver, hint='车架号必填')

    #  测试车架号输入20位字母数字组合提示必填
    def f_vin_vin005(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="qweqwe1234569513rtyu")
        quotation_license.quotation_license_click(self.driver)
        quotation_license.VIN_input_hint(self.driver, hint='车架号必填')
        quotation_license.VIN_input_hint_title(self.driver, hint='车架号必填')

    #  测试车架号输入20位字母数字组合提示必填
    def test_f_vin_vin006(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="qweqwe1234569513rtyu")
        quotation_license.quotation_license_click(self.driver)
        quotation_license.VIN_input_hint(self.driver, hint='车架号必填')
        quotation_license.VIN_input_hint_title(self.driver, hint='车架号必填')

    #  测试车架号输入17位字母数字组合o开头提示必填
    def test_f_vin_vin007(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="OS5A3ADD7CB152216")
        quotation_license.quotation_license_click(self.driver)
        quotation_license.VIN_input_hint(self.driver, hint='车架号必填')
        quotation_license.VIN_input_hint_title(self.driver, hint='车架号必填')

    #  测试车架号输入17位字母数字组合o开头提示必填
    def test_f_vin_vin008(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="OS5A3ADD7CB152216")
        quotation_license.quotation_license_click(self.driver)
        quotation_license.VIN_input_hint(self.driver, hint='车架号必填')
        quotation_license.VIN_input_hint_title(self.driver, hint='车架号必填')

    #  测试车架号输入17位字母数字组合o开头提示必填
    def test_f_vin_vin009(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="OS5A3ADD7CB152216")
        quotation_license.quotation_license_click(self.driver)
        quotation_license.VIN_input_hint(self.driver, hint='车架号必填')
        quotation_license.VIN_input_hint_title(self.driver, hint='车架号必填')

    #  测试车架号输入17位数字提示必填
    def test_f_vin_vin010(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="13236562398547563")
        quotation_license.quotation_license_click(self.driver)
        quotation_license.VIN_input_hint(self.driver, hint='车架号必填')
        quotation_license.VIN_input_hint_title(self.driver, hint='车架号必填')

    #  测试车架号输入17位数字提示必填
    def test_f_vin_vin011(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="13236562398547563")
        quotation_license.quotation_license_click(self.driver)
        quotation_license.VIN_input_hint(self.driver, hint='车架号必填')
        quotation_license.VIN_input_hint_title(self.driver, hint='车架号必填')

    #  测试车架号输入17位国产正确
    def test_f_vin_vin012(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="LS5A3ADD7CB152216")
        quotation_license.quotation_license_click(self.driver)

    #  测试车架号输入17位进口正确
    def test_f_vin_vin013(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="WS5A3ADD7CB152216")
        quotation_license.quotation_license_click(self.driver)

    #  测试车架号为空发动机号输入空
    def test_j_engine_input001(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="")
        quotation_license.engine_input(self.driver, engine='')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.VIN_input_hint(self.driver, hint='车架号必填')
        quotation_license.VIN_input_hint_title(self.driver, hint='车架号必填')

    #  测试车架号正确发动机号输入空
    def test_j_engine_input002(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="WS5A3ADD7CB152216")
        quotation_license.engine_input(self.driver, engine='')
        quotation_license.quotation_license_click(self.driver)

    #  测试车架号正确发动机号输入1
    def test_j_engine_input003(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="WS5A3ADD7CB152216")
        quotation_license.engine_input(self.driver, engine='1')
        quotation_license.quotation_license_click(self.driver)

    #  测试车架号正确发动机号输入11个0
    def test_j_engine_input004(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="WS5A3ADD7CB152216")
        quotation_license.engine_input(self.driver, engine='0000000000')
        quotation_license.quotation_license_click(self.driver)

    #  测试车架号正确发动机号输入7位数
    def j_engine_input005(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="WS5A3ADD7CB152216")
        quotation_license.engine_input(self.driver, engine='1234567')
        quotation_license.quotation_license_click(self.driver)

    #  测试车架号正确发动机号输入7位数数字字母组合
    def test_j_engine_input006(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="WS5A3ADD7CB152216")
        quotation_license.engine_input(self.driver, engine='1234qwe')
        quotation_license.quotation_license_click(self.driver)

    #  测试车架号正确发动机号输入7位字母
    def j_engine_input007(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="WS5A3ADD7CB152216")
        quotation_license.engine_input(self.driver, engine='qwerett')
        quotation_license.quotation_license_click(self.driver)

    #  测试车架号正确发动机号输入C4KB23238正确
    def test_j_engine_input008(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="WS5A3ADD7CB152216")
        quotation_license.engine_input(self.driver, engine='C4KB23238')
        quotation_license.quotation_license_click(self.driver)

    # 测试车架号上年投保公司全部为空提交
    def h_last_year_insurance_vin001(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.VIN_input(self.driver, vin="WS5A3ADD7CB152216")
        quotation_license.engine_input(self.driver, engine='C4KB23238')
        quotation_license.VIN_Last_year_insurance(self.driver, insurance2=" ")
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='')

    # 测试车架号上年投保公司全部为空提交
    def test_h_last_year_insurance_vin002(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.VIN_input(self.driver, vin="WS5A3ADD7CB152216")
        quotation_license.engine_input(self.driver, engine='C4KB23238')
        quotation_license.VIN_Last_year_insurance(self.driver, insurance2="# ￥@")
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='车架号必填')

    # 测试车架号上年投保公司纯数字提交
    def h_last_year_insurance_vin003(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.VIN_input(self.driver, vin="WS5A3ADD7CB152216")
        quotation_license.engine_input(self.driver, engine='C4KB23238')
        quotation_license.VIN_Last_year_insurance(self.driver, insurance2="12345")
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='车架号必填')

    # 测试车架号上年投保公司纯字母提交
    def test_h_last_year_insurance_vin004(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.VIN_input(self.driver, vin="WS5A3ADD7CB152216")
        quotation_license.engine_input(self.driver, engine='C4KB23238')
        quotation_license.VIN_Last_year_insurance(self.driver, insurance2="ajsdkjsadjkl")
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='车架号必填')

    #  测试车架号上年投保公司字母数字组合提交
    def h_last_year_insurance_vin005(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.VIN_input(self.driver, vin="WS5A3ADD7CB152216")
        quotation_license.engine_input(self.driver, engine='C4KB23238')
        quotation_license.VIN_Last_year_insurance(self.driver, insurance2="ajsdkj23456skl")
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='车架号必填')

    #  测试车架号上年投保公司字母数字组合字符提交
    def test_h_last_year_insurance_vin006(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.VIN_input(self.driver, vin="WS5A3ADD7CB152216")
        quotation_license.engine_input(self.driver, engine='C4KB23238')
        quotation_license.VIN_Last_year_insurance(self.driver, insurance2="ajsdkj23# %……56skl")
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='车架号必填')

    #  测试车架号上年投保公司输入正确人保车险
    def test_h_last_year_insurance_vin007(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.VIN_input(self.driver, vin="WS5A3ADD7CB152216")
        quotation_license.engine_input(self.driver, engine='C4KB23238')
        quotation_license.VIN_Last_year_insurance(self.driver, insurance2="人保车险")
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='车架号必填')

    #  测试车架号投保城市传空
    def test_i_Insured_City_vin001(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.VIN_cityCode(self.driver, vin_cityCode="")
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='车架号必填')

    #  测试车架号投保城市传空
    def test_i_Insured_City_vin002(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.title_VIN_click(self.driver)
        quotation_license.VIN_input(self.driver, vin="WS5A3ADD7CB152216")
        quotation_license.VIN_cityCode(self.driver, vin_cityCode="北京")
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='车架号必填')

    #  测试车架号投保城市传空值
    def test_i_Insured_City_vin003(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.VIN_cityCode(self.driver, vin_cityCode="南京")
        quotation_license.quotation_license_click(self.driver)
        new_quotation_case1.license_check_hint(self.driver, hint='车架号必填')

    # 测试点击下一步跳转选择险种页面是否正确
    def test_ia_page_skipping001(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        url = self.driver.current_url()
        self.assertEqual("http://userssodev.91bihu.me/# /Customer/List?c=1", url, msg="跳转选择险种页面正确")

    # 测试新增报价-输入车牌-下一步-点击客户信息-输入客户名称
    def test_ia_page_skipping002(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_kehuxinxi_kehuxingming(self.driver)

    # 测试新增报价-输入车牌-下一步-点击客户信息-输入电话1
    def test_ia_page_skipping003(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_kehuxinxi_dianhua1(self.driver)

    # 测试新增报价-输入车牌-下一步-点击客户信息-输入电话2
    def test_ia_page_skipping004(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_kehuxinxi_dianhua2(self.driver)

    # 测试新增报价-输入车牌-下一步-点击客户信息-输入类别
    def test_ia_page_skipping005(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_kehuxinxi_leibie(self.driver)# 类别尚未新增

    # 测试新增报价-输入车牌-下一步-点击客户信息-输入地址
    def test_ia_page_skipping006(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_kehuxinxi_dizhi(self.driver)   # 地址尚未新增

    # 测试新增报价-输入车牌-下一步-点击客户信息-输入地址
    def test_ia_page_skipping007(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_kehuxinxi_dizhi(self.driver)   # 地址尚未新增

    # 测试新增报价-输入车牌-下一步-点击客户信息-输入备注1
    def test_ia_page_skipping008(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_kehuxinxi_beizhu1(self.driver)   # 备注尚未新增

    # 测试新增报价-输入车牌-下一步-点击客户信息-输入备注2
    def test_ia_page_skipping009(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_kehuxinxi_beizhu2(self.driver)   # 备注2尚未新增

    # 测试新增报价-输入车牌-下一步-点击客户信息-车牌号
    def test_ia_page_skipping010(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_cheliangxinxi_chepaihao(self.driver)   # 车牌号

    # 测试新增报价-输入车牌-下一步-点击客户信息-车牌号类型
    def test_ia_page_skipping011(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_cheliangxinxi_chepaihaoleixing(self.driver)   # 车牌号类型

    # 测试新增报价-输入车牌-下一步-点击客户信息-车架号
    def test_ia_page_skipping012(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_cheliangxinxi_chejiahao(self.driver)   # 车架号

    # 测试新增报价-输入车牌-下一步-点击客户信息-发动机号
    def test_ia_page_skipping013(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_cheliangxinxi_fadongjihao(self.driver)   # 发动机号

    # 测试新增报价-输入车牌-下一步-点击客户信息-注册日期
    def test_ia_page_skipping014(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_cheliangxinxi_zhuceriqi(self.driver)   # 注册日期

    # 测试新增报价-输入车牌-下一步-点击客户信息-品牌型号
    def test_ia_page_skipping015(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_cheliangxinxi_pinpaixinghao(self.driver)   # 品牌型号

    # 测试新增报价-输入车牌-下一步-点击客户信息-车型
    def test_ia_page_skipping016(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_cheliangxinxi_chexing(self.driver)   # 车型

    # 测试新增报价-输入车牌-下一步-点击客户信息-新车购置价
    def test_ia_page_skipping017(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_cheliangxinxi_xinchegouzhijia(self.driver)   # 新车购置价

    # 测试新增报价-输入车牌-下一步-点击客户信息-座位数
    def test_ia_page_skipping018(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_cheliangxinxi_zuoweishu(self.driver)   # 座位数

    # 测试新增报价-输入车牌-下一步-点击客户信息-排量
    def test_ia_page_skipping019(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_cheliangxinxi_pailiang(self.driver)   # 排量


    # 测试新增报价-输入车牌-下一步-点击客户信息-过户车
    def test_ia_page_skipping020(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_cheliangxinxi_guohuche(self.driver, '否')   # 过户车

    # 测试新增报价-输入车牌-下一步-点击客户信息-贷款车
    def test_ia_page_skipping021(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_cheliangxinxi_daikuanche(self.driver, '否')   # 贷款车

    # 测试新增报价-输入车牌-下一步-点击客户信息-备注信息
    def test_ia_page_skipping022(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_cheliangxinxi_beizhuxinxi(self.driver)   # 备注信息

    # 测试新增报价-输入车牌-下一步-点击客户信息-投保公司
    def test_ia_page_skipping023(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_shangniantoubaoxinxi_toubaogongsi(self.driver)   # 尚未传投保公司

    # 测试新增报价-输入车牌-下一步-点击客户信息-商业到期时间
    def test_ia_page_skipping024(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_shangniantoubaoxinxi_shangyedaoqi(self.driver)   # 尚未传商业到期时间

    # 测试新增报价-输入车牌-下一步-点击客户信息-交强到期时间
    def test_ia_page_skipping025(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_shangniantoubaoxinxi_jiaoqiangdaoqi(self.driver)   # 尚未传交强到期时间

    # 测试新增报价-输入车牌-下一步-点击客户信息-被保险人
    def test_ia_page_skipping026(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_shangniantoubaoxinxi_beibaoxianren(self.driver)   # 尚未传被保险人

    # 测试新增报价-输入车牌-下一步-点击客户信息-身份证
    def test_ia_page_skipping027(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_shangniantoubaoxinxi_zhengjianleixing(self.driver, '身份证')   # 身份证

    # 测试新增报价-输入车牌-下一步-点击客户信息-机构名称
    def test_ia_page_skipping028(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_shangniantoubaoxinxi_jigoumingcheng(self.driver)   # 机构名称

    # 测试新增报价-输入车牌-下一步-点击客户信息-商业险保单号
    def test_ia_page_skipping029(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_shangniantoubaoxinxi_shangyexianbaodanhao(self.driver)   # 商业险保单号

    # 测试新增报价-输入车牌-下一步-点击客户信息-交强保单号
    def test_ia_page_skipping030(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_shangniantoubaoxinxi_jiaoqiangxianbaodanhao(self.driver)   # 交强保单号

    # 测试新增报价-输入车牌-下一步-点击客户信息-设置临时关系人
    def test_ia_page_skipping031(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_guanxirenxinxi_shezhilinshiguanxiren(self.driver)   # 设置临时关系人

    # 测试新增报价-输入车牌-下一步-点击客户信息-被保人信息-公户
    def test_ia_page_skipping032(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_gonghu(self.driver)   # 被保人信息-公户

    # 测试新增报价-输入车牌-下一步-点击客户信息-被保人信息-个人
    def test_ia_page_skipping033(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_geren(self.driver)   # 被保人信息-个人

    #  测试新增报价-输入车牌-下一步-点击客户信息-被保人信息-被保险人姓名

    def test_ia_page_skipping034(self):

        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_beibaoxianrenxingming(self.driver)   # 被保人信息-被保险人姓名

    #  测试新增报价-输入车牌-下一步-点击客户信息-被保人信息-被保人信息-证件类型
    def test_ia_page_skipping035(self):

        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhengjianleixing(self.driver, '组织机构代码证')   # 被保人信息-被保人信息-证件类型

    #  测试新增报价-输入车牌-下一步-点击客户信息-被保人信息-被保人信息-被保人电话
    def test_ia_page_skipping036(self):

        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_beibaoxianrendianhua(self.driver)   # 被保人信息-被保人电话

    #  测试新增报价-输入车牌-下一步-点击客户信息-被保人信息-被保人信息-被保人邮箱
    def test_ia_page_skipping037(self):

        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_beibaoxianrenyouxiang(self.driver)   # 被保人信息-被保人邮箱

    #  测试新增报价-输入车牌-下一步-点击客户信息-被保人信息-被保人信息-被保人住址
    def test_ia_page_skipping038(self):

        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_zhuzhi(self.driver)   # 被保人信息-被保人住址

    #  测试新增报价-输入车牌-下一步-点击客户信息-被保人信息-被保人信息-被保人民族
    def test_ia_page_skipping039(self):

        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_minzu(self.driver)   # 被保人信息-被保人民族

    #  测试新增报价-输入车牌-下一步-点击客户信息-被保人信息-被保人信息-被保人签发机关
    def test_ia_page_skipping040(self):

        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_guanxirenxinxi_beibaoxianrenxinxi_qianfajiguan(self.driver)   # 被保人信息-被保人签发机关

    #  测试新增报价-输入车牌-下一步-点击客户信息-投保人信息-公户
    def test_ia_page_skipping041(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_guanxirenxinxi_toubaorenxinxi_gonghu(self.driver)   # 投保人信息-公户

    #  测试新增报价-输入车牌-下一步-点击客户信息-投保人信息-个人
    def test_ia_page_skipping042(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_guanxirenxinxi_toubaorenxinxi_geren(self.driver)   # 投保人信息-个人

    #  测试新增报价-输入车牌-下一步-点击客户信息-投保人信息-投保人姓名
    def test_ia_page_skipping043(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_guanxirenxinxi_toubaorenxinxi_toubaorenxingming(self.driver)   # 投保人信息-投保人姓名

    #  测试新增报价-输入车牌-下一步-点击客户信息-投保人信息-证件类型
    def test_ia_page_skipping044(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_guanxirenxinxi_toubaorenxinxi_zhengjianleixing(self.driver, '身份证')   # 投保人信息-证件类型

    #  测试新增报价-输入车牌-下一步-点击客户信息-投保人信息-投保人电话
    def test_ia_page_skipping045(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_guanxirenxinxi_toubaorenxinxi_toubaorendianhua(self.driver)   # 投保人信息-投保人电话

    #  测试新增报价-输入车牌-下一步-点击客户信息-投保人信息-投保人邮箱
    def test_ia_page_skipping046(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_guanxirenxinxi_toubaorenxinxi_toubaorenyouxiang(self.driver)   # 投保人信息-投保人邮箱

    #  测试新增报价-输入车牌-下一步-点击客户信息-投保人信息-投保人住址
    def test_ia_page_skipping047(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_guanxirenxinxi_toubaorenxinxi_zhuzhi(self.driver)   # 投保人信息-投保人住址

    #  测试新增报价-输入车牌-下一步-点击客户信息-投保人信息-投保人民族
    def test_ia_page_skipping048(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_guanxirenxinxi_toubaorenxinxi_minzu(self.driver)   # 投保人信息-投保人民族

    #  测试新增报价-输入车牌-下一步-点击客户信息-投保人信息-投保人签发机关
    def test_ia_page_skipping049(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_guanxirenxinxi_toubaorenxinxi_qianfajiguan(self.driver)   # 投保人信息-投保人签发机关

    #  测试新增报价-输入车牌-下一步- 客户详情-关系人信息-车主信息-公户
    def test_ia_page_skipping050(self):
        new_quotation_case1 = new_quotation_case()
        login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
        customerlist1 = customerlist
        menu1 = menu()
        menu1.Select_Menu_case(self.driver, '客户列表')
        quotation_license.kehuxiangqiang_xinzengbaojia(self.driver)
        quotation_license.quotation_license_input(self.driver, license1='J97896')
        quotation_license.quotation_license_click(self.driver)
        quotation_license.All_the_tips(self.driver)
        sleep(30)
        customerlist1.kehuxiangqing_guanxirenxinxi_chezhuxinxi_gonghu(self.driver)   #  客户详情-关系人信息-车主信息-公户





    # 新增报价车牌
    #  def test01(self):
    #      login.login_input(self.driver, user='zdh01', pwd='123456', code='0115')
    # 
    #      # # 调用菜单
    #      # menu1 = menu()
    #      # menu1.Select_Menu_case(self.driver, '新增报价')
    #      # 输入车牌
    #      quotation_license.quotation_license_input(self.driver, license1='96')
    #      sleep(2)
    #      # 调用点击下一步
    #      quotation_license.quotation_license_click(self.driver)
    #      sleep(2)
    #      # 调用提示
    #      new_quotation_case1 = new_quotation_case()
    #      new_quotation_case1.license_check_hint(self.driver, hint='请正确填写车牌号')
    #      sleep(2)
    #      # 点击提示确定按钮
    #      # quotation_license.All_the_tips_click(self.driver)
    #      # 调用车牌号清空
    #      quotation_license.quotation_license_claer(self.driver)
    #      sleep(2)
    #      # 平安证件号
    #      quotation_license.Safety_Certificate_Number(self.driver, safety='123456')
    #      sleep(2)
    #      # 上年投保公司
    #      quotation_license.Last_year_insurance(self.driver, insurance="人保车险")
    #      # 车架title
    #      quotation_license.title_VIN_click(self.driver)
    #      # 车架号
    #      quotation_license.VIN_input(self.driver, vin="12345678978945612")
    #      # 发动机号
    #      quotation_license.engine_input(self.driver, engine='789456')
    #      # 上年投保公式
    #      quotation_license.VIN_Last_year_insurance(self.driver, insurance2='人保车险')
    #      # 投保城市
    #      quotation_license.VIN_cityCode(self.driver, vin_cityCode='北京')
    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()