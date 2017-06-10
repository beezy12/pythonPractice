# This program gives an estimate for a painting job

#GET
# size of wall space to be painted
#CALCULATE
# number of gallons of paint required
# Hours of labor required
# cost of paint
# labor charges
# total cost of paint job
#DISPLAY receipt

def main():
    wall = int( input( 'Enter square feet to be painted: '))                #size of wall space to be painted
    paint_cost = float( input( 'Enter cost of 1 gallon of paint: '))               #price of one gallon of paint
    calculations (wall,paint_cost)
    print( 'Thank You!')

def calculations (wall,paint_cost):
    gallons = wall // 115 + 1          #Calculates number of gallons needed
    paint = gallons * paint_cost       #Calculates how much paint costs
    labor = gallons * 8                #uses gallons to find labor hours
    cost = labor * 20                  #uses labor hours to find total cost of paint
    total = paint + cost
    receipt (wall,gallons,paint,labor,cost,total)

def receipt (wall,gallons,paint,labor,cost,total):
           
    print ('Keep this quote for your records.')
    print ('Total space to be painted:', \
           format( wall,','),\
           'square feet')
    print ('Gallons required: ', \
           format( gallons, ','))
    print ('Hours of labor required: ', \
           format( labor, ','))
    print ('Cost of paint: $', \
           format(paint, ',.2f'), \
           sep = '')
    print ('Charge for labor: $', \
           format(cost, ',.2f'), \
           sep = '')
    print ('----------------------------')
    print ('Total Paint Job Estimate: $', \
           format(total, ',.2f'), \
           sep = '')

main()

    
    
