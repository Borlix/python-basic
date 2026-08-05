# 5. Swap Variables: Swap the values of two variables without using a third variable.

a =int(input("Enter num for a : "))
b =int(input("Enter num for b : "))
print(f"Before value swap : a ={a},b ={b}")
a = a + b
b = a - b
a = a - b
print(f"After value swap : a ={a},b ={b}")
