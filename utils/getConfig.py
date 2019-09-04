# coding=utf-8
import os,subprocess,json

def getElement(file):
    '''
    元素以json数据格式存储，此方法读取文件
    :param file: 数据文件，json格式
    :return: dict
    '''
    if os.path.exists(file):
        try:
            f = open(file, encoding='utf-8')
        except:
            print("打开文件{0}错误".format(file))
            return {}
        try:
            elements = eval(f.read())
            # print(type(Element_methods))
            return elements
        except:
            print("解析文件{0}错误".format(file))
            return {}

    else:
        print("can not find .json file")
        return {}


if __name__ == '__main__':
    log_path = os.path.dirname(os.path.abspath('.')) + "\\Element_methods\login.json"
    element = open(log_path, encoding='utf-8')
    getElement = json.load(element)

