from collections import defaultdict
class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)      
        
    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    def traverse(self,u):  #breadth first traversal
        visited = {}
        queue = []
        queue.append(u)
        visited[u]=True
        while queue:
            u = queue.pop(0)
            print(u,)
            for i in self.graph[u]:
                if i not in visited.keys():
                    queue.append(i)
                    visited[i] = True 
                    
    def check_path(self,u,v):  #to check if a connection exists between nodes
        u-=1
        v-=1
        visited = {}
        queue = []
        queue.append(u)
        visited[u]=True
        
        while queue:
            n = queue.pop(0)
            if n==v:
                return True
            else:
                for i in self.graph[n]:
                    if i not in visited.keys():
                        queue.append(i)
                        visited[i] = True
        return False
        
g = Graph()
g.add_edge(1,2)
g.add_edge(4,2)
g.add_edge(3,2)
g.add_edge(5,2)
g.add_edge(8,2)
g.add_edge(10,2)


print(g.check_path(2,3))
g.traverse(1)


