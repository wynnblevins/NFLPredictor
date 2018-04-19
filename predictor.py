from sklearn import tree
import base64
import requests
from requests.auth import HTTPDigestAuth
import json
 
class Player: 
    def __init__(self, firstName, lastName, gamesPlayed, teamId):
        self.__lastName = lastName
        self.__firstName = firstName
        self.__gamesPlayed = gamesPlayed
        self.__teamId = teamId
        
    def get_lastName(self):
        return self.__lastName

    def set_lastName(self, lastName):
        self.__lastName = lastName

    def get_firstName(self):
        return self.__firstName

    def set_firstName(self, firstName):
        self.__firstName = firstName

    def get_teamId(self):
        return self.__teamId

    def set_teamId(self, teamId):
        self.__teamId = teamId

    def get_gamesPlayed(self):
        return self.__gamesPlayed

    def set_gamesPlayed(self, gamesPlayed):
        self.__gamesPlayed = gamesPlayed

class Team: 
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__players = []

        url = "https://api.mysportsfeeds.com/v1.2/pull/nfl/2018-playoff/cumulative_player_stats.json?playerstats=Att,Comp,Yds,TD&team=" + str(self.get_id()) 
        usrPass = ""
        b64Val = base64.b64encode(usrPass)
        response = requests.get(url, headers={"Authorization": "Basic %s" % b64Val})

        content = json.loads(response.content)
        cumulativeplayerstats = content["cumulativeplayerstats"]
        playerStats = cumulativeplayerstats["playerstatsentry"]

        for responseObj in playerStats:
            firstName = responseObj["player"]["FirstName"]
            lastName = responseObj["player"]["LastName"]
            teamUni = responseObj["team"]["ID"] 
            gamesPlayed = responseObj["stats"]["GamesPlayed"]     
            
            player = Player(firstName, lastName, gamesPlayed, teamUni)
            self.add_to_team(player)
            
    def add_to_team(self, player):
        self.__players.append(player)        

    def get_players(self):
        return self.__players

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

def getTotalNumOfGamesPlayed(team):
    totalGamesPlayed = 0
    for player in team.get_players():
        gamesPlayed = player.get_gamesPlayed()
        totalGamesPlayed += int(gamesPlayed["#text"]) 
    return totalGamesPlayed

# team definitions here
titans = Team(67, "Titans")
patriots = Team(50, "Patriots")

totalNumOfGamesPackers = getTotalNumOfGamesPlayed(titans)
totalNumOfGamesPatriots = getTotalNumOfGamesPlayed(patriots)

features = [[totalNumOfGamesPatriots], [totalNumOfGamesPackers]]
labels = [1, 0]

clf = tree.DecisionTreeClassifier()
clf.fit(features, labels)

print clf.predict([[180]])
