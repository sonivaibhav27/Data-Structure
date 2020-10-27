from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph= defaultdict(list)
    def addEdge(self,e1,e2):
        self.graph[e1].append(e2)
    
    def BFS(self,v):
        visited= [False] * len(self.graph)
        queue=[]
        visited[v] =True
        queue.append(v)
        while queue:
            s= queue.pop(0)
            print(s)
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i]= True
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)") 
g.BFS(2) 
            
