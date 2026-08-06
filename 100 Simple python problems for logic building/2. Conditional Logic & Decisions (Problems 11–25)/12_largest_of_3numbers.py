# 13. Largest of Three: Find the largest of three numbers using if-elif-else.
a = int(input("Enter value of a : "))
b = int(input("Enter value of b : "))
c = int(input("Enter value of c : "))

if a > b and a > c :
    print(f"{a} is Largest ")
elif a < b and b > c :
    print(f"{b} is Largest ")
else :
    print(f"{c} is Largest ")