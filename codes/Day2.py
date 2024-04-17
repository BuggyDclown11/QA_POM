import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service('../driver/chromedriver.exe'))
driver.maximize_window()
driver.get("http://demoblaze.com")

nav_login_bar = driver.find_element(By.ID, 'login2')
nav_login_bar.click()


username_form = driver.find_element(By.ID,'loginusername')
username_form.send_keys('testmorning')
password_form = driver.find_element(By.ID,'loginpassword')
password_form.send_keys('test123')
login_button=driver.find_element(By.XPATH,'//*[@id="logInModal"]/div/div/div[3]/button[2]')
login_button.click()
time.sleep(5)

