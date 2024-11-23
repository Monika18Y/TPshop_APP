from time import sleep
from TPshop_APP import page
from TPshop_APP.base.base import Base


class PageAppOrder(Base):
    # 点击首页
    def page_app_click_index(self):
        sleep(1)
        self.base_click(page.app_order_index)

    # 点击搜索框
    def page_app_click_search_text(self):
        sleep(1)
        self.base_click(page.app_order_search_text1)

    # 输入搜索内容
    def page_app_input_search_text(self,value="小米"):
        sleep(1)
        self.base_input(page.app_order_search_text1,value)

    # 点击搜索按钮
    def page_app_click_search_btn(self):
        sleep(1)
        self.base_click(page.app_order_search_btn)

    # 选择商品
    def page_app_select_photo(self):
        sleep(1)
        self.base_click(page.app_order_img)

    # 点击加入购物车
    def page_app_add_cart(self):
        sleep(1)
        self.base_click(page.app_order_add_cart)

    # 点击确定
    def page_app_cart_ok(self):
        sleep(1)
        self.base_click(page.app_order_cart_ok)

    # 点击购物车
    def page_app_click_cart(self):
        sleep(1)
        self.base_click(page.app_order_cart)

    # 点击立即购买
    def page_app_now_purchase(self):
        sleep(1)
        self.base_click(page.app_order_now_purchase)

    # 点击提交订单
    def page_app_click_submit_order(self):
        sleep(1)
        self.base_click(page.app_order_submit_order)

    # 点击 立即支付
    def page_app_click_now_pay(self):
        sleep(1)
        self.base_click(page.app_order_now_pay)

    # 输入 密码
    def page_app_input_pwd(self,pwd="123456"):
        sleep(1)
        self.base_input(page.app_pwd,pwd)

    # 点击确定
    def page_app_click_sure(self):
        sleep(1)
        self.base_click(page.app_order_pay_ok)

    # 获取订单编号
    def page_app_get_order_on(self):
        sleep(2)
        return self.base_get_text(page.app_order_no)

    # 下单业务方法
    def page_app_order(self,search_value="小米", pwd="123456"):
        self.page_app_click_index()
        self.page_app_click_search_text()
        self.page_app_input_search_text(search_value)
        self.page_app_click_search_btn()
        self.page_app_select_photo()
        self.page_app_add_cart()
        self.page_app_cart_ok()
        self.page_app_click_cart()
        self.page_app_now_purchase()
        self.page_app_click_submit_order()
        self.page_app_click_now_pay()
        self.page_app_input_pwd(pwd)
        self.page_app_click_sure()