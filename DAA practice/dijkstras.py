import heapq

def push_heap(heap, item):
    heapq.heappush(heap, item)

def pop_heap(heap):
    return heapq.heappop(heap)

def dijkstras(graph, src, destination):
    n = len(graph)
    distance = [float('inf') for _ in range(n)]
    distance[src] = 0 
    queue = []
    push_heap(queue, (0, src))
    parent = [-1 for _ in range(n)]
    parent[src] = src

    while queue:
        curr_dist, curr_node = pop_heap(queue)

        for v in range(n):
            if graph[curr_node][v] != 0:
                if curr_dist + graph[curr_node][v] < distance[v]:
                    distance[v] = curr_dist + graph[curr_node][v]
                    push_heap(queue, (distance[v], v))
                    parent[v] = curr_node
       
    
    print(distance)

    path = []
    def get_path(curr):
        if parent[curr] == curr:
            path.append(curr)
            return
        if parent[curr] == -1:
            return 
        
        get_path(parent[curr])
        path.append(curr)
    
    get_path(destination)
    print(path)

def input_graph():
    n = int(input('Enter number of vertices: '))
    e = int(input('Enter number of edges: '))
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for _ in range(e):
        u = int(input('Start: '))
        v = int(input('End: '))
        w = int(input('Weight: '))
        graph[u][v] = graph[v][u] = w
    
    src = int(input('Enter source vertex: '))
    dst = int(input('Enter destination vetex: '))

    return (graph, src, dst)


graph, src, destination = input_graph()
dijkstras(graph, src, destination)


