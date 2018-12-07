# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage


class BaiduSearch(unittest.TestCase):

    @classmethod    #多个用例的时候加此装饰器，防止每个用例都执行一次测试固件
    def setUpClass(cls):
   # def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod    #多个用例的时候加此装饰器，防止每个用例都执行一次测试固件
    def tearDownClass(cls):
   # def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        a=BrowserEngine(cls.driver)
        a.quit_browser()

    def test_baidu_search(self):
        #使用POM方法，将定位和方法分别分装到了 pageobjects.baidu_homepage.py 和framework.base_page.py
        homepage = HomePage(self.driver)
        homepage.type_search('selenium')  # 调用页面对象中的方法
        homepage.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
        time.sleep(2)
        homepage.get_window_img()  # 调用基类截图方法
        try:
            assert 'selenium' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_search2(self):
        homepage = HomePage(self.driver)
        homepage.type_search('python')  # 调用页面对象中的方法
        homepage.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
        time.sleep(2)
        homepage.get_window_img()  # 调用基类截图方法


'''

    def test_baidu_search(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_xpath('//*[@id="su"]').click()
        time.sleep(1)
        try:
            assert 'selenium' in self.driver.title
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

'''





if __name__ == '__main__':
    unittest.main()
