import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome(executable_path="../drivers/chromedriver")
url = "https://courses.letskodeit.com/practice"
driver.get(url)
driver.implicitly_wait(20)
driver.maximize_window()

def test_Radiobutton():
    driver.find_element(By.XPATH, '//input[@id="benzradio"]').click()

def test_Dropdown():
    dropdown=driver.find_element(By.ID, 'carselect')
    sel=Select(dropdown)
    sel.select_by_visible_text("Benz")

def test_multiselect():
    multi=driver.find_element(By.ID, 'multiple-select-example')
    sel=Select(multi)
    sel.select_by_index(1)
    sel.select_by_visible_text("Peach")

def test_checkbox():
    driver.find_element(By.ID, 'benzcheck').click()
    driver.find_element(By.XPATH, '//legend[text()="Checkbox Example"]/following::input[3]').click()

def test_switchtab():
    parent=driver.current_window_handle
    driver.find_element(By.ID, 'opentab').click()
    time.sleep(3)
    driver.switch_to.window(parent)
    print(driver.title)

def test_Alert():
    driver.find_element(By.XPATH, '//input[@placeholder="Enter Your Name"]').send_keys("Ari")
    driver.find_element(By.ID, 'alertbtn').click()
    time.sleep(3)
    driver.switch_to.alert.accept()

def test_enabledisable():
    enable=driver.find_element(By.ID, 'enabled-example-input').is_enabled()
    print(enable)
    #disabling
    driver.find_element(By.ID, 'disabled-button').click()
    disable=driver.find_element(By.ID, 'enabled-example-input').is_enabled()
    print(disable)

@pytest.mark.screen
def test_displayedornot():
    display=driver.find_element(By.ID, 'displayed-text').is_displayed()
    print(display)
    #hiding
    driver.find_element(By.ID, 'hide-textbox').click()
    hide=driver.find_element(By.ID, 'displayed-text').is_displayed()
    print(hide)
    driver.save_screenshot("image.png")

def test_frame():
    #navigating to a frame
    driver.switch_to.frame("courses-iframe")
    #clicking an item inside a frame
    driver.find_element(By.XPATH, '//a[@href="/courses/javascript-for-beginners"]').click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    driver.switch_to.default_content()
    parent=driver.current_window_handle
    driver.find_element(By.ID, 'opentab').click()
    time.sleep(3)
    driver.switch_to.window(parent)
    print(driver.title)
