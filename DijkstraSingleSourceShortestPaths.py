import numpy as np


def dijkstra_single_source_shortest_paths(mat_adj, n, s_i):
    vertices = [s_i]
    edges = []
    length = np.ones(n) * -1
    touch = np.ones(n, dtype=int) * s_i

    for i in range(n):
        if i != s_i:
            length[i] = mat_adj[s_i, i]

    while len(vertices) < n:
        idx = -1
        min_len = np.max(mat_adj) + 1
        for i, len_ in enumerate(length):
            if 0 < len_ < min_len:
                min_len = len_
                idx = i
        vertices.append(idx)
        edges.append((touch[idx], idx))
        for i in range(n):
            if i != idx and length[i] != -1:
                if length[i] > length[idx] + mat_adj[idx, i]:
                    length[i] = length[idx] + mat_adj[idx, i]
                    touch[i] = idx
        length[idx] = -1

    return edges


if __name__ == '__main__':
    adjacent_mat = np.array([
        [0, 7, 4, 6, 1],
        [100, 0, 100, 100, 100],
        [100, 2, 0, 5, 100],
        [100, 3, 100, 0, 100],
        [100, 100, 100, 1, 0]
    ], dtype=int)
    print(dijkstra_single_source_shortest_paths(adjacent_mat, 5, 0))
