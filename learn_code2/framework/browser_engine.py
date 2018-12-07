#coding=utf-8
import ConfigParser
import os.path
from framework.logger import Logger
from selenium import webdriver

logger = Logger(log="BrowserEngine").getlog()


class BrowserEngine(object):
    dir = os.path.dirname(os.path.abspath('.'))  # 注意相对路径获取方法
    chrome_driver_path = dir + '/tools/chromedriver'
    firefox_driver_path = dir + '/tools/geckodriver'

    def __init__(self, driver):
        self.driver = driver

    # read the browser type from config.ini file, return the driver
    def open_browser(self, driver):
        config = ConfigParser.ConfigParser()
        # file_path = os.path.dirname(os.getcwd()) + '/config/config.ini'
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)
        # config.read(file_path,encoding='UTF-8'), 如果代码有中文注释，用这个，不然报解码错误

        browser = config.get("browserType", "browserName")
        logger.info("You had select %s browser." % browser)
        url = config.get("testServer", "URL")
        logger.info("The test server url is: %s" % url)

        if browser == "Firefox":
            driver = webdriver.Firefox(self.firefox_driver_path)
            logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("Starting Chrome browser.")

        driver.get(url)
        logger.info("Open url: %s" % url)
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds.")
        return driver

    def quit_browser(self):
        logger.info("Now, Close and quit the browser.")
        self.driver.quit()
        logger.info('browser.quit')

