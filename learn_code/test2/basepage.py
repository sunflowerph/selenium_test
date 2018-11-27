# -*- coding:utf-8 -*-

class Basepage(object):
    def __init__(self,driver):
        self.driver=driver

    def quit_browser(self):
        self.driver.quit()
        #退出浏览器

    def open_url(self,url):
        self.driver.get(url)
        #打开一个链接


