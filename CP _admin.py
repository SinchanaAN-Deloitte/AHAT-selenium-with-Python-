from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

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
        user_input.send_keys("HUDIRECTOR")
        time.sleep(2)
        password = driver.find_element(By.ID, 'basic_password')
        password.send_keys("HUDIRECTOR")
        login_button = driver.find_element(By.XPATH, "//*[@id=\"basic\"]/div[3]/div/div/div/button/span")
        login_button.click()
        time.sleep(5)
        driver.find_element(By.CLASS_NAME,"user-avatar").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//*[@id=\"root\"]/div/div[1]/div[3]/div[2]/div/a/div[1]/span/img").click()
        time.sleep(5)
        driver.find_element(By.CLASS_NAME,"ant-dropdown-menu-title-content").click()
        time.sleep(5)
        oldpass=driver.find_element(By.ID,"form_user_old_password")
        oldpass.send_keys("ALLOCATION123")
        time.sleep(5)
        driver.find_element(By.XPATH,"//*[@id=\"form\"]/div[1]/div[2]/div/div/span/span/span").click()
        time.sleep(5)
        newpass = driver.find_element(By.ID,"form_user_new_password")
        newpass.send_keys("password1")
        time.sleep(5)
        driver.find_element(By.XPATH,"//*[@id=\"form\"]/div[2]/div[2]/div/div/span/span").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id=\"form\"]/div[3]/button").click()
        time.sleep(5)

if __name__ =="__main__":
    driver = webdriver.Chrome('chromedriver.exe')
    obj=Login(driver)
    obj.log1()