
    

class Edge:
    def __init__(self, end, c) -> None:
        self.end = end
        self.c = c

class Node:
    def __init__(self, n, edges) -> None:
        self.n = n
        self.edges = edges

    def distance(self, n):
        for e in self.edges:
            if e.end.n == n.n:
                return e.c

class Graphe:
    def __init__(self, nodes ) -> None:
        self.nodes = nodes


