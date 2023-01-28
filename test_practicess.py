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
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver.get(url)
driver.implicitly_wait(20)
driver.maximize_window()

def test_login():
    #Username
    driver.find_element(By.XPATH, '//input[@name="username"]').send_keys("Admin")
    #password
    driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("admin123")
    #login
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

def test_dropdown():
    #click the dropdown
    driver.find_element(By.XPATH, '//span[@class="oxd-userdropdown-tab"]').click()
    #logout
    driver.find_element(By.XPATH, '//a[@href="/web/index.php/auth/logout"]').click()
@pytest.mark.hello
def test_switchwindow():
    #switching to another window
    parent=driver.current_window_handle
    driver.find_element(By.XPATH, '//a[text()="OrangeHRM, Inc"]').click()
    print(driver.title)
    child=driver.window_handles
    for i in child:
        if i!=child:
            driver.switch_to.window(i)
    print(driver.title)
    driver.switch_to.window(parent)


