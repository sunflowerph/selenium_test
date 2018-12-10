# coding=UTF-8
from selenium import webdriver
import os


class operation(object):
    driver_path = os.path.dirname(os.path.abspath('.')) + '/tools/geckodriver'
    dr = webdriver.Firefox(executable_path=driver_path)


    def open_url(self,url):
        self.dr.get(url)


    def find_element(self,element):
        selector_by=element.split('=>')[0]
        selector_value=element.split('=>')[1]

        if selector_by=='xpath':
            selector=self.dr.find_element_by_xpath(selector_value)
            return selector

        elif selector_by=='css':
            selector=self.dr.find_element_by_css_selector(selector_value)
            return selector

    def click_element(self,element):
        el=self.find_element(element)
        el.click()


    def close_window(self):
        self.dr.close()


    def quit(self):
        self.dr.quit()


    def send_keys(self,element,text):
        el=self.find_element(element)
        el.send_keys(text)


    def get_title(self):

        return self.dr.title

    def wait(self,sec):
        self.dr.implicitly_wait(sec)














