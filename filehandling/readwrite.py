

#baconfile = open('/Users/brianstumbaugh/Documents/beezyWorkspace/pythonPractice/filehandling/funky.py')
#content = baconfile.read()        read all content
#content = baconfile.readlines()   read each line and put into a comma-separated list, with \n and everything


'''
ALWAYS THESE 3 STEPS: 
    - open
    - do something
    - close
'''

baconfile = open('/Users/brianstumbaugh/Documents/beezyWorkspace/pythonPractice/filehandling/bacon.txt', 'w')
baconfile.write('first I wrote this...\n')
baconfile.close()

baconfile = open('/Users/brianstumbaugh/Documents/beezyWorkspace/pythonPractice/filehandling/bacon.txt', 'a')
baconfile.write('..and then I appended this')
baconfile.close()

baconfile = open('/Users/brianstumbaugh/Documents/beezyWorkspace/pythonPractice/filehandling/bacon.txt', 'r')
content = baconfile.read()
baconfile.close()

print(content)

