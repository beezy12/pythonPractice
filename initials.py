

name = input('whats your full name? ')


def makeIt(name):
    if len(name) < 2:
        init = name.split()
        first = str(init[0][0].upper)
        last = str(init[1][0].upper)
        print (first + last)
