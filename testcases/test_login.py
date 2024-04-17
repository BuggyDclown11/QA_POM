import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from pages.login import Login


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service('../driver/chromedriver.exe'))
        self.driver.maximize_window()
        self.driver.get("http://demoblaze.com")

    def test_something(self):
        l = Login(self.driver)
        l.loginUser('testmorning', 'test123')
        time.sleep(5)
        actual_result = self.driver.find_element(By.ID, 'nameofuser').text
        expected_result = 'Welcome testmorning'
        self.assertEqual(expected_result, actual_result, 'User didint matchs')  # add assertion here

    def test_failedcase(self):
        l = Login(self.driver)
        l.loginUser('testmorning', 'skjkjkdjshakhdsa')
        time.sleep(5)
        self.driver.switch_to.alert.accept()
        self.assertEqual(True, False, 'password not match')


if __name__ == '__main__':
    unittest.main()
