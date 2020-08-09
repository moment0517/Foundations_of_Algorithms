import numpy as np


def kruskal_minimum_spanning_trees(mat_adj, n):
    edges = []
    vertice_sets = list(range(n))
    vertices = set()

    edge_dist = []
    for i in range(n-1):
        for j in range(i+1, n):
            edge = (i, j)
            dst = mat_adj[i, j]
            edge_dist.append((edge, dst))
    edge_dist = sorted(edge_dist, key=lambda x: x[1])

    for edge, _ in edge_dist:
        v1, v2 = edge
        v1_set = vertice_sets[v1]
        while v1_set != vertice_sets[v1_set]:
            v1_set = vertice_sets[v1_set]
        v2_set = vertice_sets[v2]
        while v2_set != vertice_sets[v2_set]:
            v2_set = vertice_sets[v2_set]
        if v1_set != v2_set:
            edges.append(edge)
            vertices.add(v1)
            vertices.add(v2)
            vertice_sets[v2_set] = v1_set
            if len(vertices) == n:
                break

    return edges
    

if __name__ == '__main__':
    adjacent_mat = np.array([
        [0, 1, 3, 100, 100],
        [1, 0, 3, 6, 100],
        [3, 3, 0, 4, 2],
        [100, 6, 4, 0, 5],
        [100, 100, 2, 5, 0]
        ], dtype=int
    )
    print(prim_minimum_spanning_trees(adjacent_mat, 5))
    
