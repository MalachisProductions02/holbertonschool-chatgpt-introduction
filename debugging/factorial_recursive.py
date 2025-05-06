#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n using recursion.

    Parameters:
    n (int): The number to compute the factorial of. Must be a non-negative integer.

    Returns:
    int: The factorial of the input number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Parse the first command-line argument as an integer and compute its factorial
f = factorial(int(sys.argv[1]))

# Print the result
print(f)