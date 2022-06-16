#FRIST PROBLEM STATEMENT
'''
from unittest import result


def readfile(filename):
    try:
        with open(filename,"r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {filename} was not found ")

readfile("1 pr_chpt12.txt")
readfile("2.txt")
'''
#SECOND PROBLEM STATEMENT
'''
a=[1,2,3,4,5,6,7,8,9,10]
b=[]
for index,item in enumerate(a):
    if index%2==0:
        print(f"the {index+1}th element is  {item}")
'''
#THIRD PROBLEM STATEMENT
'''
num=int(input("Enter the number: "))
a=[]
b=[1,2,3,4,5,6,7,8,9,10]

#for item in b:
#    result=num*item
#    a.append(result)
#
#print(a)#

a=[num*item for item in b]
print(a)
'''
#FOURTH PROBLEM STATEMENT
'''
try:
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    c=a/b
    print(c)
except:
    print("Infinite")
'''

#FIFFTH PROBLEM

num=int(input("Enter the number: "))
a=[]
b=[1,2,3,4,5,6,7,8,9,10]

a=[num*item for item in b]
print(a)

with open("tables pr_chpt12.txt","a") as f:
    f.write(str(a))
    f.write('\n')







