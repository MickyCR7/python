import os
#FIRST PROBLEM STATEMENT 
'''
print("Take four numbers from the user")
a1=int(input("Enter number 1: \n"))
a2=int(input("Enter number 2: \n"))
a3=int(input("Enter number 3: \n"))
a4=int(input("Enter number 4: \n"))

if(a1>a4):
    f1=a1
else:
    f1=a4
if(a2>a3):
    f2=a2
else:
    f2=a3
if(f1>f2):
    print(str(f1) + " IS THE GREATEEST NUMBER ")
else:
    print(str(f2) + " IS THE GREATEEST NUMBER ")
'''
#SECOND PROBLEM STATEMENT
'''
name= input("Enter your name: \n")
m1=int(input("Enter your mark for maths: \n"))
m2=int(input("Enter your mark for phys: \n"))
m3=int(input("Enter your mark for chem: \n"))
t=(m1+m2+m3)/3
marks=[m1,m2,m3]
print(marks)
if(m1 <33 or m2<33 or m3<33 and t<40):
    print("FAIL")
else:
     print("PASS")
'''
#THIRD PROBLEM STATEMENT
'''
text=input(("Enter yout text: \n"))

if ("make a lot of money" in text):
    spam=True
elif("click this" in text):
    spam=True
elif("subsrcibe this" in text):
    spam=True
elif("buy now" in text):
    spam=True
else:
    spam=False


if(spam==True):
    print("This is a spam")
else:
    print("This is not a spam")    
'''
#FOURTH PROBLEM STATEMENT
'''
name=input("Enter your username: \n")


j=len(name)
if(j<10):
    print("Yes it contains less than 10 characters")
else:
    print("No it contains more than 10 characters")
'''

#FIFTH PROBLEM STATEMENT
'''
name=["Meet","Jheel","Krish","Rahul","Dev"]

username=input("Enter your name: \n")

if(username in name):
    print("Yes it is there in this list")
else:
    print("No it is not there in the list")
'''
#SIXTH PROBLEM
'''
marks=int(input("Enter your marks: \n"))

if(marks<50):
    print("YOUR GRADE IS F")
elif(marks>50 and marks<60):
    print("YOUR GRADE IS E")
elif(marks>60 and marks<70):
    print("YOUR GRADE IS D")
elif(marks>70 and marks<80):
    print("YOUR GRADE IS C")
elif(marks>80 and marks<90):
    print("YOUR GRADE IS B")    
elif(marks>90 and marks<100):
    print("YOUR GRADE IS A")  
else:
    print("THIS INTEGER IS NOT THERE IN OUR MARKING SYSTEM")
'''
#SEVENTH PROBLEM
post=input("Enter the comment in the post: \n")
name=["MEET","meet","Meet","MEet","MEEt","mEet","mEEt","mEET","MeEt","mEeT","MeeT","meET"]

if(post in name):
    print("The post contains the name")
else:
    print("The post does not contain the name")