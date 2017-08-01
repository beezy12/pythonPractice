

class Car(object):
    
    def __init__(self, owner, make, model, color, year):
        self.owner = owner
        self.make = make
        self.model = model
        self.color = color
        self.year = year

    def description(self):
        print('{} has a {} {} {} colored {}'.format(self.owner, self.year, self.make, self.model, self.color))


manna = Car('manna', 'honda', 'fit', 'black', 2013)
manna.description()

brian = Car('brian', 'toyota', 'camry', 'navy', 1995)
brian.description()
