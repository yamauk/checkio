def checkio(game_result):
    for i in xrange(len(game_result)):
        for j in xrange(len(game_result[0])):
            if game_result[i][j] == 'X':
                if is_winner(i, j, game_result, 'X'):
                    return 'X'
            elif game_result[i][j] == 'O':
                if is_winner(i, j, game_result, 'O'):
                    return 'O'
    return 'D'


def is_winner(i, j, game_result, player):
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if 0 <= i + 2 * dy < len(game_result) and 0 <= j + 2 * dx < len(game_result) and (dy != 0 or dx != 0):
                if game_result[i + dy][j + dx] == player and game_result[i + 2 * dy][j + 2 * dx] == player:
                    return True
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        u"X.O",
        u"XX.",
        u"XOO"]) == "X", "Xs wins"
    assert checkio([
        u"OO.",
        u"XOX",
        u"XOX"]) == "O", "Os wins"
    assert checkio([
        u"OOX",
        u"XXO",
        u"OXX"]) == "D", "Draw"
    assert checkio([
        u"O.X",
        u"XX.",
        u"XOO"]) == "X", "Xs wins again"

