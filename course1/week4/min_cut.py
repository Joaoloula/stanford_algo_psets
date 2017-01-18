import numpy as np


def mincut(graph, n):
    """ Calculates the min cut of an undirected graph using the Karger
    randomized contraction algorithm iterated n times"""
    cutA = []
    cutB = []
    cut_size = len(graph)

    for i in range(1, n+1):
        new_cutA, new_cutB, new_cut_size = randomized_contraction(graph)
        if new_cut_size < cut_size:
            cutA = new_cutA
            cutB = new_cutB
            cut_size = new_cut_size
        if (100*i) % n == 0:
            print('{} % complete'.format((100*i)/n))

    return cutA, cutB, cut_size


def randomized_contraction(graph):
    # Create array of edges
    edges = []
    for v1, v1_neighbors in enumerate(graph):
        for v2 in v1_neighbors:
            edges.append([v1, v2])

    # Initialize number of vertices for creating loop condition
    n_vertices = len(graph)

    # Initialize list to keep track of "super" vertices (list of vertices
    # joined together)
    super_vertices = [[i] for i in range(len(graph))]
    while n_vertices > 2:
        # Select edge randomly
        v1, v2 = edges[np.random.randint(len(edges))]

        # Perform contraction
        # Keep track of the super vertex created by the fusion of v1 and v2
        super_vertices[v1] += super_vertices[v2]
        # Remove [v1, v2] from edges list and replace every instance of v2 with
        # v1
        edges = [edge for edge in edges
                 if edge != [v1, v2] and edge != [v2, v1]]
        edges = [[v1, edge[1]] if edge[0] == v2 else
                 [edge[0], v1] if edge[1] == v2 else
                 edge for edge in edges]

        # Decrease number of vertices by 1
        # print(edges)
        n_vertices -= 1

    # Get cut by checking the last two super vertices
    cutA, cutB = super_vertices[edges[0][0]], super_vertices[edges[0][1]]

    # Get number of edges in the cut by the size of edges list
    cut_size = len(edges) / 2

    return cutA, cutB, cut_size

with open('kargerMinCut.txt', 'r') as f:
    # Load txt while doing some preprocessing (converting str to int, decreasing
    # one so as to get easier indexing etc.)
    graph = [[int(num) - 1
              for num in line.split('\t')[1: len(line.split('\t')) - 1]]
             for line in f.readlines()]
    cutA, cutB, cut_size = mincut(graph, len(graph))

print(cutA)
print(cutB)
print(cut_size)
