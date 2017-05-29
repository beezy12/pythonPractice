def main():


    amount1 = input('Enter an amount for 1: ')
    amount2 = input('Enter an amount for 2: ')

    if amount1 > 10 and amount2 < 100:
            if amount1 > amount2:
                print (amount1)
            else: 
                print (amount2)
    else:
        print('You have entered an invalid number.')


main()
