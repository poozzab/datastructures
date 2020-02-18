#!/usr/bin/env python3

class DTree:
    def __init__(self, root=None):
        self.root = root

    def hasCycle(self):
        visited = dict()
        return self.root.visit(visited)

class Node:
    def __init__(self,name,edges=None):
        self.name = name
        self.edges = edges if edges is not None else list()

    def addEdge(self, newEdge ):
        self.edges.append(newEdge)

    def visit(self,visited):
        if self in visited and visited[self]:
            return True
        visited[self] = True
        for edge in self.edges:
            if edge.visit(visited):
                return True
        visited[self] = False
        return False

    def __hash__(self):
        return id(self)

class Edge:
    def __init__(self,weight,node):
        self.weight = weight
        self.node = node

    def visit(self,visited):
        return self.node.visit(visited)

    def __hash__(self):
        return id(self)
        