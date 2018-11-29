# -*- coding=utf-8 -*-
import time
from selenium import webdriver


class Lenglianbang (object):
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def loggin(self):
        self.dr=webdriver.Firefox(executable_path='/Users/ph/Documents/geckodriver')
        self.dr.get('https://qiubo-sandbox.dongpinbang.com:61511/login')
        time.sleep(3)
        self.dr.find_element_by_xpath('//*[@id="inputUsername"]').send_keys(self.username)
        self.dr.find_element_by_xpath('//*[@id="inputPassword"]').send_keys(self.password)
        self.dr.find_element_by_xpath('//*[@id="login_admin"]').click()
        time.sleep(4)

    def driver_paths(self):
        self.dr.find_element_by_xpath('/html/body/div[1]/aside/div[1]/section/ul/li[1]/a/span').click()
        self.dr.find_element_by_xpath('/html/body/div[1]/aside/div[1]/section/ul/li[1]/ul/li[1]/a/span').click()
        time.sleep(3)
        self.dr.switch_to.frame(0)
        self.dr.find_element_by_xpath('//*[@id="_easyui_textbox_input11"]').send_keys(u'彭慧')
        self.dr.find_element_by_xpath('/html/body/div[1]/div[2]/form/table/tbody/tr[4]/td[7]/a[1]/span/span').click()
        a=self.dr.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[2]/div')
        try:
            b=self.dr.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[3]')
            print('没有查找到该数据')
        except:
            if a.text==u'彭慧慧':
                print('司机路线查询-测试通过')
            else:
                print('司机路线查询-测试不通过')

username='17301691832'
password='123456'
namage=Lenglianbang(username,password)
namage.loggin()
namage.driver_paths()
#修改一个分支



