def checkio(lines_list):
    """Return the quantity of squares"""
    lines_list=map(lambda x:sorted(x),lines_list)
    count = 0
    for i in xrange(1, 12):
        for size in xrange(1, 4 - 16 % 4):
            square = get_square_edge(i, size)
            flag = 0
            for edge in square:
                if edge not in lines_list:
                    flag = 1
            if flag == 0:
                count += 1
    return count


def get_square_edge(vertex, size):
    edges = []
    edges += [[vertex + n, vertex + n + 1] for n in xrange(size)]
    edges += [[vertex + 4 * n, vertex + 4 * (n + 1)] for n in xrange(size)]
    edges += [[vertex + 4 * n + size, vertex + 4 * (n + 1) + size] for n in
              xrange(size)]
    edges += [[vertex + 4 * size + n, vertex + 4 * size + n + 1] for n in
              xrange(size)]
    return edges


if __name__ == '__main__':
    assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                     [10, 14], [12, 16], [14, 15],
                     [15, 16]]) == 3), "First, from description"
    assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15],
                     [15, 16]]) == 2), "Second, from description"
    assert (
    checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10],
                     [9, 10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
                     [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"
