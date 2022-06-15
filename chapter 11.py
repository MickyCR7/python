import os
#INHERITANCE- IT IS A WAY OF CRRATING A NEW CLASS FROM AN EXISITING CLASS...also follows DRY(dont repeat youself) princicple
#EG FOR SINGLE INHERITANCE
'''
class Employee: #parent class/base class
    company= "Goggle"

    def showDetails(self):
        print(f"THIS IS AN EMPLOYEE OF THE COMPANY {self.company}")

class Programmer(Employee):  #derived class/child class: class xyz( derived from which parent class)
    lang="Python"
    #company="YouToobh"
    def getInfo(self):
        print(f"THE LANNGUAGE THE EMPLOYEE WORKING ON IS {self.lang}")
    def showDetails(self):
        print(f"THE PROGRAMMER IS WORKING IN {self.company}")
e=Employee()
p=Programmer()
e.showDetails()
p.showDetails() #will show the details of the parent class if it doesnt have this function
p.getInfo()
'''
'''
TYPES OF INHERITANCE:   SINGLE.MULTIPLE,MULTILEVEL
1)SINGLE INHERITANCE: SINGLE INHERITANCE OCCURS WHEN THE CHILD CLASS INHERITS ONLY A SINGLE PARENT CLASS 
EG: THE ABOVE CODE IS AN EXAMPLE OF SINGLE HERITANCE

2)MULTIPLE INHERITANCE: MULTIPLE INHERITANCE WHEN THE CHILD CLASS INHERITS FROM MORE THAN ONE PARENT CLASS
EG BELOW

3)MULTILEVEL INHERITANCE: WHEN A CHILD CLASS BECOMES A PARENT FOR ANOTHER CHILD CLASS
EG BELOW MULTILEBEL CLASS
'''
'''
#EG FOR MULTIPPLE INHERITANCE
class Employee:
    company="Amazon"

class FreeLancer:
    company="NodeJS"
    level= 2

    def upgradeLevel(self):
        self.level= self.level +1

class Programming(Employee,FreeLancer):  #the properties and methods of the parent class which we write first will get the priority
        name="Meet"

p=Programming()
e=Employee()
f=FreeLancer()
p.upgradeLevel()
print(p.level)
print(p.company) #it printed aamzon because in class programming, emoloyee class was mentioned first
'''
#EG FOR MULTILEVEL CLASS
'''
class Person:
    country="India"
    def takeBreath(self):
        print("I am breathing......")

class Employee(Person):
    company="Honda"

    def getSalary(self):
        print("Salaries offered by the company")


    def takeBreath(self):
        print("I m an employee so i am luckily breathing")

class Programmer(Employee):
    company="Fiverr"
    def getSalary():
        print("No salsaries to programmers")

    def takeBreath(self):
        print("I m a Programmer so i am taking ponds....")

e=Employee()
e.takeBreath()
print(e.company)
p=Person()
p.takeBreath()

pr=Programmer()
pr.takeBreath() #it will postfrom employee because it is inherited from there(takes the funvtion from nearest parent when it itself doesnt carry that function)
print(pr.country)
'''

#SUPER METHOD: SUPER METHOD IS USED TO ACCESS THE METHODS OF A SUPER CLASS IN THE DERIVED CLASS
#SYNTAX:  super()__init__() (calls constructor of the base class)
'''
class Person:
    country="India"
    def __init__(self):
        print("!! INITIALSING PERSON !!\n")
    def takeBreath(self):
        print("I am breathing......")

class Employee(Person):
    company="Honda"

    def __init__(self):
        super().__init__()
        print("!! INITIALIZING EMPLOYEE !!\n")

    def getSalary(self):
        print("Salaries offered by the company")


    def takeBreath(self):
        super().takeBreath()  #will print takeBreath of person with employee
        print("I m an employee so i am luckily breathing")

class Programmer(Employee):
    company="Fiverr"
    def __init__(self):
        super().__init__()
        print("!! INITIALIZING PROGRAMMER !!\n")
    def getSalary():
        print("No salsaries to programmers")

    def takeBreath(self):
        super().takeBreath()   #will print takeBreath of employee with programmer
        print("I m a Programmer so i am taking ponds....")

#e=Employee()
#e.takeBreath()

#p=Person()
#p.takeBreath()

pr=Programmer()
#pr.takeBreath() 
'''
#CLASS METHOD: A METHOD WHICH IS BOUND TO THE CLASS AND NOT TO THE OBJECT OF TH CLASS
#WE USE @classmethod decorator here 
'''
class Employee:
    company="Camel"
    salary= 100   #class attribute
    location="Delhi"
    
    #def changeSalary(self,sal):
        #self.__class__.salary =sal  #this will help chanhging the class attribute(so Employee.salary will channge)..also known as dunder class
           #OR
    @classmethod  #this will remove the necessity to write self..Used to change the class attribute
    def changeSalary(cls,sal):
        cls.salary =sal
e=Employee()
print(e.salary)
e.changeSalary(500)
print(e.salary)
print(Employee.salary) #wont get changed
'''
#@property_decorator
'''
class Employee:
    company="TATA"
    salary= 5000
    salarybonus=500
    #totalSalary= 5500 #ut it will keep cahnhging according to the values of salary and salarybonus
    
    
    @property    #also called as @getter method
    def totalsalary(self):
        return self.salary+self.salarybonus


    @totalsalary.setter  #@setter decorator
    def totalsalary(self,val):
        self.salarybonus=val-self.salary  #so it will print the value of salarybonus according to the value of totalsalary assigned
e=Employee()

print(e.totalsalary) #as totalsalary is a fuction we dont have to use () because of poperty decorator
#now we specify some value of totalsalary here and want the compiler to shape the salary annd salarybonus acordingly we use @setter method
#let
e.totalsalary= 6000

print(e.totalsalary) 
print(e.salarybonus) 
print(e.salary)
#now as we change the totalsalary the values of salary and salarybomus will set accordingly
'''
#OPERATOR OVVERLOADING IN PYTHON : OVERLOADED USING DUNDER METHODS
'''
class Number:
    def __init__(self,num):
        self.num=num

    def __add__(self,num2):
        print("Lets add")
        return self.num+ num2.num

    def __mul__(self,num2):
        print("Lets multiply")
        return self.num* num2.num

    def __truediv__(self,num2):
        print("Lets divide truly")
        return self.num/ num2.num

    def __sub__(self,num2):
        print("Lets subtract")
        return self.num- num2.num

    def __floordiv__(self,num2):
        print("Lets floordiv")
        return self.num// num2.num

    

n1= Number(1)
n2=Number(2)
sum=n1+n2
print(sum)
mul=n1*n2
print(mul)
sub=n1-n2
print(sub)
truediv=n1/n2
print(truediv)
floordiv=n1//n2
print(floordiv)
'''
#OTHER OPERATOR OVERLOADING
'''
class Number:
    def __init__(self,num):
        self.num=num

    def __add__(self,num2):
        print("Lets add")
        return self.num+ num2.num

    def __mul__(self,num2):
        print("Lets multiply")
        return self.num* num2.num
    def __str__(self):      #if i want to print something with the number
        return f"DECIMAL NUMBER {self.num} "

    def __len__(self):    #if i want to specify the leght of the string
        return 1
n=Number(7)
print(n)
print(len(n))
'''





