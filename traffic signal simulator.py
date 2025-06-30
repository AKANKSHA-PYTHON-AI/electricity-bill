import time
while True:
    print('1.manual mode')
    print('2.auto mode')
    print('3.exit mode')
    print()

    choice = eval(input('Enter your choice : '))
    if choice == 1:
        signal = input('Enter the signal(red/yellow/green) or back : ')
        if signal == 'red':
            print('red-signal --> stop')
        elif signal == 'yellow':
            print('yellow-signal --> be ready')
        elif signal == 'green':
            print('green-signal --> move')
        elif signal == 'back':
            break
        else:
            print('invalid signal,please enter red/yellow/green or back')
    elif choice ==2:
        print('red-signal --> stop')
        for i in range(0,10):
            print(i)
            time.sleep(i)
        print('yellow-signal --> be ready')
        for i in range(0,10):
            print(i)
            time.sleep(i)
        print('green-signal --> move')
        for i in range(0,10):
            print(i)
            time.sleep(i)
        print('cycle completed')
        again = input('do you want to simulate again (yes/no): ')
        if again != 'yes':
            print('exiting the simulator,thank you')
            break
        elif choice == 3:
            print('thank you for using simulator!!!')
            break
        else:
            print('invalid choice!please choose either 1 or 2 or 3')
