#the is similar to THE REAL WAY TO DO AN IF ELIF ELSE HOME QUALIFIER
#except that the user only has to meet one of the requirements
# so we replace the and with or


MIN_SALARY = 30000
MIN_YEARS = 2

def main():
    salary = float(input('Enter your salary: '))
    years = int(input('Enter your years on the job: '))

    if salary >= MIN_SALARY or years >= MIN_YEARS:  #put or here to meet one of them
        print('Congrats fucker....you did it.')

    else:
        print('No way Jose. Get your shit together.')

main()
    
