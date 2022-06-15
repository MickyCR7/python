import os
#FIRST PROBLEM STATEMENT
def maximum(num1,num2,num3):
     if(num1>num2):
         if(num1>num3):
             return num1
         else:
             return num3
     else:
         if(num2>num3):
             return num2
         else:
             return num3

m= maximum (4,6,9)
print("The value of the maximum no. is " +str(m))

#SECOND PROBLEM STATEMENT
def farh(celcius):
    return (celcius*(9/5)) +32

c=0
f= farh(c)
print("The fahrenheit temperature is " +str(f))

#THIRD PROBLEM STATMENT
print("HELLO ", end="") #IF WE ADD end="" THEN WE CAN SKIP THE NEXT LINE
print("HOW ", end="")
print("ARE ", end="")
print("YOU ", end="")

#FOURTH PROBLEM STATEMENT
def sum_recursive(n):
    if n==0:
        return 0
    if n==1:
        return 1    
    return n + sum_recursive(n-1)
print("\n")
s=sum_recursive(2)
print(s)

#FIFTH PROBLEM STATEMENT
n=3
for i in range(n):
    print("*" *(n-i))

#SIXTH PROBLEM STATEMENT
def cm(inch):
    return (inch*2.54)

i=32
c=cm(i)
print("THE LENGTH IN CM IS EQUAL TO "+str(c))

#SEVENTH PROBLEM STATEMENT
#strip  function is used to remove the extra spcaes in the string
def remove_and_strip(string, word):
    newStr= string.replace(word, "")
    return newStr.strip()

YO= "       MEET IS THE FLASH     "
print(YO)
n= remove_and_strip(YO, "MEET")
print(n)

#EIGTH PROBLEM STATEMENT
def multiply(num):
    for i in range(1,11):
        print(str(num)+" X " +str(i)+ " = " +str(num*i))

x=multiply(10)
print(x)




