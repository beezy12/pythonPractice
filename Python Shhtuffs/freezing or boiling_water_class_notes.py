def main():
    temp = int(input('Enter temperature:'))

    #inside range
    if temp > 32 and temp < 212:
        print('water')

    #outside range
    if temp <= 32 or temp >= 212:
        print('not water')


main()
