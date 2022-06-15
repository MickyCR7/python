import os 
#WORKING WITH VARIABLES
a='''MEET NILESH VORA'''
# a='MEET NILESH VORA'
# a="MEET NILESH VORA"
b= 60003200095
c= 9.93 
d= True
d= None
#PRINTING THE VARIABLES
print("Name of the candidate is:", a )
print("His SapID is : ",b)
print("His CGPA is : ",c)   
print(d)
print("\n")
#PRINTING THE TYPE OF VARIABLES
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print("\n")
#WORKING WITH OPERATORS
X = 20
Y= 10

#ARITHMTIC OPERATORS
print("THE addition of the above values is: ", X+Y)
print("THE subtraction of the above values is: ", X-Y)
print("THE multiplication of the above values is: ", X*Y)
print("THE division of the above values is: ", X/Y)
print("\n")
#ASSIGNEMENT OPERATORS
x=70
x+=10
x-=10
x*=10
x/=5
print(x)
print("\n")
#COMPARISON OPERATORS
# y=(10>=7)
# y=(10<=7)
# y=(10>7)
# y=(10<7)
# y=(10==7)
y=(10!=7)
print (y)
print("\n")

#LOGICAL OPERATORS(JUST LIKE LOGIC TABLE OR BOOLEAN ALGEBRA)
bool1= True
bool2= False
print ("The value of bool1 and  bool 2 is: ", (bool1 and bool2))
print ("The value of bool1 or  bool 2 is: ", (bool1 or bool2))
print ("The value of not bool 2 is: ", (not bool2))
print("\n")

#TYPECASTING
'''NOW SUPPOSE WE CALL A VARIABLE WHOOSE TYPE WE 
WANT TO CHANGE THEN WE USE THIS TYPECASTING'''

x= "450"
print(type(x))
#THE TYPE OG A WILLL BE STRNG IRRESPECTIVE OF THE FACT THAT THE VALUE INISIDE IS INTEGER BECAUSE THE IN VALUE IS THERE IS IN DOUBLE QUOTES
# print(x+5) [THIS WILL SHOWCAST AN ERROR CAUSE WE CANNOT ADD A STRING WITH INTEGER]

#USING TYPECASTING
x= int(x)
#NOW IF WE SEE THE TYPE OF VARIABLE THEN IT WILL SHOW INTEGER VALUE
print(type(x))

print (x+5) # IT WONT SHOW AN ERROR CAUSE WE CHANGED THE TYPE OF VARIABLE TO INTEGER BY USING TYPECASTING


#INPUT FUNCTIONS
a= input("Enter your name :\n ")
print(a)