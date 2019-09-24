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
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '客户列表':
            try:
                driver.get(url + elements["kehuguanli_kehuliebiao_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '摄像头进店':
            try:
                driver.get(url + elements["kehuguanli_shexiangtoujindian_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '批量续保':
            try:
                driver.get(url + elements["kehuguanli_piliangxubao_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '车险订单':
            try:
                driver.get(url + elements["kehuguanli_chexiandingdan_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '非车订单':
            try:
                driver.get(url + elements["kehuguanli_feichedingdan_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '已出保单':
            try:
                driver.get(url + elements["kehuguanli_yichubaodan_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '战败列表':
            try:
                driver.get(url + elements["kehuguanli_zhanbailiebiao_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '回收站':
            try:
                driver.get(url + elements["kehuguanli_huishouzhan_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '组织架构':
            try:
                driver.get(url + elements["zuzhijigou_zuzhijiagou_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '角色权限':
            try:
                driver.get(url + elements["zuzhijigou_juesequanxian_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '用户管理':
            try:
                driver.get(url + elements["zuzhijigou_yonghuguanli_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '单个录入':
            try:
                driver.get(url + elements["taizhangguanli_dangeluru_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '批改车牌':
            try:
                driver.get(url + elements["taizhangguanli_pigaichepai_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '台账列表':
            try:
                driver.get(url + elements["taizhangguanli_taizhangliebiao_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))


        elif select_menu == '批量抓单':
            try:
                driver.get(url + elements["taizhangguanli_piliangzhuadan_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '个人资金列表':
            try:
                driver.get(url + elements["taizhangguanli_gerenzijinliebiao_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '短信群发':
            try:
                driver.get(url + elements["yingxiaoguanli_duanxinqunfa_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '生日短信':
            try:
                driver.get(url + elements["yingxiaoguanli_shengriduanxin_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '短信发送记录':
            try:
                driver.get(url + elements["yingxiaoguanli_duanxinfasongjilu_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '短信充值':
            try:
                driver.get(url + elements["yingxiaoguanli_duanxinchongzhi_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '业务统计':
            try:
                driver.get(url + elements["tongjimokuai_yewutongji_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '客户统计':
            try:
                driver.get(url + elements["tongjimokuai_kehutongji_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '续保统计':
            try:
                driver.get(url + elements["tongjimokuai_xubaotongji_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '工作统计':
            try:
                driver.get(url + elements["tongjimokuai_gongzuotongji_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '流向分析':
            try:
                driver.get(url + elements["tongjimokuai_liuxiangfenxi_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '流量监控':
            try:
                driver.get(url + elements["tongjimokuai_liuliangjiankong_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '进店统计':
            try:
                driver.get(url + elements["tongjimokuai_jindiantongji_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '进店列表':
            try:
                driver.get(url + elements["jindianguanli_jindianliebiao_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '进店历史':
            try:
                driver.get(url + elements["jindianguanli_jindianlishi_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '进店设置':
            try:
                driver.get(url + elements["jindianguanli_jindianshezhi_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '呼叫统计':
            try:
                driver.get(url + elements["hujiaomokuai_hujiaotongji_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '通话记录':
            try:
                driver.get(url + elements["hujiaomokuai_tonghuajilu_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '坐席管理':
            try:
                driver.get(url + elements["hujiaomokuai_zuoxiguanli_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '战败原因设置':
            try:
                driver.get(url + elements["xitongshezhi_zhanbaiyuanyinshezhi_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '客户类别设置':
            try:
                driver.get(url + elements["xitongshezhi_kehuleibieshezhi_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '客户状态设置':
            try:
                driver.get(url + elements["xitongshezhi_kehuzhuangtaishezhi_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '采集设备绑定':
            try:
                driver.get(url + elements["xitongshezhi_caijishebeibangding_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '出单员设置':
            try:
                driver.get(url + elements["xitongshezhi_chudanyuanshezhi_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '报价渠道':
            try:
                driver.get(url + elements["xitongshezhi_baojiaqudao_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '渠道费率设置':
            try:
                driver.get(url + elements["xitongshezhi_qudaofeilvshezhi_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '跟进设置':
            try:
                driver.get(url + elements["xitongshezhi_genjinshezhi_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '客户流转':
            try:
                driver.get(url + elements["xitongshezhi_kehuliuzhuan_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))

        elif select_menu == '帐号设置':
            try:
                driver.get(url + elements["xitongshezhi_zhanghaoshezhi_url"])
                logger.info("{},{}菜单已选中".format(sys._getframe().f_code.co_name,select_menu))
                sleep(2)
            except Exception:
                logbug.debug("{},{}菜单选中错误".format(sys._getframe().f_code.co_name,select_menu))
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
