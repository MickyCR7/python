import os
#Create a list usinhg []

a=[1,2,3,4,5]

#print the list using print() fucntion
print(a)

#Access using index using a[0],a[1],a[2]
print(a[2])
#Change the value of the list

a[0]=100
print(a)
#Creating a list with the items of different types
c=[2,"meet", 1000, True]
print(c)

#List slicing
friends =["Meet", "Jheel","Krish",2057,"Dev"]
print(friends[0:4])
print(friends[-4:])

#LIST METHODS

l1 =[1,5,3,8,3,6,0,3,5,1]
l1.sort() #we dont use l1_sorted=l1sort() becuse there are multiple datatypes on python so it wont show any o/p.....sorts the list
print(l1)
l1.reverse()#reverses the list
print(l1)
l1.append(12) #adds at the end of the list
print(l1)
l1.insert(0, 27)#adds 27 at the index 0
l1.insert(1, 1)#adds 1 at the index 1
print(l1)
l1.pop(2) #deleted the character at the specified index number
print(l1)
l1.remove(1) #removes the specified character
print(l1)
#can search 'list methods python docs' if you want to learn more lists

#TUPLES USING ()
t=(1,2,3,4,5)
print(t)
t1=() #empty typle
t2=(1) #wrong way to declare a single tuple(this will print a number)
t3=(1,) #right way to declare a single tuple
print(t1)
print(t2)
print(t3)
# t[0]=4 #cannoot replace a value of a tuple(major difference between tuple and list)

#TUPLE METHODS
m=(1,2,3,4,5,6,7,8,90,1,3,5,6,8,9,425,36,3,63,6,37,46,3,6,3)
print(m.count(1)) #counts the number of times a particular value gets repeated
print(m.index(1)) #shows where the value occurs first
#python.org for more tuple methods


