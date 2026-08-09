# 39. Armstrong Number: Check if a 3-digit number equals the sum of the cubes of its digits.

num = int(input("Enter 3-Digit number : "))

i = num
cube = 0

while i > 0 :
    digit = i % 10
    cube += digit**3
    i = i//10
if cube == num :
    print(f"{num} is Armstrong number.")
else :
    print(f"{num} is not Armstrong number.")