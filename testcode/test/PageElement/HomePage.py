# coding=utf-8
from base_operation.base import operation

#主页元素定位
class Home_page(operation):
    # 订单管理按钮
    order_manage = 'xpath=>/html/body/div[1]/aside/div[1]/section/ul/li[1]/a/span'

    def order_process(self):
        self.click_element(self.order_manage)
        print '点击订单管理'


