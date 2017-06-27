
import re

# pipes return whatever comes first in the search. 
# don't put spaces between the pipes, it adds white space
heroes = re.compile(r'batman|tina fey')
mo1 = heroes.search('I like tina fey and batman')
print(mo1.group())  # returns tina fey, she was first 

mo2 = heroes.search('batman destroys tina fey')
print(mo2.group()) #returns batman
