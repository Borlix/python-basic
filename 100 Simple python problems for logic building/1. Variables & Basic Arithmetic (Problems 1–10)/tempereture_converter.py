# 3. Celsius to Fahrenheit: Convert a temperature from Celsius to Fahrenheit.

c = float(input("Input Celsius : "))
f = (c * (9/5)) + 32
print(f"Fahrenheit is {f}degree")

# upgraded version :  Celsius to Fahrenheit and Fahrenheit to Celsius :

print("Enter 1, for  Celsius to Fahrenheit \nEnter 2, for Fahrenheit to Celsius  ")
v = int(input("Enter what you want! : "))
if v == 1 :
    c = float(input("Input Celsius : "))
    f = (c * (9/5)) + 32
    print(f"Fahrenheit is {f}degree")
elif v == 2 :
    f = float(input("Input Fahrenheit : "))
    c = (f - 32) * (5/9)
    print(f"Celsius is {c}degree")
else :
    print("ERROR , Type 1 or 2")