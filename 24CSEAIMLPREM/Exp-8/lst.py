def sumlist(lst):
    total = 0
    for num in lst:
        total += num
    return total

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Sum of the elements:", sumlist(numbers))
