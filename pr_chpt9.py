import os
#FIRST PROBLEM STATEMENT
'''
f=open('poems pr_chpt09.txt')
t= f.read()
if "Twinkle" in t:
    print("TWINKLE IS PRESENT")
else:
    print("TWINKLE IS NOT PRESENT")
f.close()
'''
#SECOND PROBLEM STATEMENT
'''
def game():
    return 98

score = game()
with open("highscore pr_chpt09.txt", "r") as f:
    hiscore = (f.read())
if hiscore=='':
    with open("highscore pr_chpt09.txt", "w") as f: #WILL WRITE THE SCORE IN RETURN IF THE TEXT IS EMPTY
        f.write(str(score))
elif int(hiscore)<score:
    with open("highscore pr_chpt09.txt", "w") as f: #WILL OVERWRITE IF THE NO. IN THE TEXT FILE IS LESS THAN WHAT IS IN RETURN
        f.write(str(score))
else:
    print("SCORE IS GREATER THAN HIGHSCORE")
'''

#THIRD PROBLEM STATEMENT
'''
for i in range(2,21):
    with open (f"tables pr_chpt09/Multiplication_of_{i}.txt", "w") as f:
        for j in range(1,11):
            f.write(f"{i} x {j} = {i*j}")
            if j!=10:
                f.write("\n")

'''
#FOURTH PROBLEM STATEMENT
'''
with open("replace pr_chpt09.txt") as f:
    content=f.read()

content=content.replace("MORON","!@#$%^&*")

with open("replace pr_chpt09.txt", "w") as f:
    f.write(content)
'''

#FIFTH PROBLEM STATEMENT
'''
words =["MORON","ASSHOLE","BULLSHIT"]
with open("replace pr_chpt09.txt") as f:
    content=f.read()
for word in words:
    content=content.replace(word,"!@#$%^&*")
    with open("replace pr_chpt09.txt", "w") as f:
        f.write(content)
'''

#SIXTH PROBLEM STATEMENT
'''
with open ("log chpt09.txt") as f:
    content= f.read().lower() #lower() is used to make all the words in their lower case so that therei sno hinderance due to case sensitiveness
if 'python' in content:
    print("YES PYTHON IS PRESENT")
else:
    print("NO PYTHON IS NOT PRESENT")
'''

#SEVENTH PROBLEM STATEMENT
'''
content= True
i=1
with open("log chpt09.txt") as f:
        while content:
            content=f.readline().lower()
            if 'python' in content:
               print(content)
               print(f"YES PYTHON IS PRESENT IN LINE NUMBER {i}.")
            i+=1
'''
#EIGHT PROBLEM STATEMENT     
'''
with open ("this pr_chpt09.txt") as f:
    content=f.read()

with open ("copy pr_chpt09.txt", "w") as f:
    f.write(content)
'''
#NINTH PROBLEM STATEMENT
'''
file1= "this pr_chpt09.txt"
file2="copy pr_chpt09.txt"

with open ("this pr_chpt09.txt") as f:
    f1=f.read()
with open ("copy pr_chpt09.txt") as f:
    f2=f.read()
if f1==f2:
    print("YES BOTH THE FILES ARE IDENTICAL")
else:
    print("THESE FILES ARE NOT IDENTICAL")
'''
#TENTH PROBLEM STATEMENT
'''
with open ("copy pr_chpt09.txt", "w") as f:
    f.write("")
'''
#ELEVENTH PROBELM STATEMENT
'''
oldname="copy pr_chpt09.txt"
newname="renamed_by_python.txt"

with open (oldname) as f:
    fo=f.read()

with open (newname,"w") as f:
    f.write(fo)

#os.remove(oldname) #if you want to remove that old file
'''