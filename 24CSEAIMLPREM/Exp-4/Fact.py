
def fact(n):
    res= 1
    i = 1
    while i <= n:
        res *= i
        i += 1
    return res
num = int(input("Enter a number : "))
print(f"{num}! = {fact(num)}")
