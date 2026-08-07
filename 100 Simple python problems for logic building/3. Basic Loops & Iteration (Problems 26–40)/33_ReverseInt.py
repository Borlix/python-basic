# 33. Reverse an Integer: Reverse the digits of an integer (e.g., 123 becomes 321).

num = int(input("Enter Num : "))
reverse_num = 0
while num > 0 :
    last_num = num%10
    reverse_num = (reverse_num*10)+last_num
    num = num // 10
print(reverse_num)