# 34. Palindrome Number: Check if an integer reads the same backward as forward.

num = int(input("Enter Num :"))
orgnum = num
reversed_num = 0
while num > 0 :
    last_num = num%10
    reversed_num = (reversed_num*10) + last_num
    num = num // 10
if orgnum == reversed_num :
    print("Yes, Its a Palindrome Number")
else :
    print("No, Its not a palindrome Number")
