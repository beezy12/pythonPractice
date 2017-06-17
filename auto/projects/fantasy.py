# this program tallies up all items in players inventory along with the count of items
# it then adds the dragonsloot, which is a list of strings, to it
# so this is adding a list of items to a dictionary of items

stuff = {
    'rope': 1, 
    'torch': 6, 
    'gold coin': 42, 
    'dagger': 1, 
    'arrow': 12
}

dragonsloot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def countInventory(inventory):
    print()
    print('Inventory: ')

    count = 0
    for k, v in inventory.items():
        print(v, k)
        count = count + v

    print()
    print('total: ' + str(count))
    print()

    return count


def addToInventory(inventory, dragons):
    for item in range(len(dragons)):
        if dragons[item] in inventory.keys():
            inventory[dragons[item]] += 1
        else:
            inventory.setdefault(dragons[item], 1)

    return inventory




inv = addToInventory(stuff, dragonsloot)

countInventory(inv)


    
