#ChatGPT
import random
import math

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # Accept range from user
    lower = int(input("Enter the lower bound: "))
    upper = int(input("Enter the upper bound: "))
    
    # Generate a random number within the given range
    number_to_guess = random.randint(lower, upper)
    
    # Calculate maximum allowed guesses using binary search formula
    max_guesses = math.ceil(math.log2(upper - lower + 1))
    print(f"You have {max_guesses} chances to guess the number between {lower} and {upper}.")
    
    attempts = 0

    while attempts < max_guesses:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1
        
        if guess == number_to_guess:
            print(f"Congratulations! You guessed the number {number_to_guess} correctly in {attempts} attempts.")
            break
        elif guess < number_to_guess:
            print("Try Again! You guessed too small.")
        else:
            print("Try Again! You guessed too high.")
    else:
        print(f"Better Luck Next Time! The number was {number_to_guess}.")

# Run the game
number_guessing_game()