#coding=utf-8

from framework.base_page import Basepage

class NewsHomePage(Basepage):

    sports_link='xpath=>//*[@id="channel-shanghai"]/div/ul/li[7]/a'

    def click_sports(self):
        self.click(self.sports_link)
        self.wait(5)



