'''
graph is represented as a edge list. It is a list of lists,
which have all vertices that the index vertex has an edge with.
G = [[1], []] means there are 2 vertices, vertex 0 has an outgoing edge to vertex 1
white means not visited, gray means visiting, black means visited.
for example, see course schedule on leetcode
'''

from collections import deque

#  DFS
def topo_dfs(graph):
    visited = ['white'] * len(graph)
    res = []

    def dfs(i):
        if visited[i] == 'gray': return False
        if visited[i] == 'black': return True
        visited[i] = 'gray'
        for j in graph[i]:
            if not dfs(j):
                return False
        visited[i] = 'black'
        res.append(i)
        return True

    for i in range(len(graph)):
        if not dfs(i):
            return []

    return list(reversed(res))

# bfs
def topo_bfs(graph):
    in_degree = [0] * len(graph)
    q = deque()
    res = []
    # construct in-degree
    for edges in graph:
        for v in edges:
            in_degree[v] += 1

    for i in range(len(in_degree)):
        if in_degree[i] == 0:
            q.append(i)

    while q:
        v = q.popleft()
        for u in graph[v]:
            in_degree[u] -= 1
            if in_degree[u] == 0:
                q.append(u)
        in_degree[v] = -1  # mark as visited
        res.append(v)

    return res if len(res) == len(graph) else []

graph = [[1,2], [3], [3], []]
print(topo_bfs(graph))