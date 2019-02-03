# Made By ItzFrostbiteTv

import random

number = random.randint(1, 10)
tries = 1

name = input("What Is Your Username: ")
print("Hello", name, "Would you like to play a game [Y/N]")
game = input()

if game == "n":
    print("Ok... Bye")

if game == "N":
    print("Ok... Bye")

if game == "y":
    print("Im thinking of a number 1 to 10")
    guess = int(input("Take a guess: "))

if game == "Y":
    print("Im thinking of a number 1 to 10")
    guess = int(input("Take a guess: "))

if guess > number:
        print("Guess Lower")
if guess < number:
    print("Guess Higher")

while guess != number:
    tries += 1
    guess = int(input("Try Again: "))
    if guess < number:
        print("Guess Higher")
    if guess > number:
        print("Guess Lower")
if number == guess:
	print("You got it and it only toke", tries, "tries!")
	print("Push any key to continue")
	bye = input()