print("=======Welcome to GM mart=======")
print()

print('Available items are listed below.')
print()
items = '''
  items    ---------     price 
=================================
1.apple         -       100 each
2.banana        -       120 each dozen
3.rice packet   -       3000 each
4.guava         -       50 each
5.grapes        -       150 each kg  '''
print(items)
print()
print('Choose the item what you want to buy.')
item = input('Enter the item name to add to cart or exit to check out : ').lower()
print()
total_amount = 0
while True:
    if item == 'apple':
        price = 100
    elif item == 'banana':
        price = 120
    elif item == 'rice packet':
        price = 3000
    elif item == 'guava':
        price = 50
    elif item == 'grapes':
        price = 150
    elif item == 'exit':
        break
    else:
        print(f'{item} is not available in our mart,please select any of available items.')
        print()
        
        

    qunatity = int(input('Enter quantity of your item : '))
    total_item_price = price*qunatity
    print(f'current_total = {total_item_price}')
    print()


    print('------Applying discount------')
    print('*********Final bill*********')
    print(f'the total amount before applying discount : {total_item_price}')
    print()
    if total_item_price > 1000:
        discount = total_item_price*0.10
        final_amount = total_item_price - discount
        print(f'Congratulations! you got 10% discount = {discount}')
    else:
        total_item_price < 1000
        final_amount = total_item_price
        print('Sorry! no discount applied')

    print(f'amount payable = {final_amount}')
    print()
    print('-------Thank you for shopping------')
    break