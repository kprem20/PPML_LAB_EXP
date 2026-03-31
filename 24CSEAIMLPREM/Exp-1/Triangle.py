a=float(input("Enter side 1= "))
b=float(input("Enter side 2= "))
c=float(input("Enter side 3= "))
peri=a+b+c
semi=peri/2
area=(semi*(semi-a)*(semi-b)*(semi-c))
print("Area of Triangle ",area)
print("Perimeter of Triangle ",peri)