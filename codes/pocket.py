import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("../driver/chromedriver.exe"))
driver.maximize_window()
driver.get("https://www.pocketpandit.com")

get_started = driver.find_element(By.XPATH, '//*[@id="app"]/header/div/div/div[1]/div[2]/div/button[1]')
get_started.click()
driver
#  # time.sleep()=>>>>> freezes for 5 secs
email = driver.find_element(By.ID, "login")
email.send_keys('shresthasijal9@gmail.com')
password = driver.find_element(By.ID, "password")
password.send_keys('12345678sS')
login_btn = driver.find_element(By.XPATH,
                                '//*[@id="app"]/main/section/div/div[2]/div[2]/div/div/div/div/form/div[3]/button')
login_btn.click()
time.sleep(6)
