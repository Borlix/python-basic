# 32. Sum of Digits: Find the sum of all digits in a given integer.

Num = int(input("Enter any Digit : "))
Digit = 0
sum = 0
while Num >= 1:
    Num =Num/10
    Digit+=1
    sum += Digit
print(sum)