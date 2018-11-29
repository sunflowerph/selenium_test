# coding:utf-8
from selenium import webdriver
import time
import re


class Login(object):

    def __init__(self,dr,name,password):
        self.dr=dr
        self.name=name
        self.password=password

    def log_in(self):
        #验证登录功能
        self.dr.get('https://qiubo-dev.dongpinbang.com:61021/login')
        time.sleep(3)
        self.dr.find_element_by_xpath\
            ('//*[@id="inputUsername"]').send_keys(self.name)
        self.dr.find_element_by_xpath('//*[@id="inputPassword"]').send_keys(self.password)
        self.dr.find_element_by_xpath('//*[@id="login_admin"]').click()
        time.sleep(3)
        if self.dr.title==u"冻品邦后台管理系统":
            print('test log_in pass')
        else:
            print('test log_in fail' )

    def put_in(self):
        self.dr.find_element_by_xpath("/html/body/div[1]/aside/div[1]/section/ul/li[9]/a/span").click()
        self.dr.find_element_by_xpath("/html/body/div[1]/aside/div[1]/section/ul/li[9]/ul/li[4]/a/span").click()
        time.sleep(3)
        #self.dr.find_element_by_id('_easyui_textbox_input1').send_keys('1000001045')
        #self.dr.switch_to_frame(self.dr.find_element_by_name('ck'))
        self.dr.find_element_by_name('ck').click()


dr1 = webdriver.Firefox(executable_path='/Users/ph/Documents/geckodriver')
name1='17301691832'
password1='123456'
log_in1=Login(dr1,name1,password1)
log_in1.log_in()
log_in1.put_in()

