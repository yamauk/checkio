def checkio(time_string):
    time_string = map(lambda x: "{0:0>2}".format(x), time_string.split(':'))
    result = []
    for i, time in enumerate(time_string):
        if i == 0:
            result.append(make_ord(time[0], 2) + ' ' + make_ord(time[1], 4))
        if i > 0:
            result.append(make_ord(time[0], 3) + ' ' + make_ord(time[1], 4))
    return ' : '.join(result)


def make_ord(num, n):
    spec = '0' + str(n) + 'b'
    return format(int(num), spec).replace('0', '.').replace('1', '-')


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(
        u"10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio(
        u"21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio(u"00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio(
        u"23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"

