import heapq

def push_heap(heap, item):
    heapq.heappush(heap, item)

def pop_heap(heap):
    return heapq.heappop(heap)

def dijkstras(graph, src):
    n = len(graph)
    distance = [float('inf') for _ in range(n)]
    distance[src] = 0 
    queue = []
    push_heap(queue, (0, src))

    while queue:
        edge_weight, curr_node = pop_heap(queue)
        for neighbour in graph[curr_node]:
            if edge_weight + distance[curr_node] < distance[neighbour]:
                distance[neighbour] = edge_weight + distance[curr_node]
                push_heap(queue, (distance[neighbour], neighbour))
    
    print(distance)

graph = [
    [0, 1, 4, 0, 0],
    [0, 0, 4, 2, 0],
    [0, 0, 0, 3, 0],
    [0, 0, 0, 0, 3],
    [0, 0, 0, 0, 0]
]
dijkstras(graph, 0)


