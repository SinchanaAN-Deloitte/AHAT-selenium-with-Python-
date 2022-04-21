import driver as driver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select


class Login:
    def __init__(self, webdriverval):
        # CHROME_DRIVER_PATH = "C:\\Users\\shrasuresh\\Downloads\\chromedriver\\chromedriver.exe"
        # service = Service(CHROME_DRIVER_PATH)
        # driver = webdriver.Chrome(service=service)
        driver = webdriverval
        driver.maximize_window()
        driver.implicitly_wait(10)

    ##LOGIN
    def login1(self):
        driver.get('https://automatedhuallocation-ui-urtjok3rza-wl.a.run.app/')
        time.sleep(5)
        driver.find_element(By.CLASS_NAME, "avatar").click()
        time.sleep(5)
        admin_input = driver.find_element(By.ID, 'basic_username')
        admin_input.send_keys("HUDIRECTOR")
        time.sleep(2)
        password = driver.find_element(By.ID, 'basic_password')
        password.send_keys("HUDIRECTOR")
        login_button = driver.find_element(By.XPATH, "//*[@id=\"basic\"]/div[3]/div/div/div/button/span")
        login_button.click()
        time.sleep(5)

    def product_track(self):
        driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div[1]/div[1]/div/div[3]/div").click()
        time.sleep(5)
    def add_new_project(self):
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/div/div[3]/div/div[1]/div[2]/button/span").click()
        time.sleep(5)
        driver.find_element(By.ID,"nest-messages_user_name").send_keys("NEW")
        driver.find_element(By.ID,"nest-messages_user_description").send_keys("New project")
        time.sleep(5)
        driver.find_element(By.XPATH,"//*[@id=\"nest-messages\"]/div[3]/button/span").click()
        time.sleep(5)
        driver.refresh()
        time.sleep(5)
        ## add new project with name and no description
        driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[1]/div/div[3]/div").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/div/div[3]/div/div[1]/div[2]/button/span").click()
        time.sleep(5)
        driver.find_element(By.ID, "nest-messages_user_name").send_keys("NEW")
        driver.find_element(By.ID, "nest-messages_user_description").send_keys("")
        time.sleep(5)
        driver.find_element(By.XPATH, "//*[@id=\"nest-messages\"]/div[3]/button/span").click()
        time.sleep(5)
        driver.refresh()
        time.sleep(5)
        ##add new project with no name and description
        driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[1]/div/div[3]/div").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/div/div[3]/div/div[1]/div[2]/button/span").click()
        time.sleep(5)
        driver.find_element(By.ID, "nest-messages_user_name").send_keys("")
        driver.find_element(By.ID, "nest-messages_user_description").send_keys("New project")
        time.sleep(5)
        driver.find_element(By.XPATH, "//*[@id=\"nest-messages\"]/div[3]/button/span").click()
        time.sleep(5)
        driver.refresh()
        time.sleep(5)
        ##add new project with no name and no description
        driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[1]/div/div[3]/div").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/div/div[3]/div/div[1]/div[2]/button/span").click()
        time.sleep(5)
        driver.find_element(By.ID, "nest-messages_user_name").send_keys("")
        driver.find_element(By.ID, "nest-messages_user_description").send_keys("")
        time.sleep(5)
        driver.find_element(By.XPATH, "//*[@id=\"nest-messages\"]/div[3]/button/span").click()
        time.sleep(5)
        driver.refresh()
        time.sleep(5)
    def download_sam(self):
        driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[1]/div/div[3]/div").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//*[@id=\"rc-tabs-0-panel-2\"]/div/div[2]/div[1]/div[1]/div[1]/a").click()
        time.sleep(5)
        ##second download
        driver.find_element(By.XPATH, "//*[@id=\"rc-tabs-0-panel-2\"]/div/div[2]/div[1]/div[2]/div[1]/a").click()
        time.sleep(5)
        driver.execute_script("window.scrollBy(0,500)", "")
        time.sleep(10)
        #third download
        driver.find_element(By.XPATH, "//*[@id=\"rc-tabs-0-panel-2\"]/div/div[2]/div[1]/div[3]/div[1]/a").click()
        time.sleep(5)
        ##fourth download
        driver.find_element(By.XPATH, "//*[@id=\"rc-tabs-0-panel-2\"]/div/div[2]/div[1]/div[4]/div[1]/a").click()
        time.sleep(5)
        ##fifth download
        driver.find_element(By.XPATH, "//*[@id=\"rc-tabs-0-panel-2\"]/div/div[2]/div[1]/div[5]/div[1]/a").click()
        time.sleep(5)
        ##perform analysis
        driver.find_element(By.XPATH,"//*[@id=\"rc-tabs-0-panel-2\"]/div/div[2]/div[2]/button/span").click()
        time.sleep(5)














if __name__ == "__main__":
 driver = webdriver.Chrome('chromedriver.exe')
obj = Login(driver)
obj.login1()
obj.product_track()
obj.add_new_project()
obj.download_sam()