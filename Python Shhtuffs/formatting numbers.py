format (12345.6789, '.2f')



#or to print format to 2 decimal places

print(format(12345.6789, '.2f'))



# to 1 decimal place

print(format(12345.6789, '.1f'))




print('The number is', format(1.234567, '.2f'))





amount_due = 5000.0
monthly_payment = amount_due / 12
print('The monthly payment is', \
      format(monthly_payment, '.2f'))



#inserting commas

print(format(123456789.456, ',.2f'))



#dollar display

monthly_pay = 5000.0
annual_pay = monthly_pay * 12
print('Your annual pay is $', \
      format(annual_pay, ',.2f'), \
      sep='')

