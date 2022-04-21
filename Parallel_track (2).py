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
        ##PARRALLEL TRACK BUTTON IS CLICKABLE

    def par(self):
        parallel_track = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div/div[2]/div")
        parallel_track.click()
        # driver.execute_script("window.scrollBy(0,4000)", "")
        time.sleep(5)

        #ADD NEW TRACK BUTTON IS CLICKABLE

        add_new = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/button")
        add_new.click()
        time.sleep(5)
    #
    #
    #
    #     ##ADD NEW TRACK BUTTON IS CLICKABLE WITH VALID NAME AND VALID CAPACITY
        add_name = driver.find_element(By.ID, "nest-messages_user_name")
        add_name.send_keys("IOT")
        add_cap = driver.find_element(By.ID, "nest-messages_user_capacity")
        add_cap.send_keys(20)
        time.sleep(5)
        driver.find_element(By.XPATH,"//body[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/form[1]/div[3]/button[1]/span[1]").click()
        time.sleep(3)
        driver.refresh()
        time.sleep(5)
    # #
    #     ##ADD NEW TRACK IS CLICKABLE WITH VALID NAME AND EMPTY CAPACITY
        parallel_track = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div/div[2]/div")
        parallel_track.click()
        # driver.execute_script("window.scrollBy(0,4000)", "")
        time.sleep(5)
        add_new = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/button")
        add_new.click()
        time.sleep(5)
        add_name = driver.find_element(By.ID, "nest-messages_user_name")
        add_name.send_keys("IOT")
        time.sleep(5)
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[3]/button/span").click()
        time.sleep(5)
        driver.refresh()
        time.sleep(5)
    #
    #     ##ADD NEW TRACK IS CLICKABLE WITH EMPTY NAME AND VALID CAPACITY
        parallel_track = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div/div[2]/div")
        parallel_track.click()
        # # driver.execute_script("window.scrollBy(0,4000)", "")
        time.sleep(5)
        add_new = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/button")
        add_new.click()
        time.sleep(5)
        add_name = driver.find_element(By.ID, "nest-messages_user_name")
        add_name.send_keys("")
        add_cap = driver.find_element(By.ID, "nest-messages_user_capacity")
        add_cap.send_keys(20)
        time.sleep(5)
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[3]/button/span").click()
        time.sleep(5)
        driver.refresh()
        driver.implicitly_wait(10)
    #
    #     ##ADD NEW TRACK IS CLICKABLE WITH EMPTY NAME AND EMPTY CAPACITY
        parallel_track = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div/div[2]/div")
        parallel_track.click()
        # # driver.execute_script("window.scrollBy(0,4000)", "")
        time.sleep(5)
        add_new = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/button")
        add_new.click()
        time.sleep(5)
        add_name = driver.find_element(By.ID, "nest-messages_user_name")
        add_name.send_keys("")
        add_cap = driver.find_element(By.ID, "nest-messages_user_capacity")
        add_cap.send_keys()
        time.sleep(5)
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[3]/button/span").click()
        time.sleep(5)
        driver.refresh()
        driver.implicitly_wait(10)

    ##Check IF CHOOSE FILE IS CLICKABLE OR NOT FOR UPLOAD LINKERS DATA
    # def choose_file(self):
    #     parallel_track = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div/div[2]/div")
    #     parallel_track.click()
    #     # driver.execute_script("window.scrollBy(0,4000)", "")
    #     time.sleep(5)
    #     s = driver.find_element(By.XPATH("(//input[@class='choose'])[1]")).get_attribute("innerHTML")
    #     # file path specified with send_keys
    #     s.send_keys("C:\\Users\\shrasuresh\\Downloads\\linkerdata (1).csv")
    #     # driver.find_element(By.XPATH, "(//input[@class='choose'])[1]").click()
    #     # WebElement uploadElement = driver.find_element(By.XPATH("(//input[@class='choose'])[1]"))
    #     # uploadElement.sendKeys("C:\\Users\\shrasuresh\\Downloads\\linkerdata (1).csv")

    #     time.sleep(5)

    #CHECK DOWNLOAD SAMPLE FOR UPLOAD LINKERS DATA
    def download(self):
        parallel_track = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div/div[2]/div")
        parallel_track.click()
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[1]/a").click()
        time.sleep(5)


    ##CHECK DOWNLOAD SAMPLE FOR UPLOAD TRACK RESULTS DATA
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/a").click()
        time.sleep(5)

        # ##CHECK SHOW UPLOADED FILE FOR UPLOAD TRACK RESULTS DATA
        # driver.find_element(By.XPATH, "(//button[@class='showfile btn btn-primary'])[2]").click()
        # time.sleep(5)
        # driver.find_element(By.XPATH, "(//button[@class='showfile btn btn-primary'])[2]").click()
        # time.sleep(5)
        driver.execute_script("window.scrollBy(0,500)", "")
        time.sleep(10)



    ##CHECK DOWNLOAD SAMPLE FOR UPLOAD TRACK PARALLEL DETAILS
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/a").click()
        time.sleep(5)
        # driver.execute_script("window.scrollBy(0,200)", "")
        # time.sleep(5)



    ##CHECK DOWNLOAD SAMPLE FOR UPLOAD SECTION LEAD MARKS
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/div[4]/div[1]/a").click()
        time.sleep(5)
        # driver.execute_script("window.scrollBy(0,200)", "")

    ##CHECK DOWNLOAD SAMPLE FOR UPLOAD TRACK PREFERANCES
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/div[5]/div[1]/a").click()
        time.sleep(5)
    ##perform analysis
        driver.find_element(By.XPATH,"//*[@id=\"rc-tabs-0-panel-2\"]/div/div[2]/div[2]/button/span").click()
        time.sleep(5)












    #
    # ##CHECK SHOW UPLOADED FILE FOR UPLOAD TRACK PREFERANCES
    #     driver.find_element(By.XPATH, "(//button[@class='showfile btn btn-primary'])[5]").click()
    #     time.sleep(5)
    #     driver.find_element(By.XPATH, "(//button[@class='showfile btn btn-primary'])[5]").click()
    #     time.sleep(5)





if __name__ == "__main__":
    # driver = webdriver.Chrome('chromedriver.exe')
    CHROME_DRIVER_PATH = "C:\\Users\\shrasuresh\\Downloads\\chromedriver\\chromedriver.exe"
    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service)
obj = Login(driver)
obj.login1()
obj.par()
# obj.choose_file()
obj.download()
# obj.show_file()
