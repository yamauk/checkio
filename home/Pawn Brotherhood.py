import string


def safe_pawns(pawns):
    n_safe = 0

    for pawn in pawns:
        if is_safe(pawn, pawns):
            n_safe += 1
    return n_safe


def is_safe(pawn, pawns):
    for other_pawn in [p for p in pawns if p != pawn]:
        if int(other_pawn[1]) == int(pawn[1]) - 1 and \
                (ord(other_pawn[0]) == ord(pawn[0]) - 1 or
                         ord(other_pawn[0]) == ord(pawn[0]) + 1):
            return True
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
