from selenium import webdriver
import time

driver = webdriver.Firefox()
#最大化窗口
driver.maximize_window()

#定义链接地址
first_url = "http://www.hao123.com"
secend_url = "http://www.baidu.com"
#打开第一个链接
driver.get(first_url)
time.sleep(3)
#打开第二个链接
driver.get(secend_url)
time.sleep(3)
#返回第一个链接
driver.back()
time.sleep(3)
#前进到第二个链接
driver.forward()
#添加智能等待
driver.implicitly_wait(5)
#通过xpath 定位,并清除输入框
driver.find_element_by_xpath(".//*[@id='kw']").clear()
time.sleep(3)
#获得输入框尺寸
get_size = driver.find_element_by_xpath(".//*[@id='kw']").size
print(get_size)

#返回页面指定文本信息
get_text = driver.find_element_by_id('jgwab').text
print(get_text)

#返回袁术的属性值，可以是id,name ,type等任意属性 获取对应属性的值

get_attribute = driver.find_element_by_id('jgwab').get_attribute('id')
print(get_attribute)
get_property = driver.find_element_by_id('jgwab').get_property('id')
print(get_property)

#返回元素的结果是否可见，返回结果为True,或false

get_result = driver.find_element_by_id('jgwab').is_displayed()

print(get_result)


# #输入内容
driver.find_element_by_xpath(".//*[@id='kw']").send_keys("selenium")
time.sleep(3)
#点击事件
#driver.find_element_by_xpath(".//*[@id='su']").click()
#使用submit（）提交,注意 submit一般用于提交表单，使用范围没有click()广，所以多使用click().
driver.find_element_by_xpath(".//*[@id='su']").submit()
time.sleep(3)
#刷新页面
driver.refresh()

#停留10秒
time.sleep(10)
#关闭浏览器结束（多使用quit（））
driver.quit()
#不关闭浏览器结束
#driver.close()

