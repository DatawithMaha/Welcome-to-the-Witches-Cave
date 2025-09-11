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

weapons_of_choice = [ rock, paper , scissors]

user_choice =int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if 0<= user_choice <=2:
    print(weapons_of_choice[user_choice])

print("Computer chose: ")

computer_random_pick = random.randint(0,2)
print(weapons_of_choice[computer_random_pick])

if user_choice == 0 and computer_random_pick == 2:
    print("You win")
elif user_choice == 2 and computer_random_pick ==1:
    print("You win")
elif user_choice == 1 and computer_random_pick == 0:
    print("You win")
elif user_choice == computer_random_pick:
    print("Its a Draw")
else:
    print("You lose")




