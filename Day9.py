'''
strings--->> caseconversions, searchind &finding ,string testing methods,
Replace,space removal
'''
#case conversion
#serching,finding,replacing,joining...
a='Codegnan'
'''
print(len(a))
print(min(a))
print(max(a))

b=a.index('g')
print(b)

c=a.index('n')
print(c)#it returns only the first occurannce

d=a.index('n',6)
print(d)#it returns the next occurance

#d=a.index('n',8)
#print(d) #valuerror
g=a.index('n',1,4)
print(g)

#rindex()---->>> returns the last occurance
b=a.rindex('g')
print(b)

c=a.rindex('n') #here 'n' is occuring at 7th index
print(c)
#d=a.rindex('n',8) #it return the valuerror

# count()--->>> returns the number of items object is repeating
print('codegnan'.count('n'))
print('code'.count('w'))    #it returns 0 as we dont have 'w'in code
print('venkatesh'.count('v'))

print('codegnan'.find('n'))
print('codegnan'.find('r')) #it returns '-1' becoz it dont have 'r' in codegnan

print('codegnan'.rfind('r'))

print('codegnan'.rfind('n'))


a='Data'
print(len(a))
for i in a:
    print(a.count(i),a.index(i))
'''

#replacing, splitting,Joining
#strings are immutable
'''
a='codegnan'
print(a.replace('g','s'))
print(a)
a=a.replace('g','s')
print(a)

print('venkatesh@warlu'.replace('@',' '))

print(a.replace('x','venkatesh'))
'''
'''
a='venky codegnan python'
#print(len(a))
b=a.split()  #by default if we have space it splits and (returns list)
print(b)
#print(len(b))

c='venky,codegnan,python'
d=c.split()
print(d)
print(len(d))
e=c.split(',')
print(e)
print(len(e))
'''

#JOIN()
'''
a='code'
b='gnan'
print(a.join(b))
print(b.join(a))
print('#'.join('venky'))
print(' '.join('venky'))
'''
#string testingf methods boolen
#isalpha(),isalnum(),isdigit(),isupper(),islower().........
'''
a='codegnan123'
print(a.isalnum()) #returns True for alphanumerica strings else False

b='codegnan'
print(b.isalnum()) #returns True becoz it string has completely num or alpha
print(a.isalpha()) #returns True only for alphabets
print(a.isdigit()) #returns True only for digit string

print('432634163'.isdigit())
print('563'.isnumeric()) #this has upper edge (numbers,fractions,romans)
#startswith()--->>> how it starting     
print('codegnan'.startswith('c'))
print('codegnan'.startswith('g',4))

print('codegnan'.endswith('g'))

print('codegnan'.islower()) #returns True for all lowercase
print('Codegnan'.isupper()) #returns True for all uppercase
print('Codegnan'.istitle())
'''
#space removal --->>>strip() (removes leading and trailing spaces)
'''
a=' codegnan '
print(a.strip())

b=input('enter the string:').strip().lower()
print(b)
'''

#print('hello'.zfill(2))
#print('2345'.zfill(7))

print('hello'.center(6))
print('hello'.center(9,'#'))


print('hello'.ljust(6,'#'))
print('hello'.rjust(6,'#'))






















