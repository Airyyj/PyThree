from selenium import webdriver
import unittest
import HTMLTestRunner
import time
import os
from ReadTxt_demo import readTxt



from selenium.webdriver.common.keys import Keys

class Baidu_Report(unittest.TestCase):

    def setUp(self):
        self.browser=webdriver.Firefox()
        self.browser.maximize_window()
        self.browser.implicitly_wait(3)
        self.base_url="https://pan.baidu.com"
        self.verficationErrors=[]
        self.accept_next_alert=True
    def Login(self):
        browser=self.browser
        browser.get(self.base_url+'/')
        u"""百度云登录"""

        browser.find_element_by_xpath(".//*[@id='login-middle']/div/div[6]/div[2]/a").click()

        #引入读取文件模块获取用户名密码
        # from ReadTxt_demo import readTxt
        filePath = 'userInfo.txt'
        re_name, re_pwd = readTxt(filePath)

        browser.find_element_by_name("userName").clear()
        username = browser.find_element_by_name("userName")
        username.send_keys(re_name)
        username.send_keys(Keys.TAB)
        time.sleep(2)
        password = browser.find_element_by_name("password")
        password.send_keys(re_pwd)
        password.send_keys(Keys.ENTER)
        time.sleep(3)
        browser.close()
    def Register(self):
        browser=self.browser
        browser.get(self.base_url+'/')
        u"""立即注册百度账号"""
        browser.find_element_by_class_name("link-create").click()
        time.sleep(2)
        browser.close()
    def Link(self):
        browser=self.browser
        browser.get(self.base_url+'/')
        u"""百度首页"""
        browser.find_element_by_link_text("百度首页").click()
        time.sleep(2)
        browser.close()
    def tearDown(self):
        self.browser.quit()
        self.assertEqual([],self.verficationErrors)

if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(Baidu_Report("Login"))
    testunit.addTest(Baidu_Report("Register"))
    testunit.addTest(Baidu_Report("Link"))

    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # 打开一个文件，将result写入此file中
    filepath = os.path.join(os.getcwd(), 'report')
    filename = filepath +"/result" + now + ".html"
    fp = open(filename, 'wb')

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                            title='百度搜索测试报告',
                            description='用例执行情况:')
    runner.run(testunit)
    fp.quit()
