# coding=utf-8
#获取网页上的邮箱

from selenium import webdriver
import re

dr=webdriver.Firefox(executable_path='/Users/ph/Documents/geckodriver')
dr.maximize_window()
dr.implicitly_wait(3)

dr.get('https://home.baidu.com/contact.html')
 #获取页面源代码
doc = dr.page_source
emails=re.findall(r'[\w]+@[\w\.-]+',doc) #利用正则找出  **@**.**的字段

for email in emails:
    print email

dr.quit()