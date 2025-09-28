from selenium import webdriver

from TPshop_Login_UnitTesting import page


class GetDriver:
    # 设置类属性
    driver = None

    # 获取driver
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            # 实例化浏览器
            cls.driver = webdriver.Edge()
            # 最大化
            cls.driver.maximize_window()
            # 打开浏览器
            cls.driver.get(page.url)
        return cls.driver

    # 退出driver
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None
