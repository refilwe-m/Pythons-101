''' 1. Squares List
Given a number n, create a list of the squares of numbers from 1 to n.
Example: n = 5 → [1, 4, 9, 16, 25]''' 
def sum_of_squares(n):
    return [i**2 for i in range(1,n+1)]

print((sum_of_squares(5))==[1, 4, 9, 16, 25])
