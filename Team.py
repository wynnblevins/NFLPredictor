from Player import Player
import base64
import requests
from requests.auth import HTTPDigestAuth
import json
from restconfig import REST_CONFIG

class Team: 
    def __init__(self, id, name, season):
        self.__id = id
        self.__name = name
        self.__players = []

        url = REST_CONFIG['base_url'] + season + "/cumulative_player_stats.json?playerstats=Att,Comp,Yds,TD&team=" + str(self.get_id())
        usrPass =  REST_CONFIG['username'] + ':' + REST_CONFIG['password']
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
            kickOffReturns = responseObj["stats"].get("KrYds")

            # Get fumbles     
            fumbles = 0
            if "FumTD" in responseObj["stats"]: 
                fumbles = responseObj["stats"]["FumTD"]
            
            player = Player(firstName, lastName, gamesPlayed, 
                fumbles, kickOffReturns, teamUni)
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