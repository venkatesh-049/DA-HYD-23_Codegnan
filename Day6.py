'''
Control statements --->> controlof flow of execution of tyhe program
               ---->>>conditional statements ---->>> if, elif,  else...
               ----->>>Repetition statements(Loops) --->>>for, while(for with else),(while with else)
               ---->>> Jumping statements -->>> break,continue,pass
'''
#Loops --->>loops are useful for repitation(Automative task)
# for keyword will be helpful to iterarte over a sequence / range
#syntax for (for keyword):
'''
for <temp_var> in sequence / range:
    statement.....
    ....
'''
#range(range,stop,step)
#by default range pucks 0 as start value
#range stop -->>default 0 ends at stop -1
'''
for i in range(10):
    print(i)
'''
'''
for i in range(1,10):
    print(i)
'''
'''
for i in range(1,10):
    #if i>5:
        #print(i)
    # now i want only print even numbers
    if  i>5 and i%2==0:
        print(i)
'''
'''
for i in range(6,10,2):

    print(i)
'''
'''
for i in range(10,1,-2):

    print(i)

for i in range(-10,0,1):
    print(i)
'''
'''
names=['venky','raju','vamshi']
print(len(names)) #len(obj) --->>>return the number of items in a container
for i in names:
    if i == 'vamshi':
        print(f'student name is {i}')
'''

'''
n=int(input('eneter the number'))
result = 0
for i in range(n+1):
    result = result + i   #result += i we can write like this
    #print(result)
print(result)
'''
#add first 10 even numbers
'''
result = 0
for i in range(21):
    if i%2==0:
        result=result+i
print(result)
'''

#understand the usage with fitness streak example:
work_log = [0,1,1,1,0,1,0]
longest_streak = 0
current_streak = 0
for day in work_log:
    if day == 1:
        
        current_streak=current_streak+1
        
        if current_streak >longest_streak:
            longest_streak=current_streak
    else:
        current_streak = 0
            
print(longest_streak)        






























