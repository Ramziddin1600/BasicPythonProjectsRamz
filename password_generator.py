import string
import random

characters = list(string.ascii_letters + string.digits + string.punctuation)
length = int(input("Enter the length of your password: "))
if length < 8:
    print("Your password must be at least 8 characters.")
else:
    print(f'Your password is: {"".join(random.sample(characters, length))}')