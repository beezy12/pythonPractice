# this program tallies up all items in players inventory along with the count of items

stuff = {
    'rope': 1, 
    'torch': 6, 
    'gold coin': 42, 
    'dagger': 1, 
    'arrow': 12
}

print()
print('Inventory: ')

count = 0
for k, v in stuff.items():
    print(v, k)
    count = count + v

print()
print('total: ' + str(count))
print()

    
