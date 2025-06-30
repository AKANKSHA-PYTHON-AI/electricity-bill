print('-----welcome to SV Travels-----')
print('----available serices are----')
print('1.pulivendula to banglore')
print('2.pulivendula to hyderabad')
print('3.pulivendula to vijayawada')
print('4.pulivendula to kurnool')

print('=================please carefully errors ===========')
service =input("enter from where to where : ")
fare=0

if service == 'pulivendula to banglore':
    fare = 500
elif service == 'pulivendula to kurnool':
    fare = 300
elif service == 'pulivendula to vijayawada':
    fare = 600
elif service == 'pulivendula to hyderabad':
    fare = 800
else:
    print('no service available')


print(f'your service is from {service.strip().capitalize()} , fare for it is {fare}.')
print('====thank you for visiting our travels====')