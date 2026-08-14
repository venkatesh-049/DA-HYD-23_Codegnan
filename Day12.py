'''
sequences-->> strings, Lists, Tuples, Set, Frozenset
Mapping-->>Dictionary
'''
#Sets-->> A set is a unique collection of items or objects,unordered, mutable
#Hashing,Unique,Heterogenous
#set(),{}
#a={} its a empty dictionary
#sets()-->>no index,no sliding
'''
a=set()
print(type(a))
st_id={123,435,322,123,567,864}
print(st_id)
print(type(st_id))
print(len(st_id))
print(st_id[2]) #TypeError
print(435 in st_id)
print(st_id*2)  # raise a error
print(st_id + st_id ) #TypeError #2 sets can't merged



#data={12,3,4,5,[12,3,4],'saketh'} error inside no lists
#print(data)

data= {12,3,4,5,(12,3,4),'saketh'}
print(data)
print(len(data))
for i in data:
    print(i)
'''


#methods on sets-->> add(), update(),remove(),discard(),pop()

names={'sai','raj','venky','codegnan'}
print(len(names))
'''
#add() will insert an element into the set
names.add('python')
print(names)
#names.add('mahi','poll')
#print(names)
names.add(('poll','police'))
print(names)
'''
da_names={'mani','akash','sana','chitti'}
#update() we can update multiple elements

'''
names.update(da_names)
print(names)
print(len(names))
print(da_names)
print(len(da_names))
da_names.update(names)
print(len(names))
print(len(da_names))
'''
#remove(),discard(), pop(), clear()
'''
da_names.remove('mani')
print(da_names)

#da_names.remove('sai') #it raise a keyerror becoz in that set there is no name of sai
#print(da_names)

da_names.discard('mani') #discard will never raise an error
print(da_names)
#discard() will remove an element if it is in the present else its ignores
'''
'''

#pop()
da_names.pop()
print(da_names)
print(da_names.pop()) #removes and returns the an arbritrary element
print(da_names)
#da_names.clear()
#print(da_names)
da_names.add('sairam')
print(da_names)
da_names.update(['sonu','chitti'])
print(da_names)
'''
#copy()
#creates a shallow copy of set (independent of each other)
'''
d=da_names.copy()
print(d)
d.update({'python','codegnan'})
print(d)
print(da_names)
'''


#mathematical operations --->>> union,intersection,dofference, symmetric_id
#issubset,issuperset,isdisjoint()

da_23={12,34,45,67,36}
da_24={34,36,12,35}
#da_25={11,15} #we can use | bar symbol
#event=da_23.union(da_24).union(da_25)
#union() or | . returns the all elements in both sets and remove the common elements
#print(event)
#print(len(event))
'''
common=da_23.intersection(da_24)  # & intersection
#intersection returns the common elements in both sets
print(common)
print(len(common))
'''
'''
common=da_23.intersection_update(da_24)  
print(common) #it returns none
print(da_23) #common elements are finally stored
'''
#difference -->> it returns the difference values in 1 set which we call
#a=da_23.difference(da_24)

#print(a)

#symmetric_difference or we can use ^
# it returns the all differnce values in both sets
'''
sym=da_23.symmetric_difference(da_24)
print(sym)

sym=da_23 ^(da_24)
print(sym)

#issubset-->> checks for all elements to be present in other set
da_24.remove(12)
da_24.remove(35)

print(da_24.issubset(da_23))
print(da_23.issubset(da_24))


#isdisjoint() returns false for sets having  common elements

print(da_24.isdisjoint(da_23))

'''


n=int(input())
st_id=set(map(int,input().split()))
print(len(st_id))






























