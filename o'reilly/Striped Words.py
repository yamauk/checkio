VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
import re


def checkio(text):
    words = [w.upper() for w in re.split(' |,|\.|\?|!', text)]
    regex = '([%s]{2})|([%s]{2})|[0-9]' % (VOWELS, CONSONANTS)
    return len([word for word in words if len(word) > 1 and re.search(regex, word) is None])


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"My name is ...") == 3, "All words are striped"
    assert checkio(u"Hello world") == 0, "No one"
    assert checkio(u"A quantity of striped words.") == 1, "Only of"
    assert checkio(u"Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
