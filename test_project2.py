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

#Adding the UserName
driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")

#Adding the Password
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")

#Logging in
driver.find_element(By.XPATH, "//button[@type='submit']").click()

def test_pim_01():
    #Validating whether SEARCH (Text Box) is available or not
    display=driver.find_element(By.XPATH, '//input[@placeholder="Search"]')
    pritning=display.is_displayed()
    print(pritning)

    #Searching the Keywords (Admin,pim,leave,time,recruitment,my info,performance,dashboard,directory,maintanence,buzz) in both Lower and Upper cases
    driver.find_element(By.XPATH, '//input[@placeholder="Search"]').send_keys("ADMIN")
    driver.refresh()
    driver.find_element(By.XPATH, '//input[@placeholder="Search"]').send_keys("admin")
    driver.refresh()
    driver.find_element(By.XPATH, '//input[@placeholder="Search"]').send_keys("PIM")
    driver.refresh()
    driver.find_element(By.XPATH, '//input[@placeholder="Search"]').send_keys("pim")
    driver.refresh()
    driver.find_element(By.XPATH, '//input[@placeholder="Search"]').send_keys("LEAVE")
    driver.refresh()
    driver.find_element(By.XPATH, '//input[@placeholder="Search"]').send_keys("leave")
    driver.refresh()
    driver.find_element(By.XPATH, '//input[@placeholder="Search"]').send_keys("TIME")
    driver.refresh()
    driver.find_element(By.XPATH, '//input[@placeholder="Search"]').send_keys("time")
    driver.refresh()
    driver.find_element(By.XPATH, '//input[@placeholder="Search"]').send_keys("RECRUITMENT")
    driver.refresh()
    driver.find_element(By.XPATH, '//input[@placeholder="Search"]').send_keys("recruitment")
    driver.refresh()
    driver.find_element(By.XPATH, '//input[@placeholder="Search"]').send_keys("MY INFO")
    driver.refresh()
    driver.find_element(By.XPATH, '//input[@placeholder="Search"]').send_keys("my info")
    driver.refresh()
    driver.find_element(By.XPATH, '//input[@placeholder="Search"]').send_keys("PERFORMANCE")
    driver.refresh()
    driver.find_element(By.XPATH, '//input[@placeholder="Search"]').send_keys("performance")
    driver.refresh()
    driver.find_element(By.XPATH, '//input[@placeholder="Search"]').send_keys("DASHBOARD")
    driver.refresh()
    driver.find_element(By.XPATH, '//input[@placeholder="Search"]').send_keys("dashboard")
    driver.refresh()
    driver.find_element(By.XPATH, '//input[@placeholder="Search"]').send_keys("DIRECTORY")
    driver.refresh()
    driver.find_element(By.XPATH, '//input[@placeholder="Search"]').send_keys("directory")
    driver.refresh()
    driver.find_element(By.XPATH, '//input[@placeholder="Search"]').send_keys("MAINTENANCE")
    driver.refresh()
    driver.find_element(By.XPATH, '//input[@placeholder="Search"]').send_keys("maintenance")
    driver.refresh()
    driver.find_element(By.XPATH, '//input[@placeholder="Search"]').send_keys("BUZZ")
    driver.refresh()
    driver.find_element(By.XPATH, '//input[@placeholder="Search"]').send_keys("buzz")
    driver.refresh()
    driver.find_element(By.XPATH, '//input[@placeholder="Search"]').send_keys("admin")

def test_pim_02():
    driver.find_element(By.XPATH, '//a[@href="/web/index.php/admin/viewAdminModule"]').click()
    #cliking User management dropdown
    driver.find_element(By.XPATH, '//li[@class="oxd-topbar-body-nav-tab --parent --visited"]/span').click()
    #clicking on Users from the Dropdown
    driver.find_element(By.XPATH, '//a[@role="menuitem"]').click()

    #clicking on UserRole Dropdown
    driver.find_element(By.XPATH, '//label[text()="User Role"]/following::div[5]/i').click()
    #clicking on Status Dropdown
    driver.find_element(By.XPATH, '//label[text()="Status"]/following::div[5]/i').click()

