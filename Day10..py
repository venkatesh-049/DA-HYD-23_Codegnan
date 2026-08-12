'''
sequences--->> strings,Lists,Tuples,sets
Mapping-->>>>Dictionary
'''
#Lists-->>collection of heterogenous elements(items)
#list-->>indexed,ordered,mutable,heterogenous,we use [] to store the data
'''
marks=[52,54,52,45]
print(marks)
print(len(marks))
print(type(marks))
print(55 in marks)
'''
#operationsw : Indexing, slicing, striding, membership, merging, repetition


#Nested List -->> A List inside another list
#names=['codegnan',25,2.5,[35,45,56,75],'DA23',34]
'''
print(len(names))
print(names[0])
print(names[3])
print(names[-3])

print(type(names[0]))
print(names[0][:4]) #it returns code
print(names[0][4:]) #it returns gnan

print(names[0][1::2])
print(names[0][::2])

print(names[3])
print(len(names[3]))
print(names[3][2]) # 56
'''
###indexing,Slicing--->>Mutable
'''
names[2]='python'
print(names)
'''
#by indexing if we change the elements, lengths of collection will remain same
'''
names[4]=['codegnan','raj','sai']
print(names)
'''
####################################################################
'''
#updated names=['codegnan', 25, 'python', [35, 45, 56, 75], ['codegnan', 'raj', 'sai'], 34]
#print(names[4][0][4:]) #it returns the 4th item, oth item, starts from 4th index
names[2:4]='venky','raj','sai','manoj'
#print(names)
#print(len(names))
#In slicing whatever elements u pass as per the logic lengths keeps on increase
print(names[3:6:2])
print(names[3:6])
names[3:6:2]=['python','java']
print(names)
'''

#####################################################################

#created a nested list with strings, lists and work on indexing,slicing,striding
# add advantages if you could add string functions also to it
#lists functions -->> append(),insert(), extend(),pop(), rempove(),clear()
#index(),count(),copy(),sort(),reverse()
#append()
'''
names=['codegnan','venky']
names.append('hyd')
#append()-->> insert a single element to the end of the list
names.append(['data','analysis'])
#append will always increment the length of of the list
names[3].append('chatgpt')
print(names)
'''
#extend()--->>>> inserts multiple elements to the end of the list
'''
names=['codegnan', 'venky', 'hyd', ['data', 'analysis', 'chatgpt']]
names.extend('analysis')
#print(names)
names.extend(['analysis'])
names.extend([54,25,55])
print(names)
#names.extend(25,55) type error
'''
#insert(index,object)--->>>> inserts given object before index
names=['codegnan', 'venky', 'hyd', ['data', 'analysis', 'chatgpt']]
'''
names.insert(1,'python')
#print(names)
names.insert(0,'java')
#print(names)
#names.insert([1:4],['a','b'])  #syntax error
names.insert(-1,'aaa')
print(names)

'''
#pop(),remove(),clear()
#pop() by default last
# pop() is remove by default last element when we are not insert any argument
'''
names.pop(2)
print(names)
'''

#remove() we can replace a specific value
'''
names.extend([23,24,21])
print(names)
#names.remove('venky')
#print(names)
#del---->>> is delete the perminent 
del names[2:4] #del keyword 
print(names)
'''
#########----TASK----#######
'''
data = ['codegnan','saketh','python','java'] # input
output as 
0:codegnan
1:saketh
2:python
3:java
'''
data=['codegnan','venky','python','java']
#data=input().split()
i=1
for name in data:
    
    print(i,':',name)
    i=i+1
















