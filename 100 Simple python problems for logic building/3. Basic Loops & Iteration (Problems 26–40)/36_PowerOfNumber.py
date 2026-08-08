# 36. Power of a Number: Find the value of x raised to the power of y using a loop.

x = int(input("Enter value for Num : "))
y = int(input("Enter value for Power : "))

while y > 1:
    x = x*x
    y -=1
print(x)