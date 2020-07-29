def computepay (hours, rate):
    if hours<=40:
        pay=(hours*rate)
        print(pay)
    elif hours>40:
        pay=((40*rate)+((hours-40)*rate*1.5))
        print(pay)

hours=float(input('input hours '))
rate=int(input('inpur rate '))
print(computepay(hours,rate))
