import os
#DICTIONARY
myDict ={
    "Meet" : "To communicate physically",           #key : value
    "Jheel" : "Lake",
    "Varsha" : "Rain",
    "Policyno." : [3517,3612,8978],
    "AnotherDict" :{                                        #nested dictionary
        "Barry" : "Flash",
        "Iris" : "Colour pigment of the eye",
        6:12,
    }
}

print(myDict['Meet'])
print(myDict['Jheel'])
print(myDict['AnotherDict']['Barry'])   #for nested dictionary
print(myDict['Policyno.'])
myDict['Policyno.'] = [10,20,60] #mutuable
print(myDict['Policyno.'])

#METHODS OF DICTIONARY
print(myDict.keys())  #to list all the keys in that dictionary
print(type(myDict.keys()))  
print(list(myDict.keys()))

print(myDict.values()) #to list all the values in the dictionary

print(myDict.items()) #to list all the keys and their values together in the dictionary

updateDict={
"Dhruvin" : "Brother",
"Krish" : "Friend",
"Jheel" : "Best Friend",
}
myDict.update(updateDict) #to add key-value pairs in the dictionary
print(myDict)

print(myDict.get('Meet')) #to get the value of the key without getting an error irrespective of the presence of the key in the dictinary
print(myDict['Meet']) #will throw an error if the key is not present 

#for more methods docs python.org

#SETS IN PYTHON
a= {1,2,3,4,5,1,2} 
print(type(a))
print(a) #Sets dont count repetative items

b={}
print(type(b)) #This syntax will show empty dictinary

c=set()
print(type(c)) #syntax for an empty set
c.add(1)
c.add(1)
c.add(3)
c.add(4)
c.add((8,9,10)) #can add tuple
#c.add({11}) #cannot add dictionary
#c.add([13,14]) #cannot  add lists
print(c)

#METHODS OF SET
print(len(c)) #prints the length of set

c.remove(1) #removes a particular value
print(c)

print(c.pop()) #removes ranndom value from the set
print(c)

print(c.clear()) #clears the set

#s.union # used to merge  the sets
#s.intersection #used to have an intersection set


