'''
Tokens --> variables, Punctuators

variables --> Named memeory location, its a placeholder for data
# rules are to be followed
'''

#multiAssignment of variables
'''
name,age,place = 'venky',23,'Hyderabad'
print(name,age,place)
print(name,age,place,sep=',')
print(name,age,place,sep='---->')'''

#a,b = 2,4,5 #valuError as too many values to unpack

#Reassigning variables
'''
name = 'codegnan'
a,b = 45,1.5
print(a,b)
a,b = b,a
print(a,b,sep=',')'''

# a,b = b,c ---- # NamError as c is not found
#Deleting the variables ---->ArithmeticError --->del
'''del a,b
print(a,b)'''

#Punctuators ---> [List], (tuples), {dict,sets}
'''
name = 'Codegnan';age = 7;course = 'Data_Analysis'
print(name,age,course)
'''
#Datatypes --> Numeric (int,float,complex),boolen ,None,
#-->sequences List, Tuple, sets, stirngs,
# frozensets, mapping(dict)

#Numeric type --> int, float, complex          
#int datatypes --> quantity, age
'''
age = 7
print(age)
print(type(age)) #type--> returns the datatype of object
print(type(123))
'''

#float datatype --> temp,salary,price
'''
price = 450.45;discount = 2.5
print(price, discount,sep=',')
print(type(price))
'''

#complex -->combination of real and imag
'''
i4 = 4
data = 5 + i4
print(data)

data = 5+2j #j is imag represenatrion
print(data)
print(type(data))
'''

#Boolen --> True, False
'''
valid = True
print(type(valid))

error = False
print(type(error))
'''

#TypeCasting --> converting one type to another type
#python by default folloes implicte type (we need to mention the datatype)
#we will go fofr Explicit conversion
#Every built-in datatypes is built function
#int, float, complex, boolen

# Typecastin --> int--> float,complex,bool
'''
age=23
b=float(age)
print(b)
c=complex(age)
print(c)
d=bool(age)
print(d)

'''
'''
age=23.8
b=int(age)
print(b)
c=complex(age)
print(c)
d=bool(age)
print(d)
'''
'''
#complex --> Typecasting
angle=2+3j
c=float(angle)
#complex is not typecasting except boolen
#exmaple
a=bool(angle)
'''
'''
e=int(float(bool(45)))  #bool(45)=True, float(True)-->True=1, so float of true is 1.0
print(e)                # then int=1
'''
a=45 + 2.5 + 2 + 3j + False
print(a)









