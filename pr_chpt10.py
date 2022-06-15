#FIRST PROBLEM STATEMENT
'''
class Programmer:
    company="Microsoft"
    def __init__(self,name,product):
        self.name=name
        self.product= product
        print("THE TABLE IS CREATED!")
    def getDetails(self):
        print(f"THE NAME OF THE PROGRAMMER IS {self.name}")
        print(f"THE PRODUCT HE/SHE IS WORKING ON IS {self.product}")
meet=Programmer("MEET","MSTEAMS")
jheel=Programmer("JHEEL","ACCOUNTS")
meet.getDetails()
jheel.getDetails()
'''
#SECOND PROBLEM STATEMENT
'''
class Calculator:
    def __init__(self,num):
        self.num=num

    def square(self):
        print(f"THE SQUARE OF THE NUMBER {self.num} is {self.num **2}") # ** is an operator
    
    def squareRoot(self):
        print(f"THE SQUAREROOT OF THE NUMBER {self.num} is {self.num **0.5}")
    
    def cube(self):
        print(f"THE CUBE OF THE NUMBER {self.num} is {self.num **3}")

a= Calculator(4)
a.square()
a.squareRoot()
a.cube()
'''
#THIRD PROBLEM STATEMENT
'''
class Sample:
    a="MEET"

obj=Sample()
obj.a="JHEEL"

print(Sample.a)
print(obj.a)
'''
'''
A new instant variable obj.a will be creatd but the class attributte will remian same
because we have chaged the object not the samplif we write
Sample.a= "JHEEL"
it will change the class attribute

'''

#FOURTH PROBLEM STATEMENT
'''
class Calculator:
    @staticmethod
    def greet():
        print("!!!!  HELLO USER  !!!!")

    def __init__(self,num):
        self.num=num

    def square(self):
        print(f"THE SQUARE OF THE NUMBER {self.num} is {self.num **2}") # ** is an operator
    
    def squareRoot(self):
        print(f"THE SQUAREROOT OF THE NUMBER {self.num} is {self.num **0.5}")
    
    def cube(self):
        print(f"THE CUBE OF THE NUMBER {self.num} is {self.num **3}")

    

a= Calculator(4)
a.greet()
a.square()
a.squareRoot()
a.cube()
'''
#FIFTH PROBLEM STATEMENT
'''
class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats
    def getStatus(self):
        print("************")
        print(f"The name of the train is {self.name}")
        print(f"The seat no. of the train is {self.seats}")
        print("************")
    def getFare(self):
        print(f"The fare of the train is {self.fare}")
    
    def bookTicket(self):
        if(self.seats>0):
            print(f"YOUR TICKET HAS BEEN BOOKED! YOUR SEAT NUMBER IS {self.seats}")
            self.seats=self.seats-1
        else:
            print("SORRY!THE TRAIN IS FULL..TRY IN WAITING")


rajdhani= Train("Rajdhani Express", 2000, 300)

rajdhani.getFare()
rajdhani.bookTicket()
rajdhani.getStatus()
rajdhani.bookTicket()
rajdhani.getStatus()
'''
#SIXTH PROBLEM STATEMENT
class Sample:
    def __init__(self,name):
        self.name=name

obj= Sample("meet")
print(obj.name)
#when we change self to meet 
class Sample:
    def __init__(meet,name):
        meet.name=name

obj= Sample("meet")
print(obj.name)
#when we change self to slf
class Sample:
    def __init__(slf,name):
        slf.name=name

obj= Sample("meet")
print(obj.name)
 #the code works with whstever name we write so there is no compulsion as such 


