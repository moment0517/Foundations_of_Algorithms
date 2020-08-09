import numpy as np

def prim_minimum_spanning_trees(mat_adj, n):
    edges = []
    vertices = []
    nearest_idx = [0] * n
    distance = [-1] * n

    vertices.append(0)
    for i in range(1, n):
        distance[i] = mat_adj[0, i]

    while len(vertices) < n:
        dst_min = np.max(mat_adj) + 1
        idx = -1
        for i, dst in enumerate(distance):
            if 0 < dst < dst_min:
                dst_min = dst
                idx = i
        v = nearest_idx[idx]
        vertices.append(v)
        edges.append((v, idx))
        distance[idx] = -1

        for i in range(n):
            if distance[i] != -1 and distance[i] > mat_adj[i, idx]:
                distance[i] = mat_adj[i, idx]
                nearest_idx[i] = idx

    return edges


if __name__ == '__main__':
    adjacent_mat = np.array([
        [0, 1, 3, 100, 100],
        [1, 0, 3, 6, 100],
        [3, 3, 0, 4, 2],
        [100, 6, 4, 0, 5],
        [100, 100, 2, 5, 0]
        ], dtype=int)
    print(prim_minimum_spanning_trees(adjacent_mat, 5))
    
