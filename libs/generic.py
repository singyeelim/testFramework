from getgauge.python import step, before_scenario, Messages
from libs.driver import Driver
import webbrowser
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


@step("wait<seconds>")
def wait(sec):
    Driver.driver.implicitly_wait(sec)
