# coding=utf-8
import time
from selenium import webdriver
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class Get_substring(object):
    def get_search_result(self):
        dr=webdriver.Firefox(executable_path='/Users/ph/Documents/geckodriver')
        dr.get('https://www.baidu.com')
        dr.find_element_by_xpath('//*[@id="kw"]').send_keys('selenium')
        dr.find_element_by_xpath('//*[@id="su"]').click()
        time.sleep(3)
        result_string=dr.find_element_by_xpath('/html/body/div[1]/div[5]/div[1]/div[2]/div/div[2]/span').text
        print(result_string)
        new_string=result_string.split('约')[1]# 第一次切割得到 xxxx个，[1]代表切割右边部分
        print(new_string)
        last_Result=new_string.split('个')[0]# 第二次切割，得到我们想要的数字 [0]代表切割参照参数的左边部分
        print(last_Result)
getstring=Get_substring()
getstring.get_search_result()


