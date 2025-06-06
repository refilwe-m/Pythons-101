# Guessing Game

## Number guessing game in Python

### How the Game Works?

To understand how the number guessing game functions, let’s walk through two practical scenarios. These examples demonstrate how narrowing down the range intelligently—similar to a binary search—can help guess the number efficiently.

#### Example 1: Guessing in a Range from 1 to 100

Suppose the user defines the range from 1 to 100, and the system randomly selects 42 as the target number. The guessing process might look like this:

- Guess 1: 50 → Too high
- Guess 2: 25 → Too low
- Guess 3: 37 → Too low
- Guess 4: 43 → Too high
- Guess 5: 40 → Too low
- Guess 6: 41 → Too low
- Guess 7: 42 → Correct!
- Total Guesses: 7

#### Example 2: Guessing in a Range from 1 to 50

Now consider a smaller range, from 1 to 50, with the same target number 42. Here's how the guesses might proceed:

- Guess 1: 25 → Too low
- Guess 2: 37 → Too low
- Guess 3: 43 → Too high
- Guess 4: 40 → Too low
- Guess 5: 41 → Too low
- Guess 6: 42 → Correct!
- Total Guesses: 6

> Note: In both examples, the user intelligently uses the binary search strategy, halving the guessing range with each attempt.

## Algorithm

- Accept lower and upper bounds from the user.
- Generate a random number in the selected range.
- Calculate the maximum allowed guesses using the binary search formula.
- Run a loop to take user guesses:
- If the guess is too high, print: "Try Again! You guessed too high."
- If the guess is too low, print: "Try Again! You guessed too small."
- If the guess is correct, print: "Congratulations!" and exit the loop.
- If the user runs out of chances, display the correct number and a message: "Better Luck Next Time!"