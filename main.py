from general.timezone import getTimezones
from general.countries import getCountries

from football.leagues import getLeagues, getSeasons
from football.teams import getTeamInformation, getTeamStatistics, getTeamSeason, getTeamCountries

#getTeamInformation(17)

#getTimezones()
#getCountries()


# idTeam, nameTeam, idLeague, season, nameCountry, code, idVenue, search
t = getTeamCountries
print(t)