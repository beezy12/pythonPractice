


import re

strs = "('yooo', 'wassup', 'mang')"

# creates a comma-separated list of all the words in the string above
words = re.findall(r"\'([A-Za-z]+)\'", strs)
print (words)

newone = "- butter ".join(words)
print(newone)




