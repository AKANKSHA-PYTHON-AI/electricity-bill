print('*******XYZ BIKE SHOWROOM********')
print()
print('======welcome======')
print('Good morning sir,which models you want.')
print('With us from 2023 to 2025 models are available.')
print('Please,select which year models you want to buy.')
year_2023 = '''
bike-name     -           price
================================
1.pulsar       -          150000/-
2.tvs          -          100000/-
3.suzuki       -          130000/- '''
print(year_2023)

year_2024 = '''
bike-name      -          price
================================
1.mt           -          200000/-
2.royal enfield-          180000/-
3.fz           -          150000/- '''
print(year_2024)

year_2025 = '''
bike-name      -          price
=================================
1.duke         -          130000/-
2.r15          -          210000/-
3.enfield      -          250000/-  '''
print(year_2025)

print()

print('NOTE:while entering year you must and should enter year first,(for e.g year_2025) ')
year = eval(input('Enter the year of your model that have choosen :')).strip()

if year == year_2023:
        print(f'here are {year_2023} models')
elif year == year_2024:
        print(f'here are {year_2024} models')
else:
    year == year_2025
    print(f'here are {year_2025} models')
    
    

    print('Now choose what type of bike you want.')
    bike_name = input('Enter bike name you wish to buy : ')
    print()


    if bike_name == 'pulsar':
        price = 150000
        discount = 0.10
    elif bike_name == 'tvs':
        price = 100000
        discount = 0.1
    elif bike_name == 'suzuki':
        price = 130000
        discount = 0.3
    elif bike_name == 'mt':
        price = 200000
        discount = 0.2
    elif bike_name == 'royal enfield':
        price = 180000
        discount = 0.15
    elif bike_name == 'fz':
        price = 150000
        discount = 0.5
    elif bike_name == 'duke':
        price = 130000
        discount = 0.6
    elif bike_name == 'r15':
        price = 210000
        discount = 0.25
    elif bike_name == 'enfield':
        price = 250000
        discount = 0.3
        
    else:
        print('ivalid!')
        
 
discount_price = price*discount
total_amount = price-discount_price
print(f'If discount is applied on this bike , then the disount is {discount}% .')
print(f'The total amount of {bike_name} is {total_amount}.')
print('To make your bill,please fill the following details below.')
print()
print('----billing process----')
name = input('Enter your name : ')
age =(input('Enter your age : '))
address = input('Enter your address : ')
phone = int(input('Enter your contact number : '))
method_of_payment = '''
1.online payment
2.cash '''
print(method_of_payment)
if method_of_payment == 'online payment':
    print(f'Here is tyhe scanner,scan and pay your {total_amount}')
else:
    method_of_payment == 'cash'
    print(f'Pay the money in the counter.')
print(f'You are willimg to buy {bike_name} and its final amount is {total_amount}.')
print()


print('*********BILL*********')
print(f'Name : {name}')
print(f'age : {age}')
print(f'address : {address}')
print(f'contact number : {phone}')
print(f'bike : {bike_name}')
print(f'discoun : {discount}')
print(f'price after discount : {discount_price}')
print(f'Amount : {total_amount}')
print(f'payment method : {method_of_payment}')
print()
print('Your bill proccess is successfully finished')
print()
print('========THANK YOU VISITING OUR SHOWROOM========')
    