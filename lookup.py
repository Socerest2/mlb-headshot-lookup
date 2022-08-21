import statsapi

player = input ("Enter your player (Lastname, Firstname): " + '\n')
year = input ("Enter the year you want to see (YYYY): " + '\n')
playerid = str(statsapi.lookup_player(player)[0]['id'])
print (playerid)

headshot = ("https://img.mlbstatic.com/mlb-photos/image/upload/d_people:generic:headshot:67:current.png/w_213,q_auto:best/v1/people/" + playerid + "/headshot/67/" + year)
print (headshot)
