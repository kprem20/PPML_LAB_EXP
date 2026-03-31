a, b = 1, 1
even_sum = 0

for _ in range(100): 
    if b > 1000:
        break
    if b % 2 == 0:
        even_sum += b
    a, b = b, a + b

print("Even Valued Sum = " ,even_sum)
