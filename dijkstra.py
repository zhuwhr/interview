import heapq

def dijkstra(adj, costs, s, t):
    '''
    :param adj: adjacent list representation of a undirected weighted graph
    :param costs: weight of edges
    :param s: source node
    :param t: dest node
    :return: Return predecessors and min distance if there exists a shortest path
        from s to t; Otherwise, return None
    '''
    pq = []  # pq of mutable items
    items = {}  # vertex -> [d[v], v]
    dist = {s: 0}  # vertex -> minimal distance
    pre = {}  # predecessor
    visited = set()

    for i in adj.keys():
        dist[i] = float('inf')
        item = [dist[i], i]
        items[i] = item
        pre[i] = None
        pq.append(item)

    heapq.heapify(pq)
    dist[s] = 0
    items[s][0] = 0
    heapq._siftdown(pq, 0, pq.index(items[s]))

    # add the neighbors of source node
    """
    for v in adj.get(s, []):
        dist[v] = costs[s, v]
        # item = [dist[v], s, v]
        item = [dist[v], v]
        items[v] = item
        heapq.heappush(pq, item)
        pre[v] = s
    """


    while pq:
        # expand the min dist node
        # cost, parent, u = heapq.heappop(pq)
        _, u = heapq.heappop(pq)
        if u not in visited:
            # pre[u] = parent
            visited.add(u)
            if u == t:
                return pre, dist[u]
            # generate all neighbors
            for v in adj.get(u, []):
                """
                # v has not been seen
                if v not in dist:
                    dist[v] = dist[u] + costs[u, v]
                    item = [dist[v], v]
                    items[v] = item
                    pre[v] = u
                    heapq.heappush(pq, item)
                # v has been visited, see if need to update
                else:
                """
                if dist[v] > dist[u] + costs[u, v]:
                    dist[v] = dist[u] + costs[u, v]
                    # update mutable item
                    items[v][0] = dist[v]  # update dist(pq key)
                    pre[v] = u  # update predessor
                    heapq._siftdown(pq, 0, pq.index(items[v]))  # update heap
    return None


def make_undirected(cost):
    ucost = {}
    for k, w in cost.items():
        ucost[k] = w
        ucost[(k[1],k[0])] = w
    return ucost

if __name__=='__main__':

    # adjacent list
    adj = { 1: [2,3,6],
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

    s, t = 1, 7
    predecessors, min_cost = dijkstra(adj, cost, s, t)
    c = t
    path = [c]
    print('min cost:', min_cost)
    while predecessors.get(c):
        c = predecessors[c]
        path.append(c)
    path.reverse()
    print('shortest path:', path)

'''
class implementation
http://www.bogotobogo.com/python/python_Dijkstras_Shortest_Path_Algorithm.php
'''