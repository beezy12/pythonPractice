#Brian Stumbaugh


red = 'red'
blue = 'blue'

def main():
    print('Here you will enter 2 primary colors to find their secondary color.')
    color1 = input('Enter your first primary color: ')
    color2 = input('Enter your second primary color: ')
    if color1 == red and color2 == blue or color1 == blue and color2 == red:
        #is that the best way to write that^ ?
        print('You just made purple.')

    else:
        print("You didn't listen to my instructions.")

main()
