import time

import driver as driver
from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    def __init__(self, webdriverval):
        driver = webdriverval
        driver.maximize_window()
        driver.implicitly_wait(10)

 ##LOGIN WITH VALID USERNAME AND INVALID PASSWORD
    def login1(self):
        driver.get('https://automatedhuallocation-ui-urtjok3rza-wl.a.run.app/')
        time.sleep(5)
        driver.find_element(By.CLASS_NAME, "avatar").click()
        time.sleep(5)
        admin_input = driver.find_element(By.ID, 'basic_username')
        admin_input.send_keys("HUDIRECTOR")
        time.sleep(2)
        password = driver.find_element(By.ID, 'basic_password')
        password.send_keys("HUD")
        login_button = driver.find_element(By.XPATH, "//*[@id=\"basic\"]/div[3]/div/div/div/button/span")
        login_button.click()
        time.sleep(5)
        driver.refresh()
        time.sleep(5)
##LOGIN WITH INVALID USERNAME AND VALID PASSWORD
        driver.find_element(By.CLASS_NAME, "avatar").click()
        time.sleep(5)
        admin_input = driver.find_element(By.ID, 'basic_username')
        admin_input.send_keys("HUD")
        time.sleep(2)
        password = driver.find_element(By.ID, 'basic_password')
        password.send_keys("HUDIRECTOR")
        login_button = driver.find_element(By.XPATH, "//*[@id=\"basic\"]/div[3]/div/div/div/button/span")
        login_button.click()
        time.sleep(5)
        driver.refresh()
        time.sleep(5)
##LOGIN WITH INVALID USERNAME AND INVALID PASSWORD
        driver.find_element(By.CLASS_NAME, "avatar").click()
        time.sleep(5)
        admin_input = driver.find_element(By.ID, 'basic_username')
        admin_input.send_keys("HUD")
        time.sleep(2)
        password = driver.find_element(By.ID, 'basic_password')
        password.send_keys("TOR")
        login_button = driver.find_element(By.XPATH, "//*[@id=\"basic\"]/div[3]/div/div/div/button/span")
        login_button.click()
        time.sleep(5)
        driver.refresh()
        time.sleep(5)
##LOGIN WITH ONLY VALID USERNAME
        driver.find_element(By.CLASS_NAME, "avatar").click()
        time.sleep(5)
        admin_input = driver.find_element(By.ID, 'basic_username')
        admin_input.send_keys("HUDIRECTOR")
        time.sleep(2)
        password = driver.find_element(By.ID, 'basic_password')
        password.send_keys("")
        login_button = driver.find_element(By.XPATH, "//*[@id=\"basic\"]/div[3]/div/div/div/button/span")
        login_button.click()
        time.sleep(5)
        driver.refresh()
        time.sleep(5)
##LOGIN WITH ONLY VALID PASSWORD
        driver.find_element(By.CLASS_NAME, "avatar").click()
        time.sleep(5)
        admin_input = driver.find_element(By.ID, 'basic_username')
        admin_input.send_keys("")
        time.sleep(2)
        password = driver.find_element(By.ID, 'basic_password')
        password.send_keys("HUDIRECTOR")
        login_button = driver.find_element(By.XPATH, "//*[@id=\"basic\"]/div[3]/div/div/div/button/span")
        login_button.click()
        time.sleep(5)
        driver.refresh()
        time.sleep(5)
##LOGIN WITHOUT USERNAME AND PASSWORD
        driver.find_element(By.CLASS_NAME, "avatar").click()
        time.sleep(5)
        admin_input = driver.find_element(By.ID, 'basic_username')
        admin_input.send_keys("")
        time.sleep(2)
        password = driver.find_element(By.ID, 'basic_password')
        password.send_keys("")
        login_button = driver.find_element(By.XPATH, "//*[@id=\"basic\"]/div[3]/div/div/div/button/span")
        login_button.click()
        time.sleep(5)
        driver.refresh()
        time.sleep(5)








if __name__ == "__main__":
 driver = webdriver.Chrome('chromedriver.exe')
 obj = Login(driver)
 obj.login1()