# Brian Stumbaugh

def main():
    print('This program computes your BMI.')
    weight = float(input('Enter your weight in pounds: ', )) #entered 197
    height = float(input('Enter your height in inches: ', )) #entered 72
    bmi = (weight / (height*height)) * 703
    print('Your BMI is: ', format(bmi,'.2f'))


    
main()
    


#bmi is 26.72


#should I have formatted the number another way? not sure if it looks right
