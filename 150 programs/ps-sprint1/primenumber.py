# 2. Checking for Prime Numbers
# Difficulty: Easy
# Topics: Basic Programming, Number Theory
# Description: Write a program to determine if a number is prime.
# Example:
# Input: number = 7
# Output: Prime
# Explanation: 7 has no divisors other than 1 and itself, so it is a prime number.

num=int(input("Enter a Number: "))
if num<=1:
    print("Not a Prime Number")
else:
    flag=0
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            flag=1
            break
    if flag==0:
        print("Prime Number")
    else:
        print("Not a Prime Number")