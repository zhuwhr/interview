# Union Find: Union and find techniques are not just for graph. 
# They aim to build an array indicating the parent of each element. 
# When find, do path compression. When union, do union by rank

# Python Program for union-find algorithm to detect cycle in a undirected graph
# we have one egde for any two vertex i.e 1-2 is either 1-2 or 2-1 but not both
# union by rank and compression tech:
# http://www.geeksforgeeks.org/disjoint-set-data-structures-java-implementation/

from collections import defaultdict


# This class represents a undirected graph using adjacency list representation
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph

    # function to add an edge to graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # A utility function to find the subset of an element i
    # path compression
    def find_parent(self, parent, i):
        if parent[i] == i:
            return i
        result = self.find_parent(parent, parent[i])
        parent[i] = result
        return result

    # A utility function to do union of two subsets
    # union by rank
    def union(self, parent, rank, x, y):
        x_set = self.find_parent(parent, x)
        y_set = self.find_parent(parent, y)
        if x_set == y_set: return
        if rank[x_set] < rank[y_set]:
            parent[x_set] = y_set
        elif rank[x_set] > rank[y_set]:
            parent[y_set] = x_set
        else:
            parent[x_set] = y_set
            rank[y_set] += 1

    # The main function to check whether a given graph
    # contains cycle or not
    def is_cyclic(self):

        # Allocate memory for creating V subsets and
        # Initialize all subsets as single element sets
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Iterate through all edges of graph, find subset of both
        # vertices of every edge, if both subsets are same, then
        # there is cycle in graph.
        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(parent, i)
                y = self.find_parent(parent, j)
                if x == y:
                    return True
                self.union(parent, rank, x, y)


# Create a graph given in the above diagram
g = Graph(3)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)

if g.is_cyclic():
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle ")