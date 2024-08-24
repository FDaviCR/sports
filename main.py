from general.timezone import getTimezones
from general.countries import getCountries

from football.leagues import getLeagues, getSeasons
from football.teams import getTeamInformation

#getTeamInformation(17)

#getTimezones()
#getCountries()
t = getSeasons()
print(t)