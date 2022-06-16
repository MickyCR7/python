#USING if__name__=="__main__" property

from time import thread_time


def greet(name):
    print(f"GOOD MORNING, {name}")

print(__name__) #Here  __name__ will be printed as main cause this is the main file here
if __name__=="__main__":
    n=input("Enter a name \n")
    greet(n)


#this if __name__=="__main__": fucntion is used when 
#we inherit a X file into Y file and dont want a property of X file
#getting executed in Y file...so we mention that property of X file into Y file such that 
#it only gets exectued into the X file and not in the Y file. 