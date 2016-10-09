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
    for name in teamList.readlines()[:1000]:    #fix this, too long
        # too long: takes too much time to query through
        # and will take too long to go anything above 1000-2000
        #  print(name.strip())
         G.add_node(name.strip())
         #print(G.number_of_nodes())
    teamList.close()

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
                    if G.has_node(roster[key][i]) & G.has_node(roster[key][i+1]):
                        G.add_edge(roster[key][i],roster[key][i+1],year=key)    # makes the edge have the common year
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
        # have to fix this. Goes through EVERY PATH to find shortest
        path = nx.shortest_path(G,start,end)    
        size = len(path)-1  # how many degrees away
        colors = node_colors(G,path)
        edge_labels={(n1,n2):G[n1][n2] for (n1,n2) in G.edges()}
        pylab.figure(1,figsize=(500,500))   # size of plot
        nx.draw_networkx(G,pos,node_color=colors)  
        nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
        if size > 1:
            print(start+' is '+str(size)+' degrees away from '+end)
            for i in range(size):
                # should we do a forloop where we just say 'he is connected to this guy'
                print(str(path[i]) + ' >>> '+ str(path[i+1]))
        else:
            print(start+' is '+str(size)+' degree away from '+end)

def draw_bfs_path(G,pos,start,end):
        path=nx.bfs_tree(G,start)
        size = 0
        queue=[]
        queue.append([start])
        while queue:
            pather = queue.pop(0)
            node = pather[-1]
            if node == end:
                print(pather)
            for adjacent in path:
                new_pather = list(path)
                new_pather.append(adjacent)
                queue.append(new_pather)
            # print(queue)

        colors = node_colors(G,path)
        edge_labels={(n1,n2):G[n1][n2] for (n1,n2) in G.edges()}
        pylab.figure(1,figsize=(500,500))
        nx.draw_networkx(G,pos,node_color=colors)
        nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)

def drawthis():
    # nx.draw(G, node_size = 1, node_color = 'cyan')
    nx.draw(G,pos)
    #nx.draw_random(G)
    #print(G.number_of_nodes())
    #print(G.number_of_edges())


getNodes()
createRosters()
pos = graphviz_layout(G,prog='neato')
drawthis()
draw_shortest_path(G,pos,'Donnie Abraham','Cliff Aberson')
#draw_bfs_path(G,pos,'Donnie Abraham','Cliff Aberson')
pylab.show()
#plt.savefig("testforNet", dpi=1000)