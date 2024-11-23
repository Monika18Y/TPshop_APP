import os, json

from appium.options.android import UiAutomator2Options
from selenium import webdriver
import appium.webdriver
import logging.handlers

from TPshop_APP.config import HOST, DIR_PATH


class GetDriver:
    __app_driver = None
    __web_driver = None

    # 获取App Driver
    @classmethod
    def get_app_driver(cls):
        if cls.__app_driver is None:
            # 设置启动
            desired_caps = {}
            # 必填-且正确
            desired_caps['platformName'] = 'Android'
            # 必填-且正确
            desired_caps['platformVersion'] = '6.0.1'
            # 必填
            desired_caps['deviceName'] = '192.168.56.101:5555'
            # APP包名 com.tpshop.malls/.SPMainActivity
            desired_caps['appPackage'] = "com.tpshop.malls"
            # 启动名
            desired_caps['appActivity'] = ".SPMainActivity"
            # 设置中文
            desired_caps['unicodeKeyboard'] = True
            desired_caps['resetKeyboard'] = True
            # 设置driver
            cls.__app_driver = webdriver.Remote('http://localhost:4723', options=UiAutomator2Options().load_capabilities(desired_caps))
        return cls.__app_driver

    # 获取Web Driver
    @classmethod
    def get_web_driver(cls):
        if cls.__web_driver is None:
            cls.driver = webdriver.Edge()
            cls.driver.get(HOST)
            cls.driver.maximize_window()
        return cls.driver


# 读取json工具
def read_json(filename, key):
    file_path = DIR_PATH + os.sep + "data" + os.sep + filename
    arrs = []
    with open(file_path, "r", encoding="utf-8")as f:
        for data in json.load(f).get(key):
            arrs.append(tuple(data.values())[1:])
        return arrs


def write_json(value):
    file_path = DIR_PATH + os.sep + "data" + os.sep + "expect.json"
    with open(file_path, "w", encoding="utf-8")as f:
        data = {"expect": [{"desc": "app订单编号", "order_no": value}]}
        json.dump(data, f)


# 日志封装
class GetLog:
    __log = None

    @classmethod
    def get_log(cls):
        if cls.__log is None:
            # 获取日志器
            cls.__log = logging.getLogger()
            # 设置入口级别
            cls.__log.setLevel(logging.INFO)
            # 获取处理器
            filename = DIR_PATH + os.sep + "log" + os.sep + "tpshop_auto.log"
            tf = logging.handlers.TimedRotatingFileHandler(filename=filename,
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding="utf-8")
            # 获取格式器
            fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
            fm = logging.Formatter(fmt)
            # 将格式器添加到处理器
            tf.setFormatter(fm)
            # 将处理器添加到日志器
            cls.__log.addHandler(tf)
        # 返回日志器
        return cls.__log


if __name__ == '__main__':
    # 预期：[(),()]
    GetLog.get_log().info("日志测试")
    write_json("202112312300001")
    print(read_json("expect.json", "expect")[0][0])
