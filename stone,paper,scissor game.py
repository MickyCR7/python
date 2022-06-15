'''

THIS IS A BASIC STONE PAPER SCISSOR GAME
USING PYTHON PROGRAMMIMG 
WHICH IS PLACED AGAINST THE COMPUTER

!!!!  ENJOY THE GAME  !!!!

'''


import os
import random #random is used so that the compiler can take random values


def gameWin(comp, player):
    # WHENN THE PLAYER AND COMPUTER CHOSES THE SAME OPTION
    if comp==player:
        return None

    #WHAT HAPPENS WHEN THE PLAYER CHOOSES STONE
    
    elif comp=='stone':
        if player=='paper':
            return True
        elif player=='scissor':
            return False

    #WHAT HAPPENS WHEN THE PLAYER CHOOSES PAPER

    elif comp=='paper':
        if player=='scissor':
            return True
        elif player=='stone':
            return False

    #WHAT HAPPENS WHEN THE PLAYER SCHOOSES SCISSOR

    elif comp=='scissor':
        if player=='stone':
            return True
        elif player=='paper':
            return False

print("!!!!!!!!!!   COMPUTER'S TURN: STONE(stone) PAPER(paper) or SCISSOR(scissor)   !!!!!!!!!!\n")
randNo= random.randint(1,3) #will provide random integres from 1 2 3
if randNo==1:
    comp= 'stone'
elif randNo== 2:
    comp='paper'
elif randNo==3:
    comp= 'scissor'

player= input("!!!!!!!!!!   YOUR TURN: STONE(stone) PAPER(paper) or SCISSOR(scissor)   !!!!!!!!!! \n")

a=gameWin(comp, player)

print(f"THE COMPUTER CHOSE {comp}")
print(f"YOU CHOSE {player}")

if a== None:
    print("ITS A TIE")
elif a:
    print("YOU WON AGAINST THE COMPUTER,CONGRATS!!!!!")
else:
    print("YOU LOST AGAINST THE COMPUTER,TRY AGAIN!!!!!")