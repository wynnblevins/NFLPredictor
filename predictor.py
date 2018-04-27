from sklearn import tree
import base64
import requests
from requests.auth import HTTPDigestAuth
import json
from Team import Team

def getTotalNumOfGamesPlayed(team):
    totalGamesPlayed = 0
    for player in team.get_players():
        gamesPlayed = player.get_gamesPlayed()
        totalGamesPlayed += int(gamesPlayed["#text"]) 
    return totalGamesPlayed

def getTotalFumbles(team):
    totalFumbles = 0
    for player in team.get_players():
        fumbles = player.get_fumbles()
        if (fumbles):
            totalFumbles += int(fumbles["#text"])
    return totalFumbles

def getTotalKickoffReturnYds(team):
    totalKickoffReturnYds = 0
    for player in team.get_players():
        returnYds = player.get_kickOffReturnYds()
        if (returnYds):
            totalKickoffReturnYds += int(returnYds["#text"])
    return totalKickoffReturnYds

def createTeamStatsStr(teamName, totalNumOfGames, fumbles, returnYds):
    statStr = str(teamName) + ": games played: " + str(totalNumOfGames) + ", fumbles: " + str(fumbles) + ", return Yds: " + str(returnYds) + "\n"
    return statStr


def runPredictor(teamAId, teamAName, teamBId, teamBName):
    teamA2017 = Team(teamAId, teamAName, "2017-Regular")
    teamB2017 = Team(teamBId, teamBName, "2017-Regular")
    teamA2016PO = Team(teamAId, teamAName, "2016-playoff")
    teamB2016PO = Team(teamBId, teamBName, "2016-playoff")
    teamA2016 = Team(teamAId, teamAName, "2016-Regular")
    teamB2016 = Team(teamBId, teamBName, "2016-Regular")
    teamA2015 = Team(teamAId, teamAName, "2015-Regular")
    teamB2015 = Team(teamBId, teamBName, "2015-Regular")
    teamA2014 = Team(teamAId, teamAName, "2014-Regular")
    teamB2014 = Team(teamBId, teamBName, "2014-Regular")

    totalNumOfGamesTeamA2017 = getTotalNumOfGamesPlayed(teamA2017)
    totalNumOfGamesTeamB2017 = getTotalNumOfGamesPlayed(teamB2017)
    totalNumOfGamesTeamA2016PO = getTotalNumOfGamesPlayed(teamA2016PO)
    totalNumOfGamesTeamB2016PO = getTotalNumOfGamesPlayed(teamB2016PO)
    totalNumOfGamesTeamA2016 = getTotalNumOfGamesPlayed(teamA2016)
    totalNumOfGamesTeamB2016 = getTotalNumOfGamesPlayed(teamB2016)
    totalNumOfGamesTeamA2015 = getTotalNumOfGamesPlayed(teamA2015)
    totalNumOfGamesTeamB2015 = getTotalNumOfGamesPlayed(teamB2015)
    totalNumOfGamesTeamA2014 = getTotalNumOfGamesPlayed(teamA2014)
    totalNumOfGamesTeamB2014 = getTotalNumOfGamesPlayed(teamB2014)

    totalNumberOfFumblesTeamA2017 = getTotalFumbles(teamA2017)
    totalNumberOfFumblesTeamB2017 = getTotalFumbles(teamB2017)
    totalNumberOfFumblesTeamA2016PO = getTotalFumbles(teamA2016PO)
    totalNumberOfFumblesTeamB2016PO = getTotalFumbles(teamB2016PO)
    totalNumberOfFumblesTeamA2016 = getTotalFumbles(teamA2016)
    totalNumberOfFumblesTeamB2016 = getTotalFumbles(teamB2016)
    totalNumberOfFumblesTeamA2015 = getTotalFumbles(teamA2015)
    totalNumberOfFumblesTeamB2015 = getTotalFumbles(teamB2015)
    totalNumberOfFumblesTeamA2014 = getTotalFumbles(teamA2014)
    totalNumberOfFumblesTeamB2014 = getTotalFumbles(teamB2014)

    totalNumberOfReturnYdsTeamA2017 = getTotalKickoffReturnYds(teamA2017)
    totalNumberOfReturnYdsTeamB2017 = getTotalKickoffReturnYds(teamB2017)
    totalNumberOfReturnYdsTeamA2016PO = getTotalKickoffReturnYds(teamA2016PO)
    totalNumberOfReturnYdsTeamB2016PO = getTotalKickoffReturnYds(teamB2016PO)
    totalNumberOfReturnYdsTeamA2016 = getTotalKickoffReturnYds(teamA2016)
    totalNumberOfReturnYdsTeamB2016 = getTotalKickoffReturnYds(teamB2016)
    totalNumberOfReturnYdsTeamA2015 = getTotalKickoffReturnYds(teamA2015)
    totalNumberOfReturnYdsTeamB2015 = getTotalKickoffReturnYds(teamB2015)
    totalNumberOfReturnYdsTeamA2014 = getTotalKickoffReturnYds(teamA2014)
    totalNumberOfReturnYdsTeamB2014 = getTotalKickoffReturnYds(teamB2014)

    features = [
        [
            totalNumOfGamesTeamA2014, 
            totalNumberOfFumblesTeamA2014, 
            totalNumberOfReturnYdsTeamA2014, 
            totalNumOfGamesTeamB2014, 
            totalNumberOfFumblesTeamB2014, 
            totalNumberOfReturnYdsTeamB2014
        ], 
        # [
        #     totalNumOfGamesTeamA2015, 
        #     totalNumberOfFumblesTeamA2015, 
        #     totalNumberOfReturnYdsTeamA2015, 
        #     totalNumOfGamesTeamB2015, 
        #     totalNumberOfFumblesTeamB2015, 
        #     totalNumberOfReturnYdsTeamB2015
        # ],
        [
            totalNumOfGamesTeamA2016, 
            totalNumberOfFumblesTeamA2016, 
            totalNumberOfReturnYdsTeamA2016, 
            totalNumOfGamesTeamB2016, 
            totalNumberOfFumblesTeamB2016, 
            totalNumberOfReturnYdsTeamB2016
        ],
        [
            totalNumOfGamesTeamA2017, 
            totalNumberOfFumblesTeamA2017, 
            totalNumberOfReturnYdsTeamA2017, 
            totalNumOfGamesTeamB2017, 
            totalNumberOfFumblesTeamB2017, 
            totalNumberOfReturnYdsTeamB2017
        ] 
    ]

    labels = [1, 0, 1, 0]
    clf = tree.DecisionTreeClassifier()
    clf.fit(features, labels)

    result = clf.predict([
        [
            totalNumOfGamesTeamA2015, 
            totalNumberOfFumblesTeamA2015, 
            totalNumberOfReturnYdsTeamA2015, 
            totalNumOfGamesTeamB2015, 
            totalNumberOfFumblesTeamB2015, 
            totalNumberOfReturnYdsTeamB2015
        ]
    ])

    if (result[0] == 0): 
        return teamBName + " Win"
    if (result[0] == 1): 
        return teamAName + " Win"
    