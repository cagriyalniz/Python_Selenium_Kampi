from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class Test_Sauce:
    def test_invalid_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        usernameInput = driver.find_element(By.ID, "user-name")
        userpassInput = driver.find_element(By.ID, "password")
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(5)
        usernameInput.send_keys("1")
        userpassInput.send_keys("1")
        sleep(2)
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        #print(f"errorMessage: {errorMessage.text}")
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"testResult: {testResult}")
        #sleep(500)
testClass = Test_Sauce()
testClass.test_invalid_login()

