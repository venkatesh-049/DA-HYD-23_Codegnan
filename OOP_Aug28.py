
#Lets work on an example releated to Ecommerce
'''
class Ecommerce:
    company="Flipkart"
    delivery_charge=50
    @classmethod
    def update_delivery(cls):
        cls.delivery_charge=100
        print(f'new delivery charge {cls.delivery_charge}')

product=Ecommerce()
print(product.company)
print(product.delivery_charge)
print(Ecommerce.company)
print(Ecommerce.delivery_charge)

product.update_delivery()
print(product.update_delivery)
print(product.delivery_charge)
#mobile=Ecommerce()
#print(mobile.delivery_charge)
'''
#Applying Inheritence and usage of classmethod, class attributes
#Bamking scenario -->>RBI --->>SBI,HDFD....
'''
class RBI:
    available_cash=5000000
    @classmethod
    def rbi_cash(cls):
        print(f"available cash in RBI is {cls.available_cash}")

class SBI(RBI):
    pass
class HDFC(RBI):
    cash=3000000
    @classmethod
    def hdfc_cash(cls):
        print(f"available cash in HDFC {cls.cash}")
        #print(f"available total cash is {cls.available_cash +}")
        print(f'Total cash is {HDFC.cash + RBI.available_cash}')
a=SBI()
print(a.available_cash)
a.rbi_cash()
SBI.rbi_cash()
b=HDFC()
print(b.available_cash)
print(b.cash)
b.rbi_cash()
b.hdfc_cash()
'''
'''
class RBI:
    cash=5000000
    @classmethod
    def rbi_cash(cls):
        print(f"available cash in RBI is {cls.cash}")

class SBI(RBI):
    pass
class HDFC(RBI):
    cash=3000000
    @classmethod
    def hdfc_cash(cls):
        print(f"available cash in HDFC {cls.cash}")
        #print(f"available total cash is {cls.available_cash +}")
        print(f'Total cash is {cls.cash + RBI.cash}')

a=SBI()
print(a.cash)
#a.rbi_cash()
SBI.rbi_cash()

b=HDFC()
print(b.cash)
b.hdfc_cash()
b.rbi_cash() 
'''
#If incase as abive scenario we have same name for class attributes in both 
#parent and child classes, the best approach is to call
# the class attributes is using class names such as (RBI.cash)

#Static Method-->>It doesn't depend either on the object or to the class
#we can create it using @staticmethod decorator
#it is mainly used as utility or helper functions
'''
class Ecommerce:
    @staticmethod
    def free_delivery(price):
        return price >= 500
u1=Ecommerce()
print(u1.free_delivery(450))
'''

#Now lets releate both class method and staticmethod in a single use
'''
class Ecommerce:
    platform="Flipkart"
    @classmethod
    def show_platform(cls):
        print("welcome to the platform:")
        print(f'{cls.platform}')
    @staticmethod
    def free_delivery(price):
        #return price>500
        if price > 500:
            print("you are eligible for free delivery")
        else:
            print("you need to pay for delivery charges")
user=Ecommerce()
#print(user.platform)
user.show_platform()
user.free_delivery(6666)
'''
#Abstarction: It is also one of the key feature of OOP, where it shows the 
#Only relevent details to the user and hides the implementation 

#Instagram-->> uploading a photo,uploading video,or reel
#we have abc module to implement abstraction
import abc
from abc import ABC,abstractmethod
class Content(ABC):
    #@abstractmethod
    def upload(self):
        pass
class photo(Content):
    pass
    '''def upload(self):
        print('compressing the picture')
        print('edit the picture')
        print('photo uploaded sucessfully')
        ''' #as we made upload as abstract method mandatory it has be follows
class video(Content):
    def upload(self):
        print("Encoding the video")
        print("video editing is in progress")
        print("video uploaded sucessfully")
class reel(Content):
    def upload(self):
        print("Adding effects to the reel")
        print("reel is editing")
        print("reel is uploaded sucessfully")
'''
Contents=[photo(),video(),reel()]
for content in Contents:
    content.upload()
'''
a=video()
print(a.upload())