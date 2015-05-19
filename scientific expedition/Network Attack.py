def capture(matrix):
    adjacent = {}
    for i, row in enumerate(matrix):
        adjacent[i] = []
        for j, col in enumerate(row):
            if col == 1:
                adjacent[i].append(j)

    security = [matrix[i][i] for i in xrange(len(matrix))]

    return get_time(adjacent, security)


def get_time(adjacent, security):
    visited = [0]
    clock = 0
    while len(visited) < len(adjacent):
        clock += 1
        mark = []
        for node in visited[:]:
            for adj_node in adjacent[node]:
                if security[adj_node] > 0 and adj_node not in mark:
                    security[adj_node] -= 1
                    mark.append(adj_node)
                    if security[adj_node] == 0:
                        visited.append(adj_node)
    return clock


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 8, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 8, "Base example"
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 4, "Low security"
    assert capture([[0, 1, 1],
                    [1, 9, 1],
                    [1, 1, 9]]) == 9, "Small"
