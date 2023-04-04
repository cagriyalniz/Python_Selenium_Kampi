from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.google.com")
input = driver.find_element(By.NAME, "q")
#sleep(2)
#print(f"input: {input}")
input.send_keys("cagri yalniz")
sleep(2)
#searchButton = driver.find_element(By.NAME, "btnK")
#searchButton.click()
input.send_keys(Keys.RETURN)#enter ile arama
sleep(2)
firstResult = driver.find_element(By.XPATH, "//*[@id='rso']/div[1]/div/div/div[1]/div/a")
firstResult.click()
sleep(5)
listOfExperience= driver.find_elements(By.CLASS_NAME,"experience__list")
print(f"len of listOfEducation: {len(listOfExperience)}")
sleep(500)
#html locators
#
#full xpath: /html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/a
#xpath: //*[@id="rso"]/div[1]/div/div/div[1]/div/a