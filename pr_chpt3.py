import os

#FIRST PROBLEM STATEMENT
name = input("Ennter your name:")
print("Good afternoon, " +name)

#SECONF PROBLEM STATEMENT
letter = ''' DEAR <|NAME|>,
YPU ARE SELECTED!!!!!!

DATE : <|DATE|>
'''
name =  input("Enter your name:")
date =  input("Enter date:")
letter = letter.replace("<|NAME|>", name) # dont forget to write letter = 
letter = letter.replace("<|DATE|>", date) # dont forget to write letter = 
print(letter)

#THIRD PROBLEM STATEMENT
story="MEET  IS  A  GOOD  BOY"
print(story.find("  "))

#FOURTH PROBLEM STATEMENT
print(story.replace("  ", " "))

#FIFTH PROBLEM STATEMENT
letter="DEAR HARRY, THIS PYTHON COURSE IS NICE. THANKS!"
print(letter)

editted_letter = "DEAR HARRY,\n\t THIS PYTHON COURSE IS NICE.\n THANKS!"
print(editted_letter)