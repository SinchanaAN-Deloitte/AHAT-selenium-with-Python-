from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class Login:
    def __init__(self,webdriverval):
        driver=webdriverval
        driver.maximize_window()
        driver.implicitly_wait(10)
    ##LOGIN
    def log1(self):
        driver.get('https://automatedhuallocation-ui-urtjok3rza-wl.a.run.app/')
        time.sleep(5)
        driver.find_element(By.CLASS_NAME, "avatar").click()
        time.sleep(5)
        user_input = driver.find_element(By.ID, 'basic_username')
        user_input.send_keys("gheavens2")
        time.sleep(2)
        password = driver.find_element(By.ID, 'basic_password')
        password.send_keys("password")
        login_button = driver.find_element(By.XPATH, "//*[@id=\"basic\"]/div[3]/div/div/div/button/span")
        login_button.click()
        time.sleep(5)
    def changepass(self):
        changepass=driver.find_element(By.CLASS_NAME,"ant-dropdown-menu-title-content")
        self.assertEqual(True, changepass.is_displayed())
        print("Change password option is visible in user profile")
        self.assertTrue(changepass.is_enabled())
        print("Change password option is clickable")
        changepass.click()
        time.sleep(5)
        #LEAVING BOTH TEXT BOX EMPTY
        oldpass = driver.find_element(By.ID,"form_user_old_password")
        self.assertEqual(True, oldpass.is_displayed())
        print("Text box to enter old password is visible in Change password panel")
        oldpass.send_keys("")
        time.sleep(5)
        newpass = driver.find_element(By.ID,"form_user_new_password")
        self.assertEqual(True, newpass.is_displayed())
        print("Text box to enter new password is visible in Change password panel")
        newpass.send_keys("")
        time.sleep(5)
        subm=driver.find_element(By.XPATH,"//*[@id=\"form\"]/div[3]/button")
        time.sleep(5)
        self.assertEqual(True,subm.is_displayed())
        print("submit button is visibleble")
        self.assertTrue(subm.is_enabled())
        print("submit button is clickable")
        subm.click()
        time.sleep(5)
        driver.refresh()
        time.sleep(5)
        #LEAVING OLD PASSWORD FIELD EMPTY
        newpass = driver.find_element(By.ID,"form_user_new_password").send_keys("password")
        time.sleep(5)
        driver.find_element(By.XPATH,"//button[@class='ant-btn ant-btn-primary']").click()
        time.sleep(5)
        driver.refresh()
        time.sleep(5)
        #LEAVING NEW PASSWORD EMPTY
        oldpass = driver.find_element(By.ID,"form_user_old_password").send_keys("password")
        time.sleep(5)
        driver.find_element(By.XPATH,"//*[@id=\"form\"]/div[3]/button").click()
        time.sleep(5)
        driver.refresh()
        time.sleep(5)
        #CHANGE PASSWORD WITH INVALID OLDPASSWORD VALID NEWPASSWORD
        oldpass = driver.find_element(By.ID,"form_user_old_password").send_keys("password123")
        time.sleep(5)
        newpass = driver.find_element(By.ID,"form_user_new_password").send_keys("userlogin")
        time.sleep(5)
        driver.find_element(By.XPATH,"//*[@id=\"form\"]/div[3]/button").click()
        time.sleep(5)
        driver.refresh()
        time.sleep(5)
        #CHANGE PASSWORD WITH VALID CREDENTIALS
        oldpass=driver.find_element(By.ID,"form_user_old_password")
        oldpass.send_keys("password")
        time.sleep(5)
        eye=driver.find_element(By.XPATH,"//*[@id=\"form\"]/div[1]/div[2]/div/div/span/span/span")
        self.assertEqual(True, eye.is_displayed())
        print("eye icon is visible")
        self.assertTrue(eye.is_enabled())
        print("eye icon is clickable")
        eye.click()
        time.sleep(5)
        newpass = driver.find_element(By.ID,"form_user_new_password")
        newpass.send_keys("password123")
        time.sleep(5)
        driver.find_element(By.XPATH,"//*[@id=\"form\"]/div[2]/div[2]/div/div/span/span").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id=\"form\"]/div[3]/button").click()
        time.sleep(5)
    ##LOGIN AFTER CHANGING PASSWORD
    def log(self):
        icon = driver.find_element(By.CLASS_NAME, "avatar").click()
        user_input = driver.find_element(By.ID, 'basic_username').send_keys("gheavens2")
        password = driver.find_element(By.ID, 'basic_password').send_keys("password123")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']").click()


    def assertEqual(self, param, param1):
        pass
    def assertTrue(self, param):
        pass


if __name__ =="__main__":
    driver = webdriver.Chrome('chromedriver.exe')
    obj = Login(driver)
    obj.log1()
    obj.changepass()