OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
    if operation == 'conjunction':
        return x and y
    elif operation == 'disjunction':
        return x or y
    elif operation == 'implication':
        return not x or y
    elif operation == 'exclusive':
        return (x or y) and not (x and y)
    elif operation == 'xor':
        return not (x or y) and not (x and y)
    elif operation == 'equivalence':
        return x == y

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, u"conjunction") == 0, "and"
    assert boolean(1, 0, u"disjunction") == 1, "or"
    assert boolean(1, 1, u"implication") == 1, "material"
    assert boolean(0, 1, u"exclusive") == 1, "xor"
    assert boolean(0, 1, u"equivalence") == 0, "same?"
