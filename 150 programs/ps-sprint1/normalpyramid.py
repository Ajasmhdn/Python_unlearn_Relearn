# Crafting Star Patterns
# Difficulty: Easy
# Topics: Basic Programming, Patterns
# Description: Write a program to create different star patterns (e.g., pyramid, diamond).
# Example:
# Input: patternType = "pyramid", height = 5
# Output:

#     *
#    ***
#   *****
#  *******
# *********
# Explanation: A pyramid pattern with a height of 5 is generated.


n=int(input("Enter the size of the pyramid"))
for i in range(1,n+1):
    #print spaces
    print(" "*(n-i),end="")
    #print stars
    print("*"*(2*i-1))
    