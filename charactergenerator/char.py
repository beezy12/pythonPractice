

myguy = {}
possibleraces = ['human', 'elf', 'half-elf', 'dwarf', 'halfling']
possibleclasses = ['fighter', 'thief', 'mage', 'cleric']

def getname():
    myname = input('Enter a name for your character: ')
    myguy['name'] = myname
    print()
    print('You chose the name ' + myguy['name'])
    print()


def getrace():
    print('Now choose from these races: ')
    for race in possibleraces:
        print(race)
    print()
    myguy['myrace'] = input('What race do you choose?: ')
    print()
    print('You chose the race of ' + myguy['myrace'])
    print()


def getclass():
    print('Next choose you character class:')
    for myclass in possibleclasses:
        print(myclass)
    print()
    myguy['myclass'] = input('what do you choose?: ')

    print('So far, this is your character....')
    print('A ' + myguy['myrace'] + ' ' + myguy['myclass'] + ' named ' + myguy['name'])

def main():
    getname()
    getrace()
    getclass()


if __name__ == '__main__':                                                                                                                                                   
    main()

