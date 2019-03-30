import random 
from random import randint 
game = "y"
while game == "y":    
    num = randint(1, 10)
    guess = int(input("guess a number between 1 - 10: "))
    while guess != num:
        if num > guess:
            state = "too low"
        else:
            state = "too high"
        print(f"sorry {state}")
        guess = int(input("Try again "))
    print(f"nice one - {num} was it")
    game = input("play again y/n?: ")
print("Thank you for playing!")    