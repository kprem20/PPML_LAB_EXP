a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))
c=int(input("Enter the 3rd number: "))
print(f"{a}" if (a>b and a>c ) else print(f"{b}" if (b>c) else print(f"{c}")))