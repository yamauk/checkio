def checkio(words_set):
    for word in words_set:
        for other_word in words_set:
            for n in xrange(1, len(word)):
                if other_word != word and other_word == word[n:]:
                    return True
    return False

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio({u"hello", u"lo", u"he"}) == True, "helLO"
    assert checkio({u"hello", u"la", u"hellow", u"cow"}) == False, "hellow la cow"
    assert checkio({u"walk", u"duckwalk"}) == True, "duck to walk"
    assert checkio({u"one"}) == False, "Only One"
    assert checkio({u"helicopter", u"li", u"he"}) == False, "Only end"
