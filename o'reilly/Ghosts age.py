def checkio(opacity):
    fib_list = get_fib_list()
    current = 10000
    for year in range(10000):
        if year in fib_list:
            current -= year
        else:
            current += 1
        if current == opacity:
            return year


def get_fib_list():
    fib_list = [0, 1]
    for i in range(2, 25):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    return fib_list

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"