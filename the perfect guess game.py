import os
import random

randNumber=random.randint(1,100)
#print(randNumber)
userGuess=0
guesses=0
while(userGuess!=randNumber):
    userGuess=int(input("**** Enter your guess: **** \n"))
    guesses+=1
    if (userGuess==randNumber):
        print("Congratulations, you guessed the right number!")
    else:
        if(userGuess>randNumber):
            print("Try again and enter a Smaller number")
        else:
            print("Try again and enter a Larger number")


print(f"THE NUMBER OF GUESSES U TOOK TO REACH THE CORRECT NUMBER IS {guesses}")
with open("hiscore.txt","r") as f:
    hiscore=int(f.read())

if(guesses<hiscore):
    print("CONGRATULATIONS, YOU HAVE JUST BROKEN THE HIGHSCORE")
    with open("hiscore.txt","w") as f:
        f.write(str(guesses))








