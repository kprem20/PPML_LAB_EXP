def si(p,t,r):
    return (p*t*r)/100
p=int(input("Enter principal value: "))
t=int(input("Enter time: "))
r=int(input("Enter rate "))
print("The Simple Interest Value is: ",si(p,t,r))