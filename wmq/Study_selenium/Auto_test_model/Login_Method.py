
class Login():
    def user_login(self,driver):
        driver.implicitly_wait(10)
        driver.find_element_by_name('tj_login').click()
        driver.implicitly_wait(10)
        driver.find_element_by_name("userName").clear()
        driver.implicitly_wait(10)
        driver.find_element_by_name("userName").send_keys("15201062199")
        driver.implicitly_wait(10)
        driver.find_element_by_name("password").clear()
        driver.implicitly_wait(10)
        driver.find_element_by_name("password").send_keys("CHINA927_Skyyj")
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(".//*[@id='TANGRAM__PSP_8__submit']").click()

    def user_logout(self,driver):
        driver.find_element_by_name()
        driver.quit()

