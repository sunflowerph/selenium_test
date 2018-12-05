# coding=utf-8
#基础操作

import time
import logging
import os.path

class Base(object):
    def __init__(self,driver):
        self.driver=driver

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def open_url(self,url):
        self.driver.get(url)

    def q(self):
        self.driver.quit()


class Logger(object):

    def __init__(self,log):
        self.log=logging.getLogger(log)
        self.log.setLevel(logging.DEBUG)
        rq=time.strftime('%Y %m %d %H:%M:%S',time.localtime())
        log_path=os.path.dirname(os.getcwd())+'/learn_code/Logs/'
        log_name=log_path+rq+'.log'
        fh=logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        ch=logging.StreamHandler()
        ch.setLevel(logging.INFO)


        formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.log.addHandler(fh)
        self.log.addHandler(ch)

    def getlog(self):
        return self.log









