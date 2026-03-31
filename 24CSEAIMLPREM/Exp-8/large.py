def large(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c
a=int(input("Enter a value: "))
b=int(input("Enter b value: "))
c=int(input("Enter c value: "))
print("The largest number is :",large(a,b,c))