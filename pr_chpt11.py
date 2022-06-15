#FIRST PROBLEM STATEMENT
'''
class C2DVEC:
    def __init__(self,i,j):
      self.icap=i
      self.jcap=j  
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j "

class C3DVEC(C2DVEC):
    def __init__ (self,i,j,k):
        super().__init__(i,j)
        self.kcap=k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j +{self.kcap} k"
v2d=C2DVEC(1,7)
v3d=C3DVEC(1,9,8)
print(v2d)
print(v3d)
'''
#SECONF PROBLEM STATEMENT
'''
class Animals:
    animalType="Mammal"


class Pets(Animals):
    color="Brown"


class Dogs(Pets):
    @staticmethod
    def bark():       #self is not used because bark method is not using any class or instance attribbutes
        print("BHAAUUUU BHAAAUUUU")

d=Dogs()
d.bark()
'''
#THIRD PROBLEM STATEMENT
'''
class Employee:
    salary=50000
    increment= 2

    @property
    def salaryAfterIncrement(self):
        return self.salary*self.increment
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, value):
        self.increment=value/self.salary
e=Employee()
print(e.salaryAfterIncrement)
e.salaryAfterIncrement=200000
print(e.salaryAfterIncrement)
print(e.salary)
print(e.increment)
'''

#FOURTH PROBLEM STATEMENT
'''
class Complex:
    def __init__(self,r,i):
        self.real=r
        self.imaginary=i

    def __add__(self,c):
        return Complex(self.real+c.real, self.imaginary+c.imaginary)

    def __mul__(self,c):
        mulReal= (self.real*c.real- self.imaginary*c.imaginary)
        mulImg= (self.real*c.imaginary+ self.imaginary*c.real)
        return Complex(mulReal, mulImg)

    def __str__(self):
        if self.imaginary<0:
            return f"{self.real} -{-self.imaginary}i"
        else:
            return f"{self.real} +{+self.imaginary}i"


c1= Complex(3,2)
c2=Complex(1,7)
print(c1+c2)
print(c1*c2)
'''
#FIFTH PROBLEM STATE(MENT
'''
class Vector:
    def __init__(self,vec):
        self.vector=vec

    def __str__(self):
        str1=""
        index=0
        for i in self.vector:
            str1 += f" {i} a{index} +"
            index+=1
        return str1[:-1] #string slicing so that we can get '+ after every number

    def __add__(self,vec2):
        newList=[]
        for i in range(len(self.vector)):   #we used this becasue if we just add by using the standard thing it will just append the ist(merge it)
            newList.append(self.vector[i] + vec2.vector[i] )
        return Vector(newList)

    def __mul__(self,vec2):
        sum=1 
        for i in range(len(self.vector)):   
            sum+=(self.vector[i] * vec2.vector[i] )
        return sum
    


v1= Vector([1,4,])
v2=Vector([9,6])
print(v1 + v2)
print(v1*v2)
'''
#SIXTH PROBLEM STATEMENT
'''
class Vector:
    def __init__(self,vec):
        self.vec=vec

    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k "

v1= Vector([1,2,3])
v2=Vector([4,5,6])
print( v1)
print(v2)
'''
#SEVENTH PROBLEM STATEMENT

class Vector:
    def __init__(self,vec):
        self.vector=vec

    def __str__(self):
        str1=""
        index=0
        for i in self.vector:
            str1 += f" {i} a{index} +"
            index+=1
        return str1[:-1] #string slicing so that we can get '+ after every number

    def __add__(self,vec2):
        newList=[]
        for i in range(len(self.vector)):   #we used this becasue if we just add by using the standard thing it will just append the ist(merge it)
            newList.append(self.vector[i] + vec2.vector[i] )
        return Vector(newList)

    def __mul__(self,vec2):
        sum=1 
        for i in range(len(self.vector)):   
            sum+=(self.vector[i] * vec2.vector[i] )
        if (len(self.vector) == (len(vec2.vector))):
            return sum
        else:
            print("sorry we cannot multiply these vectors ")


    
    def __len__(self):
        return len(self.vector)
        

v1= Vector([1,4])
v2=Vector([9,6])
print(v1 + v2)
print(v1*v2)
print(len(v1))
print(len(v2))







