#Brian Stumbaugh

fahrenheit = float(input("Enter a temperature in Fahreheit: ")) #68 
celsius = - 32 * fahrenheit * 5.0 / 9.0
print("Temperature converted to Celsius: ", celsius, "degrees")
 #('Temperature converted to Celsius: ', 50.222222222222221, 'degrees')


#fixed the bug by moving the -32 after the fahrenheit,
# and putting a parentheses around it, as this had to be
#calculated before the 5 //9 for it to work



fahrenheit = float(input("Enter a temperature in Fahreheit: "))
celsius = (fahrenheit - 32) * 5 // 9
print("Temperature converted to Celsius: ", celsius, "degrees")
