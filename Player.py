class Player: 
    def __init__(self, firstName, lastName, gamesPlayed, fumbles, kickOffReturnYds, teamId):
        self.__lastName = lastName
        self.__firstName = firstName
        self.__gamesPlayed = gamesPlayed
        self.__fumbles = fumbles
        self.__teamId = teamId
        self.__kickOffReturnYds = kickOffReturnYds

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

    def get_fumbles(self):
        return self.__fumbles

    def set_fumbles(self, fumbles):
        self.__fumbles = fumbles

    def get_kickOffReturnYds(self):
        return self.__kickOffReturnYds

    def set_kickOffReturnYds(self, kickOffReturnYds):
        self.__kickOffReturnYds = kickOffReturnYds 