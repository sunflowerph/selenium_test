# coding=utf-8
#基础操作

class Base(object):
    def __init__(self,driver):
        self.driver=driver

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def open_url(self,url):
        self.driver.get(url)

    def q(self):
        self.driver.quit()

