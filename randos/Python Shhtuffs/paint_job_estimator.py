#Brian Stumbaugh

def main():
    wall_size = int(input('Enter sq. feet of wall space: '))
    paint_cost = int(input('Enter cost of a gallon of paint: '))
    calculate (wall_size, paint_cost)

def calculate (wall_size, paint_cost):
    gallons = wall_size / 115 + 1
    paint = gallons * paint_cost
    labor = gallons * 8
    cost = labor * 20
    total = paint + cost
    total_cost (wall_size, gallons, paint, labor, cost, total)

def total_cost (wall_size, gallons, paint, labor, cost, total):
    print('For', wall_size, 'sq. feet of wall space you will need- ')
    print('Gallons of paint: ', format(gallons, '.2f'), sep='')
    print('Cost of the paint: $', format(paint, '.2f'), sep='')
    print('Hours of labor: ', format(labor, '.2f'), sep='')
    print('Labor charges: $', format(cost, '.2f'), sep='')
    print('The total cost is: $', format(total, '.2f'), sep='')

main()
    
