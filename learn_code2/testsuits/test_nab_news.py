# coding=utf-8
import  time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage
from pageobjects.baidu_news_home import NewsHomePage
from pageobjects.news_sport_home import SportsNewsPage

class ViewNbaNews(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser=BrowserEngine(cls)
        cls.driver=browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        a = BrowserEngine(cls.driver)
        a.quit_browser()

    def test_nba_news(self):

        #运行失败，这是一个BUG
        baiduhome=HomePage(self.driver)
        baiduhome.click_news()
        newshome=NewsHomePage(self.driver)
        newshome.click_sports()
        sporthome=SportsNewsPage(self.driver)
        sporthome.click_nba_link()






if __name__ =='__main__':
    unittest.main()








