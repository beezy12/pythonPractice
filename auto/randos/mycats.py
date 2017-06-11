
catnames = []

while True:
    print('Enter the name of cat ' + str(len(catnames) + 1) + ' or enter nothing to stop : ') 

    name = input()
    if name == '':
        break

    catnames.append(name)
print(catnames)
print('my cats are: ')
for name in catnames:
    print('   ' + name)
