import random

start = input("Do you want to play a number-guessing game? (y/n)").lower()
while start != "n":
    if start == "y":
        answer = random.randint(1, 100)
        counter = 1
        try:
            question = int(input("Guess the number Between 1 and 100?: "))
            while question < 1 or question > 100:
                question = int(input("Invalid number, please try again: "))
            while question != answer:
                if question > answer:
                    question = int(input("The number is too high, please try again: "))
                    counter += 1
                else:
                    question = int(input("The number is too low, please try again: "))
                    counter += 1

            print("Congratulations! You guessed the number!")
            print("You guessed it in " + str(counter) + " attempts!")
            start = input("Do you want to play again? (y/n)").lower()
        except ValueError:
            print("Invalid input, please try again!")


    else:
        start = input("Invalid choice, please try again? (y/n)").lower()

print("Thank you for playing!")