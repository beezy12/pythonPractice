
import os

myfiles = ['test.txt', 'racers.csv', 'home.json']

for filename in myfiles:
    print(os.path.join('~/Documents/pythontests', filename))
