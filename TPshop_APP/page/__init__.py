from selenium.webdriver.common.by import By

"""
    一、以下为app登录模块配置信息    
"""
# 我的
app_login_me = By.XPATH, "//*[@text='我的']"
# 登录图片（连接）
app_login_link = By.XPATH, "//*[@resource-id='com.tpshop.malls:id/head_img']"
# 用户名
app_username = By.XPATH, "//*[@resource-id='com.tpshop.malls:id/mobile_et']"
# 密码
app_pwd = By.XPATH, "//*[@resource-id='com.tpshop.malls:id/pwd_et']"
# 协议
app_pro = By.XPATH, "//*[@resource-id='com.tpshop.malls:id/agree_btn']"
# 登录按钮
app_login_btn = By.XPATH, "//*[@resource-id='com.tpshop.malls:id/login_tv']"
# 昵称
app_nickname = By.XPATH, "//*[@resource-id='com.tpshop.malls:id/nick_name_tv']"
"""
    二、以下为app订单模块配置信息
"""
# 首页
app_order_index = By.XPATH, "//*[@text='首页']"
# 搜索框 -1  android.widget.EditText
app_order_search_text1 = By.XPATH, "//*[@class='android.widget.EditText']"
# 搜索框 -2 com.tpshop.malls:id/search_et
app_order_search_text2 = By.XPATH, "//*[@class='android.widget.EditText']"
# 搜索按钮
app_order_search_btn = By.XPATH, "//*[@resource-id='com.tpshop.malls:id/search_btn']"
# 点击第一张图片 com.tpshop.malls:id/product_pic_img
app_order_img = By.XPATH, "//*[@resource-id='com.tpshop.malls:id/product_pic_img']"
# 加入购物车 com.tpshop.malls:id/add_cart_tv
app_order_add_cart = By.XPATH, "//*[@resource-id='com.tpshop.malls:id/add_cart_tv']"
# 确定
app_order_cart_ok = By.XPATH, "//*[@text='确定']"
# 购物车
app_order_cart = By.XPATH, "//*[@text='购物车']"
# 立即购买
app_order_now_purchase = By.XPATH, "//*[@text='立即购买']"
# 提交订单
app_order_submit_order = By.XPATH, "//*[@text='提交订单']"
# 点击立即支付
app_order_now_pay = By.XPATH, "//*[@text='立即支付']"
# 输入支付密码 com.tpshop.malls:id/pwd_et
app_order_pay_pwd = "//*[@resource-id='com.tpshop.malls:id/pwd_et']"
# 确定
app_order_pay_ok = By.XPATH, "//*[@text='确定']"
# 订单编号 com.tpshop.malls:id/pay_trade_no_tv
app_order_no = By.XPATH, "//*[@resource-id='com.tpshop.malls:id/pay_trade_no_tv']"

"""
    三、web后台登录配置信息整理
"""
# 用户名
web_login_username = By.CSS_SELECTOR, "[name='username']"
# 密码
web_login_pwd = By.CSS_SELECTOR, "[name='password']"
# 验证码
web_login_verify = By.CSS_SELECTOR, "[name='vertify']"
# 登录按钮
web_login_submit = By.CSS_SELECTOR, "[name='submit']"
# 昵称
web_login_nickname = By.CSS_SELECTOR, ".bgdopa-t"
"""
    四、web发货配置信息整理
"""
# 订单菜单
web_order = By.XPATH, "//a[text()='订单']"
# 左侧菜单 发货单
web_order_goods = By.XPATH, "//a[text()='发货单']"
# iframe
web_order_iframe = By.CSS_SELECTOR, "#workspace"
# 去发货 //div[text()='202112161517008312']/../..//td[@class='handle']//a[1]
# web_order_go_goods = By.XPATH, "//a[text()='去发货']"
web_order_go_goods = "//div[text()='{}']/../..//td[@class='handle']//a[1]"

# 物流公司
web_order_company = By.CSS_SELECTOR, "[value='YZPY']"
# 配送单号
web_order_order_no = By.CSS_SELECTOR, "#invoice_no"
# 确认发货
web_order_goods_ok = By.CSS_SELECTOR, ".ncap-btn-send"
# 打印配置单
web_order_print_order = By.CSS_SELECTOR, ".fa-print"
# 获取订单编号
web_order_on = By.XPATH, "//div[@id='printDiv']/div[@class='contact-info']/dl[1]/dd[2]"
