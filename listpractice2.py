#WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)
list1=[1,2,1]
list2=[1,2,3]

list3=list1.copy()
list1.reverse()
if list1==list3:
    print("Palindrome")
else:
    print("Not a Palindrome")