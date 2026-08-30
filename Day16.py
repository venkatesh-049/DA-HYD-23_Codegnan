'''
functions --> arugemnts usage (variable length arguments)
          -->keyword variable length arguments (**kwargs)

exception handling /scope of variabls /built- in funvtions

exception handling -->it is a mechanism thst helps to respond or make the
flow of execution in normal way,without this error will ocuurs and disrup the
flow of program

common  exception --> value error,typeerroe,indexerror,attributerror,
zerodivisionerror...
'''
#basic Exception handling
'''
try:
    a=10
    a=int(input('Enter the value:'))
    result = 20/a
    print(result)
#except Exception as e:
    #print(e) #it returns the msg of the error
except ValueError:
    print('Invalid entry enter only integer values')
except ZeroDivisionError:
    print('Division by zero is not possible')
except NameError:
    print('check the name of the variable properly')
'''
'''
try:
    a=[10,20,30]
    print(a[3])
   
    #print(result)
except Exception as e:
    print(e) #it returns the msg of the error
#except ValueError:
'''
#Similarly if we want to check other Errors-->> IndexError,AttributeError
'''
try:
    a=[10,20,30]
    print(a[2])
#except Exception as e:
   # print(e)
except IndexError:
    print('check the length of the list')
except AttributeError:
    print('Dont rush write the name properly')
def sample(*a,**b):
    result=0
    for i in a:
        if type(i) in (int,float,complex):
            result=result+i
    for key,value in b.items():
        print(f'key is {key} and value is {value}')
    return result
print(sample(2,3,4,'raj','sai',1,
       name='venky',
       age=99,
       place='hyd'))

#Handling exceptions at a time:

try:
    a=[10,20,30]
    a.apped(34)
    print(a[3])
#except Exception as e:
   # print(e)
except (IndexError,AttributeError) as e:
    print(e)
#we can take a input in the except function
'''
#BMI-->>
'''
while True:
    try:
        weight=int(input('enetr the weight in kgs:'))
        height=float(input('eneter the height:'))
        #write logical condition
        if weight > 0 and height > 0:
            break # it stop the flow of the execution of priogram
            #continue # skips the current iteration and proceed for rmng items
            #pass
        else:
            print('make sure the enter values are only +ve values')
    except ValueError:
        print('Make sure to enter the weight as integer only,height also a number')
bmi=weight/(height*height)
print(bmi)
'''
#Use Exception Handling along with Jumping statements in
#Functions BMI task


#Scope of varaible -->> scope is basically the region/area where it is
#accessiable
#Local scope, Global scope
#Global keyword, Enclosing scope(Nested Functions non-local keyword)
'''

#local scope-->> variable inside the function accessiable inside
'''
'''
def display():
    name='venkat' #local variable
    print(name)
display()
print(name) # it raises NameError
'''
#Gloabal scope(varaiable)-->Defined outside and can be accessible anywhere
# in the script
'''
place='Hyderbad' #Global Variable
def display():
    name='venkat' #local variable
    print(name)
    print(name,'is in',place)
display()
print(place)
'''
#modify the gloabal varaiable inside the function and accessiable outside the function
'''
count=20
def data():
    global count
    count=count+5
    print('value inside function is:',count)
data()
print('value outside function is:',count)
'''
#Local varaiable has high priority over global variable
'''
count=20
def data():
    count=5
    count=count+5
    print('value inside function is:',count)
data()
print('value outside function is:',count)
'''
#Enclosing scope(nonlocal keyword)
def outer():
    count=5
    def inner():
        nonlocal count
        count=count+10
        print('value inside is:', count)
    inner()
    print('value is outside:',count)
outer()






































