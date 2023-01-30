#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
limit=3
ps=0
cs=0
while True:
    player_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif player_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
        ps+=1
    else:
        print("Paper covers rock! You lose.")
elif player_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
        ps+=1
    else:
        print("Scissors cuts paper! You lose.")
elif player_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
        cs+=1
    if ps==limit or cs==limit:
        break
if ps<cs:
    print("player wins")
else:
    print("computer wins")


# In[ ]:


from random import randint
choice=['rock','paper','scissor']
player=input(f"choose from {choice}").lower()
comp=choice[randint(0,2)]

