#coding=utf-8
from framework.base_page import Basepage

class SportsNewsPage(Basepage):

    #NBA新闻入口
    nba_link='xpath=>/html/body/div[3]/div[2]/div[1]/div[2]/div/div[2]/div/ul/li[1]/a'

    def click_nba_link(self):
        self.click(self.nba_link)
        self.wait(5)
