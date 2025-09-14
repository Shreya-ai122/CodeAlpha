import random

def number_guesser():
    low = int(input("Enter lower range: "))
    high = int(input("Enter upper range: "))
    number = random.randint(low, high)

    while True:
        guess = int(input("Guess the number: "))
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("You got it! 🎉")
            break

number_guesser()
