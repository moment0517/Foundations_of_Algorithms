import itertools


def travelling_salesperson(mat_adj, n):
    mat_d = [{} for i in range(n-1)]

    for i in range(n-1):
        mat_d[i][()] = mat_adj[i, n-1]
    for k in range(1, n-1):
        for i in range(n-1):
            idxes = list(range(i)) + list(range(i+1, n-1))
            for c in itertools.combinations(idxes, k):
                tmp = []
                for j in c:
                    c_ = list(c[:])
                    c_.remove(j)
                    c_ = tuple(c_)
                    d = mat_adj[i, j] + mat_d[j][c_]
                    tmp.append(d)
                mat_d[i][c] = min(tmp)

    return mat_d
    
    
if __name__ == '__main__':
    mat = np.array([
        [0, 2, 9, 1000],
        [1, 0, 6, 4],
        [1000, 7, 0, 8],
        [6, 3, 1000, 0]
    ])
    print(travelling_salesperson(mat, 4))
