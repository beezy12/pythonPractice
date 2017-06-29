'''
“Matching Specific Repetitions with Curly Brackets
If you have a group that you want to repeat a specific number of times, follow the group in your regex with a number in curly brackets. For example, the regex (Ha){3} will match the string 'HaHaHa', but it will not match 'HaHa', since the latter has only two repeats of the (Ha) group.
Instead of one number, you can specify a range by writing a minimum, a comma, and a maximum in between the curly brackets. For example, the regex (Ha){3,5} will match 'HaHaHa', 'HaHaHaHa', and 'HaHaHaHaHa'.
You can also leave out the first or second number in the curly brackets to leave the minimum or maximum unbounded. For example, (Ha){3,} will match three or more instances of the (Ha) group, while (Ha){,5} will match zero to five instances. Curly brackets can help make your regular expressions shorter.”
'''

import re

repetition = re.compile(r'(ha){3,5}')
mo = repetition.search('hahahahahahahahaha')

print(mo.group()) # prints hahahahaha
print(mo.group()) # prints hahahahaha

over = re.compile(r'(ha){3,}')
mo1 = over.search('hahahahahahahahahahahahahaha')
print(mo1.group())





# must match EXACTLY 3 ha's

laugh = re.compile(r'(ha){3}')

molaugh = laugh.search('hahaha')

print(molaugh.group())