@pytest.mark.contact
@pytest.mark.emergency
@pytest.mark.job
@pytest.mark.Tax
def test_pim_03():
    #clicking PIM from the pane
    driver.find_element(By.XPATH, '//a[@href="/web/index.php/pim/viewPimModule"]').click()

    #clicking on Add button
    driver.find_element(By.XPATH, '//button[@type="button" and @class="oxd-button oxd-button--medium oxd-button--secondary"]').click()

    #Adding FirstName
    driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys("Arii")
    #Adding LastName
    driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys("Sankarr")

    #Turning on the Toggle
    driver.find_element(By.XPATH, '//span[@class="oxd-switch-input oxd-switch-input--active --label-right"]').click()

    #clearing the existing value in Username Field
    driver.find_element(By.XPATH, '//div[@class="oxd-form-row"]/following::div[8]/input').send_keys("qufvuwjf")

    #Adding password
    driver.find_element(By.XPATH, '//label[@class="oxd-label oxd-input-field-required" and text()="Password"]/following::input[1]').send_keys("Arisankar@08")

    #Adding Confirm Password
    driver.find_element(By.XPATH, '//label[@class="oxd-label oxd-input-field-required" and text()="Password"]/following::input[2]').send_keys("Arisankar@08")

    #clicking on Save Button
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    ele=driver.find_elements(By.XPATH, '//div[@class="orangehrm-tabs"]')
    for i in ele:
        print(i.text)

def test_pim_04():
    #validating whether the tabs were present or not
    ele=driver.find_elements(By.XPATH, '//div[@class="orangehrm-tabs"]')
    for i in ele:
        print(i.text)

def test_pim_05():
    #Adding the OTHER ID
    time.sleep(6)
    driver.find_element(By.XPATH, '//label[text()="Other Id"]/following::input[@class="oxd-input oxd-input--active"][1]').send_keys("OtherID")
    # Adding Expiry Date
    time.sleep(4)
    driver.find_element(By.XPATH,'//label[text()="License Expiry Date"]/following::input[@class="oxd-input oxd-input--active"][1]').send_keys("2024-09-01")
    # adding SSN
    time.sleep(4)
    driver.find_element(By.XPATH,'//label[text()="SSN Number"]/following::input[@class="oxd-input oxd-input--active"][1]').send_keys("1997")
    # Adding SIN
    time.sleep(4)
    driver.find_element(By.XPATH,'//label[text()="SIN Number"]/following::input[@class="oxd-input oxd-input--active"][1]').send_keys("1111")
    # Adding DOB
    time.sleep(4)
    driver.find_element(By.XPATH,'//label[text()="Date of Birth"]/following::input[@class="oxd-input oxd-input--active"][1]').send_keys("1990-01-01")
    # Adding Military Service
    time.sleep(4)
    driver.find_element(By.XPATH, '//label[text()="Military Service"]/following::input[@class="oxd-input oxd-input--active"][1]').send_keys("hii")
    #click Save
    time.sleep(4)
    driver.find_element(By.XPATH,'//div[@class="oxd-form-actions"]/p/following::button[1]').submit()

