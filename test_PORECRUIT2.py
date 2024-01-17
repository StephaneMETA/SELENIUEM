# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class OPRECRUIT1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # Maximisez la fenêtre du navigateur
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_o_p_r_e_c_r_u_i_t1(self):
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
        driver.find_element(By.XPATH, "//div[@id='app']/div/div/aside/nav/div[2]/ul/li[5]/a/span").click()
        
       
     
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")
        
        time.sleep(5)
        driver.save_screenshot("screenshot-avant.png")
        time.sleep(5)
        
        # Enregistrez le contenu de la liste avant l'ajout de l'élément
        candidat_list_class_avant = driver.find_elements(By.CLASS_NAME, "oxd-table-card")
        print ("nb candidat parclass avant",len(candidat_list_class_avant))
        #print(f'nb candidat class: {len(candidat_list_class)}')
     
        # candidat_list_selector = driver.find_elements(By.CSS_SELECTOR, ".oxd-table-card")
        # print(f'nb candidat selector: {len(candidat_list_selector)}')
        
        # candidat_list_path = driver.find_elements(By.XPATH, "//div[@class='orangehrm-container']/div/div[@class='oxd-table-body']/div[@class='oxd-table-card']")
        # # candidat_list_path = (0,1)
        # print(f'nb candidat xpath: {len(candidat_list_path)}')
        
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div[2]/div/button/i").click()
        
       # time.sleep(5)
        
     

        
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/addCandidate")
        driver.find_element(By.NAME, "firstName").click()
        driver.find_element(By.NAME, "firstName").clear()
        driver.find_element(By.NAME, "firstName").send_keys("maurice")
        driver.find_element(By.NAME, "lastName").clear()
        driver.find_element(By.NAME, "lastName").send_keys("betoun betoun")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/div/div/div").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/input").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/input").send_keys("mb@gmail.com")
          
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        driver.find_element(By.LINK_TEXT, "Candidates").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")
        
        time.sleep(5)
        driver.save_screenshot("screenshot-apres.png")
        candidat_list_path_apres = driver.find_elements(By.XPATH, "//div[@class='oxd-table-card']")
        # candidat_list_path = (0,1)
        print(f'nb candidat xpath apres: {len(candidat_list_path_apres)}')
        time.sleep(5)
                
        # Enregistrez le contenu de la liste après  l'ajout de l'élément
        candidat_list_class_apres = driver.find_elements(By.CLASS_NAME, "oxd-table-card")
        print ("nb candidat parclass apres",len(candidat_list_class_apres))
        #print(f'nb candidat class: {len(candidat_list_class)}')
        
        self.assertEqual(len(candidat_list_class_apres), len(candidat_list_class_avant)+1, "Le nombre de candidat a bien augmenté de 1")
        
       
        
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
