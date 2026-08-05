'''
Tokens--->>> keywords,identifiers,literals,operations,punctuators,variables
operations-->>>Numeric data (int,float,complex,),bool
control flows--->>>>if, elif, else, for ,while
sequences--->>>strings, lists, sets, tuple, dict(mapping)
'''

#strings -->> Group of character , we use single or double or triple quotes
# for representation of strings
# strings are immutable, ordered, indexed collection
# space is also a character
'''
name = 'codegnan'

print(name)
print(type(name))
print(len(name))
#Index[] --->> fetch the ebject (position) starts at 0 and ends at len(n-1)
#we use [] representation
print(name[0])
print(name[5])
#print(name[25]) # IndexError -->> as its out of range
# Negative Indexing --->>  -1 to len(obj)
print(name[-2]) # It return  the last character

#Slicing --->>> we can access group of character(object)
#we use [start:end] #start default --->> 0 , start is included, end is excluded
'''
'''
print(name[:]) # it returns the entire string
print(name[:4]) # starts at 0th index and ends with 4th index
print(name[1:5])
print(name[3:8])

print(name[5:15]) # it returns still end of the string
print(name[7:3]) # it returns an empty as string are immutable
# slicing is applicable from lower index to higher index not possible to reverse
'''
'''
name='python'
print(name[-5:-1])
# to get on
print(name[-2:])
print(name[4:])
print(name[4:6])


print(name[1:-2])
print(name[2:-6])
'''
#observe +ve,+ve,   -ve,-ve & +ve,-ve all possibilities
#striding--->>>>[start:end:step]
'''
course='DataAnalysis'

print(course[:4])
print(course[4:])
print(course[-3:])


print(course[::1]) #returns all values in this case
print(course[::2]) # step 2 is n-1
print(course[1:6:3])

#task: workout with all posibilities of slicing and striding on a example
'''


#name = 'codegnan'


#Operations on strings -->>> Indexing, concatenation,Repetition
#print(name*3)
#print('*'*23) #repetition

#Concatenation ---->>>> combining strings
'''
data = 'venkatesh' + 'warlu' + '  '+ 'meenugu'
print(data)
print('123' * 3 ) #Numeric string
'''
'''
for i in range 'codegnan':
    print(i,':')
# in baove case we get every character line by line

for i in range 'codegnan':
    print(i,end=' ')

'''
'''
name='dataCodegnan'
#built-in functions --->>> len(),min(),max(), sorted()
print(len(name))
print(min(name)) #alphabetical order ASCII ordering
print(max(name))
print(len(name))
print(ord('A'))
print(ord('a'))
print(chr(97))
print(sorted(name))

'''
#methods on strings--->>> case-conversions,finding/searching...
name='codegnan data'
#case conversions --->>> upper(),lower(),capitalize()
'''
a=name.upper()
print(a)
b=name.lower()
print(b)
'''
#capitalize()--->>>converts first letter to uppercase
c=name.capitalize()
print(c)
d=name.title() # cconverts every word first letter to uppercase
print(d)

#Task: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# use loops and strings to return A to Z
# Hint: ASCII 65 - 90





































































