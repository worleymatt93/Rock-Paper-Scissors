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

move_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

if user_choice >= 0 and user_choice <= 2:
    print(f"{move_images[user_choice]}\nComputer chose:\n {move_images[computer_choice]}")

    if user_choice == 0 and computer_choice == 2:
        print("You win")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose")
    elif user_choice < computer_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win")
    elif user_choice == computer_choice:
        print("You tie")

else:
    print("You chose none. You forfeit!")
    