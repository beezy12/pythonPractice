
person = {
    "amanda": {
        "age":29,
        "nickname": "manna",
        "hometown": "indy"
    }
}


while True:
    user = input('enter name of person: ')
    info = input('enter info you want to see: ')

    if user or info == '':
        break

    if user in person:
        print(person[user][info])
    else:
        print('I cant find that person')
        newperson = input('enter a name for the person you want store: ')
        newperson[topic] = input('now enter a key to list: ')
        newperson[topic][key] = input('what data do you want to set to that key?: ')

        print(person)

