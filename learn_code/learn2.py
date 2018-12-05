# coding=utf-8
#导入二次封装的模块

from selenium import webdriver
from baseoperation import Base
from baseoperation import Logger


mylog=Logger(log='my_test_log').getlog()

class Test(object):

    driver=webdriver.Firefox(executable_path='/Users/ph/Documents/geckodriver')
    dr=Base(driver)

    def open_baidu(self):
        self.dr.open_url('https://baidu.com')
        mylog.info('打开百度浏览器')

    def search(self,text):
        self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys(text)
        mylog.info('输入框中输入文本')
        self.driver.find_element_by_xpath('//*[@id="su"]').click()
        mylog.info('点击查找')

    def quit(self):
        self.dr.q()
        mylog.info('退出浏览器')

if __name__=='__main__':
    a = Test()
    a.open_baidu()
    a.search(u'你好')
    a.quit()
