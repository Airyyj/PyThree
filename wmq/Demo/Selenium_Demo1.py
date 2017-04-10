#加载unittest模块
import unittest
import time
#加载HTMLTestRunner，用于生成HTMLreuslt
import HTMLTestRunner
from selenium import webdriver
#加载键盘使用的模块
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get("https://pan.baidu.com")
print("请等待10秒钟！！")
browser.implicitly_wait(10)

browser.find_element_by_xpath(".//*[@id='login-middle']/div/div[6]/div[2]/a").click()

browser.find_element_by_name("userName").clear()
username = browser.find_element_by_name("userName")
username.send_keys("15201062199")
username.send_keys(Keys.TAB)
time.sleep(2)
password=browser.find_element_by_name("password")
password.send_keys("CHINA927_Skyyj")
password.send_keys(Keys.ENTER)
time.sleep(3)




