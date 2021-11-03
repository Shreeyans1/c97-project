import random

number = random.randint(1,9)
chances = 0

while chances <5:
    guess = int(input("enter a number between 1 to 9: "))
    if guess == number:
        print("YOU WON!")
        break
    else:
        print("try again")
    chances += 1
if not chances <5:
    print("YOU LOSE! the number is ",number)
