import random

def guesses(range, tries):
    random_number = random.randint(1, range)
    guess = 0
    count = 0

    while guess != random_number and count < tries:
        count += 1
        guess = int(input("Guess the number: "))
        if guess == random_number:
            print("yay.. You won!")
        elif count == tries:
            print("Ohh.. sorry you lost.")
            print("Computer choose number:", random_number)
        elif guess > random_number:
            print("You are above the number!")
        elif guess < random_number:
            print("You are lower the number!")


range = int(input("Range: "))
tries = int(input("Enter the number of try: "))
guesses(range, tries)
