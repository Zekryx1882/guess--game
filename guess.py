# guess.py
import random

def main():
    print("Welcome to Guess the Number!")
    number = random.randint(1, 10)
    guess = None
    while guess != number:
        guess = int(input("Guess a number 1–10: "))
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
    print("You got it!")

if __name__ == "__main__":
    main()
