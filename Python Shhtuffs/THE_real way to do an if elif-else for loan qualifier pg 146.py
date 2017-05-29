
MIN_SALARY = 30000
MIN_YEARS = 2

def main():
    salary = float(input('Enter your salary: '))
    years = int(input('Enter your years on the job: '))

    if salary >= MIN_SALARY and years >= MIN_YEARS:  #the and here is crucial
        print('Congrats fucker....you did it.')

    else:
        print('No way Jose. Get your shit together.')

main()
    
