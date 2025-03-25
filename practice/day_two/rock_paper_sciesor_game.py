import random

user = int(input("What do you want to chose? \n"))
computer = random.randint(0, 2)

if user >= 3 or user < 0:
    print("Invalid; You Lose!")
elif user == 0 and computer == 2:
    print("You Win!")
elif computer == 0 and user == 2:
    print("Computer Win!")
elif computer > user:
    print("Computer win!")
elif user > computer:
    print("You Win!")
elif computer == user:
    print("Draw! :(")
