
birthdays = {
    'manna': 'Apr 13',
    'bubby': 'Sep 11',
    'key': 'unknown',
    'bri': 'May 2'
}


while True:
    print('Enter someones birthday: ')
    entry = input()
 
    if entry == '':
        break

    if entry in birthdays:
        print(entry + "'s birthday is " + birthdays[entry])
    else:
        print('I dont seem to have ' + entry + "'s birthday in my system")
        print('...what is ' + entry + "'s birthday? I'll store it.")
        
        newone = input()
        birthdays[entry] = newone

        print(birthdays)
