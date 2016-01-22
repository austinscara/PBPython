from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get("https://www.privateequityinternational.com/GP_Search/")


userNameElement = driver.find_element_by_id("ctl00_MasterPage_NonLoggedIn1_UserName")
userNameElement.send_keys("austin.scara@pitchbook.com")



passwordElement = driver.find_element_by_id("Password")
passwordElement.send_keys("1313666a")


# loginButton = driver.find_element_by_id("ctl00_NonLoggedIn_LoginButton")
# loginButton.click()


