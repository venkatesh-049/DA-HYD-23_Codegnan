#write a program to find even,odd and -ve even, -ve odd along with zero is neither even or odd
#using if-elif-else
'''
num=int(input('enter the number'))
if num > 0 and num % 2 == 0:
    print('even number')
elif num < 0 and num % 2 == 0:
    print('-ve even number')
elif num > 0:
    print('odd number')
elif num < 0:
    print('-ve odd number')
else:
    print('Zero is neither even nor odd')
'''

#Season identifier
'''
Write a Python program using if-elif-else that takes a month number
(1–12) as input and prints the season it belongs to.


month = int(input('enter the number'))
if month < 1 or month > 12:
    print('Invalid month')
elif month==12 or month==1 or month==2:
    print('winter')
elif month==3 or month==4 or month==5:
    print('spring')
elif month==6 or month==7 or month==8:
    print('summer')
else:
    month==9 or month==10 or month==11
    print('autumn')

'''

#Grade checker using if-elif-else

marks=int(input('enter the marks'))
if marks >=90 and marks <=100:
    print('Grade A')
    print('Outstanding')
elif marks >=80 and marks <=89:
    print('Grade B')
    print('Excellent')
elif marks >=70 and marks <=79:
    print('Good')
elif marks >=60 and marks <=69:
    print('Fair,needs improvement')
elif marks >=50 and marks <=59:
    print('Poor, needs serious improvement')
elif marks < 50 and marks>=0:
    print('Failed, needs to reappear')
else:
    print('Invalid marks entered')
'''
#to find the longest sequence 
'''
'''
temps=[95,93,101,98,99,97,96,102,90]
long_seq=0
cur_seq=0
for temp in temps:
    if temp < 100:
        cur_seq = cur_seq + 1
        if cur_seq > long_seq:
            long_seq=cur_seq
    else:
        cur_seq = 0
print(long_seq)
'''      
    
    
