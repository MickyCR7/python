import os
from types import MethodDescriptorType
#CONTIONAL EXPRESSIONS
#if-elif-else ladder(here it prints the first condition it satisifies)
a=69
if(a>3) :
     print("yes") #indentation is 4spaces or tab(just like {} in other langauages)
elif(a>4) : 
     print("yes")
elif(a>68) :
    print("yes")
else:
         print("No")

#if-else (if we want to go through all the conditions and then print the ans)
a=69
if(a>3) :
     print("yes") #indentation is 4spaces or tab(just like {} in other langauages)
if(a>4) : 
     print("yes")
if(a>68) :
    print("yes")
else:
         print("No")

#   QUICK QUIZ 
a= int(input("Enter the age: "))
if(a>18):
    print("YES HE IS AND ADULT")
else:
    print("NO HE IS NOT AN ADULT")    

#LOGICIAL AND RELATIONAL OPERATORS
age= int(input("Enter the age: "))
if(age>18 and age<60) :
    print("YOU ARE ELIGIBLE FOR DRIVING LICENSE")
else:
    print("YOU ARE NOT ELIGIBLE")

if(age>18 or age<60) :
    print("YOU ARE ELIGIBLE FOR DRIVING LICENSE")
else:
    print("YOU ARE NOT ELIGIBLE")

if(age>18 and age<60) :
    print("YOU ARE ELIGIBLE FOR DRIVING LICENSE")
else:
    print("YOU ARE NOT ELIGIBLE")

#IN IS
x= None
if(x is None):          #when it declares the same thing....we can even use ==
    print("YeS")
else:
    print("No")

y=[1,2,3,4,5,6,7]
print(7 in y) #gives a boolean ans
print(8 in y) #gives a boolean ans

#IN IS NOT USED AS A LEFT OPERAND FOOR STRINGS

         






