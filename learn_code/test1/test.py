# coding=utf-8
import time
from test2.browser_engine import Browser_engine

class Test_browser_engine(object):

    def open_browser(self):
        browser_engine=Browser_engine(self)
        driver=browser_engine.get_browser()
tbe=Test_browser_engine()
tbe.open_browser()