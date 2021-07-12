import random

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

items = [rock, paper, scissors]

rand_no = random.randint(0 , 2)

user_no = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if(user_no >= 0 and user_no <= 2):
    print(f"{items[user_no]}\n\nComputer chose:\n{items[rand_no]}\n")
    if(user_no == 0 and rand_no == 2):
        print("You win!")
    elif(user_no == 2 and rand_no == 0):
        print("You lose")
    elif(rand_no > user_no):
        print("You lose")
    elif(user_no > rand_no):
        print("You win!")
    else:
        print("It's a draw")
else:
    print("You typed an invalid number, you lose!")
