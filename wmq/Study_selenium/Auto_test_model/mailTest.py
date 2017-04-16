from selenium import webdriver
from Login_Method import Login
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://www.baidu.com/")
driver.implicitly_wait(10)
Login().user_login(driver)


Login().user_logout(driver)