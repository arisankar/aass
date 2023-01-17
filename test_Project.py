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
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver.get(url)
driver.implicitly_wait(8)

@pytest.mark.validLogin
@pytest.mark.InvalidLogin
@pytest.mark.newemployee
@pytest.mark.EditingEmployee
@pytest.mark.DeletingEmployee
def test_Login_01():
    #Adding the UserName
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")

    #Adding the Password
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")

    #Logging in
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

@pytest.mark.InvalidLogin
def test_Login_02():
    #Adding the UserName
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")

    #Adding the Wrong Password
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Invalidpassword")

    #Logging in
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    #printing the Error message
    a=driver.find_element(By.XPATH, '//div[@class="oxd-alert-content oxd-alert-content--error"]')
    print(a.text)

@pytest.mark.newemployee
def test_PIM_01():
    #clicking on PIM from left panel
    driver.find_element(By.XPATH, '//a[@href="/web/index.php/pim/viewPimModule"]').click()

    #clicking on +Add button
    driver.find_element(By.XPATH,'//button[@type="button" and @class="oxd-button oxd-button--medium oxd-button--secondary"]').click()

    #Adding a Firstname
    driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys("Ari")

    #Adding a Middlename
    driver.find_element(By.XPATH, '//input[@name="middleName"]').send_keys("M")

    #Adding a Lastname
    driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys("sankar")

    #saving the employee details
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

@pytest.mark.EditingEmployee
def test_PIM_02():
    #clicking on PIM from left panel
    driver.find_element(By.XPATH, '//a[@href="/web/index.php/pim/viewPimModule"]').click()

    #clicking on Edit button
    driver.find_element(By.XPATH, '//div[@class="oxd-table-body"]/div[1]/div/div[9]/div/button[2]/i').click()

    #Editing the Employee deatil by updating the Nickname
    driver.find_element(By.XPATH, '//div[@class="orangehrm-edit-employee-content"]/div[1]/h6/following::div[20]/input').send_keys("hello")

    #saving the changes
    driver.find_element(By.XPATH, '//div[@class="oxd-form-actions"]/p/following::button[1]').click()

@pytest.mark.DeletingEmployee
def test_PIM_03():
    #clicking on PIM from left panel
    driver.find_element(By.XPATH, '//a[@href="/web/index.php/pim/viewPimModule"]').click()

    #Clicking in Delete Button
    driver.find_element(By.XPATH, '//div[@class="oxd-table-body"]/div[1]/div/div[9]/div/button[1]/i').click()

    #Delete
    driver.find_element(By.XPATH, '//div[@class="orangehrm-modal-footer"]/button[2]').click()











