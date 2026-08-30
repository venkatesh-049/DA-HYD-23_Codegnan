#Inheritence
'''
OOP ---> class,object,methods (__init__())
Encapsulation ---> public,protected,private
inheritance--->it is one of key feature of oop where we inher the propertices (attribute/methods)
from one class to another class(base class (parent class)-->dervied class (child class))
whatsapp--->personal user,business user (catalog),community advar
Features ---> code reusability,avoiding code duplication,
code maintainabilty,polymorphism (method overriding(super()),method overloading,operator overloading,__add__,__str__)



Types : 
single Inheritance(Finger print)
---->one child class inheritance properties from one parent class
multiple Inheritance(mother,father-->child)
---->one child class inheritance properties from two parent class
multilevel Inheritance(grandparent -->parent-->child)
---->level by level
hierarchical inheritance --->multiple child class
---->inheritance properties from single parent
hybrid inheritance --->it can carry one or more type of inheritance
Syntax:

single inheritance:

class baseclass:
    statement(s):
    ........
class derivedclass(baseclass):
    ............
    ............



#whatsapp scenario --->personal user,Business user

class User:
    """single Inheritance usage"""
    def send_message(self):
        print('sending message')
    def voice_call(self):
        print('making voice calls')
    def video_call(self):
        print('making video_calls')
class BusinessUser(User):
    #pass
    def create_catalog(self):
        print("dispalying products catalog")
u1 = BusinessUser()
print(dir(u1))
u1.send_message()
u1.video_call()
u1.voice_call()
'''
#social media login --> user -->update_users
'''
class users:
    """ single inheritance usage"""
    company = "codegnan" #class attribute
    def__init__(self,fname,lname):
    self.fname = fname
    self.lname = lname
def full_name(self):
    return self.fname + self.lname
u1 = users("saketh","kallepu")
print(u1.full_name())
print(u1.company)
print(u1.full_name())
print(u1.update_name())
u2 = users("sai","tarigopula")
print(u1.company)
print(u1.full_name())
'''

#what if we have constructor in child class also...
#father --->kid(property)
'''
class father:
    """usage of constructor in single inheritance"""
    def _init_(self):
        self.property = 1000000
    def father_property(self):
        print(f'father property is {self.property}')
#class Kid(father):
 #   pass
class Kid(father):
    """now childclass will have constructor"""
    def _init_(self):
        self.cash = 200000
        #self.property = 2000000
    def Kid_property(self):
        print(f'kid property is {self.cash}')

obj = Kid()
obj.father_property()
obj.Kid_property()
'''
#in above case it is giving same value for father also as 2lakhs .when 
'''
class father:
    """usage of constructor in single inheritance"""
    def __init__(self):
        self.property = 1000000
    def father_property(self):
        print(f'father property is {self.property}')
class Kid(father):
 #   pass

    """now childclass will have constructor"""
    def __init__(self):
        super().__init__()#calling superclass constructor
        self.cash = 200000
        #self.property = 2000000
    def Kid_property(self):
        print(f'kid property is {self.cash}')

obj = Kid()
obj.father_property()
obj.Kid_property()
'''
#AUG-25== PART-2
#super().
'''
class father:
    """usage of constructor in single inheritance"""
    def __init__(self,property):
        self.property=property
        #self.property = 1000000
    def father_property(self):
        print(f'father property is {self.property}')
class Kid(father):
 #   pass

    """now childclass will have constructor"""
    def __init__(self,cash,property):
        
        self.cash = cash
        super().__init__(property)
        #self.property = 2000000
    def Kid_property(self):
        print(f'kid property is {self.cash}')
        print(f'total property is {self.cash + self.property}')

obj = Kid(250000,100000)
obj.Kid_property()
obj.father_property()
'''

#what if child having same method name is parent class
#--->>Method overriding.
#Finding area of square and rectangle:
'''
class rectangle:
   
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        print(f'Area of rectangle is {self.x * self.y}')
class square(rectangle):
    def __init__(self,x):
        self.x=x
    def area(self):
        print(f'Area of the square is {self.x * self.x}')
obj=square(4)
obj.area()
obj.raera() #raise attribute error
'''
#Calling super class with arguments
'''
class square:
    """method overriding usage"""
    def __init__(self,x):
        self.x=x
        #self.y=y
    def rarea(self):
        print(f'Area of square is {self.x * self.x}')
class rectangle(square):
    def __init__(self,x,y):
        #self.x=x
        self.y=y
        super().__init__(x)
    def sarea(self):
        #super().area() #calling supperclass method
        print(f'Area of the rectangle is {self.x * self.y}')
obj=rectangle(4,5)
obj.sarea()
obj.rarea()
'''
#Multiple Inheritence
'''
class parent1:
    ......
class parent2:
    ......
class child(parent1,parent2):
    .......
'''
'''
class user:
    def voice_call(self):
        print('making voice call')
class Notifications:
    def notification(self):
        print('sending notification')
class premiumuser(user,Notifications):
    def verification(self):
        print('Blue ticket verification done')
obj=premiumuser()
obj.verification()
obj.notification()
obj.voice_call()
'''
#multilevl Inheritence-->>level by level
'''
class Grandparent:
    .....
class parent(Grandparent):
    .....
class child(parent):
    ...
'''
class Grandparent:
    def video_call(self):
        print('video call going')
class parent(Grandparent):
    def catolog(self):
        print('catolog process')
class child(parent):
    def bluetick(self):
        print('verification done')
obj=child()
obj.video_call()
obj.catolog()
obj.bluetick()

