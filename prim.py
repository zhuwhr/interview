"""
quite similar to dijkstra
find shortest path from start node to all nodes

prim vs dijkstra:
都是通过贪心的算法用BFS
dijkstra找的是最短路径，在发现环的时候，要对比最短路径是不是有变化，然后更新
prim是发现环的时候就不管它，找的是从根开始到每个点的最小总和，并不一定是到每个点的最短路径
"""
import heapq


def prim(graph, costs, start):
    items = {}
    pq = []

    for i in graph.keys():
        if i == start: continue
        item = [float('inf'), i]
        items[i] = item
        pq.append(item)

    heapq.heapify(pq)
    start_item = [0, start]
    heapq.heappush(pq, start_item)
    pre = {start: None}
    visited = set()

    while pq:
        _, u = heapq.heappop(pq)
        visited.add(u)
        for v in graph[u]:
            if v not in visited and costs[u, v] < items[v][0]:
                items[v][0] = costs[u, v]
                pre[v] = u
                heapq._siftdown(pq, 0, pq.index(items[v]))
    return pre


def make_undirected(cost):
    ucost = {}
    for k, w in cost.items():
        ucost[k] = w
        ucost[(k[1],k[0])] = w
    return ucost


if __name__=='__main__':

    # adjacent list
    graph = { 1: [2,3,6],
            2: [1,3,4],
            3: [1,2,4,6],
            4: [2,3,5,7],
            5: [4,6,7],
            6: [1,3,5,7],
            7: [4,5,6]}

    # edge costs
    cost = { (1,2):7,
            (1,3):9,
            (1,6):14,
            (2,3):10,
            (2,4):15,
            (3,4):11,
            (3,6):2,
            (4,5):6,
            (5,6):9,
            (4,7):2,
            (5,7):1,
            (6,7):12}

    cost = make_undirected(cost)

    s= 1
    predecessors = prim(graph, cost, s)

    print(predecessors)