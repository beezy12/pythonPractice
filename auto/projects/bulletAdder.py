
#! python3
# bulletAdder.py - adds a bullet to the beggining of each line
# and copies to the clipboard for easy pasting

import pyperclip

text = pyperclip.paste()

# split pasted in text into a LIST of text, splitting on each newline
# then loop through each item in the LIST and add a * to the beginning
# at the end, this gives us a LIST with each item being a * with text after it
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

# next step is to take that LIST and join all the items back into a new paragraph...
# by joining on the \n

text = '\n'.join(lines)

pyperclip.copy(text)

