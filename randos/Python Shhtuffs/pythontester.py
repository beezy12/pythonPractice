#practice from pg 153


#not right tho

def main():
    length1 = int(input('Enter length of rectangle 1: '))
    width1 = int(input('Enter width of rectangle 1: '))
    length2 = int(input('Enter length of rectangle 2: '))
    width2 = int(input('Enter width of rectangle 2: '))
    rec1_figures(length1, width1)
    rec2_figures(length2, width2)

    if area1 > area2:
        print('Rectangle 1 has a larger area with a number of', area1)
    else:
        print('Area 2 has the bigger one, with a number of', area2)

def rec1_figures(length1, width1):
    area1 = length1 * width1
    print('The area of rectangle 1 is', area1)

def rec2_figures(length2, width2):
    area2 = length2 * width2
    print('The got damn area for rectangle 2 is', area2)

main()
    
