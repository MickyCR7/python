import os
def percent(marks): #function call
    p=((marks[0]+marks[1]+marks[2]+marks[3])/400)*100 #function definition
    return p

marks1=[100,60,70,94]
percentage1= percent(marks1)
print(percentage1)

marks2=[57,68,90,90]
percentage2=percent(marks2)
print(percentage2)
#QUICK QUIZ

def greet(name):
    print("Good day," +name)
def mySum(num1, num2):
    s= num1+num2
    return s
greet("MEET")
s= mySum(12,78)
print("MEET'S BOARDS PERCENTILE ARE " +str(s) )

#Default parameter value
def love(name ="STRANGER"):  #default paramter  value means even if we dont use an input the output will show some default value
    print("Good Morning, " +name)

love("Meet")
love() #if we didnt have any default paramter value then this line of the code will show an error as there is no input

#RECURSION(used when u want the function to be called by itself)
def factorial_iter(num):
    fact=1
    for i in range(num):
        fact= fact * (i+1)
    return fact
    
f=factorial_iter(5)
print(f)

def factorial_recursive(num):
    if num==1 or num==0:
        return 1
    return num * factorial_recursive(num-1)
f= factorial_recursive(6)
print(f)


















