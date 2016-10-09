## going to try and do py

import ast
import igraph as ig
import plotly.plotly as py
from plotly.graph_objs import *
import random

py.sign_in(,) ## enter your credentials ('username','API Key')


def main():
    playerDictIndex, playerList, numPlayers = buildDictofPlayerNodeLocations() ## {playerName:numTarget/Source}
    edgesTuples = list(edgesSet(playerDictIndex)) ## [(source player, target player)]
    Xn = [i*(random.uniform(-1.05, 1)*1000) for i in range(numPlayers)]
    Yn = [i*(random.uniform(-1.05, 1)*1000) for i in range(numPlayers)]
    Zn = [i*(random.uniform(-1.05,1.05)*1000) for i in range(numPlayers)]
    axis=dict(showbackground=False,
          showline=False,
          zeroline=False,
          showgrid=False,
          showticklabels=False,
          title=''
          )

    Xe = []
    Ye = []
    Ze = []

    for e in edgesTuples[:250000]:
        source = e[0]
        dest = e[1]
        Xe+=[Xn[source],Xn[e[1]], None]
        Ye+=[Yn[source],Yn[e[1]], None]
        Ze+=[Zn[source],Zn[e[1]], None]
        
    
    trace1 = Scatter3d(x=Xn,y=Yn,z=Zn,mode='markers',name='actors',marker=Marker(symbol="dot",size=1,color="rgb(50,0,0)",line=Line(color='rgp(50,50,50',width=.2)),text=playerList,hoverinfo='text')
    trace2 = Scatter3d(x=Xe,y=Ye,z=Ze,mode='lines', line=Line(color='rgb(0,0,200)',width=1),hoverinfo="none")
    layout = Layout(title="NoneT", width = 1000, height=1000, showlegend = False, scene=Scene(xaxis=XAxis(axis),yaxis=YAxis(axis),zaxis=ZAxis(axis),), margin=Margin(t=100), hovermode='closest')
    data=Data([trace1, trace2])
    fig=Figure(data=data, layout=layout)
    py.iplot(fig, filename="testWithEdges3")


def edgesSet(playerDictIndex):
    EdgesTuples = []
    rostersFile = open("teamRosters.txt", "r") ## TeamRoster File - Builds Edges
    for line in rostersFile:
        teamName = line[0:3]
        rostersDict = ast.literal_eval(line[4:line.index('\n')])
        for rosterThatYear in rostersDict:
            i = 0;
            for playerSource in rostersDict[rosterThatYear]:
                for playerTarget in rostersDict[rosterThatYear][(i+1):]:
                    newTuple = (playerDictIndex[playerSource][0],playerDictIndex[playerTarget][0])
                    EdgesTuples.append(newTuple)
                    ## make tuple and store
                i+=1
    ee = set(EdgesTuples)
    return ee
    
                        


def buildDictofPlayerNodeLocations():
    playerDictIndex = {}
    playerList =[]
    numPlayers = 0
    f = open("names.txt",'r') ## List of Names File - Builds dict to find numerical representation of nodes
    for line in f:
        playerNodeValue = numPlayers
        playerDictIndex[line.split("\n")[0]] = [playerNodeValue, playerNodeValue*1.05]
        playerList.append(line.split("\n")[0])
        numPlayers += 1
    return playerDictIndex, playerList, numPlayers
        
    
