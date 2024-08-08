def input_graph():
    n = int(input('Enter number of vertices: '))
    graph = [[0 for _ in range(n)] for _ in range(n)]
    e = int(input('Enter number of edges: '))

    for _ in range(e):
        u, v, w = map(int, input('Enter start end cost of the edge: ').split())
        graph[u][v] = graph[v][u] = w 
    
    return graph 

def tsp(graph, source):
    min_dist = float('inf')
    n = len(graph)
    visited = [False for _ in range(n)]
    visited[source] = True 

    def backtrack(curr_vertex, curr_cost, counter):
        nonlocal min_dist

        if counter == n and graph[curr_vertex][source] != 0:
            min_dist = min(min_dist, curr_cost + graph[curr_vertex][source])
            return 
        
        for v in range(n):

            if not visited[v] and graph[curr_vertex][v]:

                visited[v] = True 
                backtrack(v, curr_cost+graph[curr_vertex][v], counter+1)
                visited[v] = False 

    backtrack(source, 0, 1)
    print(min_dist) 

tsp(input_graph(), int(input('Enter source: ')))


#ANSWER IS 21

