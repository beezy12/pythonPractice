
# this program counts the number of characters in the string and stores them in a dictionary. it uses the dictionary
# method 'setdefault' to set the characters to 0 if they don't exist
# also uses pprint to pretty print out the values


import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for char in message:
    count.setdefault(char, 0)
    
    count[char] += 1

pprint.pprint(count)
