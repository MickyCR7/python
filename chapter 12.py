import os
from re import I
from threading import main_thread

from pip import main

#USING TRY FOR EXCEPTION HANDLING
'''
while(True):
    print("Press q to exit the game!")
    a=input("Enter a number: ")
    
    if a =='q':
        break
    try:
        print("TRYING........")
        a=int(a)
        if a>0:
            print("YES! the number is positive")
    except Exception as e:
        print(f"Your input is throwing some error: {e}")

print("\n")
print("Thanks for playing this game!")
'''
#HANDLING DIFFERENT EXCEPTIONS
'''
try:
    a=int(input("Enter the number:  "))
    c=1/a
    print(c)
except Exception as e:
    print("Exception occcured")
    print(e)

print("THANKS FOR USING THIS CODE!")
'''
'''
try:
    a=int(input("Enter the number:  "))
    c=1/a
    print(c)
except ValueError as e:
    print("Exception 1 occcured") #ask the user to input a valid value
    print(e)
except ZeroDivisionError as e:
    print("Exception 2 occured") #make sure that the user doesnt divide by zero
    print(e) 
except Exception as e:
    print(e) #used for any other type of error
print("THANKS FOR USING THIS CODE!")

'''

#RAISING EXCEPTIONS(we can raise our own exceptions)
'''
def increment(num):
    try:
        return int(num)+1
    except:
        raise ValueError("This is not upto the mark, Try again!")

a=increment('vdd')
print(a)
'''
#USING TRY WITH ELSE CLAUSE
'''
try:
    i=int(input("Enter the number: "))
    c=1/i
    print(c)
except Exception as e:
    print("Exception occured")
    print(e)
else:
    print("THE CODE WAS EXECUTED SUCCESSFULLY") #else is ued when the code is excuted successfully    
'''

#TRY WITH FINALLY CLAUSE
'''
try:
    i=int(input("Enter the number: "))
    c=1/i
    print(c)
except Exception as e:
    print("Exception occured")
    print(e)
    exit() #even if write exit here finally will get executed
finally:
    print("We are done") #finally clause gets executedd irrespective of whether the code throws error or not

print("THANKS FOR USING THE CODE")#this wont get executed if the code throws exception(becasue we used exit ())    
'''

#mchapter12a, mchapter12b (we use m in front  so that the python file can import and extract properties from each other)

#globl variables are the variables declared globally and can  be used freely throughout the code
#local variables are the variables declaed locally inside a method or function and is only confined to that paticular function only!



