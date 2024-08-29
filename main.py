from general.timezone import getTimezones
from general.countries import getCountries

from football.leagues import getLeagues, getSeasons
from football.teams import getTeamInformation, getTeamStatistics, getTeamSeason, getTeamCountries
from football.standings import getStandings
from football.fixtures import getRounds, getFixtures, getHeadToHead, getStatistics, getEvents, getLineups, getPlayers
from football.injuries import getInjuries
from football.coachs import getCoachs
from football.players import getPlayers, getSeasons, getSquads, getTopScorers, getTopAssists, getTopYellowCards, getTopRedCards
from football.venues import getVenues
from football.predictions import getPredictions
from football.transfers import getTransfers
from football.trophies import getTrophies
from football.sidelined import getSidelined

from database.connectMySql import conectar

conn = conectar()

if conn:
    cursor = conn.cursor()

    # Exemplo de operação: Criando uma tabela
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS funcionarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            cargo VARCHAR(255),
            salario DECIMAL(10, 2),
            data_contratacao DATE
        )
    """)
    
    # Confirmar a operação
    conn.commit()
    
    # Fechar a conexão
    cursor.close()
    conn.close()
    print("Operação realizada e conexão fechada.")