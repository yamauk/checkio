from itertools import chain
from collections import Counter


def break_rings(rings):
    counts = Counter(list(chain.from_iterable(rings))).most_common()
    rings = list(rings)
    n = 0
    while len(rings) > 0:
        for k, c in counts:
            n += 1
            rings = remove_ring(k, rings)
            if len(rings) == 0:
                return n
            break
        # update counts
        counts = Counter(list(chain.from_iterable(rings))).most_common()
    return 0


def remove_ring(i, rings):
    result = []
    for ring in rings:
        if not i in ring:
            result.append(ring)
        else:
            print ring
    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print break_rings(({3,4},{5,6},{2,7},{1,5},{2,6},{8,4},{1,7},{4,5},{9,5},{2,3},{8,2},{2,4},{9,6},{5,7},{3,6},{1,3},))
    assert break_rings(
        ({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
    assert break_rings(
        ({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
    assert break_rings(
        ({5, 6}, {4, 5}, {3, 4}, {3, 2}, {2, 1}, {1, 6})) == 3, "Chain"
    assert break_rings((
        {8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7},
        {8, 7})) == 5, "Long chain"
