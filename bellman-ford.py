"""
bellman-ford algorithm
find the shortest path from a start vertex to every vertex
in a directed weighted graph
weight of edge could be negative
O(VE) time

Graph: adjacent list
costs:

pseudo code:
initialize-single-source (G, s):
    for each vertex v in G.V:
        v.d = inf
        v.pre = None
    s.d = 0

relax(w, u, v):
    if v.d > u.d + w(u, v):
        v.d = u.d + w(u, v)
        v.pre = u

bellman-ford(G, w, s):
    INITIALIZE-SINGLE-SOURCE (G, s)
    for i = 1 to |G.V| - 1:
        for each edge (u, v) in G.E:
            relax(u, v, w)
    for each edge (u, v) in G.E:
    # if can still relax that edge, -∞ cycle found
        if v.d > u.d + w(u, v):
            return "negative cycle"
    return True
"""


def initialize(graph, start):
    dist = {}
    pre = {}
    for i in graph.keys():
        dist[i] = float('inf')
        pre[i] = None
    dist[start] = 0
    return dist, pre


def relax(costs, u, v, dist, pre):
    if dist[v] > dist[u] + costs[u, v]:
        dist[v] = dist[u] + costs[u, v]
        pre[v] = u


def bellman_ford(graph, costs, start):
    dist, pre = initialize(graph, start)
    for _ in range(len(graph) - 1):
        for u, vertices in graph.items():
            for v in vertices:
                relax(costs, u, v, dist, pre)
    for u, vertices in graph.items():
        for v in vertices:
            if dist[v] > dist[u] + costs[u, v]:
                return 'error', 'error'
    return dist, pre


if __name__ == '__main__':
    graph = {
        1: [2, 4],
        2: [3, 4, 5],
        3: [2],
        4: [3, 5],
        5: [1, 3]
    }

    costs = {
        (1, 2): 6,
        (1, 4): 7,
        (2, 3): 5,
        (2, 4): 8,
        (2, 5): -4,
        (3, 2): -2,
        (4, 3): -3,
        (4, 5): 9,
        (5, 1): 2,
        (5, 3): 7
    }

    dist, pre = bellman_ford(graph, costs, 1)
    print(pre)


"""
首先指出，图的任意一条最短路径既不能包含负权回路，也不会包含正权回路，因此它最多包含|v|-1条边。
其次，从源点s可达的所有顶点如果 存在最短路径，则这些最短路径构成一个以s为根的最短路径树。Bellman-Ford算法的迭代松弛操作，实际上就是按每个点实际的最短路径[虽然我们还不知道，但它一定存在]的层次，逐层生成这棵最短路径树的过程。
注意，每一次遍历，都可以从前一次遍历的基础上，找到此次遍历的部分点的单源最短路径。如：这是第i次遍历，那么，通过数学归纳法，若前面单源最短路径层次为1~（i-1）的点全部已经得到，而单源最短路径层次为i的点，必定可由单源最短路径层次为i-1的点集得到，从而在下一次遍历中充当前一次的点集，如此往复迭代，[v]-1次后，若无负权回路，则我们已经达到了所需的目的--得到每个点的单源最短路径。[注意：这棵树的每一次更新，可以将其中的某一个子树接到另一个点下]
反之，可证，若存在负权回路，第[v]次遍历一定存在更新，因为负权回路的环中，必定存在一个“断点”，可用数学手段证明。
最后，我们在第[v]次更新中若没有新的松弛，则输出结果，若依然存在松弛，则输出‘CAN'T'表示无解。同时，我们还可以通过“断点”找到负权回路。
"""