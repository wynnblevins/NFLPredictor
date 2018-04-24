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


def runPredictor():
    broncosTeamId = 72
    patriotsTeamId = 50 
    patriots2017 = Team(patriotsTeamId, "Patriots", "2017-Regular")
    broncos2017 = Team(broncosTeamId, "Broncos", "2017-Regular")
    patriots2016PO = Team(patriotsTeamId, "Patriots", "2016-playoff")
    broncos2016PO = Team(broncosTeamId, "Broncos", "2016-playoff")
    patriots2016 = Team(patriotsTeamId, "Patriots", "2016-Regular")
    broncos2016 = Team(broncosTeamId, "Broncos", "2016-Regular")
    patriots2015 = Team(patriotsTeamId, "Patriots", "2015-Regular")
    broncos2015 = Team(broncosTeamId, "Broncos", "2015-Regular")
    patriots2014 = Team(patriotsTeamId, "Patriots", "2014-Regular")
    broncos2014 = Team(broncosTeamId, "Broncos", "2014-Regular")

    totalNumOfGamesPatriots2017 = getTotalNumOfGamesPlayed(patriots2017)
    totalNumOfGamesBroncos2017 = getTotalNumOfGamesPlayed(broncos2017)
    totalNumOfGamesPatriots2016PO = getTotalNumOfGamesPlayed(patriots2016PO)
    totalNumOfGamesBroncos2016PO = getTotalNumOfGamesPlayed(broncos2016PO)
    totalNumOfGamesPatriots2016 = getTotalNumOfGamesPlayed(patriots2016)
    totalNumOfGamesBroncos2016 = getTotalNumOfGamesPlayed(broncos2016)
    totalNumOfGamesPatriots2015 = getTotalNumOfGamesPlayed(patriots2015)
    totalNumOfGamesBroncos2015 = getTotalNumOfGamesPlayed(broncos2015)
    totalNumOfGamesPatriots2014 = getTotalNumOfGamesPlayed(patriots2014)
    totalNumOfGamesBroncos2014 = getTotalNumOfGamesPlayed(broncos2014)

    totalNumberOfFumblesPatriots2017 = getTotalFumbles(patriots2017)
    totalNumberOfFumblesBroncos2017 = getTotalFumbles(broncos2017)
    totalNumberOfFumblesPatriots2016PO = getTotalFumbles(patriots2016PO)
    totalNumberOfFumblesBroncos2016PO = getTotalFumbles(broncos2016PO)
    totalNumberOfFumblesPatriots2016 = getTotalFumbles(patriots2016)
    totalNumberOfFumblesBroncos2016 = getTotalFumbles(broncos2016)
    totalNumberOfFumblesPatriots2015 = getTotalFumbles(patriots2015)
    totalNumberOfFumblesBroncos2015 = getTotalFumbles(broncos2015)
    totalNumberOfFumblesPatriots2014 = getTotalFumbles(patriots2014)
    totalNumberOfFumblesBroncos2014 = getTotalFumbles(broncos2014)

    totalNumberOfReturnYdsPatriots2017 = getTotalKickoffReturnYds(patriots2017)
    totalNumberOfReturnYdsBroncos2017 = getTotalKickoffReturnYds(broncos2017)
    totalNumberOfReturnYdsPatriots2016PO = getTotalKickoffReturnYds(patriots2016PO)
    totalNumberOfReturnYdsBroncos2016PO = getTotalKickoffReturnYds(broncos2016PO)
    totalNumberOfReturnYdsPatriots2016 = getTotalKickoffReturnYds(patriots2016)
    totalNumberOfReturnYdsBroncos2016 = getTotalKickoffReturnYds(broncos2016)
    totalNumberOfReturnYdsPatriots2015 = getTotalKickoffReturnYds(patriots2015)
    totalNumberOfReturnYdsBroncos2015 = getTotalKickoffReturnYds(broncos2015)
    totalNumberOfReturnYdsPatriots2014 = getTotalKickoffReturnYds(patriots2014)
    totalNumberOfReturnYdsBroncos2014 = getTotalKickoffReturnYds(broncos2014)

# feature = [
#     totalNumOfGamesForTeamA,
#     totalTeamFumblesForTeamA,
#     totalNumberOfReturnYdsTeamA, 
#     totalNumOfGamesForTeamB,
#     totalTeamFumblesForTeamB,
#     totalNumberOfReturnYdsTeamB 
# ]

    features = [
        # Broncos win
        [
            totalNumOfGamesPatriots2014, 
            totalNumberOfFumblesPatriots2014, 
            totalNumberOfReturnYdsPatriots2014, 
            totalNumOfGamesBroncos2014, 
            totalNumberOfFumblesBroncos2014, 
            totalNumberOfReturnYdsBroncos2014
        ], 
        # Broncos win
        # [
        #     totalNumOfGamesPatriots2015, 
        #     totalNumberOfFumblesPatriots2015, 
        #     totalNumberOfReturnYdsPatriots2015, 
        #     totalNumOfGamesBroncos2015, 
        #     totalNumberOfFumblesBroncos2015, 
        #     totalNumberOfReturnYdsBroncos2015
        # ],
        # Patriots win
        [
            totalNumOfGamesPatriots2016, 
            totalNumberOfFumblesPatriots2016, 
            totalNumberOfReturnYdsPatriots2016, 
            totalNumOfGamesBroncos2016, 
            totalNumberOfFumblesBroncos2016, 
            totalNumberOfReturnYdsBroncos2016 
        ],
        # Broncos Win
        [
            totalNumOfGamesPatriots2016, 
            totalNumberOfFumblesPatriots2016, 
            totalNumberOfReturnYdsPatriots2016, 
            totalNumOfGamesBroncos2016, 
            totalNumberOfFumblesBroncos2016, 
            totalNumberOfReturnYdsBroncos2016
        ],
        # Patriots win
        [
            totalNumOfGamesPatriots2017, 
            totalNumberOfFumblesPatriots2017, 
            totalNumberOfReturnYdsPatriots2017, 
            totalNumOfGamesBroncos2017, 
            totalNumberOfFumblesBroncos2017, 
            totalNumberOfReturnYdsBroncos2017 
        ] 
    ]

    patriotsWin = 0
    broncosWin = 1
    labels = [1, 0, 1, 0]

    clf = tree.DecisionTreeClassifier()
    clf.fit(features, labels)

    result = clf.predict([
        [
            totalNumOfGamesPatriots2015, 
            totalNumberOfFumblesPatriots2015, 
            totalNumberOfReturnYdsPatriots2015, 
            totalNumOfGamesBroncos2015, 
            totalNumberOfFumblesBroncos2015, 
            totalNumberOfReturnYdsBroncos2015 
        ]
    ])

    if (result[0] == patriotsWin): 
        return "Broncos Win"
    if (result[0] == broncosWin): 
        return "Patriots Win"
    