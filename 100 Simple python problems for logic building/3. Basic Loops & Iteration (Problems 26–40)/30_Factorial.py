# 30. Factorial: Calculate the factorial of a given number.

Num = int(input("Enter Num : "))
fac =1

while Num >= 1:
    fac *=Num
    Num-=1
print(fac)