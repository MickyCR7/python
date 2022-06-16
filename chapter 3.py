#a= "Good Morning, "
#b= "Meet"
#c= a+b #Concatenanting two strings
b= "Meet"
print(b[3]) # [] are used to locate the character with the sepcified number
print(b[0:3]) # this is used to print the characters 0 1 2.....the first digit is including and last digit wont be counted by the python interpretur
print(b[:3]) #If i dont mention the starting number then it will consdier the initial non-negative number
print(b[0:]) #If i dont mention the last digit then it will consider the length of the string
print(b[-3:-1]) #is same as b[1:3]

#SKIP SLICING
a="MEETISAVERYGOODBOY"
print(a[0::2]) # a[0::2] here 2 stands for the skiiping no. i.e,how many digits should be skipped

#STRING FUNCTIONS
story ="MYSELF MEET VORA I M THE CR OF A DIVISION"
print(len(story)) #len() is the function which tells about the length of that particular function
print(story.endswith("ION")) #This function check whether a string ends with a particulat string or not(it gives true or false as output)
print(story.count("O")) #A FUNCTION USED TO COUNT A PARTICULAR character/string IN THE VARIABLE STRING
print(story.capitalize()) #this function is used to capitalize the first character of the string
print(story.find("MEET")) #used to find the irst occurence of the particular string
print(story.replace("MEET", "RAJ")) #used to replace old word with new word


