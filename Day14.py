'''
Tokens, Datatypes -->>>Control flow statements --->>>if,else,for ,while,break,
continue..

procedure Oriented Programmig


FUNCTIONS-->> A function is a block of code which perform a specific task.
Its a reusable group of statements where we define using
def keyword

Advantages-->>code reusability,code maintainability,ease of debuging,
avoid code duplication,modularity
'''
#To perform sum of given onjects
'''
def add(a,b):
    Sum of object
    c=a+b
    return c
print(add(4,5)) #Addition
print(add('code','gnan')) #concatentation
print(add([1,2],[3,4])) #Merging
e,f=map(int,input('enter the values:').split(','))
print(e,f)
print(add(e,f))
'''
'''
def add(a,b):
    print(a+b)
add('code','gnan') # when we are use the print into the body then no need to add print at end
'''
'''
name,age,salary='venky',21,35000
#usage of return

def details():
    #return name,age,salary
    #return 0
    #return # it return none
print(details())
'''

###There are 5 types of arguments:
'''
--->> Positional Arguments
--->> Default Arguments
--->> Keyword Arguments
--->> variable length Arguments (*args)
--->> Keyword variable length Arguments (**kwargs)
'''

#positional Arguments -->> Number of arguments in function defn should
#match with function call (order has to be maintained)
'''
def details(name,place):
    #name='vemky'
    #place='gajra'
    return name,place
print(details('venky','hyd'))
print(details('venky','hyd',53)) # it raises TypeError a error beecoz the as only 2 arguments
'''
'''
def details(name,place):
    #name='vemky'
    #place='gajra'
    #return name,place
    print(f'name is {name}')
    print(f'place is {place}')
name,place=map(str,input('eneter').split())
details(name,place)
'''

#default arguments -->> we can make arguments as default but not first arguments
#as default
'''
def grocery(item,price):
    print(f'Item  is {item} and price is {price}')
    return item,price
grocery('milk',34)
grocery('bread',77)

'''
'''
def grocery(item='drink',price=100):#we can also make all arg as default
    print(f'Item  is {item} and price is {price}')
    return item,price
#grocery('milk',34)
#grocery('bread',77)
grocery()
'''
'''
def grocery(item='drink',price):#no dedault always follows default
    print(f'Item  is {item} and price is {price}')
    return item,price
#grocery('milk',34)
#grocery('bread',77)
grocery(99)
'''
#keywords arguments-->>whenever we wanted to specify the name of the argument
def employee(name,salary,role,place='hyd'):
    print(f'name {name} salary is {salary} and role is {role} and place is {place}')
employee('vamsi',20000,'da')
employee(salary=3000,role='Data Engineer',name='venky')

























