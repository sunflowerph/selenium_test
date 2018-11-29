# coding=utf-8


from selenium import webdriver
import re
from selenium.webdriver.common.keys import Keys

dr=webdriver.Firefox(executable_path='/Users/ph/Documents/geckodriver')
dr.maximize_window() #窗口最大化
dr.set_window_size(1280,800) #自定义窗口大小 设置分辨率 1280*800
dr.implicitly_wait(3)

dr.get('https://home.baidu.com/contact.html')
doc = dr.page_source #获取页面源代码
emails=re.findall(r'[\w]+@[\w\.-]+',doc) #利用正则找出  **@**.**的字段,获取网页上的邮箱

for email in emails:
    print email  #遍历打印获取的邮箱
print dr.capabilities['browserVersion']#打印当前浏览器版本号
print dr.current_url#打印当前url
print dr.title#打印当前网页标题

#判断当前网页标题内容（也可以用if  else）
try:
    assert u'联系百度' == dr.title  #或者 assert u'百度' in dr.title
    print 'assertion test pass'
except Exception as e:
    print 'test fail ',e





dr.find_element_by_tag_name('body').send_keys(Keys.COMMAND+'t') #触发键盘按键 command+t 新打开一个页面，但是没成功。

dr.quit()