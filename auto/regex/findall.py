'''
findall() will not return a Match object but a list of strings — as long as there are no groups in the regular
expression.
If there are groups in the regular expression, then findall() will return a list of tuples.
'''

import re

numbers = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = numbers.findall('cell: 615-666-4433  home: 615-867-5309')
print(mo)



# this one has groups
returningTup = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
print(returningTup.findall('cell: 615-666-4433  home: 615-867-5309'))


'''
    To summarize what the findall() method returns, remember the following:
    When called on a regex with no groups, such as \d\d\d-\d\d\d-\d\d\d\d, the method findall() returns a list of string
    matches, such as ['415-555-9999', '212-555-0000'].
    When called on a regex that has groups, such as (\d\d\d)-(\d\d\d)-(\d\ d\d\d), the method findall() returns a list
    of tuples of strings (one string for each group), such as [('415', '555', '1122'), ('415', '555', '8899')].”
'''
