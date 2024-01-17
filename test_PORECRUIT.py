# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class OTRECRUIT(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_o_t_r_e_c_r_u_i_t(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.NAME, "username").click()
        driver.find_element(By.NAME, "username").clear()
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").click()
        driver.find_element(By.NAME, "password").clear()
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        driver.find_element(By.LINK_TEXT, "Recruitment").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")
        driver.find_element(By.LINK_TEXT, "Vacancies").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewJobVacancy")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div[2]/div/button/i").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/addJobVacancy")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div/div[2]/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div/div[2]/input").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div/div[2]/input").send_keys("scrum masteree")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div[2]/div/div[2]/div/div/div").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[2]/div/div/div[2]/textarea").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[2]/div/div/div[2]/textarea").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[2]/div/div/div[2]/textarea").send_keys("coucou")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[3]/div/div/div[2]/div/div/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[3]/div/div/div[2]/div/div/input").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[3]/div/div/div[2]/div/div/input").send_keys("Odis  Adalwin")
       # driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[3]/div[2]/div/div/div/div[2]/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[3]/div[2]/div/div/div/div[2]/input").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[3]/div[2]/div/div/div/div[2]/input").send_keys("1")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[4]/div/div/label/span").click()
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div/header/div/div[2]/ul/li/span/i").click()
        driver.find_element(By.LINK_TEXT, "Logout").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
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
