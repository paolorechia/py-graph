from typing import List


class GraphRepresentation:
    MATRIX = 1  # Adjacency Matrix
    LINKED_LIST = 2  # Adjacency List


class Vertex:
    def __init__(self, identifier, payload=None):
        self.identifier = identifier
        self.payload = payload


class Edge:
    "Directed Edge"

    def __init__(self, a: Vertex, b: Vertex):
        self.origin = a
        self.destiny = b


class Graph:
    """Directed graph."""

    def __init__(self):
        self._vertices = []
        pass

    def add_vertex(self, v: Vertex):
        raise NotImplementedError()

    def add_edge(self, e: Edge):
        raise NotImplementedError()

    def outgoing_degree(self, v: Vertex):
        raise NotImplementedError()

    def _dfs_traverse(self, index, visited, hook, options):
        raise NotImplementedError()

    def dfs_traverse(self, starting_vertex, hook=None, options=None):
        visited = set()
        for i, v in enumerate(self._vertices):
            if v.identifier == starting_vertex.identifier:
                visited.add(i)
                self._dfs_traverse(i, visited, hook, options)


class LinkedListGraph(Graph):
    def __init__(self):
        super().__init__()
        self._adjacency_lists = []

    def add_vertex(self, v: Vertex):
        self._vertices.append(v)
        self._adjacency_lists.append([])

    def add_edge(self, e: Edge):
        """This block could be improved with a hashmap/dict"""
        origin_index = -1
        destiny_index = -1
        i = 0
        while i < len(self._vertices) and (
            origin_index == -1 or destiny_index == -1
        ):
            v = self._vertices[i]
            if v == e.origin:
                origin_index = i
            if v == e.destiny:
                destiny_index = i
            i += 1
        if origin_index == -1:
            raise IndexError(
                "Cannot add edge: origin vertex not found in graph."
            )
        if destiny_index == -1:
            raise IndexError(
                "Cannot add edge: destiny vertex not found in graph."
            )
        self._adjacency_lists[origin_index].append(destiny_index)

    def outgoing_degree(self, v: Vertex):
        for i in range(len(self._vertices)):
            if self._vertices[i].identifier == v.identifier:
                return len(self._adjacency_lists[i])
        raise IndexError("Vertex not found")

    def bfs_traverse(self, starting_vertex, hook=None, options=None):
        """Should use a queue"""
        raise NotImplementedError("Todo")

    def dijkstra_traverse(self, starting_vertex, hook=None, options=None):
        """Should use a priority queue"""
        raise NotImplementedError("Todo")

    def _dfs_traverse(self, index, visited, hook, options):
        origin = self._vertices[index]
        if hook:
            hook(origin)
        for j in self._adjacency_lists[index]:
            if j not in visited:
                visited.add(j)
                self._dfs_traverse(j, visited, hook, options)


class MatrixGraph(Graph):
    """Matrix-like non resizable graph"""
    def __init__(self, vertices: List[Vertex]):
        self._vertices = vertices[:]
        self._matrix = []
        for i in range(len(self._vertices)):
            self._matrix.append([])
            for _ in range(len(self._vertices)):
                self._matrix[i].append(0)

    def add_edge(self, e: Edge):
        """This block is copied from LinkedList and could be refactored,
        to reduce code duplication
        """
        origin_index = -1
        destiny_index = -1
        i = 0
        while i < len(self._vertices) and (
            origin_index == -1 or destiny_index == -1
        ):
            v = self._vertices[i]
            if v == e.origin:
                origin_index = i
            if v == e.destiny:
                destiny_index = i
            i += 1
        if origin_index == -1:
            raise IndexError(
                "Cannot add edge: origin vertex not found in graph."
            )
        if destiny_index == -1:
            raise IndexError(
                "Cannot add edge: destiny vertex not found in graph."
            )
        # This line is where it differs from LinkedList
        self._matrix[origin_index][destiny_index] = 1


    def outgoing_degree(self, v: Vertex):
        for i in range(len(self._vertices)):
            if self._vertices[i].identifier == v.identifier:
                degree = 0
                for j in range(len(self._vertices)):
                    degree += self._matrix[i][j]
                return degree

        raise IndexError("Vertex not found")

    def _dfs_traverse(self, index, visited, hook, options):
        origin = self._vertices[index]
        if hook:
            hook(origin)

        for j in range(len(self._vertices)):
            if self._matrix[index][j] == 1:
                if j not in visited:
                    visited.add(j)
                    self._dfs_traverse(j, visited, hook, options)
