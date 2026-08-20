# 45. Prime Range: Print all prime numbers between two given numbers (e.g., 20 to 50).
num1 = int(input("Enter number for starting value : "))
num2 = int(input("Enter number for ending value : "))

print(f"Prime Numbers between {num1} and {num2}")

for num in range(num1,num2 +1):
    if num > 1:
        is_prime = True

        i = 2
        while i*i <= num:
            if num%i==0:
                is_prime=False
                break
            i+=1
        if is_prime:
            print(num,end=" ")
