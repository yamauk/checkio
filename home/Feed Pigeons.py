def checkio(number):
    n = 1
    while number - sum_portions(n) > 0:
        n += 1
    return max(num_pigeons(n) + min(number - sum_portions(n), 0),
               num_pigeons(n - 1))


def sum_portions(n):
    return n * (n + 1) * (n + 2) / 6


def num_pigeons(n):
    return n * (n + 1) / 2


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"