class Graph:
    def __init__(self):
        self.vertices = []
        self.adj_matrix = []

    def input_graph(self):
        n = int(input("Enter the number of vertices: "))
        print("Enter the vertices: ")
        self.vertices = [input() for _ in range(n)]

        self.adj_matrix = [[False for _ in range(n)] for _ in range(n)]

        print("Enter edges: (v1,v2)")
        while True:
            v1 = input("V1 = ")
            v2 = input("V2 = ")

            if v1 == "" or v2 == "":
                break

            v1 = self.vertices.index(v1)
            v2 = self.vertices.index(v2)

            self.adj_matrix[v1][v2] = self.adj_matrix[v2][v1] = True

    def dfs(self, start):
        n = len(self.vertices)
        q = []
        visited = [False for _ in range(n)]
        q.append(start)
        visited[start] = True

        while q:
            curr = q.pop(0)
            print("->", self.vertices[curr], end="")

            for i in range(n):
                if self.adj_matrix[curr][i] and not visited[i]:
                    visited[i] = True
                    q.append(i)

        print()

g = Graph()
g.input_graph()
g.dfs(g.vertices.index(input("Enter start vertex: ")))
