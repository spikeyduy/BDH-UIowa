
## This file converted out player data into team rosters to determine relationships


class Team(str):

    def __init__(self,name):
        self.name = name
        self.rosters = {}

    def addPlayer(self, playerName, year):
        self.rosters.update
        if year in self.rosters:
            self.rosters[year].append(playerName)
        else:
            self.rosters[year] = [playerName]


class TeamsAll():
    
    def __init__(self):
        self.teams = []

    def hasTeam(self,team):
        return team in self.teams

    def addTeam(self,team):
        self.teams.append(team)

    def addToTeamRoster(self,team, playerName, year):
        appendIndex = self.teams.index(team)
        self.teams[appendIndex].addPlayer(playerName, year)      
        
        
 
def buildNodes(filename = "test.txt"):
    allTeams = TeamsAll()
    f = open(filename, "r")
    for line in f:
        endFirstNameMark = line.index("|")
        endLastNameMark = line.index(",")
        playerName = line[endLastNameMark+2:endFirstNameMark] + " " + line[0:endLastNameMark]
        x = line[(endFirstNameMark+1):].split(";")
        for teamNameYear in x[:-1]:
            teamName = teamNameYear.split(":")[0]
            year = teamNameYear.split(":")[1]
            if(allTeams.hasTeam(teamName) != 1):
                newTeam = Team(teamName)
                allTeams.addTeam(newTeam)
            allTeams.addToTeamRoster(teamName,playerName,year)

    f.close()
    wf = open("testTeamRosters.txt", "w")
    for teamName3Letters in allTeams.teams:
        writeString = teamName3Letters.name + "%" + str(teamName3Letters.rosters) + "\n"
        wf.write(writeString)
        
            
            
    
    
