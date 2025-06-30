''' statements
units consumed:                  rate per unit:
---------------                  --------------
if the units are (0-100)          10
                 (101-200)         20
                 (201-300)          30
                 above 300          40
now ask user to enter no.of units consumed then the electricity bill be given'''


print('=========Electricity Bill=========')
Units=eval(input('Enter no.of units consumed: '))
if Units >0 and Units <=100:
    Bill = (Units*10)
elif Units >= 101 and Units <= 200:
    Bill = (100*10) + ((Units-100)*20)
elif Units >= 201 and Units <= 300:
    Bill = (100*10) + (100*20) + ((Units-200)*30)
else:
    Bill = (100*10) + (100*20) + (100*30) + ((Units-300)*40)



print('Your electricity bill is ',Bill)