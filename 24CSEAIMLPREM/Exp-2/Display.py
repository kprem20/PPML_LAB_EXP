
int_in = int(input("Enter an integer: "))
print(f"Datatype of {int_in} is: {type(int_in)}")
str_in = input("Enter a string: ")
print(f"Datatype of '{str_in}' is: {type(str_in)}")
float_in = float(input("Enter a float: "))
print(f"Datatype of {float_in} is: {type(float_in)}")
bool_in = bool(input("Enter a boolean (True or False): ").strip().lower() == 'true')
print(f"Datatype of {bool_in} is: {type(bool_in)}")
complex_in = complex(input("Enter a complex number (e.g., 1+2j): "))
print(f"Datatype of {complex_in} is: {type(complex_in)}")

