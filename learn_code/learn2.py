# coding=utf-8
#导入二次封装的模块

from selenium import webdriver
from baseoperation import Base


class Test(object):
    driver=webdriver.Firefox(executable_path='/Users/ph/Documents/geckodriver')
    dr=Base(driver)

    def open_baidu(self):
        self.dr.open_url('https://baidu.com')

    def search(self,text):
        self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys('text')
        self.driver.find_element_by_xpath('//*[@id="su"]').click()

    def quit(self):
        self.dr.q()

if __name__=='__main__':
    a = Test()
    a.open_baidu()
    a.search('你好')
    a.quit()
