from collections import OrderedDict
import string

ALPHABETS = "abcdefghijklmnopqrstuvwxyz0123456789"
TABLE_SIZE = 6


def encode(message, key):
    key_table = generate_key_table(key)
    digraph = convert_to_digraph(message)

    result = ""
    for first, second in digraph:
        first_index, second_index = get_indices(first, second, key_table)

        # both of the pair in a same row
        if first_index[0] == second_index[0]:
            if first_index[1] + 1 > TABLE_SIZE - 1:
                result += key_table[first_index[0]][0]
            else:
                result += key_table[first_index[0]][first_index[1] + 1]
            if second_index[1] + 1 > TABLE_SIZE - 1:
                result += key_table[second_index[0]][0]
            else:
                result += key_table[second_index[0]][second_index[1] + 1]
        # both of the pair in a same col
        elif first_index[1] == second_index[1]:
            if first_index[0] + 1 > TABLE_SIZE - 1:
                result += key_table[0][first_index[1]]
            else:
                result += key_table[first_index[0] + 1][first_index[1]]
            if second_index[0] + 1 > TABLE_SIZE - 1:
                result += key_table[0][first_index[1]]
            else:
                result += key_table[second_index[0] + 1][second_index[1]]
        else:
            result += key_table[first_index[0]][second_index[1]]
            result += key_table[second_index[0]][first_index[1]]

    return result


def decode(secret_message, key):
    key_table = generate_key_table(key)
    digraph = zip(*[iter(secret_message)] * 2)

    result = ""
    for first, second in digraph:
        first_index, second_index = get_indices(first, second, key_table)

        # both of the pair in a same row
        if first_index[0] == second_index[0]:
            if first_index[1] - 1 < 0:
                result += key_table[first_index[0]][-1]
            else:
                result += key_table[first_index[0]][first_index[1] - 1]
            if second_index[1] - 1 < 0:
                result += key_table[second_index[0]][-1]
            else:
                result += key_table[second_index[0]][second_index[1] - 1]
        # both of the pair in a same col
        elif first_index[1] == second_index[1]:
            if first_index[0] - 1 < 0:
                result += key_table[-1][first_index[1]]
            else:
                result += key_table[first_index[0] - 1][first_index[1]]
            if second_index[0] - 1 < 0:
                result += key_table[-1][second_index[1]]
            else:
                result += key_table[second_index[0] - 1][second_index[1]]
        else:
            result += key_table[first_index[0]][second_index[1]]
            result += key_table[second_index[0]][first_index[1]]

    return result


def get_indices(first, second, key_table):
    first_index = [0, 0]
    second_index = [0, 0]
    for i, row in enumerate(key_table):
        if first in row:
            first_index = (i, row.index(first))
        if second in row:
            second_index = (i, row.index(second))
    return first_index, second_index


def generate_key_table(key):
    chars = list(OrderedDict.fromkeys(key))
    key_table_elements = chars + [c for c in ALPHABETS if c not in chars]

    # split key_table_elements to 6x6 table
    return zip(*[iter(key_table_elements)] * TABLE_SIZE)


def convert_to_digraph(message):
    message = message.lower()
    exclude = set(string.punctuation + " ")
    message = ''.join(c for c in message if c not in exclude)
    # split message to (a,b) pairs. A residual is filled with None
    digraph = ""

    i = 0
    while i < len(message):
        first = message[i]
        second = message[i + 1]
        if first == second:
            addition = 'x'
            if first == 'x':
                addition = 'z'
            digraph += first + addition
            if i + 1 == len(message) - 1:
                digraph += second
                break
            i += 1
        else:
            digraph += first + second
            if i + 2 == len(message) - 1:
                digraph += message[i + 2]
                break
            i += 2
    if len(digraph) % 2 != 0:
        if digraph[-1] == 'z':
            digraph += 'x'
        else:
            digraph += 'z'
    return zip(*[iter(digraph)] * 2)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert encode("Fizz Buzz is x89 XX.",
                  "checkio101") == 'do2y7mt22kry94y2y2', "Encode fizz buzz"
    assert decode("do2y7mt22kry94y2y2",
                  "checkio101") == 'fizxzbuzzisx89xzxz', "Decode fizz buzz"
    assert encode("How are you?",
                  "hello") == 'ea2imb1ht0', "Encode How are you"
    assert decode("ea2imb1ht0", "hello") == 'howareyouz', "Decode How are you"
    assert encode("My name is Alex!!!",
                  "alexander") == 'i1dlkxjqlexn', "Encode Alex"
    assert decode("i1dlkxjqlexn", "alexander") == 'mynameisalex', "Decode Alex"
    assert encode("Who are you?", "human") == 'rnvftc1jd5', "Encode WHo"
    assert decode("rnvftc1jd5", "human") == 'whoareyouz', "Decode Who"
    assert encode("ATTACK AT DAWN",
                  "general") == 'ewwektewhnua', "Encode attack"
    assert decode("ewwektewhnua", "general") == 'attackatdawn', "Decode attack"
