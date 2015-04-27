FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    words = [FIRST_TEN, SECOND_TEN, OTHER_TENS, HUNDRED]
    speech = []
    n_digits = len(str(number))
    if n_digits > 2:
        speech.append(FIRST_TEN[number / 100 - 1])
        speech.append(HUNDRED)
        number %= 100

    if n_digits > 1:
        if 10 <= number <= 19:
            speech.append(SECOND_TEN[number % 10])
            return ' '.join(speech)
        elif number >= 20:
            speech.append(OTHER_TENS[number / 10 - 2])
        number %= 10

    if n_digits > 0:
        if number > 0:
            speech.append(FIRST_TEN[number - 1])
    return ' '.join(speech)


if __name__ == '__main__':
    checkio(111)
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
