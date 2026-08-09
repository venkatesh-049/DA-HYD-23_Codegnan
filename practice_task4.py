#guess the correct code based on the input hint
'''
code=1255
i=0
while i<code:
    entered_code=int(input('enter the code:'))
    if entered_code == code:
        print('correct one')
        break
    elif entered_code >= 1000 and entered_code <= code:
        print('You are little less your code,keep moving forward')
    elif entered_code > code:
        print('you are maximized your code, come backward')
    elif entered_code < 1000:
        print('you are too long to move forward to find your code')
        i=i+1
'''
#OTP verification using certain number of attempts
'''
OTP='1255'
attempt = 7
count= 0
while count < attempt:
    entered_pin=input('enter the OTP')
    if entered_pin == OTP:
        print('unlock')
        break
    else:
        print('wrong OTP')
        count=count+1
else:
    print('TRY AFTER SOME TIME')
'''

# Food Ordering and use "exit" for exit then only count the number of items they are ordered
'''
items = input("Enter food item: ")

i = 0

while items != "exit":
    
    items = input("Enter food item: ")
    i = i + 1
print("Total no. of items:", i)
'''
#Gaming to find the code and based on the number of attemps after loose the game
'''
code = "python"
total_attempts = 3
current_attempt = 0

while current_attempt < total_attempts:
    entered_code = input("Enter the code: ")

    current_attempt = current_attempt + 1
    remaining = total_attempts - current_attempt

    if entered_code == code:
        print("Code success")
        print("You have", remaining, "more chances")
        break
    else:
        print("Incorrect code")
        print("You have", remaining, "more chances")

if current_attempt == total_attempts and entered_code != code:
    print("You lost the game")
'''


#STAR printing methods
'''
for i in range(3):
    for j in range(2):
        print("*",end=" ")
    print()
'''
'''
for i in range(3):
    for j in range(3):
        if i==0 or j==0  or i==2 or j==2:
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print()
'''
'''
for i in range(3):
    for j in range(3):
        if i==2 or j==0 and j==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print()
'''
'''
for i in range(3):
    for j in range(3):
        if j==0 or i==2 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
'''
for i in range(3):
    for j in range(3):
        if j==0 or i==2 or i==1 and j==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
for i in range(3):
    for j in range(3):
        if j==0 or i==0 or i==1 and j==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()



