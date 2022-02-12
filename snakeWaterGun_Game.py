# PROJECT 1: Snake, Water, Gun game

import random #importing module random to generate random numbers

# different choices that the computer and the user have
choice = ['s','w','g']

# intitally both user and the computer both have 0 points
user = 0
comp = 0

# to give the user the flexibility with number of plays
n = input("How many rounds do you want to play: ")

for i in range(n):
    random_no = random.randrange(0,2) #randrange gives a new random no. every loop, randint doesn't
    user_choice = input("Choose Snake(s) or Water(w) or Gun(g): ").lower() #lower() reduces errors
    comp_choice = choice[random_no] #using random index for choice 
    print(comp_choice) #printing the random choice that comp makes, for fair play

    #comparing and giving points to the winner
    if((user_choice=='s' and comp_choice=='w') or (user_choice=='w' and comp_choice=='g') or (user_choice=='g' and comp_choice=='s')):
        user += 1
    elif((user_choice=='w' and comp_choice=='s') or (user_choice=='g' and comp_choice=='w') or (user_choice=='s' and comp_choice=='g')):
        comp += 1
    elif(user_choice!='s' and user_choice!='w' and user_choice!='g'):
        print("Invalid choice will cost you a point")
        comp += 1

    
# comparing the total points of the computer and the user and displaying the decision
if(comp > user):
    print("Computer wins")
elif(comp < user):
    print("You Win")
else:
    print("It's a draw")
