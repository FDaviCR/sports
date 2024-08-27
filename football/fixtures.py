from dotenv import load_dotenv
import requests
import os

load_dotenv()
secret_key = os.getenv('SECRET_KEY')

def getRounds(league, season, current):
    url = "https://v3.football.api-sports.io/fixtures/rounds"

    headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': secret_key
    }
    
    params = {
        league,
        season,
        current
    }

    response = requests.get(url, headers=headers, params=params)

    if (response.status_code == 200):
        data = response.json()
        
        return data
    else:
        return response.status_code
        
