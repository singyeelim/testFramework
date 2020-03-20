from getgauge.python import step, before_scenario, Messages
import libs.generic as generic
import uiautomation
from libs.driver import Driver
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


@step("Launch browser and specify url")
def launch_browser_and_specify_url():

    # Navigate to the application home page
    Driver.driver.get("https://shop.mercedes-benz.com/en-gb/collection/")
    generic.wait(120)
    
    
@step("Click on <Agree> button")
def click_on_button(name):

    driver = Driver.driver
    xpath = f'//button[normalize-space()="{name}"]'
    print(xpath)

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'layer-headline')))
        print("Cookies is ready")
        # Click on the 'Agree' button
        driver.find_element_by_xpath(xpath).click()
        generic.wait(120)
    except TimeoutException:
        print("No cookies")
    

@step("Navigate to Collection & accesories <menu> <submenu>")
def navigate_to_collection_and_accessories(menu, submenu):
    
    driver = Driver.driver
    wait = WebDriverWait(driver, 10)

    try:
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'main-navigation')))
        print ("Page is ready")
    except TimeoutException:
        print ("Initial loading took too much time!")

    # Click on 'Collection & accessories'
    generic.wait(120)
    driver.find_element_by_link_text('Collection & accessories').click()
    generic.wait(120)

    # Click on 'News'
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'shopnav-main-breadcrumb-container')))
    driver.find_element_by_link_text(menu).click()
    driver.implicitly_wait(120)

    # Click on 'Model cars'
    driver.find_element_by_link_text(submenu).click()
    driver.implicitly_wait(200)


@step("Select <productName> product")
def select_product(name):
    
    driver = Driver.driver
    wait = WebDriverWait(driver, 10)
    xpath = f'//*[text()="{name}"]'

    # Choose and click on a product
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'col-xs-12')))
    product = driver.find_element_by_xpath(xpath)
    generic.wait(1200)
    product.click()
    generic.wait(12000)

    try:
        wait.until(EC.presence_of_element_located((By.NAME, 'Mercedes-Benz Customer Solutions GmbH')))
        print ("Page is loaded")
    except TimeoutException:
        print ("Loading took too much time!")

    page = driver.find_element_by_tag_name("html")
    page.send_keys(Keys.PAGE_DOWN)
    generic.wait(120)


@step("Click on <Add to basket> to proceed")
def click_button_to_proceed(buttonName):
    
    driver = Driver.driver
    xpath = f'//*[text()="{buttonName}"]'

    button = driver.find_element_by_xpath(xpath)
    generic.wait(120)
    button.click()
    print (f'Clicking on {buttonName} button')
    generic.wait(120)


@step("Key in <fieldName> with value <fieldValue>")
def key_in_field(fieldName, fieldValue):
    
    driver = Driver.driver

    if fieldName == "Email address":
        id = "dcp-login-guest-user-email"
    elif fieldName == "First name":
        id = "co_payment_address-firstName"
    elif fieldName == "Last name":
        id = "co_payment_address-lastName"
    elif fieldName == "Street":
        id = "co_payment_address-line1"
    elif fieldName == "Number":
        id = "co_payment_address-line2"
    elif fieldName == "Postcode":
        id = "co_payment_address-postalCode"
    elif fieldName == "Town/city":
        id = "co_payment_address-town"
    elif fieldName == "Phone":
        id = "co_payment_address-phone"
    

    # Key in the value specified in the field
    field = driver.find_element_by_id(id)
    field.send_keys(fieldValue)
    generic.wait(120)

    # Todo: Assert field value equals to the specified value

    if fieldName == "Email address":
        # TAB to set focus on 'Place order as guest' button
        field.send_keys(Keys.TAB)
        generic.wait(120)
        # 'Click' on 'Place order as guest' button
        field.send_keys(Keys.ENTER)

    if fieldName == "Phone":
        generic.wait(240)
        field.send_keys(Keys.PAGE_DOWN)
        generic.wait(120)


@step("Click on <rafioButtonName> radio button")
def click_radio_button(radioButtonName):
    
    driver = Driver.driver
    xpath = f'//*[text()="{radioButtonName}"]'

    if radioButtonName == "Paypal":
        generic.wait(240)
        page = driver.find_element_by_tag_name("html")
        page.send_keys(Keys.PAGE_DOWN)

    radioButton = driver.find_element_by_xpath(xpath)
    generic.wait(120)
    radioButton.click()


@step("Verify <fieldName> field equals <expectedValue>")
def verify_field_value(fieldName, expectedValue):

    driver = Driver.driver

    field = driver.find_element_by_id("co_payment_address-email").click()
    value = field.send_keys(Keys.CONTROL + 'c')

    print(value)

    assert value == expectedValue, f'{fieldName} should have {expectedValue} instead of {value}'


