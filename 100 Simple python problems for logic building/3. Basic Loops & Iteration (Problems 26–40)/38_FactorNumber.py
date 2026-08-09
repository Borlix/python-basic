# 38. Find Factors: Print all factors of a given integer.

num = int(input("Enter number : "))

print(f"Factor of a number {num} is : ")
for i in range(1 , num+1) :
    if num%i == 0 :
        print(i)
