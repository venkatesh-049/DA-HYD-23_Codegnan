'''
Usage of else with for  --->>>> the else keyword will only be executed when


'''
'''
work_log = [0,1,1,1,0,1,0]
longest_streak = 0
current_streak = 0
for day in work_log:
    if day == 1:
        
        current_streak=current_streak+1
        
        if current_streak >longest_streak:
            longest_streak=current_streak
            print(longest_streak)
        break
    else:
        current_streak = 0  #streak break
else:
    print(f'longest streak is {longest_streak}')
             
'''
# in this case when the entire loop execution is done we get result of else block


# same program with break usage:
'''
work_log = [0,1,1,1,0,1,0]
longest_streak = 0
current_streak = 0
for day in work_log:
    if day == 1:
        
        current_streak=current_streak+1
        
        if current_streak >longest_streak:
            longest_streak=current_streak
            print(longest_streak)
            break
    else:
        current_streak = 0

else:
    print(f'longest streak is {longest_streak}')
            
print('execution done!')
'''

# for -else with notification scenario:
#try to take notificatiins from user ---->>>> list of integers
#notifications=[0,0,0,0,0]
'''
notifications=list(map(int,input('enter the values -->> 0 or 1:').split(',')))
for notification in notifications:
    if notification == 1:
        print('unread notification')
        break
else:
    print('All caught up!')
'''
#try to take notifications from user --->> list of integers


#WHILE Keyword ----->>>>>it relies on the condition, it will be completely executed until the
# condition is satisified
'''
syntax while:

while <condition>:
    statement(s)...
    .....
    ....1354
'''
'''
while True:
    print('yes')
#it runs ann infinite loop, we need to press ctrl c+v to stop
    break
'''
# to get 1 to 10
'''
i=0  # initialised statement
while i<=10: 
    print(i)
    i=i+1 #counter
'''
# it decrement to the 10 to 1
'''
i=10 # initialised statement
while i>=1: 
    print(i)
    i=i - 1 #counter
'''
#banking scenario --->>> PIN authentication if more than 3 attempts
# Account locked...

pin='1255'
max_attempts = 3
cur_attempt = 0
while cur_attempt < max_attempts:
    entered_pin = input('enter the pin:')
    if entered_pin == pin:
        print('login sucess')
        break
        #Continue  # it holds for this condition and skips to the next part of the loop
    else:
        print('entered pin wrong....try again')
        cur_attempt +=1
else:
    print('Account Locked, Try after 24 hrs')



















