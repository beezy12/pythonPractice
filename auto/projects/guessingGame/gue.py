
import random

mine = random.randint(1, 20)
print('you get 6 guesses')


for guess in range(1, 7):
    user = int(input('enter a number between 1 and 20: '))

    if user < mine:
        print('too low')
    elif user > mine:
        print('you too high now')
    else:
        break

if user == mine:
    print('bout time. it took you ' + str(guess) + ' guesses.')
else:
    print('you loser. the number was ' + mine)



