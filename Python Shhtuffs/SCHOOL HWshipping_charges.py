#Brian Stumbaugh
#kinda saw how this one was done in class
#but I had the general idea down.
#just cleaned it up using your suggestions

RATE1 = 1.10
RATE2 = 2.20
RATE3 = 3.70
RATE4 = 3.80


def main():
    weight = int(input('Enter the package weight: '))
    shipping_charge(weight)
    
    
def shipping_charge(weight):

    if weight <= 0:
        shipping_charge = 0

    elif weight <= 2:
        shipping_charge = RATE1

    elif weight <= 6:
        shipping_charge = RATE2

    elif weight <= 10:
        shipping_charge = RATE3

    else:
        shipping_charge = RATE4

    if shipping_charge != 0:
        print('The shipping charge is $', format(shipping_charge * weight, '.2f'))
    else:
        print('error') #put the error in the else part




main()
    
