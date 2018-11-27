# -*- coding:utf-8 -*-

import time
from selenium import webdriver
from test2.basepage import Basepage

class Baidu_search(object):
    dr=webdriver.Firefox(executable_path='/Users/ph/Documents/geckodriver')
    basepage=Basepage(dr)

    def open_url(self):
        self.basepage.open_url('https://www.baidu.com')
        time.sleep(3)
        #打开百度浏览器
    def sure_text(self):
        self.dr.find_element_by_xpath('//*[@id="kw"]').send_keys('selenium')
        self.dr.find_element_by_xpath('//*[@id="su"]').click()
        print self.dr.title
        try:
            assert 'selenium' in self.dr.title
            print ('Test pass.')

        except Exception as e:
            print ('Test fail.')


        self.basepage.quit_browser()

        

baidu=Baidu_search()
baidu.open_url()
baidu.sure_text()
