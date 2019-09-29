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
from Private_methods.The_customer_list_test.customer_list_test import customerlist

logger = Log()
logbug = LogBug()
log_path = os.path.dirname(os.path.abspath('.')) + "\\Element_methods\\requotation_and_addition.json"
element = open(log_path, encoding='utf-8')
elements = json.load(element)

'''报价后验证相关'''


class Quotation_Verification:
    '''详情保险公司切换验证  实例：switch==太平洋（1）或人保\平安（6），首先知道太平洋是否存在，如存在那么找到太平洋元素并且点击'''
    '''保险公司左侧切换'''
    def Division_switch(driver, switch):
        try:
            lengtn = driver.execute_script(elements['详情保险公司切换验证'])
            if lengtn != '':
                pingan = '平安'
                tpy = '太平洋'
                renbao = '人保'
                guoshoucai = '国寿财'
                if switch == 1:
                    for i in range(lengtn):
                        text = driver.execute_script("return $('.sourceIcon.anticon~span').eq(" + str(i) + ").text()")
                        if tpy in text:
                            textclick = driver.execute_script("$('.sourceIcon.anticon~span').eq(" + str(i) + ").click()")
                elif switch == 2:
                    for i in range(lengtn):
                        text = driver.execute_script("return $('.sourceIcon.anticon~span').eq(" + str(i) + ").text()")
                        if pingan in text:
                            textclick = driver.execute_script(
                                "$('.sourceIcon.anticon~span').eq(" + str(i) + ").click()")
                elif switch == 3:
                    for ii in range(lengtn):
                        text = driver.execute_script("return $('.sourceIcon.anticon~span').eq(" + str(ii) + ").text()")
                        if pingan in text or tpy in text:
                            textclick = driver.execute_script(
                                "$('.sourceIcon.anticon~span').eq(" + str(ii) + ").click()")
                elif switch == 4:
                    for i in range(lengtn):
                        text = driver.execute_script("return $('.sourceIcon.anticon~span').eq(" + str(i) + ").text()")
                        if renbao in text:
                            textclick = driver.execute_script(
                                "$('.sourceIcon.anticon~span').eq(" + str(i) + ").click()")
                elif switch == 5:
                    for ii in range(lengtn):
                        text = driver.execute_script("return $('.sourceIcon.anticon~span').eq(" + str(ii) + ").text()")
                        if renbao in text or tpy in text:
                            textclick = driver.execute_script(
                                "$('.sourceIcon.anticon~span').eq(" + str(ii) + ").click()")
                elif switch == 6:
                    for ii in range(lengtn):
                        text = driver.execute_script("return $('.sourceIcon.anticon~span').eq(" + str(ii) + ").text()")
                        if pingan in text or renbao in text:
                            textclick = driver.execute_script(
                                "$('.sourceIcon.anticon~span').eq(" + str(ii) + ").click()")
                elif switch == 7:
                    for ii in range(lengtn):
                        text = driver.execute_script("return $('.sourceIcon.anticon~span').eq(" + str(ii) + ").text()")
                        if pingan in text or renbao in text or tpy in text:
                            textclick = driver.execute_script(
                                "$('.sourceIcon.anticon~span').eq(" + str(ii) + ").click()")
                elif switch == 8:
                    for i in range(lengtn):
                        text = driver.execute_script("return $('.sourceIcon.anticon~span').eq(" + str(i) + ").text()")
                        if guoshoucai in text:
                            textclick = driver.execute_script(
                                "$('.sourceIcon.anticon~span').eq(" + str(i) + ").click()")
                elif switch == 9:
                    for i in range(lengtn):
                        text = driver.execute_script("return $('.sourceIcon.anticon~span').eq(" + str(i) + ").text()")
                        if guoshoucai in text or tpy in text:
                            textclick = driver.execute_script(
                                "$('.sourceIcon.anticon~span').eq(" + str(i) + ").click()")
                elif switch == 10:
                    for i in range(lengtn):
                        text = driver.execute_script("return $('.sourceIcon.anticon~span').eq(" + str(i) + ").text()")
                        if guoshoucai in text or pingan in text:
                            textclick = driver.execute_script(
                                "$('.sourceIcon.anticon~span').eq(" + str(i) + ").click()")
                elif switch == 11:
                    for i in range(lengtn):
                        text = driver.execute_script("return $('.sourceIcon.anticon~span').eq(" + str(i) + ").text()")
                        if guoshoucai in text or pingan in text or tpy in text:
                            textclick = driver.execute_script(
                                "$('.sourceIcon.anticon~span').eq(" + str(i) + ").click()")
                elif switch == 12:
                    for i in range(lengtn):
                        text = driver.execute_script("return $('.sourceIcon.anticon~span').eq(" + str(i) + ").text()")
                        if guoshoucai in text or renbao in text:
                            textclick = driver.execute_script(
                                "$('.sourceIcon.anticon~span').eq(" + str(i) + ").click()")
                elif switch == 13:
                    for i in range(lengtn):
                        text = driver.execute_script("return $('.sourceIcon.anticon~span').eq(" + str(i) + ").text()")
                        if guoshoucai in text or renbao in text or tpy in text:
                            textclick = driver.execute_script(
                                "$('.sourceIcon.anticon~span').eq(" + str(i) + ").click()")
                elif switch == 14:
                    for i in range(lengtn):
                        text = driver.execute_script("return $('.sourceIcon.anticon~span').eq(" + str(i) + ").text()")
                        if guoshoucai in text or renbao in text or pingan in text:
                            textclick = driver.execute_script(
                                "$('.sourceIcon.anticon~span').eq(" + str(i) + ").click()")
                elif switch == 15:
                    for i in range(lengtn):
                        text = driver.execute_script("return $('.sourceIcon.anticon~span').eq(" + str(i) + ").text()")
                        if guoshoucai in text or renbao in text or pingan in text or tpy in text:
                            textclick = driver.execute_script(
                                "$('.sourceIcon.anticon~span').eq(" + str(i) + ").click()")
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
                logger.info(f'请求方法{sys._getframe().f_code.co_name},实际结果:{Left, comparisons}，报价返回车型验证验证通过')
            else:
                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},实际结果:{Left, comparisons}，报价返回车型验证验证通过')
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

    # 选择险种，传值数字字母相加如：车损 ，车损加不计免赔 例如：车损+车损不计免赔
    '''报价选择险种'''
    def selective_insurance(driver, selective):
        try:
            selective1 = selective.split('+')
            for selective2 in selective1:
                if selective2 == '车损':
                    customerlist.kehuxiangqing_baojiaxinxi_chesun(driver, 1, 0)
                elif selective2 == '车损不计免赔':
                    customerlist.kehuxiangqing_baojiaxinxi_chesun(driver, 1, 1)
                elif selective2 == '三者':
                    customerlist.kehuxiangqing_baojiaxinxi_sanzhe(driver, 1, 0, 5)
                elif selective2 == '三者不计免赔':
                    customerlist.kehuxiangqing_baojiaxinxi_sanzhe(driver, 1, 1, 5)
                elif selective2 == '司机':
                    customerlist.kehuxiangqing_baojiaxinxi_siji(driver, 1, 0, 1)
                elif selective2 == '司机不计免赔':
                    customerlist.kehuxiangqing_baojiaxinxi_siji(driver, 1, 1, 1)
                elif selective2 == '乘客':
                    customerlist.kehuxiangqing_baojiaxinxi_chengke(driver, 1, 0, 1)
                elif selective2 == '乘客不计免赔':
                    customerlist.kehuxiangqing_baojiaxinxi_chengke(driver, 1, 1, 1)
                elif selective2 == '盗抢':
                    customerlist.kehuxiangqing_baojiaxinxi_daoqiang(driver, 1, 0)
                elif selective2 == '盗抢不计免赔':
                    customerlist.kehuxiangqing_baojiaxinxi_daoqiang(driver, 1, 1)
                elif selective2 == '划痕':
                    customerlist.kehuxiangqing_baojiaxinxi_huahen(driver, 1, 0, 2000)
                elif selective2 == '划痕不计免赔':
                    customerlist.kehuxiangqing_baojiaxinxi_huahen(driver, 1, 1, 2000)
                elif selective2 == '玻璃国产':
                    customerlist.kehuxiangqing_baojiaxinxi_boli(driver, 1, '国产')
                elif selective2 == '玻璃进口':
                    customerlist.kehuxiangqing_baojiaxinxi_boli(driver, 1, '进口')
                elif selective2 == '自燃':
                    customerlist.kehuxiangqing_baojiaxinxi_ziran(driver, 1, 0)
                elif selective2 == '自燃不计免赔':
                    customerlist.kehuxiangqing_baojiaxinxi_ziran(driver, 1, 1)
                elif selective2 == '涉水':
                    customerlist.kehuxiangqing_baojiaxinxi_sheshui(driver, 1, 0)
                elif selective2 == '涉水不计免赔':
                    customerlist.kehuxiangqing_baojiaxinxi_sheshui(driver, 1, 1)
                elif selective2 == '第三方':
                    customerlist.kehuxiangqing_baojiaxinxi_chesunwufazhaodaodisanfang(driver, 1)
                elif selective2 == '指定修理厂国产':
                    customerlist.kehuxiangqing_baojiaxinxi_zhidingxiulichang(driver, 1, '国产')
                elif selective2 == '指定修理厂进口':
                    customerlist.kehuxiangqing_baojiaxinxi_zhidingxiulichang(driver, 1, '进口')
                elif selective2 == '设备险':
                    customerlist.kehuxiangqing_baojiaxinxi_xinzengshebeisunshi(driver, 1, 0)
                elif selective2 == '设备险不计免赔':
                    customerlist.kehuxiangqing_baojiaxinxi_xinzengshebeisunshi(driver, 1, 1)
                elif selective2 == '节假日':
                    customerlist.kehuxiangqing_baojiaxinxi_sanzexianfujiafadingjiejiarixianefanbei(driver, 1)
                elif selective2 == '修理厂补偿险':
                    customerlist.kehuxiangqing_baojiaxinxi_xiuliqijianfeiyongbuchang(driver, 1, 100, 1)
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name}，报价选择险种代码执行异常')

    # # 详情页险种，勾选了那些险种需要传值，拿值去找对应的值是否存在并且有价钱，（存在通过）总计计算：所有险种价钱相加并等于当前保险公司金额
    '''报价险种单个险种及总金额'''
    def total_sum(driver, sum):
        try:
            sum1 = sum.split('+')
            zhuxian = 'ant-checkbox-wrapper ant-checkbox-wrapper-checked'#主险勾选class
            nozhuxian = 'ant-checkbox-wrapper'#主险未勾选
            bjzhuxian = 'ant-switch ant-switch-checked ant-switch-small'#主险加不计免赔勾选
            guochan = 'ant-select ant-select-focused ant-select-enabled'#国产和进口的校验
            if sum1 == '车辆损失险' or sum1 == '车辆损失险及不计免赔':
                cheshunclass = driver.execute_script(elements['车损-报价返回详情险种信息'])
                if cheshunclass == zhuxian:
                    chesunbaofei = driver.execute_script(elements['车损-报价返回详情险种保费信息'])
                    logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{zhuxian}，实际结果{cheshunclass}，车损保费{chesunbaofei},车损主险验证通过')
                elif cheshunclass == bjzhuxian:
                    bjmchesunbaofei = driver.execute_script(elements['不计免赔车损-报价返回详情险种保费信息'])
                    logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{bjzhuxian}，实际结果{cheshunclass}，车损不计免赔保费{bjmchesunbaofei},车损主险及不计免赔验证通过')
                else:
                    logbug.debug(f'请求方法{sys._getframe().f_code.co_name}，实际结果{cheshunclass}，车损主险及不计免赔验证异常')
            elif sum1 == '	第三者责任险' or sum1 == '第三者责任险及不计免赔':
                sanzheclass = driver.execute_script(elements['三者-报价返回详情险种信息'])
                if sanzheclass == zhuxian:
                    sanzhebaofei = driver.execute_script(elements['三者-报价返回详情险种保费信息'])
                    logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{zhuxian}，实际结果{sanzheclass}，三者保费{sanzhebaofei}.三者主险验证通过')
                elif sanzheclass == bjzhuxian:
                    bjmsanzhebaofei = driver.execute_script(elements['不计免赔三者-报价返回详情险种保费信息'])
                    sanzheclassjine = driver.execute_script(elements['三者金额-报价返回详情险种信息'])
                    logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{bjzhuxian}，金额结果{sanzheclassjine},实际结果{sanzheclass}，三者不计免赔保费{bjmsanzhebaofei},三者主险及不计免赔验证通过')
                else:
                    logbug.debug(f'请求方法{sys._getframe().f_code.co_name}，实际结果{sanzheclass}，三者主险及不计免赔验证异常')
            elif sum1 == '司机座位险' or sum1 == '司机座位险及不计免赔':
                sijiclass = driver.execute_script(elements['司机-报价返回详情险种信息'])
                if sijiclass == zhuxian:
                    sijibaofei = driver.execute_script(elements['司机-报价返回详情险种保费信息'])
                    logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{zhuxian}，实际结果{sijiclass}，司机保费{sijibaofei}，司机主险验证通过')
                elif sijiclass == bjzhuxian:
                    sijiclassjine = driver.execute_script(elements['司机金额-报价返回详情险种信息'])
                    bjmsijibaofei = driver.execute_script(elements['不计免赔司机-报价返回详情险种保费信息'])
                    logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{bjzhuxian}，金额结果{sijiclassjine},实际结果{sijiclass}，司机不计免赔保费{bjmsijibaofei}，司机主险及不计免赔验证通过')
                else:
                    logbug.debug(f'请求方法{sys._getframe().f_code.co_name}，实际结果{sijiclass}，司机主险及不计免赔验证异常')
            elif sum1 == '乘客座位险' or sum1 == '乘客座位险及不计免赔':
                chengkeclass = driver.execute_script(elements['乘客-报价返回详情险种信息'])
                if chengkeclass == zhuxian:
                    chengkeclassjine = driver.execute_script(elements['乘客-报价返回详情险种保费信息'])
                    logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{zhuxian}，实际结果{chengkeclass}，乘客保费{chengkeclassjine}，乘客主险验证通过')
                elif chengkeclass == bjzhuxian:
                    chengkeeclassjine = driver.execute_script(elements['乘客金额-报价返回详情险种信息'])
                    bjmchengkebaofei = driver.execute_script(elements['不计免赔乘客-报价返回详情险种保费信息'])
                    logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果 :{bjzhuxian}，金额结果{chengkeeclassjine},实际结果{chengkeclass}，乘客不计免赔保费{bjmchengkebaofei}，乘客主险及不计免赔验证通过')
                else:
                    logbug.debug(f'请求方法{sys._getframe().f_code.co_name}，实际结果{chengkeclass}，乘客主险及不计免赔验证异常')
            elif sum1 == '盗抢险' or sum1 == '盗抢险及不计免赔':
                daoqiangclass = driver.execute_script(elements['盗抢-报价返回详情险种信息'])
                if daoqiangclass == zhuxian:
                    daoqiangclassjine = driver.execute_script(elements['盗抢-报价返回详情险种保费信息'])
                    logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{zhuxian}，实际结果{daoqiangclass}，盗抢保费{daoqiangclassjine}，盗抢主险验证通过')
                elif daoqiangclass == bjzhuxian:
                    bjmdaoqiangbaofei = driver.execute_script(elements['不计免赔盗抢-报价返回详情险种保费信息'])
                    logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{bjzhuxian}，实际结果{daoqiangclass}，盗抢不计免赔保费{bjmdaoqiangbaofei}，盗抢主险及不计免赔验证通过')
                else:
                    logbug.debug(f'请求方法{sys._getframe().f_code.co_name}，实际结果{daoqiangclass}，盗抢主险及不计免赔验证异常')

            elif sum1 == '划痕险' or sum1 == '划痕险及不计免赔':
                huahenclass = driver.execute_script(elements['划痕-报价返回详情险种信息'])
                if huahenclass == zhuxian:
                    huahenclassjine = driver.execute_script(elements['划痕-报价返回详情险种保费信息'])
                    logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{zhuxian}，实际结果{huahenclass}，划痕保费{huahenclassjine}，划痕主险验证通过')
                elif huahenclass == bjzhuxian:
                    huahenclassjine = driver.execute_script(elements['划痕金额-报价返回详情险种信息'])
                    bjmhuahenbaofei = driver.execute_script(elements['不计免赔划痕-报价返回详情险种保费信息'])
                    logger.info(
                        f'请求方法{sys._getframe().f_code.co_name},预期结果:{bjzhuxian}，金额结果{huahenclassjine},实际结果{huahenclass}，划痕不计免赔保费{bjmhuahenbaofei}，划痕主险及不计免赔验证通过')
                else:
                    logbug.debug(f'请求方法{sys._getframe().f_code.co_name}，实际结果{huahenclass}，划痕主险及不计免赔验证异常')

            elif sum1 == '玻璃单独破碎险' or sum1 == '玻璃单独破碎险国产' or sum1 == '玻璃单独破碎险进口':
                boliclass = driver.execute_script(elements['玻璃-报价返回详情险种信息'])
                if boliclass == zhuxian:
                    boliclassjine = driver.execute_script(elements['玻璃-报价返回详情险种保费信息'])
                    logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{zhuxian}，实际结果{boliclass}，玻璃保费{boliclassjine},玻璃主险验证通过')
                    boliclassguochan = driver.execute_script(elements['玻璃国进-报价返回详情险种信息'])
                    if boliclassguochan == guochan:
                        logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{guochan}，实际结果{boliclassguochan},玻璃主险国产进口验证通过')
                else:
                    logbug.debug(f'请求方法{sys._getframe().f_code.co_name}，实际结果{boliclass}，玻璃主险及不计免赔验证异常')

            elif sum1 == '自燃损失险' or sum1 == '自燃损失险及不计免赔':
                ziranclass = driver.execute_script(elements['自燃-报价返回详情险种信息'])
                if ziranclass == zhuxian:
                    ziranclassjine = driver.execute_script(elements['自燃-报价返回详情险种保费信息'])
                    logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{zhuxian}，实际结果{ziranclass}，自燃保费{ziranclassjine}，自燃主险验证通过')
                elif ziranclass == bjzhuxian:
                    bjmziranbaofei = driver.execute_script(elements['不计免赔自燃-报价返回详情险种保费信息'])
                    logger.info(
                        f'请求方法{sys._getframe().f_code.co_name},预期结果:{bjzhuxian}，实际结果{ziranclass}，自燃不计免赔保费{bjmziranbaofei}，自燃主险及不计免赔验证通过')
                else:
                    logbug.debug(f'请求方法{sys._getframe().f_code.co_name}，实际结果{ziranclass}，自燃主险及不计免赔验证异常')

            elif sum1 == '涉水行驶损失险' or sum1 == '涉水行驶损失险及不计免赔':
                sheshuiclass = driver.execute_script(elements['涉水-报价返回详情险种信息'])
                if sheshuiclass == zhuxian:
                    seshuiclassjine = driver.execute_script(elements['涉水-报价返回详情险种保费信息'])
                    logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{zhuxian}，实际结果{sheshuiclass}，涉水保费{seshuiclassjine}，涉水主险验证通过')
                elif sheshuiclass == bjzhuxian:
                    bjmsheshuibaofei = driver.execute_script(elements['不计免赔涉水-报价返回详情险种保费信息'])
                    logger.info(
                        f'请求方法{sys._getframe().f_code.co_name},预期结果:{bjzhuxian}，实际结果{sheshuiclass}，涉水不计免赔保费{bjmsheshuibaofei}，涉水主险及不计免赔验证通过')
                else:
                    logbug.debug(f'请求方法{sys._getframe().f_code.co_name}，实际结果{sheshuiclass}，涉水主险及不计免赔验证异常')

            elif sum1 == '车损无法找到第三方险':
                disanfangclass = driver.execute_script(elements['涉水-报价返回详情险种信息'])
                if disanfangclass == zhuxian:
                    disanfangclassjine = driver.execute_script(elements['涉水-报价返回详情险种保费信息'])
                    logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{zhuxian}，实际结果{disanfangclass}，第三方保费{disanfangclassjine}，涉水主险验证通过')
                else:
                    logbug.debug(f'请求方法{sys._getframe().f_code.co_name}，实际结果{disanfangclass}，涉水主险及不计免赔验证异常')
            elif sum1 == '指定修理厂' or sum1 == '指定修理厂国产' or sum1 == '指定修理厂进口':
                xiulichangclass = driver.execute_script(elements['指定修理厂-报价返回详情险种信息'])
                if xiulichangclass == zhuxian:
                    boliclassjine = driver.execute_script(elements['指定修理厂-报价返回详情险种保费信息'])
                    logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{zhuxian}，实际结果{xiulichangclass}，指定修理厂保费{boliclassjine},指定修理厂主险验证通过')
                    disanfangclassguochan = driver.execute_script(elements['指定修理厂国进-报价返回详情险种信息'])
                    if disanfangclassguochan == guochan:
                        logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{guochan}，实际结果{disanfangclassguochan},指定修理厂主险国产进口验证通过')
                else:
                    logbug.debug(f'请求方法{sys._getframe().f_code.co_name}，实际结果{xiulichangclass}，指定修理厂主险及不计免赔验证异常')

            elif sum1 == '新增设备损失险' or sum1 == '新增设备损失险及不计免赔':
                shebeiclass = driver.execute_script(elements['设备险-报价返回详情险种信息'])
                if shebeiclass == zhuxian:
                    shebeiclassjine = driver.execute_script(elements['设备险-报价返回详情险种保费信息'])
                    logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{zhuxian}，实际结果{shebeiclass}，设备险保费{shebeiclassjine}，设备险主险验证通过')
                elif shebeiclass == bjzhuxian:
                    bjmsshebeibaofei = driver.execute_script(elements['不计免赔设备险-报价返回详情险种保费信息'])
                    logger.info(
                        f'请求方法{sys._getframe().f_code.co_name},预期结果:{bjzhuxian}，实际结果{shebeiclass}，设备险不计免赔保费{bjmsshebeibaofei}，设备险主险及不计免赔验证通过')
                else:
                    logbug.debug(f'请求方法{sys._getframe().f_code.co_name}，实际结果{shebeiclass}，设备险主险及不计免赔验证异常')
            elif sum1 == '三责险附加法定节假日限额翻倍险':
                sanzhejiejiariclass = driver.execute_script(elements['节假日-报价返回详情险种信息'])
                if sanzhejiejiariclass == zhuxian:
                    disanfangclassjine = driver.execute_script(elements['节假日-报价返回详情险种保费信息'])
                    logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{zhuxian}，实际结果{sanzhejiejiariclass}，三责险附加法定节假日保费{disanfangclassjine}，三责险附加法定节假日主险验证通过')
                else:
                    logbug.debug(f'请求方法{sys._getframe().f_code.co_name}，实际结果{sanzhejiejiariclass}，三责险附加法定节假日主险及不计免赔验证异常')
            elif sum1 == '修理期间费用补偿险':
                xiulichangfeiyongclass = driver.execute_script(elements['修理厂补偿险-报价返回详情险种信息'])
                if xiulichangfeiyongclass == zhuxian:
                    disanfangclassjine = driver.execute_script(elements['修理厂补偿险-报价返回详情险种保费信息'])
                    logger.info(f'请求方法{sys._getframe().f_code.co_name},预期结果:{zhuxian}，实际结果{xiulichangfeiyongclass}，修理厂补偿险保费{disanfangclassjine}，修理厂补偿险主险验证通过')
                else:
                    logbug.debug(f'请求方法{sys._getframe().f_code.co_name}，实际结果{xiulichangfeiyongclass}，修理厂补偿险及不计免赔验证异常')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name}，详情险种验证异常')

    '''报价左侧金额与险种总金额对比'''
    # 只支持单个保险公司进行查询 入值要求（1-太平洋）（2-平安）（4-人保）（8-国寿财）传数字即可
    def left_total_sum(driver, switchtow):
        global listsumnew1
        listsum = []
        listsumnew = 0
        try:
            lengtn = driver.execute_script(elements['详情保险公司切换验证'])
            if lengtn != '':
                pingan = '平安'
                tpy = '太平洋'
                renbao = '人保'
                guoshoucai = '国寿财'
                r = '[, ()]+'  # 英文逗号未添加
                if switchtow == 1:
                    for i in range(len(lengtn)):
                        text = driver.execute_script("return $('.sourceIcon.anticon~span').eq(" + str(i) + ").text()")
                        if tpy in text:
                            textclick = driver.execute_script("$('.sourceIcon.anticon~span').eq(" + str(i) + ").click()")
                            zongjie = driver.execute_script("return $('.sourceIcon.anticon~span~p').eq(" + str(i) + ").text()")  # 找太平洋金额
                            for i in range(0, 30):
                                if i == 2:
                                    sum = driver.execute_script(elements["车损-报价返回详情险种保费信息"]) + driver.execute_script(elements["不计免赔车损-报价返回详情险种保费信息"])
                                    listsum.append(sum)
                                elif i == 3:
                                    sum1 = driver.execute_script(elements["三者-报价返回详情险种保费信息"]) + driver.execute_script(elements["不计免赔三者-报价返回详情险种保费信息"])
                                    listsum.append(sum1)
                                elif i == 4:
                                    sum2 = driver.execute_script(elements["司机-报价返回详情险种保费信息"]) + driver.execute_script(elements["不计免赔司机-报价返回详情险种保费信息"])
                                    listsum.append(sum2)
                                elif i == 5:
                                    sum3 = driver.execute_script(elements["乘客-报价返回详情险种保费信息"]) + driver.execute_script(elements["不计免赔乘客-报价返回详情险种保费信息"])
                                    listsum.append(sum3)
                                elif i == 6:
                                    sum4 = driver.execute_script(elements["盗抢-报价返回详情险种保费信息"]) + driver.execute_script(elements["不计免赔盗抢-报价返回详情险种保费信息"])
                                    listsum.append(sum4)
                                elif i == 7:
                                    sum5 = driver.execute_script(elements["划痕-报价返回详情险种保费信息"]) + driver.execute_script(elements["不计免赔划痕-报价返回详情险种保费信息"])
                                    listsum.append(sum5)
                                elif i == 8:
                                    sum6 = driver.execute_script(elements["玻璃-报价返回详情险种保费信息"])
                                    listsum.append(sum6)
                                elif i == 9:
                                    sum7 = driver.execute_script(elements["自燃-报价返回详情险种保费信息"]) + driver.execute_script(elements["不计免赔自燃-报价返回详情险种保费信息"])
                                    listsum.append(sum7)
                                elif i == 10:
                                    sum8 = driver.execute_script(elements["涉水-报价返回详情险种保费信息"]) + driver.execute_script(elements["不计免赔涉水-报价返回详情险种保费信息"])
                                    listsum.append(sum8)
                                elif i == 11:
                                    sum9 = driver.execute_script(elements["第三方-报价返回详情险种保费信息"])
                                    listsum.append(sum9)
                                elif i == 12:
                                    sum10 = driver.execute_script(elements["指定修理厂-报价返回详情险种保费信息"]) + driver.execute_script(elements["不计免赔划痕-报价返回详情险种保费信息"])
                                    listsum.append(sum10)
                                elif i == 13:
                                    sum11 = driver.execute_script(elements["设备险-报价返回详情险种保费信息"]) + driver.execute_script(elements["不计免赔设备险-报价返回详情险种保费信息"])
                                    listsum.append(sum11)
                                elif i == 14:
                                    sum12 = driver.execute_script(elements["节假日-报价返回详情险种保费信息"])
                                    listsum.append(sum12)
                                elif i == 15:
                                    sum13 = driver.execute_script(elements["修理厂补偿险-报价返回详情险种保费信息"])
                                    listsum.append(sum13)
                            for hei in listsum:
                                line = re.sub(r, '', hei)
                                listsum.remove(hei)
                                listsum.append(line)
                            for heiyes in listsum:
                                heiyesyes = eval(heiyes)
                                listsumnew += heiyesyes
                                listsumnew1 = ("{:.2f}".format(listsumnew))# 保留2位小数四舍五入
                            tpyjine = re.sub(r, '', zongjie)
                            if tpyjine == listsumnew1:
                                logger.info(f'请求方法{sys._getframe().f_code.co_name},太平洋相加总金额:{listsumnew1}，太平洋页面展示总金额{tpyjine}，太平洋页面总金额与险种相加金额验证通过')
                            else:
                                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},太平洋相加总金额:{listsumnew1}，太平洋页面展示总金额{tpyjine}，太平洋页面总金额与险种相加金额验证异常')
                if switchtow == 2:
                    for i in range(lengtn):
                        text = driver.execute_script("return $('.sourceIcon.anticon~span').eq(" + str(i) + ").text()")
                        if pingan in text:
                            textclick = driver.execute_script("$('.sourceIcon.anticon~span').eq(" + str(i) + ").click()")
                            pinganzongjie = driver.execute_script("return $('.sourceIcon.anticon~span~p').eq(" + str(i) + ").text()") # 找平安金额
                            for i in range(0, 30):
                                if i == 2:
                                    sum = driver.execute_script(elements["车损-报价返回详情险种保费信息"])
                                    sums = driver.execute_script(elements["不计免赔车损-报价返回详情险种保费信息"])
                                    listsum.append(sum)
                                    listsum.append(sums)
                                elif i == 3:
                                    sum1 = driver.execute_script(elements["三者-报价返回详情险种保费信息"])
                                    sum1s = driver.execute_script(elements["不计免赔三者-报价返回详情险种保费信息"])
                                    listsum.append(sum1)
                                    listsum.append(sum1s)
                                elif i == 4:
                                    sum2 = driver.execute_script(elements["司机-报价返回详情险种保费信息"])
                                    sum2s = driver.execute_script(elements["不计免赔司机-报价返回详情险种保费信息"])
                                    listsum.append(sum2)
                                    listsum.append(sum2s)
                                elif i == 5:
                                    sum3 = driver.execute_script(elements["乘客-报价返回详情险种保费信息"])
                                    sum3s = driver.execute_script(elements["不计免赔乘客-报价返回详情险种保费信息"])
                                    listsum.append(sum3)
                                    listsum.append(sum3s)
                                elif i == 6:
                                    sum4 = driver.execute_script(elements["盗抢-报价返回详情险种保费信息"])
                                    sum4s = driver.execute_script(elements["不计免赔盗抢-报价返回详情险种保费信息"])
                                    listsum.append(sum4s)
                                    listsum.append(sum4)
                                elif i == 7:
                                    sum5 = driver.execute_script(elements["划痕-报价返回详情险种保费信息"])
                                    sum5s = driver.execute_script(elements["不计免赔划痕-报价返回详情险种保费信息"])
                                    listsum.append(sum5s)
                                    listsum.append(sum5)
                                elif i == 8:
                                    sum6 = driver.execute_script(elements["玻璃-报价返回详情险种保费信息"])
                                    listsum.append(sum6)
                                elif i == 9:
                                    sum7 = driver.execute_script(elements["自燃-报价返回详情险种保费信息"])
                                    sum7s = driver.execute_script(elements["不计免赔自燃-报价返回详情险种保费信息"])
                                    listsum.append(sum7)
                                    listsum.append(sum7s)
                                elif i == 10:
                                    sum8 = driver.execute_script(elements["涉水-报价返回详情险种保费信息"])
                                    sum8s = driver.execute_script(elements["不计免赔涉水-报价返回详情险种保费信息"])
                                    listsum.append(sum8s)
                                    listsum.append(sum8)
                                elif i == 11:
                                    sum9 = driver.execute_script(elements["第三方-报价返回详情险种保费信息"])
                                    listsum.append(sum9)
                                elif i == 12:
                                    sum10 = driver.execute_script(elements["指定修理厂-报价返回详情险种保费信息"])
                                    sum10s = driver.execute_script(elements["不计免赔划痕-报价返回详情险种保费信息"])
                                    listsum.append(sum10)
                                    listsum.append(sum10s)
                                elif i == 13:
                                    sum11 = driver.execute_script(elements["设备险-报价返回详情险种保费信息"])
                                    sum11s = driver.execute_script(elements["不计免赔设备险-报价返回详情险种保费信息"])
                                    listsum.append(sum11s)
                                    listsum.append(sum11)
                                elif i == 14:
                                    sum12 = driver.execute_script(elements["节假日-报价返回详情险种保费信息"])
                                    listsum.append(sum12)
                                elif i == 15:
                                    sum13 = driver.execute_script(elements["修理厂补偿险-报价返回详情险种保费信息"])
                                    listsum.append(sum13)
                            for hei in listsum:
                                line = re.sub(r, '', hei)
                                listsum.remove(hei)
                                listsum.append(line)
                            heiyesnow = list(filter(None, listsum))
                            for heiyes in heiyesnow:
                                heiyesyes = eval(heiyes)
                                listsumnew += heiyesyes
                                listsumnew1 = ("{:.2f}".format(listsumnew))# 保留2位小数四舍五入
                            pajine = re.sub(r, '', pinganzongjie)
                            if pajine == listsumnew1:
                                logger.info(f'请求方法{sys._getframe().f_code.co_name},平安相加总金额:{listsumnew1}，平安页面展示总金额{pajine}，平安页面总金额与险种相加金额验证通过')
                            else:
                                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},平安相加总金额:{listsumnew1}，平安页面展示总金额{pajine}，平安页面总金额与险种相加金额验证异常')
                if switchtow == 4:
                    for i in range(len(lengtn)):
                        text = driver.execute_script("return $('.sourceIcon.anticon~span').eq(" + str(i) + ").text()")
                        if renbao in text:
                            textclick = driver.execute_script("$('.sourceIcon.anticon~span').eq(" + str(i) + ").click()")
                            renbaozongjie = driver.execute_script("return $('.sourceIcon.anticon~span~p').eq(" + str(i) + ").text()") # 找平安金额
                            for i in range(0, 30):
                                if i == 2:
                                    sum = driver.execute_script(elements["车损-报价返回详情险种保费信息"]) + driver.execute_script(elements["不计免赔车损-报价返回详情险种保费信息"])
                                    listsum.append(sum)
                                elif i == 3:
                                    sum1 = driver.execute_script(elements["三者-报价返回详情险种保费信息"]) + driver.execute_script(elements["不计免赔三者-报价返回详情险种保费信息"])
                                    listsum.append(sum1)
                                elif i == 4:
                                    sum2 = driver.execute_script(elements["司机-报价返回详情险种保费信息"]) + driver.execute_script(elements["不计免赔司机-报价返回详情险种保费信息"])
                                    listsum.append(sum2)
                                elif i == 5:
                                    sum3 = driver.execute_script(elements["乘客-报价返回详情险种保费信息"]) + driver.execute_script(elements["不计免赔乘客-报价返回详情险种保费信息"])
                                    listsum.append(sum3)
                                elif i == 6:
                                    sum4 = driver.execute_script(elements["盗抢-报价返回详情险种保费信息"]) + driver.execute_script(elements["不计免赔盗抢-报价返回详情险种保费信息"])
                                    listsum.append(sum4)
                                elif i == 7:
                                    sum5 = driver.execute_script(elements["划痕-报价返回详情险种保费信息"]) + driver.execute_script(elements["不计免赔划痕-报价返回详情险种保费信息"])
                                    listsum.append(sum5)
                                elif i == 8:
                                    sum6 = driver.execute_script(elements["玻璃-报价返回详情险种保费信息"])
                                    listsum.append(sum6)
                                elif i == 9:
                                    sum7 = driver.execute_script(elements["自燃-报价返回详情险种保费信息"]) + driver.execute_script(elements["不计免赔自燃-报价返回详情险种保费信息"])
                                    listsum.append(sum7)
                                elif i == 10:
                                    sum8 = driver.execute_script(elements["涉水-报价返回详情险种保费信息"]) + driver.execute_script(elements["不计免赔涉水-报价返回详情险种保费信息"])
                                    listsum.append(sum8)
                                elif i == 11:
                                    sum9 = driver.execute_script(elements["第三方-报价返回详情险种保费信息"])
                                    listsum.append(sum9)
                                elif i == 12:
                                    sum10 = driver.execute_script(elements["指定修理厂-报价返回详情险种保费信息"]) + driver.execute_script(elements["不计免赔划痕-报价返回详情险种保费信息"])
                                    listsum.append(sum10)
                                elif i == 13:
                                    sum11 = driver.execute_script(elements["设备险-报价返回详情险种保费信息"]) + driver.execute_script(elements["不计免赔设备险-报价返回详情险种保费信息"])
                                    listsum.append(sum11)
                                elif i == 14:
                                    sum12 = driver.execute_script(elements["节假日-报价返回详情险种保费信息"])
                                    listsum.append(sum12)
                                elif i == 15:
                                    sum13 = driver.execute_script(elements["修理厂补偿险-报价返回详情险种保费信息"])
                                    listsum.append(sum13)
                            for hei in listsum:
                                line = re.sub(r, '', hei)
                                listsum.remove(hei)
                                listsum.append(line)
                            for heiyes in listsum:
                                heiyesyes = eval(heiyes)
                                listsumnew += heiyesyes
                                listsumnew1 = ("{:.2f}".format(listsumnew))# 保留2位小数四舍五入
                            rbjine = re.sub(r, '', renbaozongjie)
                            if rbjine == listsumnew1:
                                logger.info(f'请求方法{sys._getframe().f_code.co_name},人保相加总金额:{listsumnew1}，人保页面展示总金额{rbjine}，人保页面总金额与险种相加金额验证通过')
                            else:
                                logbug.debug(
                                    f'请求方法{sys._getframe().f_code.co_name},人保相加总金额:{listsumnew1}，人保页面展示总金额{rbjine}，人保页面总金额与险种相加金额验证异常')
                if switchtow == 8:
                    for i in range(len(lengtn)):
                        text = driver.execute_script("return $('.sourceIcon.anticon~span').eq(" + str(i) + ").text()")
                        if guoshoucai in text:
                            textclick = driver.execute_script("$('.sourceIcon.anticon~span').eq(" + str(i) + ").click()")
                            guoshoucaijie = driver.execute_script("return $('.sourceIcon.anticon~span~p').eq(" + str(i) + ").text()") # 找国寿财金额
                            for i in range(0, 30):
                                if i == 2:
                                    sum = driver.execute_script(elements["车损-报价返回详情险种保费信息"]) + driver.execute_script(elements["不计免赔车损-报价返回详情险种保费信息"])
                                    listsum.append(sum)
                                elif i == 3:
                                    sum1 = driver.execute_script(elements["三者-报价返回详情险种保费信息"]) + driver.execute_script(elements["不计免赔三者-报价返回详情险种保费信息"])
                                    listsum.append(sum1)
                                elif i == 4:
                                    sum2 = driver.execute_script(elements["司机-报价返回详情险种保费信息"]) + driver.execute_script(elements["不计免赔司机-报价返回详情险种保费信息"])
                                    listsum.append(sum2)
                                elif i == 5:
                                    sum3 = driver.execute_script(elements["乘客-报价返回详情险种保费信息"]) + driver.execute_script(elements["不计免赔乘客-报价返回详情险种保费信息"])
                                    listsum.append(sum3)
                                elif i == 6:
                                    sum4 = driver.execute_script(elements["盗抢-报价返回详情险种保费信息"]) + driver.execute_script(elements["不计免赔盗抢-报价返回详情险种保费信息"])
                                    listsum.append(sum4)
                                elif i == 7:
                                    sum5 = driver.execute_script(elements["划痕-报价返回详情险种保费信息"]) + driver.execute_script(elements["不计免赔划痕-报价返回详情险种保费信息"])
                                    listsum.append(sum5)
                                elif i == 8:
                                    sum6 = driver.execute_script(elements["玻璃-报价返回详情险种保费信息"])
                                    listsum.append(sum6)
                                elif i == 9:
                                    sum7 = driver.execute_script(elements["自燃-报价返回详情险种保费信息"]) + driver.execute_script(elements["不计免赔自燃-报价返回详情险种保费信息"])
                                    listsum.append(sum7)
                                elif i == 10:
                                    sum8 = driver.execute_script(elements["涉水-报价返回详情险种保费信息"]) + driver.execute_script(elements["不计免赔涉水-报价返回详情险种保费信息"])
                                    listsum.append(sum8)
                                elif i == 11:
                                    sum9 = driver.execute_script(elements["第三方-报价返回详情险种保费信息"])
                                    listsum.append(sum9)
                                elif i == 12:
                                    sum10 = driver.execute_script(elements["指定修理厂-报价返回详情险种保费信息"]) + driver.execute_script(elements["不计免赔划痕-报价返回详情险种保费信息"])
                                    listsum.append(sum10)
                                elif i == 13:
                                    sum11 = driver.execute_script(elements["设备险-报价返回详情险种保费信息"]) + driver.execute_script(elements["不计免赔设备险-报价返回详情险种保费信息"])
                                    listsum.append(sum11)
                                elif i == 14:
                                    sum12 = driver.execute_script(elements["节假日-报价返回详情险种保费信息"])
                                    listsum.append(sum12)
                                elif i == 15:
                                    sum13 = driver.execute_script(elements["修理厂补偿险-报价返回详情险种保费信息"])
                                    listsum.append(sum13)
                            for hei in listsum:
                                line = re.sub(r, '', hei)
                                listsum.remove(hei)
                                listsum.append(line)
                            for heiyes in listsum:
                                heiyesyes = eval(heiyes)
                                listsumnew += heiyesyes
                                listsumnew1 = ("{:.2f}".format(listsumnew))# 保留2位小数四舍五入
                            gscine = re.sub(r, '', guoshoucaijie)
                            if gscine == listsumnew1:
                                logger.info(f'请求方法{sys._getframe().f_code.co_name},国寿财相加总金额:{listsumnew1}，国寿财页面展示总金额{gscine}，国寿财页面总金额与险种相加金额验证通过')
                            else:
                                logbug.debug(f'请求方法{sys._getframe().f_code.co_name},国寿财相加总金额:{listsumnew1}，国寿财页面展示总金额{gscine}，国寿财页面总金额与险种相加金额验证异常')
        except Exception:
            logbug.debug(f'请求方法{sys._getframe().f_code.co_name}，报价左侧金额与险种总金额对比验证异常')



if __name__ == '__main__':
    unittest.main()
