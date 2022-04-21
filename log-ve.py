import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class Login:
    def __init__(self,webdriverval):
        driver=webdriverval
        driver.maximize_window()
        driver.implicitly_wait(10)
    ##LOGIN
        driver.get('https://automatedhuallocation-ui-urtjok3rza-wl.a.run.app/')
        time.sleep(5)
        driver.find_element(By.CLASS_NAME, "avatar").click()
        time.sleep(5)
        # LEAVING BOTH THE TEXT FIELDS EMPTY
        user_input = driver.find_element(By.ID, 'basic_username').send_keys("")
        time.sleep(2)
        password = driver.find_element(By.ID, 'basic_password').send_keys("")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']").click()
        expected_text = "Please input your email!"
        actual_text = driver.find_element(By.XPATH, "//div[@role='alert']")
        actual_text1 = actual_text.text
        assert expected_text == actual_text1
        print("Please input your email!....msg is displayed")
        time.sleep(5)
        #LEAVING USERNAME EMPTY
        password = driver.find_element(By.ID, 'basic_password').send_keys("password")
        time.sleep(5)
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
        expected_text = "Please input your email!"
        actual_text = driver.find_element(By.XPATH, "//div[@role='alert']")
        actual_text1 = actual_text.text
        assert expected_text == actual_text1
        print("Please input your email!....msg is displayed")
        driver.refresh()
        time.sleep(2)
        # LEAVING PASSWORD EMPTY
        driver.find_element(By.CLASS_NAME, "avatar").click()
        user_input = driver.find_element(By.ID, 'basic_username').send_keys("gheavens2")
        time.sleep(2)
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
        # LOGIN WITH GIVING INVALID USERNAME AND VALID PASSWORD
        driver.refresh()
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "avatar").click()
        time.sleep(5)
        user_input = driver.find_element(By.ID, 'basic_username').send_keys("gheavens")
        time.sleep(2)
        password = driver.find_element(By.ID, 'basic_password').send_keys("password")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
        #LOGIN WITH GIVING INVALID PASSWORD AND VALID USERNAME
        driver.refresh()
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "avatar").click()
        time.sleep(5)
        user_input = driver.find_element(By.ID, 'basic_username').send_keys("gheavens2")
        time.sleep(2)
        password = driver.find_element(By.ID, 'basic_password').send_keys("passwordd")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
        #LOGIN WITH INVALID CREDENTIALS
        driver.refresh()
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "avatar").click()
        time.sleep(5)
        user_input = driver.find_element(By.ID, 'basic_username').send_keys("gheavens")
        time.sleep(2)
        password = driver.find_element(By.ID, 'basic_password').send_keys("passwordd")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
        # LOGIN WITH VALID CREDENTIALS
        user_input = driver.find_element(By.ID, 'basic_username')
        user_input.send_keys("gheavens2")
        time.sleep(2)
        password = driver.find_element(By.ID, 'basic_password')
        password.send_keys("password")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)


if __name__ =="__main__":
    driver = webdriver.Chrome('chromedriver.exe')
    obj=Login(driver)
    obj.log1()