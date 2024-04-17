import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service('../driver/chromedriver.exe'))
driver.maximize_window()
driver.get("http://demoblaze.com")

nav_login_bar = driver.find_element(By.ID, 'login2')
nav_login_bar.click()
# username_form = driver.find_element(By.ID,'loginusername')
# WebDriverWait(driver,10).until(EC.element_to_be_clickable(username_form))
###### webDriverWait waits for a particular element until it doesnt render it waits


#####  above 2 line code can be written as this
username_form = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'loginusername')))

username_form.send_keys('testmorning')
password_form = driver.find_element(By.ID, 'loginpassword')
password_form.send_keys('test123')
login_button = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
login_button.click()
time.sleep(5)
