from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    # 初始化
    def __init__(self, driver):
        self.driver = driver

    # 查找元素方法 (提供：点击、输入、获取文本)使用
    def base_find_element(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击方法
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 输入方法
    def base_input(self, loc, value):
        el = self.base_find_element(loc)
        # 清空
        el.clear()
        # 输入
        el.send_keys(value)

    # 获取文本方法
    def base_get_text(self, loc):
        # 注意：一定要返回元素的文本信息
        return self.base_find_element(loc).text

    # 截图方法
    def base_get_image(self):
        self.driver.get_screenshot_as_file("../iamge/fail.png")

    # 封装判断元素是否存在
    def base_if_exist(self, loc):
        try:
            self.base_find_element(loc, timeout=2)
            # 找到元素  aseertTrue
            return True
        except:
            # 没找到元素
            return False
