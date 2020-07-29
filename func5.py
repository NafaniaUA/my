night=int(input('input night '))
city=input('input city ')
days=int(input('input days '))
spending_money=float(input('Input money to spend '))

def hotel_cost(night):
    return night*140

#night=int(input('input night '))
print('pay for hotel ',hotel_cost(night),'$')

def plane_ride_cost(city):
    if city=="Charlotte":
        return 183
    elif city=="Tampa":
        return 220
    elif city=="Pitssburg":
        return 222
    elif city == "Los Angeles":
        return 475
    else:
        return 0

#city=input('input city ')
print('Ride_cost ', plane_ride_cost(city),'$')

def rental_car_cost(days):
    if days<3:
        return days*40
    elif days>=3 and days<7:
        return days*40-20
    elif days >=7:
        return days*40-50
#days=int(input('input days '))
print('CAR_cost ', rental_car_cost(days),'$')    

def trip_cost(city,days,spending_money):
    if plane_ride_cost(city)==0:
        print("No such City")
    else:
        print(hotel_cost(night)+plane_ride_cost(city)+rental_car_cost(days)+spending_money)
print('You spend ', spending_money)
print('Тotal: ', trip_cost(city,days,spending_money))
#Результат правильний, але звідкись вилазить None