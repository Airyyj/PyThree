
from selenium import webdriver
import time

#模块化驱动测试实例
driver = webdriver.Firefox()

url = "http://mail.163.com/"
driver.implicitly_wait(5)
driver.get(url)
driver.implicitly_wait(10)
#登陆
time.sleep(5)
driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys('wmqyyj_test')
driver.find_element_by_id('auto-id-1492316062723').clear()
driver.find_element_by_id('auto-id-1492316062723').send_keys('WMQyyj2017')

driver.find_element_by_id('dologin').click()
print('执行登陆')

#退出

driver.find_element_by_link_text("退出").click()
print("执行退出")
driver.quit()