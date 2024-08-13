from typing import List
from collections import deque

def findTheCity(n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    edges = [edge for edge in edges if edge[2] <= distanceThreshold]
    connected_cities = {x[0] for x in edges}.union({x[1] for x in edges})
    non_connected = set(range(n)).difference(connected_cities)
    if non_connected:
        return max(non_connected)

    nodes = {x: {} for x in range(n)}
    for edge in edges:
        nodes[edge[0]][edge[1]] = edge[2]
        nodes[edge[1]][edge[0]] = edge[2]
        
    for node in range(n):
        # bfs
        adj = deque(nodes[node].keys())
        while adj:
            curr = adj.pop()
            weight = nodes[node][curr]
            for edge in nodes[curr]:
                if edge == node:
                    continue
                if weight + nodes[curr][edge] > distanceThreshold:
                    continue
                if (edge in nodes[node]) and (nodes[node][edge] <= weight + nodes[curr][edge]):
                    pass
                else:
                    nodes[node][edge] = weight + nodes[curr][edge]
                    adj.appendleft(edge)
                if (node in nodes[edge]) and (nodes[edge][node] <= weight + nodes[curr][edge]):
                    pass
                else:
                    nodes[edge][node] = weight + nodes[curr][edge]
    result = 0
    min_len = n
    for x in range(n):
        if len(nodes[x]) <= min_len:
            min_len = len(nodes[x])
            result = x
    return result

print(findTheCity(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4))