import ast
import igraph as ig
import plotly.plotly as py
from plotly.graph_objs import *
import random
py.sign_in('liamacrawford', 'xy31mz7ima')

def main():
    listOfTeams, teamNodes = giveTeamCodes()
    playerNodes, Xp, Yp, Zp, playerList, jumpNodes = makePlayerNodes(listOfTeams,teamNodes)


    Xe = []
    Ye = []
    Ze = []

    for jump in jumpNodes:
        Xe += [jump[0][0],jump[1][0],None]
        Ye += [jump[0][1],jump[1][1],None]
        Ze += [jump[0][2],jump[0][2],None]

    axisx=dict(showbackground=False,showline=False,zeroline=False,showgrid=True,showticklabels=True,title='Year')
    axisy=dict(showbackground=False,showline=False,zeroline=True,showgrid=True,showticklabels=False,title='Team')
    axisz=dict(showbackground=False,showline=False,zeroline=False,showgrid=False,showticklabels=False,title='')



    trace1 = Scatter3d(x=Xp,y=Yp,z=Zp,mode='markers',name='Players',marker=Marker(symbol="dot",size=1,color="rgb(50,0,0)",line=Line(color='rgp(50,0,0',width=.1)),text=playerList,hoverinfo='text')
    trace2 = Scatter3d(x=Xe,y=Ye,z=Ze,mode='lines', line=Line(color='rgb(100,0,100)',width=1),hoverinfo="none")
    layout = Layout(title="NFL Visualization", width = 1000, height=1000, showlegend = False, scene=Scene(xaxis=XAxis(axisx),yaxis=YAxis(axisy),zaxis=ZAxis(axisz),), margin=Margin(t=100), hovermode='closest')
    data=Data([trace1, trace2])
    fig=Figure(data=data, layout=layout)

    py.iplot(fig, filename="testNewDataWithEdgesR3")

def makePlayerNodes(listOfTeams,teamInfoDict):
    playerInfo = {} ## player:[indexNum,xCoord=startTeam*30000/122,yCoord=startYear*1000,zCoord=random.randrange(0:40000, 400)]
    playersX = []
    playersY = []
    playersZ = []
    playerList = []
    jumpNodes = [] ##[[(startx,starty,startz),(endx,endy,endz)]]    
    namesFile = open("allPlayers","r")
    i=0
    switches = 0
    for line in namesFile:
        endFirstNameMark = line.index("|")
        endLastNameMark = line.index(",")
        firstColon = line.index(":")
        firstSemiColon = line.index(";")
        playerName = line[endLastNameMark+2:endFirstNameMark] + " " + line[0:endLastNameMark]
        playerList.append(playerName)
        startYearXCoord = int(line[firstColon+1:firstSemiColon])
        startTeamYCoord = teamInfoDict[line[endFirstNameMark+1:firstColon]][2]
        playerZCoord = random.randrange(-120000,120000,300)
        playersX.append(startYearXCoord)
        playersY.append(startTeamYCoord)
        playersZ.append(playerZCoord)
        playerInfo[playerName] = [i, startYearXCoord, startTeamYCoord, playerZCoord]

        teamsYears = line[endFirstNameMark+1:].split(";")
        splitTeam = teamsYears[0].split(":")[0]
        splitYear = teamsYears[0].split(":")[1]
        for t in teamsYears[:-1]:
            tt = t.split(":")
            if tt[0]!= splitTeam:
                switches += 1
                jumpNodes+= [ [(splitYear, teamInfoDict[splitTeam][2],playerZCoord),(tt[1],teamInfoDict[tt[0]][2],playerZCoord)]]
                splitTeam = tt[0]
                splitYear = tt[1]          
        i+=1

    return playerInfo, playersX, playersY, playersZ, playerList, jumpNodes
        

def giveTeamCodes():
    listOfTeams = []
    teamInfoDict = {} ## team:[indexNum, xCoord=0, yCoord = index*(32000/122), zCoord = 0]
    f = open("teamRosters.txt","r")

    i=0
    for line in f:
        teamName = line[0:3]
        listOfTeams.append(teamName)
        teamInfoDict[teamName]=[i,0,i*(320000/122),0]
        i+=1
    f.close()
    return listOfTeams, teamInfoDict
        
        
        
    
            
    
