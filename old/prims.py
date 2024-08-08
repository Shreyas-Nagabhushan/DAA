import heapq

def make_graph():
    graph = {}
    while(True):
        ch = int(input('1 to add new edges OR 0 to exit : '))
        if ch == 1 :
            v1 = input('V1 : ')
            v2 = input('V2 : ')
            cost = int(input('Cost : '))
            if not v1 in graph : 
                graph[v1] = []
            if not v2 in graph:
                graph[v2] = []
            graph[v1].append( (v2, cost) )
            graph[v2].append( (v1, cost) )
        else:
            break
    return graph 

def prims(graph):
    edges = [] # used as heap items will be (weight, parent, child)
    mst = [] # result
    explored = set()
    total_cost = 0

    src = input('Enter src vertex : ')

    heapq.heappush(edges, (0, None, src))

    while edges :
        w, parent, child = heapq.heappop(edges)

        if child in explored:
            continue

        explored.add(child)

        if parent is not None :
            #Need to add the edge parent->child to mst 
            mst.append((parent, child, w))
            total_cost += w 

        #Add all adjacent edges to heap 
        for vertex, cost in graph[child]:
            if vertex not in explored:
                heapq.heappush(edges, (cost, child, vertex))
    print(f"total cost : {total_cost}")
    print(mst)

graph = make_graph()
prims(graph)