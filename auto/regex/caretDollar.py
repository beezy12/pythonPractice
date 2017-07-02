
import re

# begins with 'hello'
begins = re.compile(r'^Hello')
print(begins.search('Hello there friend'))
# <_sre.SRE_Match object; span=(0, 5), match='Hello'>

# end with 1 or more digits 
ends = re.compile(r'\d$')
print(ends.search('robot number 655'))
# <_sre.SRE_Match object; span=(15, 16), match='5'>

# begins AND ends with a digits (+ symbol means one or more
# numbers with a gap in them will not matc
allnumber = re.compile(r'^\d+$')
print(allnumber.search('32832346283462'))
#print(allnumber.findall())

# can't grab a number with a gap in it, must be consecutive
print(allnumber.search('3535 35353 33533535') == None)
