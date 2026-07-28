#sum of two numbers.

a = int(input("Enter the num a: "))
b = int(input("Enter the num b: "))
sum = a+b
print (sum)

#Area of a square.

length = float(input("Enter the length of any side of square: "))
Area = length*length
print(f"Area of a square is : {Area}")

#Print Average of two numbers.

num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))

Avg = (num1+num2)/2

print(f"Average of two numbers is :{Avg}")

# WAP to input 2 numbers a and b , print True if a is greater or equal to b , if not print false.
a = int(input("Enter a number a : "))
b = int(input("Enter a number b : "))

is_greater = (a>=b)
print(is_greater)
if is_greater == True:
        print("Yes , a is greater or equal to b")
else:
        print("No , a is less then b")