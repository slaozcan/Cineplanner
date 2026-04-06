import requests
from bs4 import BeautifulSoup
import json
import random

def scrape_real_movies_and_sessions(city, target_date):
    """
    Gerçek Web Kazıma (Web Scraping) metodu ile vizyondaki filmleri çeker.
    """
    url = "https://www.sinemalar.com/filmler/vizyondaki"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    
    scraped_movies = []
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            movie_elements = soup.find_all('h2')
            
            # Sinemalar.com'daki h2 etiketlerini geziyoruz
            for item in movie_elements:
                film_adi = item.text.strip()
                if not film_adi or film_adi in ["Vizyona Girecek Filmler", "En Çok Beklenen Filmler"]:
                    continue
                
                if len(scraped_movies) >= 6: # Çok fazla film olmasın, ilk 6 popüler filmi alalım
                    break
                
                # Gerçek web kazıma sonucunda seansları anlık çekmek için
                # her bir filmin detayına veya sinema bazlı sayfasına gitmek gerekir.
                # Demo amaçlı vizyondaki "Gerçek" filmleri aldık, 
                # Seansları dinamik oluşturuyoruz.
                
                theaters = [
                    {"sinema_adi": f"{city} Paribu Cineverse", "seanslar": ["11:00", "14:30", "18:00", "21:15"], "bilet_linki": "https://www.paribucineverse.com"},
                    {"sinema_adi": f"{city} Biletinial Salonu", "seanslar": ["12:15", "15:45", "19:30"], "bilet_linki": "https://www.biletinial.com"}
                ]
                
                scraped_movies.append({
                    "film_adi": film_adi,
                    "temiz_film_adi": film_adi, # Arama için ekstra eklenti olmayan salt isim.
                    "salonlar": theaters
                })
                
        return json.dumps({"movies": scraped_movies})

    except Exception as e:
        print(f"Scraping Error: {e}")
        return json.dumps({"movies": []})
