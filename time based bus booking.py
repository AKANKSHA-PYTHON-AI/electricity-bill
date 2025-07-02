import datetime
Present_time=datetime.datetime.now()
print('present time is ',Present_time)


print('=====welcome to OVR travels=====')

print('---available buses are---')

print('1.tadipatri to kurnool')
print('2.tadipatri to hyderabad')
print('3.tadipatri to guntur')
print('4.tadipatri to pulivendula')


print('------be careful while entering you details-------')
print()
print('fill the following details to book your ticket one by one---->')
print()
name = input('enter your name :')
age = input('enter your age :')
phone = input('enter your number :')

route = input('enter from start location to stop location :')
print(route)


if route == 'tadipatri to pulivendula':
    bus_fare = 100
elif route == 'tadipatri to kurnool':
    bus_fare = 400
elif route == 'tadipatri to hyderabad':
    bus_fare = 700
elif route == 'tadipatri to guntur':
    bus_fare = 800
else:
    print('out of service')



print()
print('your name is ',name)
print()
print('you are ',age)
print()
print('your contact number is ',phone)
print()
print('your service is from ',route)
print()
print('the amount you should pay is ',bus_fare)

print('============thank you for visiting for travels===========')