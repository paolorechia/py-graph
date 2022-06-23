import pytest
from graph import LinkedListGraph, MatrixGraph, Vertex, Edge


def build_test_linked_list_graph():
    g = LinkedListGraph()

    A = Vertex("A")
    B = Vertex("B")
    C = Vertex("C")
    D = Vertex("D")
    E = Vertex("E")

    g.add_vertex(A)
    g.add_vertex(B)
    g.add_vertex(C)
    g.add_vertex(D)
    g.add_vertex(E)

    g.add_edge(Edge(A, B))

    return g, A, B, C, D, E

def build_matrix_graph():

    A = Vertex("A")
    B = Vertex("B")
    C = Vertex("C")
    D = Vertex("D")
    E = Vertex("E")

    g = MatrixGraph([A, B, C, D, E])

    g.add_edge(Edge(A, B))

    return g, A, B, C, D, E


def test_linked_list_graph_representation():
    g, A, B, C, D, E = build_test_linked_list_graph()

    # Since it's a directed graph, we have an edge from A->B
    assert g.outgoing_degree(A) == 1
    # But we don't have one from B->A
    assert g.outgoing_degree(B) == 0

    g.add_edge(Edge(B, A))
    # Now both should be one
    assert g.outgoing_degree(A) == 1
    # But we don't have one from B->A
    assert g.outgoing_degree(B) == 1

    g.add_edge(Edge(A, C))
    assert g.outgoing_degree(A) == 2



def test_linked_list_graph_traverse():
    g, A, B, C, D, E = build_test_linked_list_graph()

    l = []
    def hook(v: Vertex):
        l.append(v.identifier)
        print(v.identifier)

    g.dfs_traverse(A, hook)

    assert l == ["A", "B"]
    g.add_edge(Edge(A, B))
    g.add_edge(Edge(A, C))
    g.add_edge(Edge(C, D))
    g.add_edge(Edge(D, E))
        
    l = []
    g.dfs_traverse(A, hook)
    assert l == ["A", "B", "C", "D", "E"]


def test_graph_representation():
    g, A, B, C, D, E = build_matrix_graph()

    assert len(g._vertices) == 5
    # Since it's a directed graph, we have an edge from A->B
    assert g.outgoing_degree(A) == 1
    # But we don't have one from B->A
    assert g.outgoing_degree(B) == 0

    g.add_edge(Edge(B, A))
    # Now both should be one
    assert g.outgoing_degree(A) == 1
    # But we don't have one from B->A
    assert g.outgoing_degree(B) == 1

    g.add_edge(Edge(A, C))
    assert g.outgoing_degree(A) == 2
    

def test_matrix_graph_traverse():
    g, A, B, C, D, E = build_matrix_graph()

    l = []
    def hook(v: Vertex):
        l.append(v.identifier)
        print(v.identifier)

    g.dfs_traverse(A, hook)

    assert l == ["A", "B"]
    g.add_edge(Edge(A, B))
    g.add_edge(Edge(A, C))
    g.add_edge(Edge(C, D))
    g.add_edge(Edge(D, E))
        
    l = []
    g.dfs_traverse(A, hook)
    assert l == ["A", "B", "C", "D", "E"]
