from getgauge.python import before_suite, after_suite
from selenium import webdriver

class Driver(object):
    driver = None

    @before_suite
    def init(self):
        Driver.driver = webdriver.Chrome()
        Driver.driver.maximize_window()

    # @after_suite
    # def close(self):
    #     self.driver.close()
