'''
n=list(map(int,input('enter').split(',')))
count=0
for i in n:
    count=count+i
print(count)
'''




password = input()
upper = lower = digit = special=0
for ch in password:
    if 'A'<= ch<='Z':
        upper+=1
    elif 'a'<=ch <='z':
        lower+=1
    elif '0'<= ch <='9':
        digit+=1
    else:
        special+=1
print("upper",upper)
print("lower",lower)
print("digit",digit)
print("special",special)
'''




'''
email=input().split()
for mail in email:
    print(mail.split("@")[1])
'''
movies=list(map(int,input().split()))
for i in movies:
    
    
    

