for n in range(10) : # range (start)
    print(n)

for m in range(10 , 20) : # range (start , stop)
    print(m)

for m in range(10 , 20 , 2) : # range (start , stop , step)
    print(m)

# WAP to print 1-100 using loop
i = 1
for m in range(0 ,101) : 
    if i <= 100 :
        print(i)
    i += 1

# WAP to print 100-1 using loop
i = 1
i = 100
for m in range(0 ,101) : 
    if i >= 0 :
        print(i)
    i -= 1

# WAP to print multiples of n

n = int(input("Enter your number : "))
for i in range (1,11) :
    print(i*n)