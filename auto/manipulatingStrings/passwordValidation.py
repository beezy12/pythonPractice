
while True:
    age = input('Enter your age: ')
    if age.isdecimal():
        break
    print('You must enter a number....')
    
print()
print('You entered ' + age)
print()

while True:
    password = input('Enter a new passwordword (only numbers and letters): ')
    if password.isalnum():
        break
    print('you failed my simple instructions...')

print()
print('you new passwordword is: ' + password)

