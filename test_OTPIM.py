# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

import requests
# pip install beautifulsoup4

from bs4 import BeautifulSoup

class OTPIM(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_o_t_p_i_m(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.NAME, "username").click()
        driver.find_element(By.NAME, "username").clear()
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").clear()
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        driver.find_element(By.LINK_TEXT, "PIM").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div[2]/div/button").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee")
        driver.find_element(By.NAME, "firstName").click()
        driver.find_element(By.NAME, "firstName").clear()
        driver.find_element(By.NAME, "firstName").send_keys("raoul")
        driver.find_element(By.NAME, "lastName").clear()
        driver.find_element(By.NAME, "lastName").send_keys("raoul")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/63")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div/aside/nav/div[2]/ul/li[2]/a/span").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div/header/div/div[2]/ul/li/span/i").click()
        
        
        liste_employes = driver.find_elements(By.XPATH, "//div[@class='oxd-table-card --mobile']/div")
        assert len(liste_employes) == 50, "Le nombre d'éléments dans le panier n'est pas égal à 3"
        
        employes_list_before = driver.find_elements(By.CLASS_NAME, "oxd-table-card")
        print("l1", len(employes_list_before))
        
        employes_list_after = driver.find_elements(By.CSS_SELECTOR, ".oxd-table-card")
        print("l2", len(employes_list_after))
        
        #=========================================
        

        # url = 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList'
        # total_employes = 0
        # page = 1

        # while True:
        #      # Construire l'URL de la page actuelle avec le numéro de la page
        #    # url_page = f"{url}?page={page}"
        #     url_page = url if page == 1 else f"{url}?page={page}"
        #     print (url_page)
    
        #     # Effectuer la requête HTTP pour obtenir le contenu de la page
        #     response = requests.get(url_page)
    
        #     # Vérifier si la requête a réussi (code 200)
        #     if response.status_code == 200:
        #         # Analyser le contenu de la page avec BeautifulSoup
        #         soup = BeautifulSoup(response.text, 'html.parser')
        
        #         # Trouver le nombre d'employés sur la page actuelle (en utilisant votre classe spécifique)
        #         employes_sur_page = len(soup.find_all(class_='oxd-table-card'))
        
        #         # Ajouter le nombre d'employés sur la page actuelle au total
        #         total_employes += employes_sur_page
        
        #          # Vérifier s'il y a une page suivante
        #         next_page_link = soup.find('a', {'class': 'pagination-next'})
        #         if not next_page_link:
        #             break  # Sortir de la boucle s'il n'y a plus de pages suivantes
        
        #         # Passer à la page suivante
        #         page += 1
        #     else:
        #             print(f"Erreur lors de la récupération de la page {page}. Statut de la requête : {response.status_code}")
        #             break

        # print(f"Nombre total d'employés : {total_employes}")

        
        #============================================

        
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
