'''
Created on Nov 12, 2018

@author: kroberts


PROBLEM: GUESS THE NUMBER

The program will first randomly generate a number unknown 
to the user. The user needs to guess what that number is. 
(In other words, the user needs to be able to input information.) 
If the user’s guess is wrong, the program should return some sort of 
indication as to how wrong (e.g. The number is too high or too low). 
If the user guesses correctly, a positive indication should appear. 
You’ll need functions to check if the user input is an actual number 
(if the input is not a number, the user should be able to try again), 
to see the difference between the inputted number and the randomly 
generated numbers, and to then compare the numbers.
'''


import random

def RandNum():
    num = random.randint(1,10)
    return num

def UserInput():
    user_guess = input('Guess a number between 1-10:')
    if user_guess.isnumeric():
        return user_guess
    else:
        print('Not a valid input, try again')
        return user_guess

def GuessNumber():
    rand_num = RandNum()
    user_input = UserInput()
    if user_input.isnumeric():
        if int(user_input) == rand_num:
            print('You guessed Correct!!!!')
        elif int(user_input) < rand_num:
            print('Your answer is too low')
        else:
            print('Your answer is too high')
    else:
        GuessNumber()
        
GuessNumber()    



