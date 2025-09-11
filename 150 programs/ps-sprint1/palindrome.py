# Identifying Palindromes
# Difficulty: Easy
# Topics: Basic Programming, String Manipulation
# Description: Write a program to check if a string or number is a palindrome.
# Example:
# Input: string = "radar"
# Output: Palindrome
# Explanation: "radar" reads the same backward as forward.


str1=input("Enter the String:")
str2=str1[::-1]
if(str1==str2):
    print("Palindrome")
else:
    print("Not a Palindrome")