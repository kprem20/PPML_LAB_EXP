eng=float(input("Enter english marks: "))
math=float(input("Enter maths marks: "))
chem=float(input("Enter chem marks: "))
bio=float(input("Enter bio marks: "))
phy=float(input("Enter  phy marks: "))
sum = eng+math+chem+bio+phy
per=(sum/250)*100
print ("Percentage is= ",per)
if per>=90:
    print("Grade= O")
elif per >=80 and per<90:
    print("Grade= E")
elif per >=70 and per<80:
    print("Grade= A")
elif per >=60 and per<70:
    print("Grade= B")
elif per >=50 and per<60:
    print("Grade= C")
else:
    print("Fail ")
