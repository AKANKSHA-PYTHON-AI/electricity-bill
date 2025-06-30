print('-----calculator------')
print()
print('Following are some operations that you can perform by this calculator====> ')
print()
options = '''
1.addition
2.subtraction
3.multiplication
4.division
5.modulus '''
print(options)
print()
print('Now enter the option number that you want to perform by this calculator===>')
choice = eval(input('Enter your option : '))
print()
a = eval(input('enter first number = '))
b = eval(input('enter second number = '))
print()

if choice > 0 and choice < 6:
    if choice == 1:
        c = a+b
        print(f'The addition of {a} and {b} is ',c)
    elif choice == 2:
        c = a-b
        print(f'The subtraction of {a} and {b} is ',c)
    elif choice == 3:
        c = a*b
        print(f'The multiplication of {a} and {b} is ',c)
    elif choice == 4:
        c = a/b
        print(f'The division of {a} and {b} is ',c)
    else:
        c = a%b
        print(f'The modulus of {a} and {b} is ',c)
else:
    print('option is invalid,please enter 1 or 2 or 3 or 4 or 5')