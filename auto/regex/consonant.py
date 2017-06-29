
import re

# the caret ^ negates the search
consonant = re.compile(r'[^aeoiuAEOIU]')
text = consonant.findall('Robocop eats baby food. BABY FOOD')
print(text)


# to get vowels 
vowels = re.compile(r'[aeiouAEIOU]')
print(vowels.findall('Robocop eats baby food. BABY FOOD'))
