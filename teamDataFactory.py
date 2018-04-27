from Team import Team

def buildDataArray(teamAId, teamAName, teamBId, teamBName):
    seasons = [
        '2017-Regular',
        '2016-Regular',
        '2015-Regular'
    ]
    for season in seasons:
        generateTeamData(teamAId, teamAName, seasons[season])
        generateTeamData(teamBId, teamBName, seasons[season])

def generateTeamData(teamId, teamName, seasonStr):
    team = Team(teamId, teamName, seasonStr)
    return team