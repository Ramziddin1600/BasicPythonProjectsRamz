import random

inquiry = input("Roll the dice? (y/n)").lower()
while inquiry != "n":
    if inquiry == "y":
        print(f"({random.randint(1, 6)}, {random.randint(1, 6)})")
        inquiry = input("Roll the dice? (y/n)").lower()
    else:
        print('Invalid input, try again.')
        inquiry = input("Roll the dice? (y/n)").lower()
    if inquiry == "n":
        print("Process Terminated")
        break
