# The Perfect Guess
'''
Write a program that generates random no. and asks user to guess it
If the player's guess is higher than the actual no. then the program displays "lower number please" and if the guess is too low then the program displays "higher number please"

When the user arrives at the correct guess, the program displays number of guesses the user took to arrive at the number.
'''
from pickle import TRUE
import random

count = 0
random = random.randint(1,100)

number = int(input("Guess the number between 1 to 100: "))
while TRUE:
    if(number > random):
        count += 1
        number = int(input("lower number please: "))
        continue
    elif(number < random):
        count += 1
        number = int(input("higher number please: "))
        continue
    else:
        print("Finally the right number!!")
        print(f"Number of guesses you needed = {count}")
        break