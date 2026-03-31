n=int(input("Enter a digit: "))
count=0
for i in range(1,10):
    if(n%i==0):
        count=count+1
if(count==2):
        print("The Number is Prime" )
else:
      print("The number is not prime")
       