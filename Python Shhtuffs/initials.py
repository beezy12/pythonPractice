#Brian Stumbaugh

def main():
    name = input('Enter your full name (first, middle, and last): ')
    initials = name.split()
    first = (initials[0][0].upper() + '.')
    second = (initials[1][0].upper() + '.')
    third = (initials[2][0].upper() + '.')
    print(first + second + third)
    

main()

#entered: Brian Patrick Stumbaugh
#returned: B.P.S.
