#test scores
A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60


def main():
    score = int(input('Enter test score: '))

    if score >= A_SCORE:
        print('You made an A! Noice!')

    else:
        if score >= B_SCORE:
            print('Mleh.....a B.')
        else:
            if score >= C_SCORE:
                print('Average C for that ass.')
            else:
                if score >= D_SCORE:
                    print('D is for dumbass.')
                else:
                    print('F is for failure. You are a huge failure and ' \
                        'will never do anything with your life. Die.')

main()
                      
        
