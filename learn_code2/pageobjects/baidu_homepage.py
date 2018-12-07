# coding=utf-8
from framework.base_page import Basepage


class HomePage(Basepage):
    input_box = "id=>kw"
    search_submit_btn = "xpath=>//*[@id='su']"
    #百度新闻入口
    news_link='xpath=>/html/body/div[1]/div[1]/div/div[3]/a[1]'

    def type_search(self, text):
        self.type(self.input_box, text)

    def send_submit_btn(self):
        self.click(self.search_submit_btn)

    def click_news(self):
        self.click(self.news_link)
        self.wait(5)


