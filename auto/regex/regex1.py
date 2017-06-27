# “by putting an r before the first quote of the string value, you can mark the string as a raw string, which does not escape characters.”
# “Typing r'\d\d\d-\d\d\d-\d\d\d\d' is much easier than typing '\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d'.”

import re

#phoneNumber = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# create a regex object
phoneNumber = re.compile(r'\d{3}-\d{3}-\d{4}')

# search regex object
# “If the pattern is found, the search() method returns a Match object”
# mo is the generic term for match object
mo = phoneNumber.search('my phone number is 615-862-5309')

# use the group() method to show what was found
print('the number that was found was ' + mo.group())


