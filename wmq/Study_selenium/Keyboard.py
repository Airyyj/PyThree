
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

'''

from selenium.webdriver.common.keys import Keys
在使用键盘按键方法前需要先导入 keys 类包。
下面经常使用到的键盘操作：
send_keys(Keys.BACK_SPACE) 删除键（BackSpace）
send_keys(Keys.SPACE) 空格键(Space)
send_keys(Keys.TAB) 制表键(Tab)
send_keys(Keys.ESCAPE) 回退键（Esc）
send_keys(Keys.ENTER) 回车键（Enter）
send_keys(Keys.CONTROL,'a') 全选（Ctrl+A）
send_keys(Keys.CONTROL,'c') 复制（Ctrl+C）博客园---虫师
http://fnng.cnblogs.com 52
send_keys(Keys.CONTROL,'x') 剪切（Ctrl+X）
send_keys(Keys.CONTROL,'v') 粘贴（Ctrl+V）
Keys 类所提供的按键请查阅 webdriver API.

'''



driver = webdriver.Firefox()
url = "http://www.hao123.com"
driver.maximize_window()
driver.get(url)

driver.implicitly_wait(3)
driver.find_element_by_id('search-input').clear()
driver.find_element_by_id('search-input').send_keys('seleniumm')
driver.implicitly_wait(3)
#回删
driver.find_element_by_id('search-input').send_keys(Keys.BACK_SPACE)
driver.implicitly_wait(3)
#追加空格
driver.find_element_by_id('search-input').send_keys(Keys.SPACE)
driver.implicitly_wait(3)
driver.find_element_by_id('search-input').send_keys('教程')
driver.implicitly_wait(3)
#全选内容
driver.find_element_by_id('search-input').send_keys(Keys.CONTROL,'a')
driver.implicitly_wait(3)
#剪切内容
driver.find_element_by_id('search-input').send_keys(Keys.CONTROL,'x')
driver.implicitly_wait(3)

#粘贴内容
driver.find_element_by_id('search-input').send_keys(Keys.CONTROL,'v')
driver.implicitly_wait(3)

#回车代替 点击
driver.find_element_by_id('search-input').send_keys(Keys.ENTER)
driver.implicitly_wait(3)

time.sleep(10)

driver.quit()