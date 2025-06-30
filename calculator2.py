print('=======calculator========')
def add(x,y):
    return add(x,y)
def subtract(x,y):
    return subtract(x,y)
def multiply(x,y):
    return multiply(x*y)
def divide(x,y):
    return divide(x/y)


print('''
      select operation 
      1.addition
      2.subtaction
      3.multiplication
      4.division ''')

print()
choice = input('Enter choice(1/2/3/4) :')
x = int(input('Enter first number :'))
y = int(input('Enter second number :'))

print()
if choice == 1:
    print(add(x,y))
elif choice == 2:
    print(subtract(x,y))
elif choice == 3:
    print(multiply(x,y))
elif choice == 4:
    print(divide(x,y))
else:
    print('invalid option')
