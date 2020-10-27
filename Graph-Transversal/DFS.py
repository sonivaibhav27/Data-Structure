from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,e1,e2):
        self.graph[e1].append(e2)
    def printEdge(self):
        print(self.graph)
    def _DFS(self,visited,v):
        visited[v] = True
        print(v,end=" ")
        try:
            for i in self.graph[v]:
                if visited[i] == False:
                    self._DFS(visited,i)
        except:
            print("Error")
            
    def DFS(self,startingVertex):
        #We have to maintain all visited vertex
        visited = [False] * (max(self.graph.keys())+1)
        print(visited)
        self._DFS(visited,startingVertex)
        
g= Graph()
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
g.printEdge()
g.DFS(2)
