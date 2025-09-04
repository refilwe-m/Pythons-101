''' 1. Squares List
Given a number n, create a list of the squares of numbers from 1 to n.
Example: n = 5 → [1, 4, 9, 16, 25]''' 
def sum_of_squares(n):
    return [i**2 for i in range(1,n+1)]

print((sum_of_squares(5))==[1, 4, 9, 16, 25])

"""Unique Words
Ask for a sentence, split it into words, and print a list of unique words."""

"""Find Max and Min
Ask the user for numbers separated by spaces. Convert them into a list of integers and print the largest and smallest numbers."""


'''Word Frequency
Ask for a sentence and count how many times each word appears. Store results in a dictionary.
Example:
"the cat and the dog" → { "the": 2, "cat": 1, "and": 1, "dog": 1 }'''