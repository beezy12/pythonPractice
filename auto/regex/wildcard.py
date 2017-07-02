
import re

# “The . (or dot) character in a regular expression is called a wildcard and will match any character except for a newline.”

# the dot will match just one character that ends in 'at'
regex = re.compile(r'.at')
print(regex.findall('the cat in the hat went splat flat'))
# ['cat', 'hat', 'lat', 'lat']


names = re.compile(r'First Name: (.*) and Last Name: (.*)')
mo = names.search('First Name: Brian and Last Name: Stumbaugh')
print(mo.group(1))
print(mo.group(2))
