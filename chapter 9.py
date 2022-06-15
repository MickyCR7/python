import os
#USE OPEN FUNCTION TO READ THE CONTENT OF THE FILE

f=open('sample text chpt 09.txt', 'r')  #('the text file we are reffering to', 'type  of mode(here it is reading mode)')
#even if we dont mention the mode it will consder it as read mode only

data=f.read() #cannont use read two times
#data=f.read(5) #will read only the first 5 characters

print(data)
f.close() #always remember to close the file


#USING READLINE
f=open('sample text chpt 09.txt')
#will read the first line
data= f.readline() 
print(data)
#will read the second line
data= f.readline() 
print(data)
#will read the third line
data= f.readline() 
print(data)
#will read the fourth line
data= f.readline() 
print(data)

#USING APPEND AND WRITE MODE

f=open('anotherchpt 09.txt','w') #if we dont create  a new file for using eirte funtion then it will replace evrythin that is in the exisiting function and then write what we mentioned
f.write("NOW GO TO SLEEP") #CHANGES MADE HERE WILL BE SHOWN THERE IN THE FILE
f.close()

f=open('anotherchpt 09.txt', 'a')
f.write("YOYO") #THIS WILL APPEND THE TEXT IN THE TEXT FILE
f.close()

#USING WITH STATEMENT
with open('anotherchpt 09.txt', 'r') as f:
    a=f.read()
with open('anotherchpt 09.txt','w') as f:
    a=f.write(" SONE JAA")
print(a)




