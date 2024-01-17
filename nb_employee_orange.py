import requests
from bs4 import BeautifulSoup

def compte_employes(url):
    total_employes = 0
    page = 1

    while True:
        # Construire l'URL de la page actuelle avec le numéro de la page
        url_page = f"{url}?page={page}"
        
        # Effectuer la requête HTTP pour obtenir le contenu de la page
        response = requests.get(url_page)
        
        # Vérifier si la requête a réussi (code 200)
        if response.status_code == 200:
            # Analyser le contenu de la page avec BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Trouver le nombre d'employés sur la page actuelle (en utilisant votre classe spécifique)
            employes_sur_page = len(soup.find_all(class_='EMP'))
            
            # Ajouter le nombre d'employés sur la page actuelle au total
            total_employes += employes_sur_page
            
            # Vérifier s'il y a une page suivante
            next_page_link = soup.find('a', {'class': 'pagination-next'})
            if not next_page_link:
                break  # Sortir de la boucle s'il n'y a plus de pages suivantes
            
            # Passer à la page suivante
            page += 1
        else:
            print(f"Erreur lors de la récupération de la page {page}. Statut de la requête : {response.status_code}")
            break

    return total_employes

# Remplacez 'url_de_votre_site' par l'URL réelle de votre site
url_de_votre_site = 'https://example.com/employes'
total_employes = compte_employes(url_de_votre_site)

print(f"Nombre total d'employés : {total_employes}")
