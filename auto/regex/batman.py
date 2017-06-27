
import re

batRegex = re.compile(r'bat(man|mobile|arang|copter)')
mo = batRegex.search('batmobile lost its wheel and batman died')

print(mo.group())
print(mo.group(1))
#print(mo.group(2))

# NOTE: 'batman' was not listed as group2 because batmobile came first and was matched
