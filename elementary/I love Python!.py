import random

def i_love_python():
    """
        Let's explain why do we love Python.
    """
    
    lovely_monkey='I love Python!'.split()
    while True:
        if lovely_monkey==sorted(lovely_monkey, key=lambda k: random.random()):
            return ' '.join(lovely_monkey)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert i_love_python() == "I love Python!"
