from src.api.general.timezone import getTimezones
from src.api.general.countries import getCountries

from src.api.football.leagues import getLeagues, getSeasons
from src.api.football.teams import getTeamInformation, getTeamStatistics, getTeamSeason, getTeamCountries
from src.api.football.standings import getStandings
from src.api.football.fixtures import getRounds, getFixtures, getHeadToHead, getStatistics, getEvents, getLineups, getPlayers
from src.api.football.injuries import getInjuries
from src.api.football.coachs import getCoachs
from src.api.football.players import getPlayers, getSeasons, getSquads, getTopScorers, getTopAssists, getTopYellowCards, getTopRedCards
from src.api.football.venues import getVenues
from src.api.football.predictions import getPredictions
from src.api.football.transfers import getTransfers
from src.api.football.trophies import getTrophies
from src.api.football.sidelined import getSidelined

from src.database.connectMySql import conectar
'''
conn = conectar()

if conn:
    cursor = conn.cursor()

    # Exemplo de operação: Criando uma tabela
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS timezones (
            id INT AUTO_INCREMENT PRIMARY KEY,
            timezone VARCHAR(255) NOT NULL
        )
    """)
    
    # Confirmar a operação
    conn.commit()
    
    # Fechar a conexão
    cursor.close()
    conn.close()
    print("Operação realizada e conexão fechada.")
'''


from src.models.timezones import Timezone

Timezone()
