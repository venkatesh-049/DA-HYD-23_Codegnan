#To calculate the performance of the player to calculate the total score and number of boundries and dots.
'''
score=list(map(int,input().split()))
boundries=0
dot=0
runs=0
for i in score:
    runs=runs+i
#print(runs)     # her it calculate the total score of the player\

    if i == 4 or i == 6:
        boundries=boundries+1  # number of boundries calculate
        #print(boundries)
    elif i == 0:
        dot=dot+1     #number of dot
    #print(dot) 
print('boundries',boundries)
print('dot',dot)
print('runs',runs)
'''
#To ulock the phone by using password with only 3 max attempts

pin='1255'
attempt = 3
count= 0
while count < attempt:
    entered_pin=input('enter the pin')
    if entered_pin == pin:
        print('unlock')
        break
    else:
        print('wrong pin')
        count=count+1
else:
    print('phone locked')


'''
#movies:
movies=input().split()
i=1
for movie in movies:
    print(i,movie)
    i=i+1
'''
#ATM PIN
'''
pin='1255'
attempt = 3
count= 0
while count < attempt:
    entered_pin=input('enter the ATM-pin')
    if entered_pin == pin:
        print('LOGIN SUCCESSFUL')
        break
    else:
        print('ENTERED PIN IS WRONG, TRY AGAIN')
        count=count+1
else:
    print('Account is locked, try aganin after 24 hrs')
'''





















