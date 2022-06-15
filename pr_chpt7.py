import os
#FIRST PROBLEM STATEMENT
'''
num=int(input("ENTER THE NUMBER \n"))
for i in range(11):
    print(str(num)+ "X" + str(i) + "=" +str(num*i))
    #3print(f"{num}X{i}={num*i}")  #f strings
'''
#SECOND PROBLEM STATEMENT
'''
l1=['Harry','Soham','Sachin','Rahul']
for names in l1:
    if names.startswith("S"):
        print("Hello " + names + " Good Morning, we are happy to see you here!")
'''
#THIRD PROBLEM STATEMENT
'''
num=int(input("ENTER THE NUMBER \n"))
i=0
while i<11:
    print(f"{num}X{i}={num*i}")
    i=i+1
'''
#FOURTH PROBLEM STATEMENT
'''
num=int(input("ENTER THE NUMBER \n"))
prime= True
for i in range(2, num):
    if(num%i==0):
        prime=False
    break
if prime:
    print("THE NUMMBER IS PRIME:")
else:
    print("THE NUMBER IS NOT PRIME")
'''
#FIFTH PROBLEM STATTEMENT
'''
num=int(input("ENTER THE NUMBER \n"))
i=0
sum=0
while i<=num:
    sum=sum +i
    i=i+1
    print("therefore the sum is :" +str(sum))
'''
#SIXTH PROBLEM STATEMENT
'''
num=int(input("ENTER THE NUMBER \n"))
f=1
for i in range(1, num+1):
    f=f*i
print("the factorial for " +str(num) +" is " +str(f))
'''
#EIGHT PROBLEM STATEMENT
'''
num=int(input("ENTER THE NUMBER \n"))
i=0
for i in range(0, num):
    i=i+1
    print("*" *i)
'''
#SEVENTH PROBLEM STATEMENT
'''
num=int(input("ENTER THE NUMBER \n"))
i=0
for i in range(1,num+1):
    print(" " *(num-i) , end="") #by writing this end="" function the compiler wont print new line(to avoid the spaces in the code which arent desried)
    print("*" *(2*i-1) , end="")
    print(" " *(num-i))
  '''
#NINTH PROBLEM STATEMENT
'''
n = 3

for i in range(1,4):
    if i%2 == 0:
        print("*"*(n-2) + " "*(n-2) + "*"*(n-2))
        continue
    elif i%2 != 0:
        print("*"*n)
'''
#TENTH PROBLEM STATEMENT
num=int(input("ENTER THE NUMBER \n"))
i=0
for i in range(10,0,-1):
    print(f"{num}X{i}= {num*i}")

