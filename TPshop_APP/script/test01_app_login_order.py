import unittest
from parameterized import parameterized

from TPshop_APP.base import log
from TPshop_APP.page.page_app_login import PageAppLogin
from TPshop_APP.page.page_app_order import PageAppOrder
from TPshop_APP.util import GetDriver, read_json, write_json


class TestAppLoginOrder(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = GetDriver.get_app_driver()
        # 获取PageAppLogin实例
        self.app = PageAppLogin(self.driver)
        # 获取PageAppOrder
        self.order = PageAppOrder(self.driver)

    def tearDown(self) -> None:
        self.driver.quit()

    @parameterized.expand(read_json("app_order.json","order"))
    def test01_login_order(self, search_value, pwd,expect_text):
        try:
            # 调用登录
            self.app.page_app_login()
            # 打印昵称->断言
            nickname = self.app.page_app_get_nickname()
            print("登录账户昵称为：", nickname)
            self.assertEqual(expect_text, nickname)
            # 下订单
            self.order.page_app_order(search_value, pwd)
            # 获取订单编号
            order_on = self.order.page_app_get_order_on()
            print("获取的订单编号为：", order_on)
            # 记录订单编号 --> 发货完成后做断言使用
            write_json(order_on[5:])
            log.info("=======>app下单成功，订单编号为：{}".format(read_json("expect.json", "expect")[0][0]))
        except Exception as e:
            log.error(e)
            # 截图
            self.order.base_get_img()
            # 抛异常
            raise
