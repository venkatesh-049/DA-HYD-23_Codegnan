'''
Lists..
'''
'''
#List --->>>>Mutable,ordered,heterogenous
#index(),count(),copy(),sort(),reverse()

details = ['codegnan',4,5025,'hyderabad']
print(len(details))
print(details.index(4))
#details.extend([7,21,45,21])
print(details.index('codegnan'))
details.extend([7,21,45,21])
print(details)
print(details.index(21)) #it returns the first occurance
print(details.index(21,6))
#print(details.index('python')  #value error


print(details.count(21))
print(details.count('python')) #it returns the 0 as we dont have it
'''
'''
data=['codegnan','venky','python','java']
for name in data:
    print(data.index(name),':',name)

for name in range(len(data)):
    print(name,':',data[name])
'''
#copy()--->>>shallow copy of the given collection
'''
data=['codegnan','venky','python','java']
new=data.copy()
print(new)
print(type(new))
print(len(data))

new[2] = 'Agentic AI'
print(new)
print(data)

data.append('raj')
print(data)
print(new)
'''
#nested listed
'''
data=[1,4,5,[21,34,45],23]
print(data)
new=data.copy()
print(new)

new[3][2]='Agents' #whenever we make changes in nested list original will also be effected or changed
print(new)
print(data)

new[1] = 'python'
print(new)
print(data)
'''
'''
# strings are not allowing to sorting it's raise a error
marks=[14,24,-45,27,35]
print(marks)
#marks.sort()
#print(marks) # returns the ascending order
marks.sort(reverse=True)
print(marks)

#reverse() --->> return the reverse order
marks.reverse()
print(marks)
print(marks[::-1])
'''
'''
#type(),len(),max(),min(),print()
print(sorted('codegnan'))# retuns list in ascending order
print(sorted(['code','23',34,35])) #raise aerror
'''
#**********************TUPLE****************************
#Tuples -->> Tuples are indexed, ordered, Heterohenous,Immutable collection
#dimensions,coordinates,database records, we prefer () for tuple notat
'''
a=()
print(type(a))
print(len(a))

dimensions=1.5,2.5
print(dimensions)
print(type(dimensions))
print(len(dimensions))
'''
#operations -->> Indexing, slicing, striding,membership,merging,repitation
'''
course=('pfs','jfs',('da','ds'),'agenticai',[100,6,6])
print(course)
print(len(course))
print(course[-1][2])
print(course[-2][-2:])
#course[2]=23 #error becoz Tuples are immutable
course[-1].append('codegnan')#we can make any modifucation inside list not the tuple
print(course)
'''
#course=('pfs','jfs',('da','ds'),'agenticai',[100,6,6])
'''
print('pfs' in course)
d=course*2
print(d)
e= course + (2,3,4,5) # merging
print(e)
'''
#tuples Immutable  -->>> count(),index
'''
print(course.index('agenticai'))#returns the first occurence
#print(course.index('agent'))

#print(course.sort()) #attribute error
print(sorted(course[-1]))
#print (sorted (course)) #as we have mixed type

#typecasting
d=tuple(sorted((23,21,52,2)))
print(d)
'''
#Accept group of integers space seperated
'''
a,b=map(int,input('enter').split())
print(a,b)

a=tuple(map(int,input('enter').split()))
print(a)
'''
'''


print(eval('9+3'))

a= eval(input('enter the list'))
print(a)
print(type(a))
'''

#TASK :
#TAKE a user input as a string,
#do this in two ways.....
'''
1) give the count of each repeating character
TEST CASE1: programming

r is repeating 2 times
g -- 2 times
m--2 times

2)  r is repeating 2 times
index = [1,4]
 ---same as r to g
 index = [3,10]
 
'''
#TASK 1
'''
text=input('enter the character').split()
for char in text:
    if text.count(char) > 1:
        print(char,text.count(char))

        
    #text.count(char)
    #print(char)
    #count+=1
    #if count > 1:
       # print(char,'is repeating',count,'times')
'''
text = "programming"

for char in set(text):
    if text.count(char) > 1:
        indexes = []

        for i in range(len(text)):
            if text[i] == char:
                indexes.append(i)

        print(char, "=", text.count(char), "times", "indexes:", indexes)

























































