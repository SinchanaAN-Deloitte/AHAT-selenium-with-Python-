import driver as driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select



class Login:
    def __init__(self, webdriverval):
        driver = webdriverval
        driver.maximize_window()
        driver.implicitly_wait(10)

 ##LOGIN
    def login1(self):
        driver.get('https://automatedhuallocation-ui-urtjok3rza-wl.a.run.app/')
        time.sleep(5)
        assert driver.find_element(By.CLASS_NAME, "avatar").is_displayed() == True
        print("icon is visible")
        assert driver.find_element(By.CLASS_NAME, "avatar").is_enabled() == True
        print("icon is clickable")
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

 ##ADMIN PROFILE
    def admin(self):
        ##INSTRUCTION MANUAL
        instruction_manual = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div/div[1]/div")
        instruction_manual.click()
        driver.execute_script("window.scrollBy(0,4000)", "")
        # target = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div/div[2]/div")
        # driver.execute_script('arguments[0].scrollIntoView(true);', target)
        # driver.execute_script("window.scrollBy(0,4000)", "")
        time.sleep(5)

 ##PARALLEL TRACK
    # def parallel(self):

        # parallel_track = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div/div[2]/div")
        # parallel_track.click()
    #     #MARKS ALLOCATED
    #     time.sleep(5)
    #     marks_alloted = driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/div[2]/div[4]/div[2]/div[2]/div/div/h2/button")
    #     marks_alloted.click()
    #     driver.execute_script("window.scrollBy(1500,2500)", "")
    #     time.sleep(5)
    #     marks_alloted = driver.find_element(By.XPATH,"//*[@id=\"root\"]/div/div[2]/div[4]/div[2]/div[2]/div/div/h2/button")
    #     marks_alloted.click()
    #     ##SECTION LEAD INSIGHTS
    #     time.sleep(5)
    #     section_lead = driver.find_element(By.XPATH,"//*[@id=\"root\"]/div/div[2]/div[4]/div[2]/div[3]/div/div/h2/button")
    #     section_lead.click()
    #     driver.execute_script("window.scrollBy(2500,3000)", "")
    #     time.sleep(5)
    #     section_lead = driver.find_element(By.XPATH,"//*[@id=\"root\"]/div/div[2]/div[4]/div[2]/div[3]/div/div/h2/button")
    #     section_lead.click()
    #     time.sleep(2)
    # def preference(self):
    #     driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/div[2]/div[3]/div[1]/button/span").click()
    #     time.sleep(5)
    #     dd = driver.find_element(By.XPATH, "//*[@id=\"vertical-tabpanel-0\"]/div/p/button")
    #     sel = Select(dd)
    #     sel.select_by_visible_text('IOT')
    #     time.sleep(2)
    # def changepass(self):
    #     driver.find_element_by_class_name("user-avatar").click()

if __name__ == "__main__":
 driver = webdriver.Chrome('chromedriver.exe')
obj = Login(driver)
obj.login1()
obj.admin()
# obj.parallel()
# obj.preference()
# obj.changepass()
