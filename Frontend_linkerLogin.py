from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Login:
    def __init__(self,webdriverval):
        driver=webdriverval
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get('https://automatedhuallocation-ui-urtjok3rza-wl.a.run.app/')
        time.sleep(5)
    ##LOGIN PAGE
    def log1(self):
        icon = driver.find_element(By.CLASS_NAME, "avatar")
        assert icon.is_displayed()==True
        print("Icon is visible")
        assert icon.is_enabled()==True
        print("Icon is Clickble")
        icon.click()
        time.sleep(3)
        cancel=driver.find_element(By.XPATH,"//div[@class='ant-space-item']")
        self.assertEqual(True, cancel.is_displayed())
        print("Cancel button is visible")
        self.assertTrue(cancel.is_enabled())
        print("cancel button is clickable")
        cancel.click()
        time.sleep(3)
        icon.click()
        user_input = driver.find_element(By.ID, 'basic_username')
        self.assertEqual(True, user_input.is_displayed())
        print("user input text field is displayed on web page")
        time.sleep(5)
        user_input.send_keys("gheavens2")
        time.sleep(2)
        password = driver.find_element(By.ID, 'basic_password')
        self.assertEqual(True, password.is_displayed())
        print("password text field is displayed on web page")
        time.sleep(5)
        password.send_keys("password")
        eyel=driver.find_element(By.XPATH,"//span[@class='anticon anticon-eye-invisible ant-input-password-icon']")
        self.assertEqual(True, eyel.is_displayed())
        print("eye icon is visible")
        self.assertTrue(eyel.is_enabled())
        print("Eye icon is clickable:Password is visible")
        eyel.click()
        time.sleep(2)
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        self.assertEqual(True, login_button.is_displayed())
        print("Submit button is visible")
        self.assertTrue(login_button.is_enabled())
        print("Submit button is Clickable")
        login_button.click()
        time.sleep(5)
    #USER PROFILE
    def user(self):
        profile = driver.find_element(By.XPATH, "//div[@class='info1']")
        self.assertEqual(True, profile.is_displayed())
        print("Successful Login User Profile is Visible")
        time.sleep(5)
    def grades(self):
    # GRADES ACHIEVED
        grades_achieved = driver.find_element(By.XPATH, "//h2[@class='accordion-header']")
        self.assertEqual(True, grades_achieved.is_displayed())
        print("Grades Achieved field is Visible")
        time.sleep(5)
        self.assertTrue(grades_achieved.is_enabled())
        print("Grades Achieved drop down is clickable")
        grades_achieved.click()
        driver.execute_script("window.scrollBy(0,2000)", "")
        time.sleep(5)
        grades_achieved = driver.find_element(By.XPATH, "//h2[@class='accordion-header']")
        grades_achieved.click()
        time.sleep(5)
    def marks(self):
    #MARKS ALLOCATED
        marks_alloted = driver.find_element(By.XPATH,"//*[@id=\"root\"]/div/div[2]/div[4]/div[2]/div[2]/div/div/h2/button")
        self.assertEqual(True, marks_alloted.is_displayed())
        print("Marks Allocated field is Visible")
        time.sleep(5)
        self.assertTrue(marks_alloted.is_enabled())
        print("Marks Allocated drop down is clickable")
        marks_alloted.click()
        driver.execute_script("window.scrollBy(1500,2500)", "")
        time.sleep(5)
        marks_alloted = driver.find_element(By.XPATH,"//*[@id=\"root\"]/div/div[2]/div[4]/div[2]/div[2]/div/div/h2/button")
        marks_alloted.click()
        time.sleep(5)
    def lead(self):
    #SECTION LEAD INSIGHTS
        section_lead = driver.find_element(By.XPATH,"//*[@id=\"root\"]/div/div[2]/div[4]/div[2]/div[3]/div/div/h2/button")
        self.assertEqual(True, section_lead.is_displayed())
        print("Section lead insights field is Visible")
        time.sleep(5)
        self.assertTrue(section_lead.is_enabled())
        print("Section lead insights drop down is clickable")
        section_lead.click()
        driver.execute_script("window.scrollBy(2500,3000)", "")
        time.sleep(5)
        section_lead = driver.find_element(By.XPATH,"//*[@id=\"root\"]/div/div[2]/div[4]/div[2]/div[3]/div/div/h2/button")
        section_lead.click()
        time.sleep(5)
    def notis(self):
    #NOTIFICATION PANEL
        notifs = driver.find_element(By.CLASS_NAME, "user-avatar")
        self.assertEqual(True, notifs.is_displayed())
        print("Notifications panel is visible in user profile")
        self.assertTrue(notifs.is_enabled())
        print("Notifications panel is clickable")
        notifs.click()
        time.sleep(5)
    def logout(self):
        driver.find_element(By.XPATH,"//span[@class='ant-avatar ant-avatar-circle ant-avatar-image']").click()
        time.sleep(10)
        logo=driver.find_element(By.XPATH, "/html/body/div[4]/div/div/ul/li[3]").click()
        obj.log1()

    def assertEqual(self, param, param1):
        pass

    def assertTrue(self, param):
        pass
if __name__ =="__main__":
    driver = webdriver.Chrome('chromedriver.exe')
    obj=Login(driver)
    obj.log1()
    obj.user()
    obj.grades()
    obj.marks()
    obj.lead()
    obj.notis()
    obj.logout()