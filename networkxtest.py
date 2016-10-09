import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt
import ast
import requests
import pylab



G=nx.MultiGraph()
teamList = open('names.txt','r') 
teamroster = open('teamRosters.txt','r')

def getNodes():
    for name in teamList.readlines():
        #  print(name.strip())
         G.add_node(name.strip())
         #print(G.number_of_nodes())
    teamList.close()

def add_attribute_to_edge(G,id_node_source,id_node_target,new_attr,value_attr):
        keydict=G[id_node_source][id_node_target]
        key=len(keydict)
        for k in keydict:
            if 'teamer' not in G.edge[id_node_source][id_node_target][k]:
                    G.add_edge(id_node_source,id_node_target,key=k,new_attr=value_attr)

def createRosters():
# create for each team, a set (no-repeat dict) 
# with all of their keys and data (year and data)
    for word in teamroster.readlines():
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
                    # could use add_path to create an auto path between them
                    #G.add_path(roster[key])     # creates too many duplicate edges
                      # if the node is in the graph, THEN do this
                    if G.has_node(roster[key][i]) & G.has_node(roster[key][i+1]):
                        G.add_edge(roster[key][i],roster[key][i+1],teamer=22,yearer=33)
                        # NEED TO CHANGE TEAMER AND YEARER
                        # adding the team value to the edge and maybe the year value?
        # print(y)
        #print(roster)
    teamroster.close()

def node_colors(G,path):
    colors = []
    for node in G.nodes():
        if node in path:
            colors.append('b')
        else:
            colors.append('r')
    return colors

def draw_shortest_path(G,pos,start,end):
        path = nx.shortest_path(G,start,end)    # may need another param
        size = len(path)
        colors = node_colors(G,path)
        edge_labels={(n1,n2):G[n1][n2] for (n1,n2) in G.edges()}
        pylab.figure(1,figsize=(8,8))
        nx.draw_networkx(G,pos,node_color=colors)
        nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
        if size > 1:
            print(start+' is '+str(size)+' degrees away from '+end)
        else:
            print(start+' is '+str(size)+' degree away from '+end)

def sixDegrees(firstplaya, secondplaya):
    # easy way, recursive? have to check the weights of the edges
    # need to put weights on the edges first
    print('nothing')

def drawthisshit():
    # nx.draw(G, node_size = 1, node_color = 'cyan')
    nx.draw(G,pos)
    #nx.draw_random(G)
    print(G.number_of_nodes())
    print(G.number_of_edges())


getNodes()
createRosters()
pos = graphviz_layout(G,prog='neato')
#drawthisshit()
draw_shortest_path(G,pos,'Bryan Anderson','Jerry Azumah')
#pylab.show()
#plt.savefig("testforNet", dpi=1000)