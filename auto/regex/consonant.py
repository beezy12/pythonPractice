
import re

# the caret ^ negates the search
# “You can also use the caret symbol (^) at the start of a regex to indicate that a match must occur at the beginning of the searched text. Likewise, you can put a dollar sign ($) at the end of the regex to indicate the string must end with this regex pattern.”
consonant = re.compile(r'[^aeoiuAEOIU]')
text = consonant.findall('Robocop eats baby food. BABY FOOD')
print(text)
# ['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', ' ', 'B', 'B', 'Y', ' ', 'F', 'D']

# to get vowels 
vowels = re.compile(r'[aeiouAEIOU]')
print(vowels.findall('Robocop eats baby food. BABY FOOD'))
# ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']
