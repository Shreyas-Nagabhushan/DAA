def input_graph():
    n = int(input('Enter number of vertices: '))
    e = int(input('Enter number of edges: '))
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for _ in range(e):
        u = int(input('Start: '))
        v = int(input('End: '))
        graph[u][v] = graph[v][u] = 1

    return graph


def dfs(graph, source):
    n = len(graph)
    visited = [False for _ in range(n)]
    visited[source] = True 

    def f(current):

        print(current)

        for i in range(n):
            if graph[current][i] and not visited[i]:
                visited[i] = True 
                f(i)

    f(source)

def bfs(graph, source):
    n = len(graph)
    queue = [source]
    visited = [False for _ in range(n)]

    while len(queue):
        curr = queue.pop(0)
        print(curr)
        for i in range(n):
            if graph[curr][i] and not visited[i]:
                visited[i] = True 
                queue.append(i)


graph = input_graph()
source = int(input('Enter source vertex: '))
dfs(graph, source)   
bfs(graph, source)     

