from dotenv import load_dotenv
import requests
import os

load_dotenv()
secret_key = os.getenv('SECRET_KEY')


def getTeamInformation(idTeam, nameTeam, idLeague, season, nameCountry, code, idVenue, search):
    url = "https://v3.football.api-sports.io/teams"

    headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': secret_key
    }

    params = {
        'id': idTeam,
        'name': nameTeam, 
        'league': idLeague, 
        'season': season, 
        'country': nameCountry, 
        'code': code, 
        'venue': idVenue, 
        'search': search
    }

    response = requests.get(url, headers=headers, params=params)

    if (response.status_code == 200):
        data = response.json()
        print("Dados recebidos:", data)
        
        return data
    else:
        print("Erro na requisição:", response.status_code)
        
def getTeamStatistics(idLeague, season, idTeam, date):
    url = "https://v3.football.api-sports.io/teams"

    headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': secret_key
    }

    params = {
        'league': idLeague, 
        'season': season, 
        'team': idTeam,
        'date': date
    }

    response = requests.get(url, headers=headers, params=params)

    if (response.status_code == 200):
        data = response.json()
        print("Dados recebidos:", data)
        
        return data
    else:
        print("Erro na requisição:", response.status_code)
        
    
