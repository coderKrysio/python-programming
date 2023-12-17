import random

print("Welcome to the rock paper scissor game\n")
# creating game options
options = ["rock", "paper", "scissor"]

# looping variable
want_to_continue = True

# continue till user wants to play
while(want_to_continue):
    # computer selecting its choice
    computer_choice = random.randint(0, 2)

    # user selecting its choice
    print("------")
    print("Choice:\n1 - Rock\n2 - Paper\n3 - Scissor")
    user_choice = int(input("Enter choice no: ")) - 1

    # if valid choice
    if user_choice in range(3):
        # Printing players choices
        print("------")
        print("User Choice: " + options[user_choice])
        print("Computer Choice: " + options[computer_choice])

        # checking conditions
        if user_choice == 0 and computer_choice == 1 or user_choice == 1 and computer_choice == 2 or user_choice == 2 and computer_choice == 0:
            print("*** COMPUTER WINS ***")
        elif user_choice == 0 and computer_choice == 2 or user_choice == 1 and computer_choice == 0 or user_choice == 2 and computer_choice == 1:
            print("*** USER WINS ***")
        elif user_choice == computer_choice:
            print("*** DRAW ***")

        # continuation query
        print("------")
        want_to_continue = input("Do you want to continue (y/n): ") == 'y'
    else:
        # if invalid choice then reenter the value
        print("Invalid Choice")
        continue

# game end
print("--- Thank You ---")