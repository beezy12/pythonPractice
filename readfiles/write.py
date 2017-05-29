#filename = "hello.txt"
#file = open(filename, "r")
#for line in file:
    #print line,

fh = open('hello.txt', 'w')
mylines = ['this is a picture \n', 'of what you ask \n', 'of my dog bubby \n']
fh.writelines(mylines)
fh.close()
