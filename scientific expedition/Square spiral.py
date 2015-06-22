def find_distance(first, second):
    # decide size
    size = 1
    while max(first, second) > size ** 2:
        size += 2

    table = create_table(size)
    first_index, second_index = search_indices(table, first, second)

    return calc_distance(first_index, second_index)


def calc_distance(first_index, second_index):
    return abs(first_index[0] - second_index[0]) + abs(
        first_index[1] - second_index[1])


def search_indices(table, first, second):
    first_index = (-1, -1)
    second_index = (-1, -1)
    for r, row in enumerate(table):
        if first in row:
            first_index = (r, row.index(first))
        if second in row:
            second_index = (r, row.index(second))
    return first_index, second_index


def create_table(size):
    table = [[0 for _ in range(size)] for _ in range(size)]

    # center
    r, c = (size / 2, size / 2)

    # initialize center
    count = 1
    table[r][c] = count
    edge_length = 1

    while edge_length < size:
        edge_length += 2

        # up
        r -= 1
        count += 1
        table[r][c] = count

        # left
        for i in xrange(edge_length - 2):
            c += 1
            count += 1
            table[r][c] = count

        # down
        for i in xrange(edge_length - 1):
            r += 1
            count += 1
            table[r][c] = count

        # right
        for i in xrange(edge_length - 1):
            c -= 1
            count += 1
            table[r][c] = count

        # up
        for i in xrange(edge_length - 1):
            r -= 1
            count += 1
            table[r][c] = count
    return table


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_distance(1, 9) == 2, "First"
    assert find_distance(9, 1) == 2, "Reverse First"
    assert find_distance(10, 25) == 1, "Neighbours"
    assert find_distance(5, 9) == 4, "Diagonal"
    assert find_distance(26, 31) == 5, "One row"
    assert find_distance(50, 16) == 10, "One more test"
