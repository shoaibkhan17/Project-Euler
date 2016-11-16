# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(number):
    number = str(number)
    for i, char in enumerate(number):
        if char != number[-i-1]:
            return False
    return True

largestNumber = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        if is_palindrome(i * j):
            if largestNumber < i * j:
                largestNumber = i * j

print(largestNumber)