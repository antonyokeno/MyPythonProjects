rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
user_choice=input("What do you choose?Type Rock, Paper or Scissors\n").lower()
options=["rock", "paper", "scissors"]
computer_choice =random.choice(options)

print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")
if user_choice==computer_choice:
    print("its a draw!")
elif user_choice=="rock":
    if computer_choice=="scissors":
        print("You Win!")
    else:
        print("You lose")
elif user_choice == "paper":
    if computer_choice=="rock":
        print("You Win!")
    else:
        print("You lose")
elif user_choice == "scissors":
    if computer_choice=="paper":
        print("You Win!")
    else:
        print("You lose")
else:
    print("Undefined")