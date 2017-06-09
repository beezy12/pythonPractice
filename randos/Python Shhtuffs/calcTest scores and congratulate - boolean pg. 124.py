#pg 123 boolean practice - teacher wants a program that will let her students
#calulate their average test scores over 3 tests. She also wants the program to congratulate
#the student if the average is above 95

#here's the pseudocode:
#get the first test score
#get the second test score
#get the third test score
#calculate the average
#display the average
#congratulate those over 95


#global constant for high score
HIGH_SCORE = 95

def main():
#get the three test scores
    test1 = int(input('Enter the score for test 1: '))
    test2 = int(input('Enter the score for test 2: '))
    test3 = int(input('Enter the score for test 3: '))

#calculate the average test score
    average = (test1 + test2 + test3) / 3

#print the average
    print('The average test score is', average)

#if the average score is 95 or greater, congratulate
    if average >= HIGH_SCORE:
        print('You fookin rock bro!')

#call the main function
main()
