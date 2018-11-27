# -*- coding:utf-8 -*-
from selenium import webdriver

class Browser_engine(object):
    def __init__ (self,driver):
        self.driver=driver
    type ='Firefox'

    def get_browser(self):
        if self.type =='IE':
            driver=webdriver.IE()

        elif self.type=='Chrome':
            driver=webdriver.Chrome()

        elif self.type=='Firefox':
            driver=webdriver.Firefox(executable_path='/Users/ph/Documents/geckodriver')

        else:
            driver=webdriver.IE()

        return driver