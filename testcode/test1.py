# coding=utf-8

from selenium import webdriver


dr=webdriver.Firefox(executable_path='/Users/ph/Documents/geckodriver')

#登录后台开发环境,并打开订单列表
def login(count,password):
    dr.get('https://qiubo-dev.dongpinbang.com:61511/login')
    dr.find_element_by_xpath('//*[@id="inputUsername"]').send_keys(count)
    dr.find_element_by_xpath('//*[@id="inputPassword"]').send_keys(password)
    dr.find_element_by_xpath('//*[@id="login_admin"]').click()
    dr.implicitly_wait(4)
    dr.find_element_by_xpath('/html/body/div[1]/aside/div[1]/section/ul/li[1]/a/span').click()
    dr.find_element_by_xpath('/html/body/div[1]/aside/div[1]/section/ul/li[1]/ul/li[1]/a/span').click()

#订单已确认操作
def confirm():

    dr.switch_to.frame(0)
    dr.find_element_by_xpath('//div[2]/table/tbody/tr/td/div/input').click()
    dr.find_element_by_xpath('/html/body/div[3]/div/div/div/div[1]/table/tbody/tr/td[2]/a/span/span').click()
    dr.find_element_by_xpath('/html/body/div[18]/div[3]/a/span/span[1]').click()
    dr.find_element_by_css_selector(".l-btn-focus .l-btn-text").click()
    dr.implicitly_wait(4)

#订单备货完成
def goods_ready():

    dr.find_element_by_xpath('//div[2]/table/tbody/tr/td/div/input').click()
    dr.find_element_by_xpath('/html/body/div[3]/div/div/div/div[1]/table/tbody/tr/td[3]/a/span/span').click()
    dr.find_element_by_css_selector('.messager-button > a:nth-child(1) > span:nth-child(1) > span:nth-child(1)').click()
    dr.find_element_by_css_selector('.messager-button > a:nth-child(1) > span:nth-child(1) > span:nth-child(1)').click()
    dr.implicitly_wait(4)


#订单已发货操作
def send_out():

    dr.find_element_by_xpath('//div[2]/table/tbody/tr/td/div/input').click()
    dr.find_element_by_xpath('/html/body/div[3]/div/div/div/div[1]/table/tbody/tr/td[5]/a/span/span').click()
    dr.find_element_by_css_selector\
        ('div.panel:nth-child(27) > div:nth-child(3) > a:nth-child(1) > span:nth-child(1) > span:nth-child(1)').click()
    dr.find_element_by_css_selector('.messager-button > a:nth-child(1) > span:nth-child(1) > span:nth-child(1)').click()
    dr.implicitly_wait(4)

#订单已交付
def delivered():
    dr.find_element_by_xpath('//div[2]/table/tbody/tr/td/div/input').click()
    dr.find_element_by_xpath('/html/body/div[3]/div/div/div/div[1]/table/tbody/tr/td[7]/a/span/span').click()
    dr.find_element_by_css_selector('.messager-button > a:nth-child(1) > span:nth-child(1) > span:nth-child(1)').click()
    dr.find_element_by_css_selector('.messager-button > a:nth-child(1) > span:nth-child(1)').click()
    dr.implicitly_wait(4)

#买家对账完成
def account_check():
    dr.find_element_by_xpath('//div[2]/table/tbody/tr/td/div/input').click()
    dr.find_element_by_xpath('/html/body/div[3]/div/div/div/div[1]/table/tbody/tr/td[8]/a/span/span').click()
    dr.find_element_by_css_selector('#_easyui_textbox_input15').send_keys('1')
    dr.find_element_by_css_selector\
        ('div.panel:nth-child(40) > div:nth-child(3) > a:nth-child(1) > span:nth-child(1) > span:nth-child(1)').click()

    dr.find_element_by_css_selector('.messager-button > a:nth-child(1) > span:nth-child(1)').click()
    dr.implicitly_wait(4)

#供应商结算完成
def Settlement_completion():
    dr.switch_to.frame(0)
    dr.find_element_by_xpath('//div[2]/table/tbody/tr/td/div/input').click()
    dr.find_element_by_xpath('/html/body/div[3]/div/div/div/div[1]/table/tbody/tr/td[9]/a/span/span').click()
    dr.find_element_by_css_selector('.messager-button > a:nth-child(1) > span:nth-child(1) > span:nth-child(1)').click()
    dr.find_element_by_css_selector('.messager-button > a:nth-child(1) > span:nth-child(1)').click()
    dr.implicitly_wait(4)

a=login('17301691832','123456')
b=confirm()
c=goods_ready()
d=send_out()
e=delivered()
g=Settlement_completion()





