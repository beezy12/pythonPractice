
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
        first = word[0]
            print word[1:len(word)] + first + pyg
        else:
            print 'empty'
