from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

class Login:
    def __init__(self,webdriverval):
        driver=webdriverval
        driver.maximize_window()
        driver.implicitly_wait(10)
    ##LOGIN
    def log1(self):
        driver.get('https://huallocation-backend-urtjok3rza-wl.a.run.app/admin/login/?next=/admin/')
        time.sleep(5)
        # LEAVING BOTH THE TEXT FIELDS EMPTY
        user_input = driver.find_element(By.ID, 'id_username').send_keys("")
        time.sleep(2)
        password = driver.find_element(By.ID, 'id_password').send_keys("")
        login_button = driver.find_element(By.XPATH, "//input[@value='Log in']")
        login_button.click()
        '''expected_text = "Please input your email!"
        actual_text = driver.find_element(By.XPATH, "//div[@role='alert']")
        actual_text1 = actual_text.text
        assert expected_text == actual_text1
        print("Please input your email!....msg is displayed")'''
        time.sleep(5)
        # LEAVING USERNAME EMPTY
        password = driver.find_element(By.ID, 'id_password').send_keys("HUDIRECTOR")
        time.sleep(5)
        login_button = driver.find_element(By.XPATH, "//input[@value='Log in']")
        login_button.click()
        time.sleep(5)
        driver.refresh()
        time.sleep(2)
        # LEAVING PASSWORD EMPTY
        user_input = driver.find_element(By.ID, 'id_username').send_keys("HUDIRECTOR")
        time.sleep(2)
        login_button = driver.find_element(By.XPATH, "//input[@value='Log in']")
        login_button.click()
        # LOGIN WITH GIVING INVALID USERNAME AND VALID PASSWORD
        driver.refresh()
        user_input = driver.find_element(By.ID, 'id_username').send_keys("gheavens")
        time.sleep(2)
        password = driver.find_element(By.ID, 'id_password').send_keys("HUDIRECTOR")
        time.sleep(2)
        login_button = driver.find_element(By.XPATH, "//input[@value='Log in']")
        login_button.click()
        # LOGIN WITH GIVING INVALID PASSWORD AND VALID USERNAME
        driver.refresh()
        user_input = driver.find_element(By.ID, 'id_username').clear()
        time.sleep(2)
        user_input = driver.find_element(By.ID, 'id_username').send_keys("HUDIRECTOR")
        time.sleep(2)
        password = driver.find_element(By.ID, 'id_password').send_keys("passwordd")
        login_button = driver.find_element(By.XPATH, "//input[@value='Log in']")
        login_button.click()
        # LOGIN WITH INVALID CREDENTIALS
        driver.refresh()
        user_input = driver.find_element(By.ID, 'id_username').clear()
        time.sleep(2)
        time.sleep(2)
        user_input = driver.find_element(By.ID, 'id_username').send_keys("gheavens")
        time.sleep(2)
        password = driver.find_element(By.ID, 'id_password').send_keys("passwordd")
        login_button = driver.find_element(By.XPATH, "//input[@value='Log in']")
        login_button.click()
        driver.refresh()
        user_input = driver.find_element(By.ID, 'id_username').clear()
        time.sleep(2)
        time.sleep(2)
        user_input = driver.find_element(By.ID, 'id_username')
        user_input.send_keys("HUDIRECTOR")
        time.sleep(2)
        password = driver.find_element(By.ID, 'id_password')
        password.send_keys("HUDIRECTOR")
        login_button = driver.find_element(By.XPATH, "//input[@value='Log in']")
        login_button.click()
        time.sleep(5)
        #changepassword
        change_password = driver.find_element(By.XPATH, "//*[@id=\"user-tools\"]/a[2]")
        change_password.click()
        time.sleep(5)
        #old_password = driver.find_element(By.ID, 'id_old_password')
        #old_password.send_keys("HUDIRECTOR")
        #time.sleep(3)
        #new_password = driver.find_element(By.ID, 'id_new_password1')
        #new_password.send_keys("ALLOCATION123")
        #time.sleep(3)
        #confirm_new_password = driver.find_element(By.ID, 'id_new_password2')
        #confirm_new_password.send_keys("ALLOCATION123")
        #By leaving all three fields empty
        old_password = driver.find_element(By.ID, 'id_old_password')
        old_password.send_keys("")
        time.sleep(3)
        new_password = driver.find_element(By.ID, 'id_new_password1')
        new_password.send_keys("")
        time.sleep(3)
        confirm_new_password = driver.find_element(By.ID, 'id_new_password2')
        confirm_new_password.send_keys("")
        time.sleep(3)
        change_password = driver.find_element(By.XPATH,"//input[@value='Change my password']").click()
        time.sleep(3)
        driver.refresh()
        # LOGIN WITH ONLY ENTERING OLD PASSWORD
        old_password = driver.find_element(By.ID, 'id_old_password')
        old_password.send_keys("HUDIRECTOR")
        time.sleep(3)
        new_password = driver.find_element(By.ID, 'id_new_password1')
        new_password.send_keys("")
        time.sleep(3)
        confirm_new_password = driver.find_element(By.ID, 'id_new_password2')
        confirm_new_password.send_keys("")
        time.sleep(3)
        change_password = driver.find_element(By.XPATH, "//input[@value='Change my password']").click()
        time.sleep(3)
        driver.refresh()
        #LOGIN WITH ONLY ENTERING NEW PASSWORD
        old_password = driver.find_element(By.ID, 'id_old_password')
        old_password.send_keys("")
        time.sleep(3)
        new_password = driver.find_element(By.ID, 'id_new_password1')
        new_password.send_keys("HUDIRECTOR")
        time.sleep(3)
        confirm_new_password = driver.find_element(By.ID, 'id_new_password2')
        confirm_new_password.send_keys("")
        time.sleep(3)
        change_password = driver.find_element(By.XPATH,"//input[@value='Change my password']").click()
        time.sleep(3)
        driver.refresh()
        #LOGIN WITH ONLY ENTERING CONFIRMPASSWORD
        old_password = driver.find_element(By.ID, 'id_old_password')
        old_password.send_keys("")
        time.sleep(3)
        new_password = driver.find_element(By.ID, 'id_new_password1')
        new_password.send_keys("")
        time.sleep(3)
        confirm_new_password = driver.find_element(By.ID, 'id_new_password2')
        confirm_new_password.send_keys("HUDIRECTOR")
        change_password = driver.find_element(By.XPATH, "//input[@value='Change my password']").click()
        time.sleep(3)
        driver.refresh()

        #driver.find_element_by_xpath("//*[@id=\"content-main\"]/form/div/div/input").click()
        #time.sleep(5)

        #Logout
        #logout = driver.find_element(By.XPATH, "//*[@id=\"user-tools\"]/a[3]")
        #logout.click()
        #Linkers Data
        driver.find_element(By.XPATH,"//a[@href='/admin/HUAllocation/linkerdata/']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//a[@href='/admin/HUAllocation/linkerdata/701/change/']").click()
        time.sleep(10)
        #trackresults
        driver.find_element(By.XPATH, "//a[@href='/admin/HUAllocation/trackresult/']").click()
        time.sleep(10)
        driver.find_element(By.XPATH, "//a[@href='/admin/HUAllocation/trackresult/715/change/']").click()
        time.sleep(10)
        #trackallocated
        driver.find_element(By.XPATH, "//a[@href='/admin/HUAllocation/trackallocated/']").click()
        time.sleep(10)
        driver.find_element(By.XPATH, "//a[@href='/admin/HUAllocation/trackallocated/1/change/']").click()
        time.sleep(10)
        #sectionleads
        driver.find_element(By.XPATH, "//a[@href='/admin/HUAllocation/sectionlead/']").click()
        time.sleep(10)
        driver.find_element(By.XPATH, "//a[@href='/admin/HUAllocation/sectionlead/701/change/']").click()
        time.sleep(10)
        #notifys
        driver.find_element(By.XPATH, "//a[@href='/admin/HUAllocation/notif/']").click()
        time.sleep(10)
        driver.find_element(By.XPATH, "//a[@href='/admin/HUAllocation/notif/103/change/']").click()
        time.sleep(10)
        #parallelpref
        driver.find_element(By.XPATH, "//a[@href='/admin/HUAllocation/parallelpref/']").click()
        time.sleep(10)
        driver.find_element(By.XPATH, "//a[@href='/admin/HUAllocation/parallelpref/703/change/']").click()
        time.sleep(10)
        # paralleltracks
        driver.find_element(By.XPATH, "//a[@href='/admin/HUAllocation/paralleltrack/']").click()
        time.sleep(10)
        driver.find_element(By.XPATH, "//a[@href='/admin/HUAllocation/paralleltrack/33/change/']").click()
        time.sleep(10)
        # parallelallocated
        driver.find_element(By.XPATH, "//a[@href='/admin/HUAllocation/productallocated/']").click()
        time.sleep(10)
        driver.find_element(By.XPATH, "//a[@href='/admin/HUAllocation/productallocated/1/change/']").click()
        time.sleep(10)
        #productdetail
        driver.find_element(By.XPATH, "//a[@href='/admin/HUAllocation/productdetail/']").click()
        time.sleep(10)
        driver.find_element(By.XPATH, "//a[@href='/admin/HUAllocation/productdetail/320/change/']").click()
        time.sleep(10)
        # productpref
        driver.find_element(By.XPATH, "//a[@href='/admin/HUAllocation/productpref/']").click()
        time.sleep(10)
        driver.find_element(By.XPATH, "//a[@href='/admin/HUAllocation/productpref/701/change/']").click()
        time.sleep(10)
        # Logout
        logout = driver.find_element(By.XPATH, "//*[@id=\"user-tools\"]/a[3]")
        logout.click()




if __name__ =="__main__":
    driver = webdriver.Chrome('chromedriver.exe')
    obj=Login(driver)
    obj.log1()