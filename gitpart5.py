# HOMEWORK ASSIGNMENT 3
from sys import maxsize as maxi
#FUNCTION TO INPUT GLOBAL LISTS
def lists_input(n=5,connections=[],weights=[]):
    T=''
    for i in range (n):
        x =[]
        z =[]
        T = int(input())
        for j in range(T):
            y =str(input())
            y =y.split(' ')
            x.append(int(y[0])) 
            z.append(int(y[1])) 
        weights.append(z)
        connections.append(x)


        
#FUNCTION TO SOLVE DIJKSTRA'S SINGLE SOURCE SHORTEST PATH PROBLEM
def dijkstra(a,graph):
    #SPLITTING THE GRAPH BACK INTO CONNECTIONS,WEIGHTS
    connections=graph[0]
    weights=graph[1]
    #LIST OF UNVISITED VERTICES
    Q=[]
    #LIST CONTAINING DIJKSTRA DISTANCE 
    dist =[]
    
    # FOR LOOP TO INITIALISE ((Q WITH ALL THE VERTICES)) AND ((DIST WITH INFINITY))
    for i in range(len(connections)):
        dist.append(maxi)
        Q.append(i)

    dist[a] = 0

    while len(Q) > 0:
        # LIST CONTAINING DISTANCES FROM SOURCE OF VERICES PRESENT IN Q
        dist_copy =[]
        for i in Q:
            dist_copy.append(dist[i])

        #FINDING THE VERTEX NUMBER AT MINIMUM DISTANCE   
        for i in Q:
            if min(dist_copy)== dist[i]:
                u = i
                break 
    
        Q.remove(u)

        #GETTING THE DISTANCES OF THAT VERTEX'S NEIGHBOURS
        i=0
        for v in connections[u]:
            temp = dist[u] + weights[u][i]
            dist[v] = min(dist[v],temp)
            #INCREMENTING IT  TO ACCESS THE NEXT INDEX OF WEIGHT
            i+=1

    #RETURNING THE DIJKSTRA DISTANCE
    return dist