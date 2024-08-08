class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def find_ultimate_parent(self, v):
        if self.parent[v] == v:
            return v 
        self.parent[v] = self.find_ultimate_parent(self.parent[v])
        return self.parent[v]
    
    def union_by_size(self, u, v):
        uu = self.find_ultimate_parent(u)
        uv = self.find_ultimate_parent(v)

        if uu == uv:
            return 
        
        else:
            if self.size[u] > self.size[v]:
                self.parent[v] = u 
                self.size[u] += self.size[v]
            else:
                self.parent[u] = v 
                self.size[v] += self.size[u]

class Graph:
    def __init__(self):
        self.edges = [] 
        self.vertices = [] 
        self.input_graph()
    
    def input_graph(self):
        ...
    
def kruskals(graph):
    edges = graph.edges 
    edges.sort(key = lambda x : x[0])
    mst = []
    cost = 0
    ds = DisjointSet(len(graph.vertices))
    for edge in edges:
        if ds.find_ultimate_parent(edge[1]) != ds.find_ultimate_parent(edge[2]):
            mst.append(edge)
            cost += edge[0] 
            ds.union_by_size(edge[1], edge[2])
    print(mst)