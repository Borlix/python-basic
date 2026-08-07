# 29. Sum of N Numbers: Find the sum of the first N natural numbers.

Num = int(input("Enter Num : "))
i = 1
Sum = 0
while i <= Num:
        Sum= Sum+i
        i+=1
print(f"Sum of N natural number is : {Sum}") 