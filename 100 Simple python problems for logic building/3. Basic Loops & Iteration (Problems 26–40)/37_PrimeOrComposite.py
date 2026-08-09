# 37. Prime Number Check: Check if a given number is prime or composite.

num = int(input("Enter Number : "))

if num <=1 :
    print(f"{num} is nither prime nor composite.")
else :
    is_prime = True
    i = 2
    while i * i <= num :
        if i%num == 0 :
            is_prime=False
            break
        i +=1
if is_prime :
    print(f"{num} is prime!")
else :
    print(f"{num} is composite!")