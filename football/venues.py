from dotenv import load_dotenv
import requests
import os

load_dotenv()
secret_key = os.getenv('SECRET_KEY')

def getVenues(idVenue, nameVenue, cityVenue, countryVenue, search):
    url = "https://v3.football.api-sports.io/countries"

    headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': secret_key
    }
    
    params = {
        'id': idVenue,
        'name': nameVenue, 
        'city': cityVenue, 
        'country': countryVenue,
        'search': search
    }

    response = requests.get(url, headers=headers, params=params)

    if (response.status_code == 200):
        data = response.json()
        
        return data
    else:
        return response.status_code
        
