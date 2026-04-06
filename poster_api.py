import requests
import os
from dotenv import load_dotenv

load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

def get_movie_poster(movie_name):
    """Film ismine göre TMDB'den afiş URL'sini çeker."""
    if not TMDB_API_KEY: return "https://via.placeholder.com/500"
    url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={movie_name}"
    try:
        response = requests.get(url).json()
        if response.get('results'):
            path = response['results'][0]['poster_path']
            return f"https://image.tmdb.org/t/p/w500{path}"
    except: pass
    return "https://via.placeholder.com/500x750?text=Afis+Yok"