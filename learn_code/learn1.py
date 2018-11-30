# coding=utf-8


from selenium import webdriver
import re
from selenium.webdriver.common.keys import Keys

dr=webdriver.Firefox(executable_path='/Users/ph/Documents/geckodriver')
dr.maximize_window() #窗口最大化
dr.set_window_size(1280,800) #自定义窗口大小 设置分辨率 1280*800
dr.implicitly_wait(5)

dr.get('https://home.baidu.com/contact.html')
doc = dr.page_source #获取页面源代码
emails=re.findall(r'[\w]+@[\w\.-]+',doc) #利用正则找出  **@**.**的字段,获取网页上的邮箱

for email in emails:
    print email  #遍历打印获取的邮箱
print dr.capabilities['browserVersion']#打印当前浏览器版本号
print dr.current_url#打印当前url
print dr.title#打印当前网页标题
dr.find_element_by_tag_name('body').send_keys(Keys.COMMAND+'t') #触发键盘按键 command+t 新打开一个页面，但是没成功。

#判断当前网页标题内容（也可以用if  else）
try:
    assert u'联系百度' == dr.title  #或者 assert u'百度' in dr.title
    print 'assertion test pass'
except Exception as e:
    print 'test fail ',e


try:
    a=dr.find_element_by_xpath('/html/body/div/div[4]/div/div[1]/div[3]/div[2]/a/div')
    a.is_displayed #判断元素是否存在
    print a.size #打印元素的大小
    print 'test pass'
except:
    print 'test fail'

dr.find_element_by_tag_name('body').send_keys(Keys.COMMAND+'A') #全选页面上的文字



element=dr.find_element_by_xpath('/html/body/div/div[4]/div/div[1]/div[6]/div[2]/a/div')
dr.execute_script('return arguments[0].scrollIntoView();',element) #执行JavaScript脚本，使浏览器滚动到目标元素所在的位置
dr.execute_script('scroll(0,1800)') #也可以实现触发滚动条的目的
dr.execute_script('window.alert("你好吗");') #执行JavaScript脚本，创建内容为"你好吗"的alert弹窗vv
dr.quit()