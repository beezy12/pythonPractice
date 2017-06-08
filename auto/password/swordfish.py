

while True:
    print('who are you?')

    name = input()
    if name != 'beezy':
        print('Access Denied!!')
        continue
    print('hello there ' + name + '. What is the password? Hint: it is a fish')
    password = input()
    if password == 'swordfish':
        break
    print('Wrong password.....start over!')

print('Access Granted')
