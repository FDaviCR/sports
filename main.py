from general.timezone import getTimezones
from general.countries import getCountries

from football.leagues import getLeagues, getSeasons
from football.teams import getTeamInformation, getTeamStatistics, getTeamSeason, getTeamCountries
from football.standings import getStandings
from football.fixtures import getRounds, getFixtures, getHeadToHead, getStatistics

#getTeamInformation(17)

#getTimezones()
#getCountries()


# idTeam, nameTeam, idLeague, season, nameCountry, code, idVenue, search
t = getTeamCountries
print(t)