#Task 1-->observe +ve +ve,-ve -ve, +ve -ve,-ve +ve all possibilities
#Workout with all possibilities of slicing and striding on a example
# eg:s = "MEENUGU VENKATESHWARLU"
'''
name='MEENUGU VENKATESHWARLU'
#Entire string
print(name[:])
# +ve start,+ve start
print(name[0:7])      # MEENUGU
print(name[8:22])     # VENKATESHWARLU
print(name[2:10])     # ENUGU VE
print(name[5:15])     # GU VENKATE

#-ve Start, -ve End
print(name[-14:-1])    # VENKATESHWARL
print(name[-10:-5])    # ATESH
print(name[-22:-15])   # MEENUGU
print(name[-8:-3])     # ESHWA

#+ve Start, -ve End

print(name[0:-15])     # MEENUGU
print(name[8:-1])      # VENKATESHWARL
print(name[2:-5])      # ENUGU VENKATESH
print(name[5:-10])     # GU VENK

#-ve Start, +ve End
print(name[-14:22])    # VENKATESHWARLU
print(name[-8:21])     # ESHWARL
print(name[-5:22])     # WARLU
print(name[-22:7])     # MEENUGU

#Negative step
print(name[::-1])          # ULRAWHSETAKNEV UGUNEEM
print(name[21:7:-1])       # ULRAWHSETAKNEV
print(name[-1:-15:-1])     # ULRAWHSETAKNEV
print(name[-5:0:-2])       # WSTKE GNE
'''

#Task: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# use loops and strings to return A to Z
# Hint: ASCII 65 - 90

for i in range(65,91):
    print(chr(i),end=',')
