a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

dis= b**2 - 4*a*c

if dis > 0:

    root1 = (-b + (dis)**0.5) / (2 * a)
    root2 = (-b - (dis)**0.5) / (2 * a)
    print(f"The real roots are: {root1} and {root2}")
elif dis == 0:
  
    root = -b / (2 * a)
    print(f"There is one real root: {root}")
else:
    print("The equation has no real roots.")
