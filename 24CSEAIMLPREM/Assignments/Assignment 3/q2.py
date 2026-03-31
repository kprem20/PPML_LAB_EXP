x= int(input("Enter a number: "))
fact=1
if x<0:
    print("It is negative number")
elif x==0:
    print("The factorial off",x,"is",fact)
else:
    for i in range(1,x+1):
        fact=fact*1
    print("The factorial of ",x,"is" ,fact)