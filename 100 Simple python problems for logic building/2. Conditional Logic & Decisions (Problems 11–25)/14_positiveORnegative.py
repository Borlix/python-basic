# 14. Positive or Negative: Check if a number is positive, negative, or zero.

num = int(input("Enter num : "))

if num==0 :
    print("Zero")
elif num > 0 :
    print(f"{num} is Positive number.")
elif num < 0 :
    print(f"{num} is Negative number.")
else :
    print("ERROR!, undefine character")