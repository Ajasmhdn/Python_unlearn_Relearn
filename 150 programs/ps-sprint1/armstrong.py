# Calculating Armstrong Numbers
# Difficulty: Easy
# Topics: Basic Programming, Number Theory
# Description: Write a program to check if a number is an Armstrong number.
# Example:
# Input: number = 153
# Output: Armstrong Number
# Explanation: 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.

num=int(input("Enter a Number:"))
armstrong=0
temp=num
while(num>0):
    rem=num%10
    armstrong=armstrong+rem**3
    num=num//10
if armstrong==temp:
    print("Armstrong")
else:
    print("Not Armstrong")