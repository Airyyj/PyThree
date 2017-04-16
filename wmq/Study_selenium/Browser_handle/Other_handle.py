#获取验证信息
from selenium import webdriver
import time
#导入 WebDriverWait 包
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()
url = "http:www.hao123.com"
driver.get(url)

#打印当前页面title
get_title = driver.title
print(get_title)
#打印当前的url
now_url = driver.current_url
print(now_url)

#获取页面文本信息
get_text = driver.find_element_by_xpath(".//*[@id='login']/div/a/span").text
print(get_text)

'''
title:用于获得当前页面的标题
current_url : 用户获得当前页面的url.
text:获取页面文本信息。
这些一般用于页面验证

'''
#获取截图
#这个截图可以用于截取测试报告的图片。
driver.get_screenshot_as_file(r'D:\SProgram\PySpace\ScreenShot\hao123_jmg.jpg')


driver.quit()