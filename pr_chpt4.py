import os
#FIRST PROBLEM STATEMENT

f1= input("Enter the name of the fruit 1: ")
f2= input("Enter the name of the fruit 2: ")
f3= input("Enter the name of the fruit 3: ")
f4= input("Enter the name of the fruit 4: ")
f5= input("Enter the name of the fruit 5: ")
f6= input("Enter the name of the fruit 6: ")
f7= input("Enter the name of the fruit 7: ")
F=[f1,f2,f3,f4,f5,f6,f7]
print(F)
#SECONF PROBLEM STATEMENT

m1= int(input("Enter the marks of student 1: ")) #Good sign to show int as marks are integer
m2= int(input("Enter the marks of student 2: ")) #Good sign to show int as marks are integer
m3= int(input("Enter the marks of student 3: ")) #Good sign to show int as marks are integer
m4= int(input("Enter the marks of student 4: ")) #Good sign to show int as marks are integer
m5= int(input("Enter the marks of student 5: ")) #Good sign to show int as marks are integer
m6= int(input("Enter the marks of student 6: ")) #Good sign to show int as marks are integer

M=[m1,m2,m3,m4,m5,m6]
M.sort()
print(M)

#THIRD PROBLEM STATEMENT

#a=(1,2,3,4,5,6,7,8)
#a[0]=4 

#FOURTH PROBLEM STATEMENT

L=[1,10,100,1000]
print(L[0]+L[1]+L[2]+L[3])
print(sum(L))
#FIFTH PROBLEM STATEMENT

t=(7,0,8,0,0,9)
print(t.count(0))


