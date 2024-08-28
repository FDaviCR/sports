from dotenv import load_dotenv
import requests
import os

load_dotenv()
secret_key = os.getenv('SECRET_KEY')


def getSeasons(idPlayer):
    url = "https://v3.football.api-sports.io/players/seasons"

    headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': secret_key
    }
    
    params = {
        idPlayer
    }

    response = requests.get(url, headers=headers, params=params)

    if (response.status_code == 200):
        data = response.json()
        
        return data
    else:
        return response.status_code

def get(fixture):
    url = "https://v3.football.api-sports.io/"

    headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': secret_key
    }
    
    params = {
        fixture
    }

    response = requests.get(url, headers=headers, params=params)

    if (response.status_code == 200):
        data = response.json()
        
        return data
    else:
        return response.status_code

def get(fixture):
    url = "https://v3.football.api-sports.io/"

    headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': secret_key
    }
    
    params = {
        fixture
    }

    response = requests.get(url, headers=headers, params=params)

    if (response.status_code == 200):
        data = response.json()
        
        return data
    else:
        return response.status_code

def get(fixture):
    url = "https://v3.football.api-sports.io/"

    headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': secret_key
    }
    
    params = {
        fixture
    }

    response = requests.get(url, headers=headers, params=params)

    if (response.status_code == 200):
        data = response.json()
        
        return data
    else:
        return response.status_code

def get(fixture):
    url = "https://v3.football.api-sports.io/"

    headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': secret_key
    }
    
    params = {
        fixture
    }

    response = requests.get(url, headers=headers, params=params)

    if (response.status_code == 200):
        data = response.json()
        
        return data
    else:
        return response.status_code

def get(fixture):
    url = "https://v3.football.api-sports.io/"

    headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': secret_key
    }
    
    params = {
        fixture
    }

    response = requests.get(url, headers=headers, params=params)

    if (response.status_code == 200):
        data = response.json()
        
        return data
    else:
        return response.status_code
