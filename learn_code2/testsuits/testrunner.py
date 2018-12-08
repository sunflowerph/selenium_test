# coding=utf-8
import HTMLTestRunner
import os.path
import time
import unittest
from testsuits.baidu_search import BaiduSearch
from testsuits.test_get_page_title import GetPageTitle

'''
#使用unittest.TestSuite.addTest执行不同文件下的测试用例
suite = unittest.TestSuite()
suite.addTest(BaiduSearch('test_baidu_search'))
suite.addTest(BaiduSearch('test_search2'))
suite.addTest(GetPageTitle('test_get_title'))



'''



#使用unittest.makesuit()添加一个类文件下所有的测试用例

suite=unittest.TestSuite(unittest.makeSuite(BaiduSearch))



'''
#使用 unittest.TestLoader().discover()添加一个文件内或包内所有的用例
suite=unittest.TestLoader().discover('testsuits')
'''
report_path=os.path.dirname(os.path.abspath('.'))+'/testreport/'
ti=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
# 设置报告名称格式
HtmlFile = report_path + ti + "HTMLtemplate.html"
fp = file(HtmlFile, "wb")




if __name__ == '__main__':
    # 执行用例
    runner = unittest.TextTestRunner()
    runner.run(suite)


