from general.timezone import getTimezones
from general.countries import getCountries

from football.leagues import getLeagues, getSeasons
from football.teams import getTeamInformation, getTeamStatistics

#getTeamInformation(17)

#getTimezones()
#getCountries()


# idTeam, nameTeam, idLeague, season, nameCountry, code, idVenue, search
t = getTeamStatistics('null', 'null', 33, 'null')
print(t)