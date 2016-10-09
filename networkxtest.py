import networkx as nx
import matplotlib.pyplot as plt
import ast


G=nx.MultiGraph()
teamList = open('names.txt','r') 
teamroster = open('teamRosters.txt','r')

def getNodes():
    for name in teamList.readlines()[:2]:
        #  print(name.strip())
         G.add_node(name.strip())
         #print(G.number_of_nodes())
    teamList.close()

def createRosters():
# create for each team, a set (no-repeat dict) 
# with all of their keys and data (year and data)
    for word in teamroster.readlines()[:1]:
        roster = word[0:3]
        #print(word[4:])
        roster = ast.literal_eval(word[4:word.index('\n')])
        # for each one, find out who played at what and match them up
        for key in roster:
            # for each key of roster?
            # use the i to load the Key
            # roster[i] will load the individual name
            if len(roster[key])>1:    # if there is more than 1 data piece
                #print(roster[key])
                for i in range(len(roster[key])-1):
                    # for j in range(len(roster[key])):
                        # duplicate edges?
                        # set up them into sets?
                        # G.add_edge(roster[key][i],roster[key][j])
                    # G.add_edges_from(roster[key])
                    G.add_edge(roster[key][i],roster[key][i+1])
        # print(y)
        #print(roster)
    teamroster.close()

def drawthisshit():
    nx.draw(G, node_size = 100, node_color = 'cyan')
    #nx.draw_random(G)
    print(G.number_of_nodes())
    print(G.number_of_edges())

getNodes()
createRosters()
drawthisshit()
plt.savefig("testforNet")