#PROGRAM TO ADD TWO NUMBERS USING OOP(OBJECT OREINTED PROGRAMMING)
'''
class Number:   #class has some methods and variables
    def sum(self):
        return self.a + self.b

num=Number() #OBJECT INSTANTIATION(instance for number)
num.a=1
num.b=12
s=num.sum()
print(s)
'''

'''
In OOPS classes dont take memories, no memory is stored in classes
classes arre like the blueprint for  creating obejcts
(Just like blueprint of railway reservaion form)

blank form of railway reservation(class) creating information of valid application i.e, object
when filled by  someone with appropriate name address id etc. becomes a filled form(object)

OOPS FOLLOWS DRY(DONT REPEAT YOURSELF) PRINCICPLE


PascelCase
eg:
MeetVora, StringName,IsFloatOrInt.

camelCase
eg:
meetVora, stringName, isFloatOrInt.

'''
#class name is usually in PascelCase
'''
THE APPLICATION WONT BE SUBMITTED IF THE OBJECT IS NOT MADE...MEMORY IS ALLOCATED ONLY AFTER OBJECT INSTANTIATION

'''
#EG OF OOPS BY USING RAILWAY FORM
'''
class RailwayForm:
    formType="RailwayForm"
    def printData(self):
        print(f"Name is {self.name} ")
        print(f"Train is {self.train} ")
        print(f"Number is {self.number} ")

meetsApplication = RailwayForm() #object
meetsApplication.name= "MEET"
meetsApplication.train= "RAJDHANI"
meetsApplication.number= "69"
meetsApplication.printData()
'''
#EG OF GAME USINF OOPS
'''
class Player: #all the functions related to the player are encapsulated here in one class which means encapsulation and which makes sense to that class.
    def moveRight(self):
        pass
    def moveLeft(self):
        pass
    def moveTop(self):
        pass
    def moveBottom(self):
        pass

class Remote:
    pass
   

player1= Player()
remote1= Remote()
if(remote1.isLeftPressed()): #isLeftPresssed means abstraction which means we need not specify the implementation detials to the user
    player1.moveLeft()
'''

#MODELLING IN OOPS
'''
NOUN= CLASS(EMPLOYEE)
ADJECTIVE= ATTRIBUTES(NAME,AGE,SALARY)
VERBS= METHODS(getSalary(),increment())

'''
#CLASS ATTRIBUTES AND INSTANCE ATTRIBUTES

#CA= AN ATTRIBUTE THAT BELONGS TO A PARTICULAR CLASS RATHER THAN AN OBJECT
#EG:
'''
class Employee:
    company= "Google" 

meet = Employee()
jheel = Employee()
print(meet.company)
print(jheel.company)
Employee.company="Youtube" #WE USED EMPOLYEE.COMPANY INSTEAD OF USING JHEEL OR MEET BECAUSE EMPLOYEE IS A CLASS ATTRIBUTE
print(meet.company)
print(jheel.company)
'''
#IA=  AN ATTRIBUTE THAT BELONGS TO THE INSTANCE(OBJECT)
#NOW MEET JHEEL WILL HAVE DIFFERENT PHONE NUMBERS AND ADDRESS AND NAME AND AGE AND SALARY WHICH IS LINKED WITH ONLY THEM SO IT IS IA.
#EG:
'''class Employee:
    company= "Google" 
    salary=100 #CA
meet = Employee()
jheel = Employee()
#CREATING IA FOR BOTH THE OBJECTS
#meet.salary=500 #IA BECAUSE SALARY OF MEET IS SPECIFIC TO HIM
#jheel.salary=1000 #IA BECAUSE SALARY OF JHEEL IS SPECIFIC TO JHEEL
print(meet.company)
print(jheel.company)
Employee.company="Youtube" #WE USED EMPOLYEE.COMPANY INSTEAD OF USING JHEEL OR MEET BECAUSE EMPLOYEE IS A CLASS ATTRIBUTE
print(meet.company)
print(jheel.company)
print(meet.salary) #MAIN CONFUSION IS IF THERE IS CA AND IA BOTH WHICH WILL GET PRINTED?
print(jheel.salary)
'''
'''
ANS: ASK YOURSELF WHERE DOES THE ATTRIBUTE BELONG?
DOES IT BELONG TO SOME OBJECT I.E IA(PREFERENE 1)
OR DOES IT BELONG TO SOME CLASS I.E CA(PREFERENCE 2)
IF IT IS NEITHER OF TWO THEN IT WILL THROW AND ERROR

'''
'''
SO NOW WHEN I WILL PRINT THEIR SALARIES IT WILL GIVE ME INSTANT ATTRIBUTE(500,1000) BUT IF I COMMENT OUT THE 
INSTRANT ATTRIBUTE THEN IT WILL PRINT CLASS ATTRIBUTE(100) FOR ME


INSTANT attributes take preference over class attributes during assignment and retreival
'''

#SELF
'''
class Employee:
    company="Google"
    def getSalary(self):
        print("THE SALARY IS 500K")

meet= Employee()
meet.getSalary() #after using self his comment gets coverted to
#Employee.getSalary(meet) 
#so if we dont use self it wont get coverted to it but it will say that there was 1 arguemtn given which is meet=Employee()

'writing the same code in different way'
class Employee:
    company="Google"
    def getSalary(self):
        print(f"The salary of this employee working in a company named {self.company} is {self.salary} ")

meet= Employee()
meet.salary= 10000
meet.getSalary()
'''

#STATIC METHOD
'''
#decorator is a speciaal function which modifies a function
class Employee:
    company="Google"
    def getSalary(self,sign):
        print(f"The salary of this employee working in a company named {self.company} is {self.salary}\n {sign}")
    @staticmethod  #sometimes we need a function to be called without a self so we use static method..its like a decorator to make greet as a staticmethod
    def greet():
        print("KEM SO, SIR")
    @staticmethod
    def time():
        print("THE TIME IS 9AM IN THE MORNING")
meet= Employee()
meet.salary= 10000
meet.getSalary("YO!") # will get converted to Employee.getSalary(meet)
meet.greet() #will get converted to Employee.greet()
meet.time()
'''
#CONTRUCTOR

#SYNTAX: __init__()
#it is a special method which is run as soon as the object is created...it takes self and other arguments....this method is knowns as constructor
'''
class Employee:
    company="Google"
    def getSalary(self,sign):
        print(f"The salary of this employee working in a company named {self.company} is {self.salary}\n {sign}")

    def __init__(self, name,salary,subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print(" EMPLOYEEE IS CREATED!")
    def getDetails(self):
        print(f"The name of the employee is {self.name}")        
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")

    @staticmethod 
    def greet():
        print("KEM SO, SIR")
    @staticmethod
    def time():
        print("THE TIME IS 9AM IN THE MORNING")
meet= Employee("MEET", 100, "YOUTOOBH")
#meet=  Employee()--> this throws an error
meet.salary= 10000
meet.getSalary("YO!") 
meet.greet() 
meet.time()
meet.getDetails()
'''







