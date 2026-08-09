# 40. Until Zero: Keep accepting numbers from the user until they enter 0, then show the total sum. [1, 2, 3, 4, 5]

num = 1
b = num
total_sum = num
while num != 0:
    num = int(input("Enter number :"))
    total_sum += num
print(f"Total Sum = {total_sum - b}")