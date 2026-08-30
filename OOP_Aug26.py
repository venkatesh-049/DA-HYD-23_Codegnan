#Polymorphism
'''
Polymorphism-->>It is also one key feature od oop
poly-->many
morph-->>>forms
Methods with same name can take different parameters(arguments,methods)
-->>methods overloading (compile polymorphism)
-->>method overriding(run-time)
--->>>operator overloading(+,*)(__add__,__str__)
'''
#Hotstar
# -->>Free User ---->>can watch the movie with advertisements
#--->>premium user --->>can watch premium content without advertisements
#--->>VIP user---->>>live content,streaming qulaity,premium content

#Method Overloading : 
'''
class Hotstar:
    def watch():
        print(f'user logged into Hotstar....opening hotstar')
    def watch(self,movie):
        self.movie=movie
        print(f'user watching {self.movie}')
app=Hotstar()
app.watch('LEO')
#app.watch() -->> it raises a error as watch() is overloading.
'''
#1)method usage with default arguments
#2)method usage with variable length arguments(*args)
#3)method usage with type of arguments
'''
class Hotstar:
    def watch(self,movie=None):
        if movie is None:
            print(f'user logged into hotstar...checking..')
        else:
            self.movie=movie
            print(f'user satrted watching {self.movie}')
app = Hotstar()
app.watch()
app.watch('hello')
'''
#method overloading length of arguments
'''
class Hotstar:
    def watch(self,*movies):
        #print(movies)
        for movie in movies :
            self.movie=movie
            print(f'user watching {self.movie}')
app = Hotstar()
app.watch()
app.watch('hello','raj')
'''
#method overloading with type of arguments usage
#Hotstar -->>one movie at a time
#        --->>multiple movies at a time
'''
class Hotstar:
    def watch(self,content):
        #self.content=content
        if isinstance(content,str):
            
            print(f'user watching {content}')
        elif isinstance(content,list):
            print('playing playlist')
            for movie in content:
                print(movie)
app=Hotstar()
app.watch('sairam')
#app.watch([1,2,3])
'''
#Method Overiding-->>
#it happens in the scenario of Inheritence, WHere if child class name 
# is having method name same as parent class thats where overriding
#we can use super() or if we create different objects
'''
class Freeuser:
    def watch(self):
        print('user logged into homepage....')
class premiumuser(Freeuser):
    def watch(self,movie):
        self.movie=movie
        print(f'user watching {self.movie}')
obj=premiumuser()
obj.watch('vikram')
obj2=Freeuser()
obj2.watch()
'''
'''
class Freeuser:
    def watch(self):
        print('user logged into homepage....')
class premiumuser(Freeuser):
    def watch(self,movie):
       
        self.movie=movie
        super().watch()
        print(f'user watching {self.movie}')
obj=premiumuser()
obj.watch('vikram')
'''
#Operator Overloadding--->> Operators(+,-,*,/)-->>operators will behave
#in a different way as per user defined objects

'+'# (addition,concatenation,merging)
'''
print(3+5)
print('sai'+'ram')
print([1,2,3]+[4,5,6])

#print(3.__add__(4)) #__add__(self,other)
a=11;b=22
print(a.__add__(b))
a=[1,2,3];b=[4,5,6]
print(a.__add__(b))#merging
print(a.__len__()) #len (a)
print(a.__mul__(2))
'''
#let's apply the above scenario hotstar watchhistory
'''
class WatchHistory:
    def __init__(self,hours):
        self.hours=hours
venky=WatchHistory(100)
print(venky.hours)
vamshi=WatchHistory(50)
print(vamshi.hours)
#print(venky+vamshi) #TypeError unsupported operation
print(venky.hours + vamshi.hours)
'''
class WatchHistory:
    def __init__(self,hours):
        self.hours=hours
    def __add__(self,other):
        return self.hours + other.hours
    def __str__(self):
        return f'WatchHistory is {self.hours}'
    
venky=WatchHistory(100)
print(venky)
vamshi=WatchHistory(59)
print(vamshi)
print(venky+vamshi)


