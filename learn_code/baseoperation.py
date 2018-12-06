# coding=utf-8
#基础操作

import time
import logging
import os.path
from selenium.common.exceptions import NoSuchElementException

class Base(object):
    #浏览器基础操作
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


class Logger(object):
    #封装一个日志类，打印日志

    def __init__(self,log):
        self.log=logging.getLogger(log)
        self.log.setLevel(logging.DEBUG)
        rq=time.strftime('%Y %m %d %H:%M:%S',time.localtime())
        log_path=os.getcwd()+'/Logs/'
        log_name=log_path+rq+'.log'
        fh=logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        ch=logging.StreamHandler()
        ch.setLevel(logging.INFO)


        formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.log.addHandler(fh)
        self.log.addHandler(ch)

    def getlog(self):
        return self.log


class Element_operation(object):
    #元素相关操作：定位、输入文本、点击事件等
    def __init__(self,driver):
        self.driver=driver


    def find_element(self, selector):
        """
         这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
         submit_btn = "id=>su"
         login_lnk = "xpath => //*[@id='u1']/a[7]"  # 百度首页登录链接定位
         如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selector:
        :return: element
        """
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == "i" or selector_by == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)

            except NoSuchElementException as e:
                print '没找到元素'


        elif  selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif  selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif  selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)

            except NoSuchElementException as e:
                print '没找到元素'


        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return element

    def write_keys(self,selector,text):
        el=self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            print '选择输入框，输入文本: ' + text
        except:
            print '输入文本失败'


    def click(self,selector):
        el = self.find_element(selector)
        try:
            el.click()
            print '元素点击成功'
        except:
            print '元素点击失败'









                         












