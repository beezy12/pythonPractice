
# using parentheses allows you to create groups, starting at 1 for group 1
# using 0 or no argument will return the entire matched text

import re

phoneNum = re.compile(r'(\d{3})-(\d{3}-\d{4})')

mo = phoneNum.search('my number is 615-867-5309')

# groups start at 1. group 0 and empty are all groups
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())

# also retrieve everything by using 'groups'
# notice the parentheses are escaped here for the area code
print('using groups****************')
phoneNum = re.compile(r'(\(\d{3}\))-(\d{3}-\d{4})')
mo = phoneNum.search('my number is (615)-867-5309')
#mo.groups()
areacode, number = mo.groups()
print(areacode)
print(number)
