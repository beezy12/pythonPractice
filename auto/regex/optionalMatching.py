
import re

# use parens followed by a ? to indicate optional matching
batRegex = re.compile(r'bat(wo)?man')

mo = batRegex.search('I saw batwoman flying over')
print(mo.group()) # returns batwoman

mo2 = batRegex.search('batman is my jam')
print(mo2.group()) # returns batman



# using the phone number reference from regex1 and regex2
# we can optionally check for an area code
phoneReg = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
mophone = phoneReg.search('my number is 867-5309')
print(mophone.group()) # prints 867-5309

motwo = phoneReg.search('mine has an area code 615-911-9111')
print(motwo.group())
