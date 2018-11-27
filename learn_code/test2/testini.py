# coding=utf-8
import ConfigParser
import os


class Test_read_file(object):
    def get_value(self):
        root_dir=os.path.dirname(os.path.abspath('.'))#获取项目根目录的相对路径
        print('当前项目根目录的相对路径：')
        print root_dir

        config=ConfigParser.ConfigParser()
        file_path=os.path.dirname(os.path.abspath('.'))+'/config/config.ini'
        config.read(file_path)

        browser=config.get('browserType','browserName')
        url=config.get('testServer','URL')

        #print(browser,url)
        print('browsertype和url分别为：')
        return (browser,url) #返回的是一个元组

trcf=Test_read_file()

print trcf.get_value()
