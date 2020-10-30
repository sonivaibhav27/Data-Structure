#Here I am not using external package to maintain dictionary with list items attached.
class Graph:
    def __init__(self):
        self.graph = {}
    def addEdge(self,source,to):
        a= self.graph.get(source)
        if(a):
            self.graph[source].append(to)
        else:
            self.graph[source] = [to]
    def BFS(self,start):
        visited = [False] * len(self.graph)
        queue= []
        visited[start] = True
        queue.append(start)
        while queue:
            s= queue.pop()
            print(s)
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i]=True
        print(visited)
        
        
g = Graph()
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
g.BFS(0)
