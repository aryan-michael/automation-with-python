from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from login_info import *


class instaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        time.sleep(2)
        
        login_field = self.driver.find_element(By.NAME, "username")
        login_field.send_keys(self.username)
        login_field = self.driver.find_element(By.NAME, "password")
        login_field.send_keys(self.password)
        login_field.send_keys(Keys.RETURN)
        
        time.sleep(10)

        login_field = self.driver.find_element(By.CLASS_NAME, "_ac8f").click()
        time.sleep(3)
        login_field = self.driver.find_element(By.XPATH, "//button[contains(.,'Not Now')]").click()
        time.sleep(10)
    
instaBot(username, password)

