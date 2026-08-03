'''
Identity Operators --> checks the identity of an object --> id()

a=5
b=a
print(id(a))
print(id(b))
c=5
print(id(c))
print(a is c)
print (5==5)
'''
'''
a = [1,3,5,6]
b = a
print(id(a))
print(id(b))
c = [1,3,5,6]
print(id(c))
#as we have lists (mutable collection)
print(c is a) #output False
print(c == a) #output True
print(a is not c)
'''

'''
#Bitwise Operations --> we perform bitwise operations over operands
# & (and), | (or), ^ (xor), shifting operators(<<,>>)

print(5&3) #both 5 and 3 to be converted binary to bitwise and is performed

print(5|3) #bitwise or

print(5^3) #bitwise xor

print(5 and 3) #here and is logical operator checks for both existances
# returns 5 above case
print(5 or 3)# here returns 3 in this case

# Leftshit operator <<, Right shift operator >>
#print(5<1) #false comparision
'''
'''
print(5>>1) # left shift operation by 1 position

print(15>>2)
print(15<<2)
'''
#Input formating -->> input(), int(input()), float(input())
#you know --> single input
#2 or 3 inputs --> map()
#group of integers --> list(map(int,input()).split(',')
'''
names = input('enter the names:').split(',')
print (names)
'''
'''
name1,name2 = map(str,input('enter the frds name:').split(','))
print(name1,name2)
'''

#tokens --> numeric datatypes --> operations --> flow of the program

#conditional statements -----> if, if else, elif, else


'''
syntax :
if <condition>:
   statement(s)....
   .....
'''
'''
#age = 14
age=int(input('eneter the age'))
if age>18:
        print('your age is:',age)

'''
'''
age = int(input('eneter the age'))
if age>=18 and age in [19,20,21]:
    print('your age is:',age)
print(age)
'''
'''
# if-else:
if <condition>:
   statement(s)....
else:
    statement(s)...
'''
#Vote eligibility
'''
age=int(input('eneter the age'))
if age >= 18:
    print('elgible for vote',age) 
    print('Access granted')
else:
    age = 18-age
    print('you dont have eligibility as your age is:',age,'years')

'''
'''
task:student mark and grade analayzer(if-else)
90--100
89--90
79--80
69--70

marks should not be > 100 and < 0
'''
# THIS IS THE TASK FOR TODAY CLASS USING IF AND ELSE STATEMENT:

marks = int(input('Enter the marks'))
if marks >0 and marks <= 100:
            if marks > 90:
                print('A')
            else:
                if marks > 80:
                    print('B')
                else:
                    if marks > 70:
                        print('C')
                    else:
                        if marks > 60:
                            print('D')
                        else:
                            if marks < 60:
                                print('Fail')
else:
    print('invalid number')




















