import math


def checkio(a, b, c):
    a, b, c = sorted(map(float, [a, b, c]))
    if a + b <= c:
        return [0, 0, 0]

    # replace this for solution
    return sorted(
        [get_angle(a, b, c), get_angle(c, a, b), get_angle(b, c, a)])


def get_angle(a, b, c):
    return int(round(
        math.degrees(math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)))))


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
