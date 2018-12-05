# coding=utf-8
import unittest
from selenium import webdriver
import time

class Baidu_search(unittest.TestCase):
    def setUp(self):
        self.dr=webdriver.Chrome(executable_path='/Users/ph/Documents/chromedriver')
        self.dr.get('https://www.baidu.com')
        self.dr.implicitly_wait(3)

    def tearDown(self):
        self.dr.quit()

    def test_baidu_search(self):
        self.dr.find_element_by_xpath('//*[@id="kw"]').send_keys('selenium')
        self.dr.find_element_by_xpath('//*[@id="su"]').click()
        time.sleep(2)
        '''
        try:
            assert u'selenium' in self.dr.title
            print 'testpass'
        except:
            print 'tetfail'
           '''
        assert u'selenium' in self.dr.title
if __name__=='__main__':
    unittest.main()