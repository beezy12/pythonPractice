#this demonstrates a function that accepts two arguments

def main():
    print('The sum of 12 and 45 is')
    show_sum(12,45)

#the show_sum function accepts two arguments
#and displays their sum

def show_sum(num1, num2):
    result = num1 + num2
    print(result)

main()


#basically....the 12 and 45 are arguments
#and are passed by their position inside
#the parentheses to the corresponding
#parameter variables. the first num goes
#to the first parameter variable blah blah

#if you switched the numbers positions, then 45
#would get passed to the num1 etc.
