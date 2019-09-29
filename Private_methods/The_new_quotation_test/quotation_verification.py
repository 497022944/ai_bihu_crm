import unittest, os, json, sys, re
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
log_path = os.path.dirname(os.path.abspath('.')) + "\\Element_methods\\requotation_and_addition.json"
element = open(log_path, encoding='utf-8')
elements = json.load(element)


'''报价后验证相关'''
class Quotation_Verification:

        '''详情保险公司切换验证  实例：switch==太平洋（1）或人保\平安（6），首先知道太平洋是否存在，如存在那么找到太平洋元素并且点击'''
        def Division_switch(driver, switch):
            try:
                lengtn = driver.execute_script(elements['详情保险公司切换验证'])
                if lengtn != '':
                        pingan = '平安'
                        tpy = '太平洋'
                        renbao = '人保'
                        guoshoucai = '国寿财'
                        if switch == 1:
                            for i in range(len(lengtn)):
                                text = driver.execute_script("return $('.sourceIcon.anticon~span').eq(" + str(i) +").text()")
                                if tpy in text:
                                    textclick = driver.execute_script("$('.sourceIcon.anticon~span').eq(" + str(i) + ").click()")
                        elif switch == 2:
                            for i in range(len(lengtn)):
                                text = driver.execute_script("return $('.sourceIcon.anticon~span').eq(" + str(i) +").text()")
                                if pingan in text:
                                    textclick = driver.execute_script("$('.sourceIcon.anticon~span').eq(" + str(i) + ").click()")
                        elif switch == 3:
                            for ii in range(len(lengtn)):
                                text = driver.execute_script("return $('.sourceIcon.anticon~span').eq(" + str(ii) + ").text()")
                                if pingan in text or tpy in text:
                                    textclick = driver.execute_script("$('.sourceIcon.anticon~span').eq(" + str(ii) + ").click()")
                        elif switch == 4:
                            for i in range(len(lengtn)):
                                text = driver.execute_script("return $('.sourceIcon.anticon~span').eq(" + str(i) + ").text()")
                                if renbao in text:
                                    textclick = driver.execute_script("$('.sourceIcon.anticon~span').eq(" + str(i) + ").click()")
                        elif switch == 5:
                            for ii in range(len(lengtn)):
                                text = driver.execute_script("return $('.sourceIcon.anticon~span').eq(" + str(ii) + ").text()")
                                if renbao in text or tpy in text:
                                    textclick = driver.execute_script("$('.sourceIcon.anticon~span').eq(" + str(ii) + ").click()")
                        elif switch == 6:
                            for ii in range(len(lengtn)):
                                text = driver.execute_script("return $('.sourceIcon.anticon~span').eq(" + str(ii) + ").text()")
                                if pingan in text or renbao in text:
                                    textclick = driver.execute_script("$('.sourceIcon.anticon~span').eq(" + str(ii) + ").click()")
                        elif switch == 7:
                            for ii in range(len(lengtn)):
                                text = driver.execute_script("return $('.sourceIcon.anticon~span').eq(" + str(ii) + ").text()")
                                if pingan in text or renbao in text or tpy in text:
                                    textclick = driver.execute_script("$('.sourceIcon.anticon~span').eq(" + str(ii) + ").click()")
                        elif switch == 8:
                            for i in range(len(lengtn)):
                                text = driver.execute_script("return $('.sourceIcon.anticon~span').eq(" + str(i) + ").text()")
                                if guoshoucai in text:
                                    textclick = driver.execute_script("$('.sourceIcon.anticon~span').eq(" + str(i) + ").click()")
                        elif switch == 9:
                            for i in range(len(lengtn)):
                                text = driver.execute_script("return $('.sourceIcon.anticon~span').eq(" + str(i) + ").text()")
                                if guoshoucai in text or tpy in text:
                                    textclick = driver.execute_script("$('.sourceIcon.anticon~span').eq(" + str(i) + ").click()")
                        elif switch == 10:
                            for i in range(len(lengtn)):
                                text = driver.execute_script("return $('.sourceIcon.anticon~span').eq(" + str(i) + ").text()")
                                if guoshoucai in text or pingan in text:
                                    textclick = driver.execute_script("$('.sourceIcon.anticon~span').eq(" + str(i) + ").click()")
                        elif switch == 11:
                            for i in range(len(lengtn)):
                                text = driver.execute_script("return $('.sourceIcon.anticon~span').eq(" + str(i) + ").text()")
                                if guoshoucai in text or pingan in text or tpy in text:
                                    textclick = driver.execute_script("$('.sourceIcon.anticon~span').eq(" + str(i) + ").click()")
                        elif switch == 12:
                            for i in range(len(lengtn)):
                                text = driver.execute_script("return $('.sourceIcon.anticon~span').eq(" + str(i) + ").text()")
                                if guoshoucai in text or renbao in text:
                                    textclick = driver.execute_script("$('.sourceIcon.anticon~span').eq(" + str(i) + ").click()")
                        elif switch == 13:
                            for i in range(len(lengtn)):
                                text = driver.execute_script("return $('.sourceIcon.anticon~span').eq(" + str(i) + ").text()")
                                if guoshoucai in text or renbao in text or tpy in text:
                                    textclick = driver.execute_script("$('.sourceIcon.anticon~span').eq(" + str(i) + ").click()")
                        elif switch == 14:
                            for i in range(len(lengtn)):
                                text = driver.execute_script("return $('.sourceIcon.anticon~span').eq(" + str(i) + ").text()")
                                if guoshoucai in text or renbao in text or pingan in text:
                                    textclick = driver.execute_script("$('.sourceIcon.anticon~span').eq(" + str(i) + ").click()")
                        elif switch == 15:
                            for i in range(len(lengtn)):
                                text = driver.execute_script("return $('.sourceIcon.anticon~span').eq(" + str(i) + ").text()")
                                if guoshoucai in text or renbao in text or pingan in text or tpy in text:
                                    textclick = driver.execute_script("$('.sourceIcon.anticon~span').eq(" + str(i) + ").click()")
                else:
                    logbug.debug(f'请求方法{sys._getframe().f_code.co_name},实际结果:{lengtn}，详情左侧保险公司切换验证代码执行异常')


            except Exception:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name}，详情左侧保险公司切换验证代码执行异常')



        '''车牌号验证'''
        def License_Verification(driver, License):
            try:
                licens = driver.execute_script(elements['报价返回车牌验证'])
                licens_re = BasePage.Regular_Designation(driver, licens)
                if License == licens_re:
                    logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{License},实际结果:{licens_re}，报价返回车牌号验证通过')
                else:
                    logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{License},实际结果:{licens_re}，报价返回车牌号验证失败')
            except Exception:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{License}，车牌号验证代码执行异常')

        '''报价返回车型验证'''
        def Vehicle_type(driver, Vehicle):
            try:
                Vehicles = driver.execute_script(elements['报价返回车型验证'])
                if Vehicle in Vehicles:
                    logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{Vehicle},实际结果:{Vehicles}，报价返回车型验证验证通过')
                else:
                    logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{Vehicle},实际结果:{Vehicles}，报价返回车型验证验证通过')
            except Exception:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},预期结果:{Vehicle}，报价返回车型验证代码执行异常')

        '''报价返回报价状态左侧与详情对比'''
        def Left_comparisons_details(driver):
            try:
                Left = driver.execute_script(elements['报价返回左侧验证'])
                comparisons = driver.execute_script(elements['报价返回详情验证'])
                if Left in comparisons:
                    logger.info(f'请求方法{sys._getframe().f_code.co_name},实际结果:{Left,comparisons}，报价返回车型验证验证通过')
                else:
                    logbug.debug(f'请求方法{sys._getframe().f_code.co_name},实际结果:{Left,comparisons}，报价返回车型验证验证通过')
            except Exception:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name}，报价返回报价状态左侧与详情对比代码执行异常')

        '''报价返回报价内容 成功与失败'''
        def quotation_contents(driver):
            try:
                quotation_contents = driver.execute_script(elements['报价返回报价内容验证'])
                logger.info(f'请求方法{sys._getframe().f_code.co_name},实际结果:{quotation_contents}，报价返回车型验证验证通过')

            except Exception:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name}，报价返回报价状态报价内容 成功与失败代码执行异常')

        '''报价返回详情出险信息'''
        def information(driver):
            try:
                information = driver.execute_script(elements['报价返回详情出险信息'])
                logger.info(f'请求方法{sys._getframe().f_code.co_name},实际结果:{information}，报价返回车型验证验证通过')
            except Exception:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name}，报价返回详情出险信息 成功与失败代码执行异常')

        '''报价返回详情系数信息'''
        def coefficient(driver):
            try:
                coefficient = driver.execute_script(elements['报价返回详情系数信息'])
                logger.info(f'请求方法{sys._getframe().f_code.co_name},实际结果:{coefficient}，报价返回车型验证验证通过')
            except Exception:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name}，报价返回详情出险信息 成功与失败代码执行异常')

        '''报价返回详情核保信息'''
        def underwriting(driver):
            try:
                underwriting = driver.execute_script(elements['报价返回详情核保信息'])
                logger.info(f'请求方法{sys._getframe().f_code.co_name},实际结果:{underwriting}，报价返回车型验证验证通过')
            except Exception:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name}，报价返回详情出险信息 成功与失败代码执行异常')

        '''报价返回详情报价渠道信息'''
        def channel(driver):
            try:
                channel = driver.execute_script(elements['报价返回详情报价渠道信息'])
                logger.info(f'请求方法{sys._getframe().f_code.co_name},实际结果:{channel}，报价返回车型验证验证通过')
            except Exception:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name}，报价返回详情出险信息 成功与失败代码执行异常')

        ''''''



        # # 详情页险种，勾选了那些险种需要传值，拿值去找对应的值是否存在并且有价钱，（存在通过）总计计算：所有险种价钱相加并等于当前保险公司金额
        # '''报价险种单个险种及总金额'''
        # def total_sum(driver, sum):
        #     try:
        #





if __name__ == '__main__':
    unittest.main()
