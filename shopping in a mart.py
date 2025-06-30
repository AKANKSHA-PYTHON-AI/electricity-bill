print('========WELCOME TO SMART========')
print()
print('Available products list given below.')
products = '''
PRODUCT-NAME        -       PRICE
=====================================
1.Bottle            -        150/- each
2.Book              -        100/- each
3.Perfume           -        250/- each
4.Carry bag         -        500/- each
5.Set of boxes      -        200/- each set
6.Exam plank        -        150/- each  '''
print(products)
print()
print('Now choose the product you want to buy.')
product_name = input('Enter product name to buy or quit to exit : ').capitalize()

while True:
    if product_name == 'Bottle':
        price = 150
    elif product_name == 'Book':
        price = 100
    elif product_name == 'Perfume':
        price = 250
    elif product_name == 'Carry bag':
        price = 500
    elif product_name == 'Set of boxes':
        price = 200
    elif product_name == 'Exam plank':
        price = 150
    elif product_name == quit:
        break
    else:
        print(f'{product_name} is not available,please buy available items.')
        continue

    print('Now enter the quantity of your product.')
    product_quantity = int(input('Enter product quantity : '))
    print()
    total_amount = product_quantity*price
    print(f'Your current bill = {total_amount}')
    note1 = 'Note : Discount is applied when your total_amount > 2000.'
    print(note1)
    print('--------verifying your bill---------')
    if total_amount > 2000:
        discount = total_amount*0.20
        final_amount = total_amount - discount
        print('Congrats dear customer! you got 20% discount.')
    else:
        total_amount < 2000
        final_amount = total_amount
        print('Sorry,you have no discount') 
        print()

    print("********BILL********")
    print(f'Your total bill is {final_amount}.')
    print()
    print('========THANK YOU FOR JOINING US=========')
         