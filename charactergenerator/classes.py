

class Character(object):

    def __init__(self, race, classname, gender, age):
        self.race = race
        self.classname = classname
        self.gender = gender
        self.age = age

    def get_stats():
        stats = {
            strength: 0,
            intelligence: 0,
            wisdom: 0,
            dexterity: 0,
            constitution: 0,
            charisma: 0
        }

        return stats

    def description(self):
        print('I am a {2} {0} {1}, {3} years of age'.format(self.race, self.classname, self.gender, self.age))
        stats = get_stats()
        print(stats)



beez = Character('elf', 'thief', 'male', 32)

beez.description()
