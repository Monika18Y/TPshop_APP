from TPshop_Login_UnitTesting import page
from TPshop_Login_UnitTesting.base.base import Base


class PageLogin(Base):
    # 点击登录链接
    def page_click_login_link(self):
        self.base_click(page.login_link)

    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.login_username, username)

    # 输入密码
    def page_input_password(self, pwd):
        self.base_input(page.login_pwd, pwd)

    # 输入验证
    def page_input_verify_code(self, code):
        self.base_input(page.login_verify_code, code)

    # 点击登录按钮
    def page_click_login_btn(self):
        self.base_click(page.login_btn)

    # 获取异常提示信息
    def page_get_error_info(self):
        return self.base_get_text(page.login_err_info)

    # 点击异常信息框 确定
    def page_click_err_btn_ok(self):
        self.base_click(page.login_err_btn_ok)

    # 截图
    def page_get_img(self):
        self.base_get_image()

    # 点击 安全退出 --》退出使用
    def page_click_logout(self):
        self.base_click(page.login_logout)

    # 判断是否登录成功
    def page_is_login_success(self):
        return self.base_if_exist(page.login_logout)

    # 判断是否退出成功
    def page_is_logout_success(self):
        return self.base_if_exist(page.login_link)

    # 组合业务方法
    def page_login(self, username, pwd, code):
        self.page_input_username(username)
        self.page_input_password(pwd)
        self.page_input_verify_code(code)
        self.page_click_login_btn()