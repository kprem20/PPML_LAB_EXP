arr=[]
x= int(input("Enter the no. of elements: "))
for i in range (x):
    m=int(input("Enter the element: "))
    arr.append(m)
for j in range (len(arr)-1):
    for k in range(len(arr)-j):
        if arr[k]>arr[k+1]:
            arr[k],arr[k+1]=arr[k+1],arr[k]
print("The Sorted array is ")
print(arr)
second_largest=arr[-2]
second_smallest=arr[1]
print("Second Largest element is ",second_largest)
print("Second Smallest element is ",second_smallest)

