# 20. Multiple of 5 and 11: Check if a number is divisible by both 5 and 11.

num = int(input("Enter num : "))

if num%5 == 0 and num%11 == 0 :
    print(f"Yes the number {num} is divisible by both 5 and 11 ")
else :
    print(f"No the number {num} is not divisible by both 5 and 11 ")