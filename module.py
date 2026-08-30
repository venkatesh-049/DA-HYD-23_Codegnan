import OOP_Aug29
'''
print(dir(OOP_Aug29))
print(type(OOP_Aug29.details))
print(type(OOP_Aug29.greetings))

print(OOP_Aug29.greetings())
print(OOP_Aug29.details)

#we can access functions/datatypes using . operator

OOP_Aug29.details['subject']=['python','sql','Power-BI']
print(OOP_Aug29.details.keys())
print(OOP_Aug29.details.values())
'''
'''
from OOP_Aug29 import details
print(details)
#print(greetings())# as we did not import it raises NameError
details['subjects']=['python','sql','Power-BI']
print(details)
'''
#we want to access group of methods/datatypes we can use commas
'''
from OOP_Aug29 import details,greetings
print(greetings())
print(details)
'''
'''
#you want to access all functions from at a time
# * is recommended only for user defined modules
from OOP_Aug29 import *
print(greetings())
print(details)
'''

#Aliasing 
'''
import OOP_Aug29 as mod
print(mod.details)
'''
#we will work on some built-in-modules --->>random, math
import random,time
#import time
#random module -->> get random number generation, random text
print(dir(random))

#OTP generation --
#print(random.randint(1,10))
'''for i in range(5):
    print(random.randint(1000,9999)) #start limit and end limiy
    time.sleep(2) #it delays the execution of time

print(random.random()) # returns a float value of random'''
'''
details=['A long back','once upon a time','Ten years ago']
print(random.choice(details))
'''

#you can try for story generation using choice -->> try in practice

#math module -->> mathematical constants, log, expo, trignometric....

import math
#print(dir(math))
print(math.ceil(4.5))
print(math.floor(4.76))
print(math.factorial(5))
print(math.pi)
print(math.gcd(2,4))
print(math.trunc(4.09))