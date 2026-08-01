'''
marks = int(input('Enter the marks'))
if marks >0 and marks <= 100:
            if marks >= 90:
                print('A')
            else:
                if marks >= 80:
                    print('B')
                else:
                    if marks >= 70:
                        print('C')
                    else:
                        if marks >= 60:
                            print('D')
                        else:
                            if marks < 60:
                                print('Fail')
else:
    print('invalid number')
'''
'''
marks = int(input('Enter the marks'))
if marks >0 and marks <= 100:
            if marks >= 90 and marks <=100:
                print('secured A')
            if marks >= 80 and marks <= 89:
                print('secured B')
            if marks >= 70 and marks <= 79:
                print('secured C')
            if marks >= 60 and marks <= 69:
                print('secured D')
            if marks < 60:
                print('User has failed, study again')
else:
    print('invalid number')
'''
'''
#Elif keyword --> if-elif-else:
marks = int(input('Enter the marks'))
if marks >100:
    print('enter the less than 100 numbers')
elif marks >= 90 and marks <=100:
    print('secured A')
elif marks >= 80 and marks <= 89:
    print('secured B')
elif marks >= 70 and marks <= 79:
    print('secured C')
elif marks >= 60 and marks <= 69:
    print('secured D')
elif marks < 60 and marks >= 0:
    print('User has failed, study again')
else:
    print('invalid number')
'''
#voter eligibility checkcase --> make sure to satisfy all possible condition:
# >= 18   ---->>> access
#negative values -->>> not acceptable
'''
age = int(input('enter the age:'))
if age >= 18 and age <= 100:
    print('-----Access Granted-----')
    print('-----User has vote eligibility-----')
elif age < 18 and age >= 0:
    print('---user still need to wait for vote eligilibity---')
    print('---user need to wait for',(18 - age),'years----')
else:
    print('only +ve values')
'''
#Output formating -->>> old style formatting (using commas)
# % usage (%f, %d),.formate() usage, fstring notation
'''
a,b = 7,9
print(a)
print(b)
print(a,b)
name = 'codegnan'; batch = 'Data_Analysis'
print(name,batch,sep='\n')

'''
# old formatting -- >>> %d -->> integers,%s--->>,%f--->>>float
'''
salary=25167.235
print('his salary is %d'%(salary))
print('his salary is %f'%(salary))
print('his salary is %.1f'%(salary))
'''
name = 'codegnan';batch = 'DA';place = 'hyderabad'
#.format() usage
print('{} is in {}'.format(name,place)) #order matter
print(f'{name} is in {place}')


































