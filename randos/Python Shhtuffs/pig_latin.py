#Brian Stumbaugh

VOWELS = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
          
def main():
    pig = input('Enter a sentence to be converted to Pig Latin: ')

    words = pig.split()

    for word in words:
          if word[0] in VOWELS:
              print (word + 'ay'),
          else: print (word[1:] + word[0] + 'ay'),

main()
