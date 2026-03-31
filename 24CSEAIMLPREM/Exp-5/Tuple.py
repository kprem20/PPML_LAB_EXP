# Define the collections
list = ["apple", "banana", "cherry"]
tuple = (1, 2, 3, 4)
set = {"red", "green", "blue"}
dict = {"name": "Alice", "age": 25, "city": "Paris"}

print("Looping over list:")
for item in list:
    print(item)

print("Looping over tuple:")
for item in tuple:
    print(item)

print("Looping over set:")
for item in set:
    print(item)

print("Looping over dictionary (keys and values):")
for key, value in dict.items():
    print(f"{key} -> {value}")
