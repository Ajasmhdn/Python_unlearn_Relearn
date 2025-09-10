n=int(input("Enter a Number: "))
if n<=1:
    print("Not a Prime Number")
else:
    for num in range(2,n+1):
        flag=0
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                flag=1
                break
        if flag==0:
            print(num,end=" ")
                
