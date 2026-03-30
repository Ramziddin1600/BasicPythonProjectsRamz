import random

choices = ("r", "p", "s")

start = input("Do want to play rock paper scissors? (y/n)").lower()
while start != "n":
    if start == "y":
        computer_choice = random.choice(choices)
        user_choice = input("Rock, paper, scissors? (r/p/s): ")
        while user_choice not in choices:
            user_choice = input("Invalid input, please try again. (r/p/s): ").lower()

        computer_choice = random.choice(choices)
        while computer_choice == user_choice:
            print("Whoa we have the same choice!")
            computer_choice = random.choice(choices)
            user_choice = input("Let's try again. (r/p/s)").lower()

        if computer_choice == "r" and user_choice == "p":
            print("I chose " + computer_choice)
            print("You win!")
            start = input('Do you want to play again? (y/n)').lower()
        elif computer_choice == "p" and user_choice == "r":
            print("I chose " + computer_choice)
            print("You lose!")
            start = input('Do you want to play again? (y/n)').lower()
        elif computer_choice == "s" and user_choice == "r":
            print("I chose " + computer_choice)
            print("You win!")
            start = input('Do you want to play again? (y/n)').lower()
        elif computer_choice == "r" and user_choice == "s":
            print("I chose " + computer_choice)
            print("You lose!")
            start = input('Do you want to play again? (y/n)').lower()
        elif computer_choice == "p" and user_choice == "s":
            print("I chose " + computer_choice)
            print("You win!")
            start = input('Do you want to play again? (y/n)').lower()
        elif computer_choice == "s" and user_choice == "p":
            print("I chose " + computer_choice)
            print("You lose!")
            start = input('Do you want to play again? (y/n)').lower()

    else:
        print("Invalid input, please try again.")

print("Thank you for playing!")
