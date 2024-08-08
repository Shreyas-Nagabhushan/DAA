class Graph:
    def __init__(self):
        self.vertices = []
        self.adj_matrix = []

    def input_graph(self):
        n = int(input("Enter the number of vertices: "))
        print("Enter the vertices: ")
        self.vertices = [input() for _ in range(n)]

        self.adj_matrix = [[float('inf') for _ in range(n)] for _ in range(n)]

        print("Enter edges: (v1,v2,weight)")
        while True:
            v1 = input("V1 = ")
            v2 = input("V2 = ")

            if v1 == "" or v2 == "":
                break

            v1 = self.vertices.index(v1)
            v2 = self.vertices.index(v2)

            self.adj_matrix[v1][v2] = self.adj_matrix[v2][v1] = float(input("Enter weight: "))
    
    def dijikstras(self, start):
        n = len(self.vertices)
        unvisited = [v for v in self.vertices]
        paths = {v: (float('inf') if v!=start else 0, None) for v in self.vertices} 
        
        while unvisited:
            curr = min(unvisited, key= lambda x: paths[x][0])
            index = self.vertices.index(curr)

            for i in range(n):
                if self.adj_matrix[index][i] != float('inf'):
                    if paths[curr][0] +  self.adj_matrix[index][i] < paths[self.vertices[i]][0]:
                        paths[self.vertices[i]] = (paths[curr][0] +  self.adj_matrix[index][i], curr)
            
            unvisited.remove(curr)

        print(paths)

g = Graph()
g.input_graph()
g.dijikstras(input("Enter start: "))

