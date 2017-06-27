
#! python3

import pyperclip
import re

text = pyperclip.paste()
words = text.split('\n')
lines = list(filter(None, words))  #filters out blank items in LIST

# this is called list comprehension
# list comprehension example: squares = [x**2 for x in range(1, 11)
#lines[:] = [x for x in lines if ]

searchObj = re.compile(r'[')
test = searchObj.search('this is a [] test')
print('found this: ' + test.group())


#for i in range(len(lines)):
#    print(lines[i])
    #if lines[i][0] == '[':
    #    lines.remove(lines[i])

text = '\n'.join(lines)
pyperclip.copy(text)



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
