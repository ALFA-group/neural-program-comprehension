import random
choice = input("Enter your guess between 1 and 10: ")
if (choice + random.randint(1, 10))%10 == random.randint(1, 10):
    print("You guessed right!")
else:
    print("Tough luck.")