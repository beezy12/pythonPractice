def main():
    value = 99
    print('The value is', value)
    change_me(value)
    print('Back in main the value is still', value)

def change_me(arg):
    print('I am changing the value.')
    arg = 0
    print('Now the value is', arg,'.')   #<--- couldnt figure out how to
                                        #end this with a period after the arg

main()
