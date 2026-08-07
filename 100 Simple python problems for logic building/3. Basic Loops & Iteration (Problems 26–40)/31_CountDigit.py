# 31. Count Digits: Count the total number of digits in an integer.

Num = int(input("Enter any Digit : "))
Digit = 0
while Num >= 1:
    Num =Num/10
    Digit+=1
print(Digit)