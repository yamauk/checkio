def count_gold(pyramid):
    """
    Return max possible sum in a path from top to bottom
    """
    # replace this for solution
    sum_list = []
    dfs(0, 0, 0, pyramid, sum_list)
    return max(sum_list)


def dfs(x, y, sum, pyramid, sum_list):
    if y == 0:
        sum += pyramid[0][0]
    if y + 1 < len(pyramid) and x < len(pyramid[y + 1]):
        if dfs(x, y + 1, sum + pyramid[y + 1][x], pyramid, sum_list):
            return True

    if y + 1 < len(pyramid) and x + 1 < len(pyramid[y + 1]):
        if dfs(x + 1, y + 1, sum + pyramid[y + 1][x + 1], pyramid, sum_list):
            return True

    sum_list.append(sum)
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_gold((
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        (3, 1, 3, 1, 3),
        (2, 2, 2, 2, 2, 2),
        (5, 6, 4, 5, 6, 4, 3)
    )) == 23, "First example"
    assert count_gold((
        (1,),
        (2, 1),
        (1, 2, 1),
        (1, 2, 1, 1),
        (1, 2, 1, 1, 1),
        (1, 2, 1, 1, 1, 1),
        (1, 2, 1, 1, 1, 1, 9)
    )) == 15, "Second example"
    assert count_gold((
        (9,),
        (2, 2),
        (3, 3, 3),
        (4, 4, 4, 4)
    )) == 18, "Third example"
