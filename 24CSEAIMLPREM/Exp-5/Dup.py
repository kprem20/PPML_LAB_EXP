
num = []
n = int(input(" Enter a group of numbers : "))
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    num.append(num)
unique_num = list(set(num))
unique_num.sort()
print("Numbers after removing duplicates and sorting:", unique_num)
















                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               