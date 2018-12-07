# coding=utf-8

#使用unittest.TestSuite.addTest执行不同文件下的测试用例
import unittest

from testsuits.baidu_search import BaiduSearch
from testsuits.test_get_page_title import GetPageTitle

suite = unittest.TestSuite()
suite.addTest(BaiduSearch('test_baidu_search'))
suite.addTest(BaiduSearch('test_search2'))
suite.addTest(GetPageTitle('test_get_title'))

if __name__ == '__main__':
    # 执行用例
    runner = unittest.TextTestRunner()
    runner.run(suite)
