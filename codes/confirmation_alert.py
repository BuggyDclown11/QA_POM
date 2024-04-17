import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(service=Service('../driver/chromedriver.exe'))
driver.maximize_window()
driver.get('https://demo.automationtesting.in/Alerts.html')


confirmation_alert=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a')
confirmation_alert.click()
click_btn=driver.find_element(By.XPATH,'//*[@id="CancelTab"]/button')
click_btn.click()
time.sleep(5)
driver.switch_to.alert.dismiss()
time.sleep(5)