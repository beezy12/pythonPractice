


S1 = 1.10
S2 = 2.20
S3 = 3.70
S4 = 3.80

def main():
    weight = int(input('Enter weight: '))
    print('Your shipping charge is: ')
    shipping_charge(weight)

def shipping_charge(weight):

    if weight <= 0:
        shipping_charge = -99 #or 0

    elif weight <= 2:
        shipping_charge = S1
    elif weight <= 6:
        shipping_charge = S2
    elif weight <= 10:
        shipping_charge = S3

    else:
        shipping_charge = S4



    if shipping_charge != -99: #or 0
        print('The shipping charge is $', format(shipping_charge * weight, '.2f'))
    else:
        print('error') #put the error in the else part

main()
