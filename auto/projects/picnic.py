
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
                'Bob': {'ham sandwiches': 3, 'apples': 2},
                'Carol': {'cups': 3, 'apple pies': 1}}

def countFood(guests, food):
    numbrought = 0
    for k, v in guests.items(): 
        # v here is apples: 5, pretzels: 12
        numbrought = numbrought + v.get(food, 0)

    return numbrought



print('- apples: ' + str(countFood(allGuests, 'apples')))
print('- ham sandwiches: ' + str(countFood(allGuests, 'ham sandwiches')))
print('- cups: ' + str(countFood(allGuests, 'cups')))
print('- roaches: ' + str(countFood(allGuests, 'roaches')))
print('- pretzels: ' + str(countFood(allGuests, 'pretzels')))
