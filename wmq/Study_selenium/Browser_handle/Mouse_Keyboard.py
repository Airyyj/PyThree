
from selenium import webdriver
#引入ActionChains类  提供了鼠标的操作方法
from selenium.webdriver.common.action_chains import  ActionChains

from selenium.webdriver.common.keys import Keys
from ReadTxt_demo import readTxt
import time


#鼠标键盘事件
'''
ActionChains 常用方法

perform()  执行所有ActionChains 中存储的行为；
context_click()  右击；
double_click()   双击；
drag_and_drop()  拖动；
move_to_element()  鼠标悬停。
click_and_hold()  按住鼠标左键在一个元素上。

'''

driver = webdriver.Firefox()

driver.maximize_window()
#打开百度网盘
driver.get("https://pan.baidu.com")

#点击 “帐号密码登录”
driver.find_element_by_xpath(".//*[@id='login-middle']/div/div[6]/div[2]/a").click()
# 引入读取文件模块获取用户名密码
# from ReadTxt_demo import readTxt
filePath = 'userInfo.txt'
re_name, re_pwd = readTxt(filePath)
#清空输入框，防止追加输入
driver.find_element_by_name("userName").clear()
username = driver.find_element_by_name("userName")
#输入用户名
username.send_keys(re_name)
#通过键盘敲击tab ,切换到下一个输入框。
username.send_keys(Keys.TAB)
time.sleep(2)
password = driver.find_element_by_name("password")
password.send_keys(re_pwd)
password.send_keys(Keys.ENTER)
time.sleep(3)

# 事实证明如果不加隐式等待implicitly_wait(5) 会出现：错误：Message: Unable to locate element:
#所以 implicitly_wait(5)  比sleep 靠谱
driver.implicitly_wait(5)
#测试单击操作
#driver.find_element_by_xpath(".//*[@id='h5Input0']").click()

#定位到元素，进行右击操作
#通过 link_text 定位。
right_click = driver.find_element_by_link_text('新建文件夹(1)')
driver.implicitly_wait(5)
#鼠标悬停
ActionChains(driver).move_to_element(right_click).perform()
time.sleep(10)
#对定位到的元素执行右击操作
ActionChains(driver).context_click(right_click).perform()
#.//*[@id='layoutMain']/div[2]/div[3]/div/div/dd[1]/div[2]/div[1]

#鼠标拖动操作，
#定义原位置、目标位置=right_click
driver.implicitly_wait(5)
file_source = driver.find_element_by_xpath(".//*[@id='layoutMain']/div[2]/div[3]/div/div/dd[1]/div[2]/div[1]")

#按住鼠标左键

ActionChains(driver).click_and_hold(file_source).perform()

driver.implicitly_wait(5)
ActionChains(driver).drag_and_drop(file_source,right_click).perform()
driver.implicitly_wait(5)

#鼠标双击
ActionChains(driver).double_click(right_click).perform()
time.sleep(13)



'''
from selenium.webdriver.common.action_chains import  ActionChains
导入提供鼠标操作的 ActionChains 类
ActionChains(driver)
调用ActionChains()类，将浏览器驱动driver作为参数传入
context_click(right_click)
context_click()方法用户模拟鼠标右键操作，在调用时需要指定元素定位
perform()
执行所有ActionChains中存储的行为，可以理解为对整个操作的提交动作。

'''



driver.quit()
#driver.close()





