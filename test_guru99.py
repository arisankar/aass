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

driver = webdriver.Chrome(executable_path="../drivers/chromedriver3")
url = "https://demo.guru99.com/V4/"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(8)

@pytest.mark.Newcustomer
@pytest.mark.Newaccount
def test_Login():
    #Adding Username
    driver.find_element(By.XPATH,'//input[@name="uid"]').send_keys("mngr463462")
    #Adding Password
    driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("hUzUsYg")
    #Logging in
    driver.find_element(By.XPATH, '//input[@name="btnLogin"]').click()

@pytest.mark.Newcustomer
def test_NewCustomer():
    #clicking on New customer from the left pane
    driver.find_element(By.XPATH, '//a[text()="New Customer"]').click()

    #Adding a Customer Name
    driver.find_element(By.XPATH, '//input[@onkeyup="validatecustomername();"]').send_keys("AriSankar")
    #Adding Gender
    driver.find_element(By.XPATH, '//input[@name="rad1" and @value="m"]').click()
    #Adding DOB
    driver.find_element(By.XPATH, '//input[@id="dob"]').send_keys("01/01/1990")
    #Adding Address
    driver.find_element(By.XPATH, '//textarea[@name="addr"]').send_keys("123 main street")
    #Adding City
    driver.find_element(By.XPATH, '//input[@name="city"]').send_keys("Chennai")
    #Adding State
    driver.find_element(By.NAME, 'state').send_keys("Tamil Nadu")
    #Adding Pin
    driver.find_element(By.NAME, 'pinno').send_keys("123123")
    #Adding Mob No
    driver.find_element(By.NAME, 'telephoneno').send_keys("1231231231")
    #Adding E-mail
    driver.find_element(By.XPATH, '//input[@onkeyup="validateEmail();"]').send_keys("evb@g.com")
    #Adding password
    driver.find_element(By.XPATH, '//input[@onkeyup="validatepassword();"]').send_keys("evb@g.com")
    #submitting
    driver.find_element(By.XPATH, '//input[@type="submit"]').click()
    #printing details
    s= driver.find_element(By.XPATH, '//table[@id="customer"]')
    print(s.text)

@pytest.mark.Newaccount
def test_NewAccount():
    #clicking on New Account from left pane
    driver.find_element(By.XPATH, '//a[text()="New Account"]').click()
    #Adding customer id
    driver.find_element(By.NAME, 'cusid').send_keys("75820")
    #Adding deposit amount
    driver.find_element(By.NAME, 'inideposit').send_keys("600")
    #submitting
    driver.find_element(By.XPATH, '//input[@name="button2"]').click()
    #printing
    c=driver.find_element(By.XPATH, '//table[@id="account"]')
    print(c.text)
