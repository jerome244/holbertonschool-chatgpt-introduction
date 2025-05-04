#!/usr/bin/python3
import sys

# Function Description:
# This function calculates the factorial of a given number n using recursion.
# The factorial of a number n (denoted as n!) is the product of all positive integers less than or equal to n.

# Parameters:
# n (int): The number for which the factorial needs to be calculated. Must be a non-negative integer.

# Returns:
# int: The factorial of the input number n. If n is 0, the result is 1 (as 0! = 1 by definition).

def factorial(n):
    if n == 0:
        return 1  # Base case: factorial of 0 is 1
    else:
        return n * factorial(n-1)  # Recursive case: n! = n * (n-1)!

# The following lines get the input from command line arguments, calculate the factorial of the number, and print the result.
f = factorial(int(sys.argv[1]))
print(f)
