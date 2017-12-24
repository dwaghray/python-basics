import random

# allows the player to guess a number randomly chosen by the computer
# the computer provides hints about their guess ("too high", "too low")

print("\tWelcome to the number guessing game!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

cpu_number = random.randrange(1, 101)
guess = eval(input("Take a guess: "))
tries = 1

while (guess != cpu_number):
    if (guess > cpu_number):
        print("Too high!")
    else:
        print("Too low!")

    guess = eval(input("Guess again: "))
    tries += 1

print("You guessed it! The number was", cpu_number)
print("And it only took you", tries, "tries!\n")
