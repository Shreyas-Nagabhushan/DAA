def relax(edges, distance):
    for edge in edges:
        u,v,w = edge[0], edge[1], edge[2]
        if distance[u] == float('inf'):
            continue
        distance[v] = min(distance[v], distance[u] + w)

def bellman(edges, n, src):
    distance = [float('inf') for _ in range(n)]
    distance[src] = 0

    for _ in range(n-1):
        relax(edges, distance)
    
    distcpy = distance[:]
    relax(edges, distcpy)

    if distcpy == distance:
        print(distance)
    else:
        print('Negative cycle exists')
    
def input_graph():
    n = int(input('Enter number of vertices: '))
    e = int(input('Enter number of edges: '))
    edges = []
    for _ in range(e):
        u = int(input('Start: '))
        v = int(input('End: '))
        w = int(input('Weight: '))
        edges.append([u,v,w])
    
    src = int(input('Enter source vertex: '))
    return (n, edges, src)

n, edges, src = input_graph()
bellman(edges, n, src)

#O(n * e) 