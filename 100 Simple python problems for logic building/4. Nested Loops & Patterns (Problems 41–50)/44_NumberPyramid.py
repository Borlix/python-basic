# 44. Number Pyramid: Print a pyramid where row i contains the number i repeated i times.
num = int(input("Enter a number : "))
for i in range (0,num+1):
    print(" "*(num -i)+f"{num} "*i)
    