# Summing Digits of a Number
# Difficulty: Easy
# Topics: Basic Programming, Mathematical Computations
# Description: Write a program to calculate the sum of digits of a number.
# Example:
# Input: number = 1234
# Output: 10
# Explanation: The sum of the digits 1 + 2 + 3 + 4 = 10.

num=int(input("Enter the number : "))
sums=0
while(num>0):
    rem=num%10
    sums+=rem
    num=num//10
print("The sum of digits is ",sums)

   
    