'''
Mapping-->>>Dictionary-->>collection of key-value pairs used to store
related data-->>JSON,APIs,database records

dict() -->> data = {}
Ductionary is Mutable,Indexed through Keys, Heterogenous,ordered
keys must be unique(int,strings,float values...)
'''
details={}
print(type(details))

details={'Id':'CGH4052',
         'Name':'Venky',
         'Batch':'DA23',
         'Age' : 23,
         'Place':'HYD'}

print(details)
print(len(details))

#Access the data from dictionary
#details[0] #keyError

print(details.keys()) #it returns keys from the dictionary
print(details['Id'],details['Name'])
#if key name is not matching / invalid
#print(details['marks']) #keyError as marks is not present
details['marks']=[]
print(details)

print(type(details['marks'])) #to store the marks in list

details['marks']=(20,30,40)
print(details)
'''
details['marks'].append(20)
print(details)

details['marks'].extend([21,22,23,24])
print(details)

#create a key-value pair of practice session
details['PS']=('Tuesday','Thursday','Saturday')
print(details.keys())

#Accessing 3rd day marks of students
print(details['marks'][2])
#Accessing 2nd day of practice session
print(details['PS'][1])

details['Mock']=('Monday','Wednesday','Friday')
print(details.keys())

#operations-->> mutable,indexing,through keys,membership

print('Wednesday' in details)
print('Mock' in details) # returns True as we have Mock as key


for i in details:
    
    print(i)          #it returns the keys
    print(details[i]) #it return the values
    #print(f'value={details[i]}')
    print(i,':',details[i]) # it returns the keys:values

for i in details.values(): # return values for the details
    print(i)

for i in details.items(): #return the key-value pairs
    print(i)

for key,value in details.items():
    print(key)
    print(value)


#update()-->>Updating the dictionary with key -values pairs
details.update({'marks':[],'PS':('Tuesday','Thursday','Saturday')})
print(details)
print(len(details))
#details['marks'].extend([99,98,97])
#print(details)

marks=list(map(int,input('eneter the marks').split()))
#print(marks)
details['marks'].extend(marks)
print(details)

print(details.keys())
print(details.get('Name'))
print(details.get('Brach')) #returns NONE as we dont have a Branch as key

details.setdefault('Branch','ECE')# if key is not present it inserts into a dict
print(details)

#details['Branch'] = 'ECE'
#print(details)

print(details.setdefault('Name'))
#print(details.keys())

details.pop('Branch')
print(details)
print(details.keys())

print(details.popitem()) # it removes the last key and value
print(details.keys())
print(details.popitem())
print(details.keys())
print(details.popitem())
print(details.keys())

del details['Id']
print(details.keys())

details.clear() #removes all elements from dict
print(details)

#fromkeys()-->> create a dictionary from iterable(list,tuples,sets,stringd)
data=['venky','sai','raj']
a=dict.fromkeys(data) #create a dict  but value set to None
print(a)
a['venky']=21
a['sai']=22
a['raj']=23
print(a)

#c=dict.fromkeys(['CGH123','CGH2345'],['code','gnan'])
#print(c)

#TASK:
#Create a dictionary with your personal details, similar to your
#codegnan profile

info={'Name':'venky','Id':123,'

'''









