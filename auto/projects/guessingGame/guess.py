
import random

myNum = random.randint(1, 20)
print(myNum)

print('Im thinking of a number between 1 and 20')

def prompted():
    return int(input('Take a guess: '))

guessCount = 0

guess = prompted()

print('user guesses....' + str(guess))

if myNum == guess:
    guessCount += 1
    print('you got my number in ' + guessCount + ' guesses.')
elif guess < myNum:
    guessCount += 1
    print('too low pardner')
    prompted()
else:
    guessCount += 1
    print('too high man')
    prompted()


#while guess not myNum:
#    if guess < myNum:
###        guessCount += 1
###        print('too low pardner')
    
