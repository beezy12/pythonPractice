
def collatz(number):
    if number % 2 == 0:
        eve = number // 2
        print(eve)
        return eve 
    else:
        odd = 3 * number + 1
        print(odd)
        return odd


try:
    usernum = int(input('enter a positive number that will always end up at 1: '))
    while usernum != 1 and usernum > 1:
        usernum = collatz(usernum)
except ValueError:
    print('invalid......enter an integer')
