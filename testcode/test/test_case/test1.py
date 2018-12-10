#coding=utf-8


from PageElement.HomePage import Home_page
from PageElement.LoginPage import Login
import unittest
import time


class Order_process(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        a=Home_page()
        a.open_url('https://qiubo-dev.dongpinbang.com:61511/login')

    @classmethod
    def tearDownClass(cls):
        a = Home_page()
        a.quit()


    def test_login(self):
        b=Login()
        b.login('17301691832','123456')
        time.sleep(3)
        try:
            assert u'开发-白沙洲在线管理系统' == b.get_title()
            print '登录成功'
        except:
            print '登录失败'

    def test_order(self):
        a=Home_page()
        a.order_process()



if __name__ =="__main__":
    unittest.main()
