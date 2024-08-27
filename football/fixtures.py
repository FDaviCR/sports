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
        
def getFixtures(id, ids, live, date, league, season, team, last, next, fromDat, to, round, status, venue, timezone):
    url = "https://v3.football.api-sports.io/fixtures"

    headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': secret_key
    }
    
    params = {
        'id': id, 
        'ids': ids, 
        'live': live, 
        'date': date, 
        'league': league, 
        'season': season, 
        'team': team, 
        'last': last, 
        'next': next, 
        'from': fromDat, 
        'to': to, 
        'round': round, 
        'status': status, 
        'venue': venue, 
        'timezone': timezone
    }

    response = requests.get(url, headers=headers, params=params)

    if (response.status_code == 200):
        data = response.json()
        
        return data
    else:
        return response.status_code

def getHeadToHead(h2h, date, last, next, fromDat, to, round, status, venue, timezone):
    url = "https://v3.football.api-sports.io/fixtures/headtohead"

    headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': secret_key
    }
    
    params = {
        'h2h': h2h,
        'date': date,
        'last': last, 
        'next': next, 
        'from': fromDat, 
        'to': to, 
        'round': round, 
        'status': status, 
        'venue': venue, 
        'timezone': timezone
    }

    response = requests.get(url, headers=headers, params=params)

    if (response.status_code == 200):
        data = response.json()
        
        return data
    else:
        return response.status_code

def getStatistics(fixture, team, type):
    url = "https://v3.football.api-sports.io/fixtures/statistics"

    headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': secret_key
    }
    
    params = {
        fixture,
        team,
        type
    }

    response = requests.get(url, headers=headers, params=params)

    if (response.status_code == 200):
        data = response.json()
        
        return data
    else:
        return response.status_code

