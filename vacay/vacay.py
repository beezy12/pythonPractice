def hotel_cost(nights):
    return 140 * nights
    
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
        
def rental_car_cost(days):
    total = 40 * days
    if days >= 7:
        return total - 50
    elif days >=3:
        return total - 20
    else:
        return total
        
def trip_cost(city, days):
    hotel = hotel_cost(days)
    plane = plane_ride_cost(city)
    car = rental_car_cost(days)
    
    return hotel + plane + car
