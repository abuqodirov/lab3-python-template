# Lab 3 - Exercise 5: Greatest common divisor (Euclid's method)
#
# Read two positive integers x and y, then compute and print their gcd.
#
# Euclid's method:
#   1. Let M be the larger and m the smaller of x and y.
#   2. r = M % m
#   3. If r == 0, m is the gcd.
#   4. Otherwise set M = m, m = r, and go back to step 2.
#
# Example: x = 15, y = 40
#   40 % 15 = 10, 15 % 10 = 5, 10 % 5 = 0  ->  gcd is 5

# Write your code below this line

