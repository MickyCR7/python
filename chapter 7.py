import os
# while loop
'''i=0
while i<10:
    print("yes" + str(i))
    i=i+1
    print("done") '''
#QUICK QUIZ
'''i=1
while i<=50:
    print("the numbers are " +str(i))
    i=i+1    
'''
#AN EXAMPLE
'''i=0
while i<5:
    print("MEET")
    i=i+1
'''
#QUICK QUIZ
'''bff=['MEET','JHEEL','KRISH','DEV','MIHIKA','BHAVISHA']
i=0
while i<len(bff):
    print(bff[i])
    i=i+1
'''
#for loop
#same using for loop
'''bff=['MEET','JHEEL','KRISH','DEV','MIHIKA','BHAVISHA']

for items in bff:
    print(items)
'''
#range function
'''for i in range(0,100,25):   #range(start value, end value, skip value)  wonr end att 100 it will end st 99
    print(i)
'''
#for with else and break
'''for i in range(10):
    print(i)
    if i>6: 
       break 
else:
    print("HENCE THE LOOP IS EXHAUSTRED ")''' #we use else in for when the loop gets exhausted
#else will only get executed when the whole loop is completed...if there is some bresk statement or something in between then else wont get executed

#for with continue
'''for i in range(10):
    if i%2!=0:
        continue #skip everything which is below continue if the condition is reached nd then again execute the loop from thee next variable
    print(i)
'''
#pass statement
i=8
while i>6:
    pass #basically instructs us to do nothing for that function/loop
if i<9:
    pass

print("Meet is a very good boy")










