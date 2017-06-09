#look what you wrote in your book on pg 104.

#the main function has 4 parts:

def main():    
    value = 99          #1
    print('The value is', value)     #2
    change_me(value)       #3
    print('Back in the main the value is', value)     #4

def change_me(arg):
    print('I am changing the value.')
    arg = 0
    print('Now the value is', arg)

main()
    
    
