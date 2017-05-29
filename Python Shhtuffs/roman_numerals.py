#Brian Stumbaugh



def main():
    number = int(input('Enter your number: '))

    if number == 1:
        print('The Roman Numeral of 1 is I.')
    if number == 2:
        print('The Roman Numeral of 2 is II.')
    if number == 3:
        print('The Roman Numeral of 3 is III.')
    if number == 4:
        print('The Roman Numeral of 4 is IV.')
    if number == 5:
        print('The Roman Numeral of 5 is V.')
    if number == 6:
        print('The Roman Numeral of 6 is VI.')
    if number == 7:
        print('The Roman Numeral of 7 is VII.')
    if number == 8:
        print('The Roman Numeral of 8 is VIII.')
    if number  == 9:
        print('The Roman Numeral of 9 is IX.')
    if number == 10:
        print('The Roman Numeral of 10 is X.')


    if number > 10 or number < 1:
        print('You have entered an invalid number. We are doing 1' \
              ' through 10, you idiot.', sep=' ')
    

main()
        
                 
