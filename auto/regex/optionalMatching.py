
import re

# use parens followed by a ? to indicate optional matching
batRegex = re.compile(r'bat(wo)?man')

mo = batRegex.search('I saw batwoman flying over')
print(mo.group()) # return batwoman

mo2 = batRegex.search('batman is my jam')
print(mo2.group()) # returs batman
