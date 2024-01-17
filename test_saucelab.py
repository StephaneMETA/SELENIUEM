# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Test1(unittest.TestCase):
    def test_login22(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID,"user-name").click()
        driver.find_element(By.ID,"user-name").clear()
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        driver.find_element(By.ID,"password").click()
        driver.find_element(By.ID,"password").clear()
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        driver.find_element(By.ID,"login-button").click()
        
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_1(self):
        driver = self.driver
        self.test_login22();
        
        driver.get("https://www.saucedemo.com/inventory.html")
        driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light").click()
        driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.XPATH,"//div[@id='shopping_cart_container']/a/span").click()
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.XPATH,"//div[@id='root']/div/div[2]/div[2]/div").click()
        driver.find_element(By.ID,"login_credentials").click()
        driver.find_element(By.ID,"login_credentials").click()
        #ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=login_credentials | ]]
        driver.find_element(By.ID,"user-name").click()
        driver.find_element(By.ID,"user-name").clear()
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        driver.find_element(By.XPATH,"//div[@id='root']/div/div[2]/div[2]/div/div[2]").click()
        driver.find_element(By.XPATH,"//div[@id='root']/div/div[2]/div[2]/div/div[2]").click()
        #ERROR: Caught exception [ERROR: Unsupported command [doubleClick | xpath=//div[@id='root']/div/div[2]/div[2]/div/div[2] | ]]
        driver.find_element(By.ID,"password").click()
        driver.find_element(By.ID,"password").clear()
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        driver.find_element(By.ID,"login-button").click()
        driver.save_screenshot("Login.png")
        driver.find_element(By.LINK_TEXT,"2").click()
        driver.find_element(By.ID,"checkout").click()
        driver.find_element(By.ID,"first-name").click()
        driver.find_element(By.ID,"first-name").clear()
        driver.find_element(By.ID,"first-name").send_keys(u"Stéphane")
        driver.find_element(By.ID,"last-name").clear()
        driver.find_element(By.ID,"last-name").send_keys("Bernardini")
        driver.save_screenshot("Login2.png")
        driver.find_element(By.ID,"postal-code").clear()
        driver.find_element(By.ID,"postal-code").send_keys("06600")
        driver.find_element(By.ID,"postal-code").click()
        driver.find_element(By.ID,"continue").click()
        driver.find_element(By.ID,"finish").click()
        driver.find_element(By.ID,"back-to-products").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
