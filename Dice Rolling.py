'''
Created on Nov 12, 2018

@author: kroberts


PROBLEM: DICE ROLLING SIMULATOR

The Goal: Like the title suggests, this project involves writing a 
program that simulates rolling dice. When the program runs, it will 
randomly choose a number between 1 and 6. (Or whatever other integer 
you prefer — the number of sides on the die is up to you.) The program 
will print what that number is. It should then ask you if you’d like to 
roll again. For this project, you’ll need to set the min and max number 
that your dice can produce. For the average die, that means a minimum of 
1 and a maximum of 6. You’ll also want a function that randomly grabs a 
number within that range and prints it.
'''


import random

def DiceRolling(n):
    #Dice Roll
    print(random.randint(1,n))
    
    #Ask user if they would like to roll again
    roll_again = input('Would you like to roll again? (yes/no)')
    
    #Logic statements depending on what the user wants to do
    if roll_again.lower() == 'no':
        print('Thanks for rolling!')
        
    else:
        dice = input('What size dice would you like to use? (any number)')
        DiceRolling(int(dice)) 
  
        
        
        
    

DiceRolling(6)
