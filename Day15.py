




'''
def sample(*args):
    print(args)
    #print(type(args))
sample() #no arguments
sample(1,3,5,6) #any number
sample('codegnan','venky',23)
details=[24,45,35,65]
sample(details) #passing a collection
sample(*details) #unpacking values from collection
'''
'''
a,b,c=13,4,'da'
print(a,b,c)
# * is used for unpacking the values from acollecton
a,*b,c='python','codegnan',23,45,'data'
print(a)
print(b)
print(c)
'''
'''
a,b,*c='codegnan','python'
print(a)
print(b)
print(c) #it returns the empty list because we are use * 
c.extend([2,4,6,8])
print(c)
'''
'''
#Task-->> we wanted to calculate the sum of given objects using function
def add(*a):
    print(a)
    #take output varaiable as result
    result=0
    for i in a:
        #if type(i)==int or type(i)==float:
        if type(i) in (int,float,complex):
            result =result + i
    return result
#print(add())
#print(add(11,22,33))
#print(add(1.1,2.2,'fjjbas',3.3))
#print(add(2,3,
b=list(map(int,input('enter').split())) 
print([add(*b)]) # * is used to unpack the value from collection
#print([x])
print(*b) # it returns each value side by side
for i in b:
    print(i,end=' ') # as same as here
'''
#keyword variable length arguments --->> we can pass any number of keywords
#arguments we use ** represenatation
 ## and data is stored in dictionary
'''
def details(**kwargs):
    print(kwargs)
details()
details(name='venky',place='hyd',batch='da23')
batch={'number':33,'state':'tg'}
details(**batch)
'''

#Now  let us include both of them into a function
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
    












    



