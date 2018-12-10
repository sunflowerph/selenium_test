# coding=UTF-8
#登录页面元素
from base_operation.base import operation

class Login(operation):
    # 登录输入框
    ele_login = 'xpath=>//*[@id="inputUsername"]'

    # 密码输入框
    ele_password = 'xpath=>//*[@id="inputPassword"]'

    # 登录按钮
    menu = 'xpath=>//*[@id="login_admin"]'


    def login(self,text1,password1):
        self.send_keys(self.ele_login,text1)
        print '输入账号'+text1
        self.send_keys(self.ele_password,password1)
        print '输入密码******'
        self.click_element(self.menu)
        print '登录'


