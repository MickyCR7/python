'''

import flask
import pandas as pd
import pygame


q)whi is virtual environment used?
ans: Virtual environement is used when we are working on some projects....while working on some projects we use a particuular version of packages which may change after some x amount of years because which we wont be able to get the desired output...virtual environement solves this  problem because inn the virtual environment we will still be using the same version of packages.

'''
#pip freeze =  used to print all the packages that are there in that particular environment(virtual environment/system interpreter) along with its version
#pip free > requirements.txt = used to print all the packages that are there in that particular environment(virtual environment/system interpreter)along with its version in teh file requirements.txt

#pip install - r.\requirements.txt = this will install all the packages that are there in the file requirements.txt 
#deactivate- will take you out from the virtual environment


#LAMBDA FUNCTIONS(WE USE THIS WHEN WE WANT TO PASS THE FUNTION AS ARGUMENT)

'''
def func(a):
    return a+5 #normal method
'''
func= lambda a:a+5 #lamda argumments:expression
sqaure=lambda x:x*x 
sum=lambda a,b,c:a+b+c
x=5
print(func(x))
print(sqaure(x))
print(sum(x,1,2))

#JOIN METHOD
'''
l=["ASUS","DELL","HP","LENOVO","APPLE","SAMSUNG","ACER"]

sentence=" and ".join(l) #What lies between " " will act as a seperator
list=" \n ".join(l)
print(sentence)
print(list)

#FORMAT METHOD

name="Meet"
sapid="60003200095"
branch="Information technology"

#info=f"Name= {name}, SapID= {sapid}, Branch= {branch}" #modern method
info="My name is {}".format(name)
info="My name is {} and my SapId is {}".format(name,  sapid)
info="My name is {2} and my SapId is {0} and my branch is {1}".format(name,  sapid, branch)#we can give index {} to provide a specific var as info 
print(info)
'''
#MAP FUNCTION
def square(num):
    return num**2
l1=[1,2,3]
'''
#OLD METHOD
l2=[]
for item in l1:
    l2.append(square(item))

print(l2)
'''
print(list(map(sqaure, l1)))

#FILTER METHOD

def less_than_5(n):
    if n<5:
        return True
    else:
        return False

l3=[1,2,3,4,5,6,7,8,9,10]
print(list(filter(less_than_5,l3)))

#REDUCE FUNCTION
from functools import reduce

sum=  lambda x,y:x+y
li=[1,2,3,4,5]

print((reduce(sum,li))) #1+2 first then  3+3 then 6+4...then 10+5