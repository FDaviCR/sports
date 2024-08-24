from general.timezone import getTimezones
from general.countries import getCountries

from football.leagues import getLeagues, getSeasons
from football.teams import getTeamInformation

#getTeamInformation(17)

#getTimezones()
#getCountries()


# idTeam, nameTeam, idLeague, season, nameCountry, code, idVenue, search
t = getTeamInformation(33, 'null', 'null', 'null', 'null', 'null', 'null', 'null')
print(t)