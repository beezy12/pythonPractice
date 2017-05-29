#this program shows how you can use a global constant (number that cannot be
#changed) to calculate a compnay that matches 5% of your salary each year
# and your bonuses each year and puts it in your retirement fund


#so first we set up the global constant, which will be the 5% we are trying
#to calculate out of the salary and bonuses.

CONTRIBUTION_RATE = 0.05

def main():
    gross_pay = float(input('Enter gross pay: '))
    bonus = float(input('Enter the amount of bonuses: '))
    show_pay_contrib(gross_pay)
    show_bonus_contrib(bonus)


def show_pay_contrib(gross):
    contrib = gross * CONTRIBUTION_RATE
    print('Contribution for gross pay: $', \
          format(contrib, ',.2f'), \
          sep='')

def show_bonus_contrib(bonus):
    contrib = bonus * CONTRIBUTION_RATE
    print('Contribution for gross pay: $', \
          format(contrib, ',.2f'), \
          sep='')

main()
