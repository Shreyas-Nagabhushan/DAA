class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)] 
        self.size = [1] * n 

    def find_ultimate_parent(self, node):
        if self.parent[node] == node:
            return node 
        self.parent[node] = self.find_ultimate_parent(self.parent[node])
        return self.parent[node]
    
    def union_by_size(self, u, v):
        ult_u = self.find_ultimate_parent(u)
        ult_v = self.find_ultimate_parent(v)
        if ult_u == ult_v:
            return 
        if self.size[ult_u] > self.size[ult_v]:
            self.parent[v] = u 
            self.size[u] += self.size[v]
        else:
            self.parent[u] = v 
            self.size[v] += self.size[u]


def input_graph():
    n = int(input('Enter number of vertices: '))
    e = int(input('Enter number of edges: '))
    edges = []
    for _ in range(e):
        u = int(input('Start: '))
        v = int(input('End: '))
        w = int(input('Weight: '))
        edges.append([w,u,v])

    return (n, edges)

def kruskals():
    n, edges = input_graph()
    disjointSet = DisjointSet(n)
    edges.sort(key = lambda x: x[0])
    mst_edges = []
    mst_cost = 0 

    for edge in edges:
        w = edge[0]
        u = edge[1]
        v = edge[2]
        if disjointSet.find_ultimate_parent(u) != disjointSet.find_ultimate_parent(v):
            disjointSet.union_by_size(u, v)
            mst_edges.append([u, v, w])
            mst_cost += w 

    print(mst_cost)
    print(mst_edges)

kruskals()