@pytest.mark.contact
def test_pim_06():
    #Cligking Contact Details
    time.sleep(12)
    driver.find_element(By.XPATH, '//a[text()="Contact Details"]').click()
    #Adding Street1
    time.sleep(4)
    driver.find_element(By.XPATH, '//label[text()="Street 1"]/following::input[@class="oxd-input oxd-input--active"][1]').send_keys("123 main")
    time.sleep(2)
    driver.find_element(By.XPATH, '//label[text()="Street 2"]/following::input[@class="oxd-input oxd-input--active"][1]').send_keys("123 side")
    time.sleep(2)
    driver.find_element(By.XPATH, '//label[text()="Street 2"]/following::input[@class="oxd-input oxd-input--active"][1]').send_keys("Tenkasi")
    time.sleep(2)
    driver.find_element(By.XPATH, '//label[text()="State/Province"]/following::input[@class="oxd-input oxd-input--active"][1]').send_keys("Tamilnadu")
    time.sleep(2)
    driver.find_element(By.XPATH, '//label[text()="Zip/Postal Code"]/following::input[@class="oxd-input oxd-input--active"][1]').send_keys("627811")
    time.sleep(2)
    driver.find_element(By.XPATH, '//button[@type="submit"]').submit()

@pytest.mark.emergency
def test_pim_07():
    #clicking on Emergency contacts
    time.sleep(5)
    driver.find_element(By.XPATH, '//a[text()="Emergency Contacts"]').click()
    #clicking on Add
    time.sleep(2)
    driver.find_element(By.XPATH, '//h6[text()="Attachments"]/following::button/i').click()
    #Adding file
    time.sleep(2)
    driver.find_element(By.XPATH, '//i[@class="oxd-icon bi-upload oxd-file-input-icon"]').send_keys("/Users/arisankarm/Downloads/kjs9.png")
    #clicking Save
    time.sleep(2)
    driver.find_element(By.XPATH, '//button[@type="submit"]').submit()
@pytest.mark.job
def test_pim_09():
    #clicking on Job
    time.sleep(5)
    driver.find_element(By.XPATH, '//a[text()="Job"]').click()
    time.sleep(3)
    a=driver.find_element(By.XPATH, '// label[text() = "Job Title"] / following::div[3]')
    a.click()
    ActionChains(driver).key_down(Keys.ARROW_DOWN).click(a).perform()
    time.sleep(3)
    b=driver.find_element(By.XPATH, '//label[text()="Job Category"]/following::div[3]')
    b.click()
    ActionChains(driver).key_down(Keys.ARROW_DOWN).click(b).perform()
    time.sleep(3)
    c=driver.find_element(By.XPATH, '//label[text()="Sub Unit"]/following::div[4]')
    c.click()
    ActionChains(driver).key_down(Keys.ARROW_DOWN).click(c).perform()
    time.sleep(3)
    d=driver.find_element(By.XPATH, '//label[text()="Location"]/following::div[4]')
    d.click()
    ActionChains(driver).key_down(Keys.ARROW_DOWN).click(d).perform()
    driver.find_element(By.XPATH, '//button[@type="submit"]').submit()

@pytest.mark.job
def test_pim_10():
    time.sleep(3)
    driver.find_element(By.XPATH, '//div[@class="orangehrm-horizontal-padding orangehrm-vertical-padding"][2]/div/h6/following::button[1]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//div[@class="oxd-date-input"]/following::input[2]').send_keys("2040-01-01")
    time.sleep(3)
    dd=driver.find_element(By.XPATH, '//label[text()="Termination Reason"]/following::div[1]')
    dd.click()
    ActionChains(driver).key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).click(dd).perform()
    time.sleep(3)
    driver.find_element(By.XPATH, '//textarea[@placeholder="Type here"]').send_keys("sffefef")
    time.sleep(3)
    driver.find_element(By.XPATH, '//p[text()=" * Required"]/following::button[2]').submit()

@pytest.mark.Tax
def test_pim_13():
        time.sleep(3)
        driver.find_element(By.XPATH, '//a[text()="Tax Exemptions"]').click()
        time.sleep(3)
        aa = driver.find_element(By.XPATH, '//div[@class="oxd-form-row"]/following::div[5]/label/following::div[1]/div')
        aa.click()
        ActionChains(driver).key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).click(aa).perform()
        time.sleep(3)
        driver.find_element(By.XPATH, '//button[@type="submit"]').submit()


