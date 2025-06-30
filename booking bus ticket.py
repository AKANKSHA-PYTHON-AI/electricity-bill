print('========Welcome to "MT Travels"========')
print()
from datetime import datetime
print('Your booking time is ',datetime.now())
print() 
print('Our available serices from hyderabad to some places are currently given below.')
print("-----Services-----")
print()
services = '''
1.hyderabad to pulivendula
2.hyderabad to kadapa
3.hydearbad to guntur
4.hyderabad to banglore
5.hyderbad to ongle '''
print()
print('------Please choose correct places----')
service = input('Enter from where to where you want to go :  ')
print('Next choose type of bus you want.')
print('Our available types of buses are ---->')
type = '''
1.a/c
2.non-a/c
3.ordinary '''
print(type)
print()
bus_type = input('Enter what type you need : ')
print()
print('Now fill the following details.')
passenger_name= input('Enter your name : ')
age = input ('Enter your age : ')
phone = input('Enter your contact numnber : ')
address = input('Enter your address : ')
print()
fare = 0
if service == 'hyderabad to pulivendula':
    if bus_type == 'a/c':
        fare = 1500
    elif bus_type == 'non-a/c':
        fare = 1000
    else:
        bus_type == 'ordinary'
        fare = 800
elif service == 'hyderabad to kadapa':
    if bus_type == 'a/c':
        fare = 1300
    elif bus_type == 'non-a/c':
        fare = 1100
    else:
        bus_type == 'ordinary'
        fare = 900
elif service == 'hyderabad to guntur':
    if bus_type == 'a/c':
        fare = 1400
    elif bus_type == 'non-a/c':
        fare = 1000
    else:
        bus_type == 'ordinary'
        fare = 900
elif service == 'hyderabad to banglore':
    if bus_type == 'a/c':
        fare = 2000
    elif bus_type == 'non-a/c':
        fare = 1800
    else:
        bus_type == 'ordinary'
        fare = 1500
elif service == 'hyderabad to ongle':
    if bus_type == 'a/c':
        fare = 1700
    elif bus_type == 'non-a/c':
        fare = 1500
    else:
        bus_type == 'ordinary'
        fare = 1200 
else:
    print('out of service')
    fare = 0

print()
print('Now all details are displayed below.') 
print('If any mistakes again fill your details corectly.')  
print()
print(f'Your name is {passenger_name}')
print(f'Your are {age} old.')
print(f'Your contact number is {phone}.')
print(f'Your address is {address}.')
print(f'You are going from {service} in {bus_type} bus and fare amount for that is {fare}.')
print()
print('Your booking is successfully done.')
print('=========Thank you for choosing our MT Travels==========')    