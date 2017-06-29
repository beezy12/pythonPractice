
#! python3

import pyperclip
import re
import pprint

text = pyperclip.paste()
words = text.split('\n')
lines = list(filter(None, words))  #filters out blank items in LIST
lines = ' '.join(lines)

# this is called list comprehension
# list comprehension example: squares = [x**2 for x in range(1, 11)
#lines[:] = [x for x in lines if ]

regex = re.compile(r'(\[\d\:\d{2}\])')
#fulltext = 'this is a test [7:12]'
#test = regex.search(fulltext)
#print('found this: ' + test.group())

#print(re.sub(regex, '', fulltext))
newlines = re.sub(regex, '', lines)

#filtered = list(filter(lambda i: not regex.search(i), fulltext))
#filtered = [i for i in fulltext if not regex.search(i)]
#print(filtered)


text = ' '.join(newlines)
pyperclip.copy(text)


# use only one of the following lines, whichever you prefer
#filtered = filter(lambda i: not regex.search(i), full)
#filtered = [i for i in full if not regex.search(i)]


'''
Oh yeah, good point

[6:53] 
it will give you all _unfinished_ golf slates

[6:53] 
so you'll have to delete the non-weekend one

[6:54] 
...which you have to do every week anyway

[6:54] 
I assume you did that yesterday
'''
