
def splitit(list):
    #newone = ', '.join(list)
    #print(newone)

    for i in range(len(myArray)):
        print(myArray[i] + ', ', end='')
        if myArray[i] == myArray[-2]:
            print('and ' + myArray[-1])


myArray = ['eggs', 'butter', 'milk', 'chicken']

splitit(myArray)
