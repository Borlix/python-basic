# WAP to print num from 1 to 100

num = 1
while num <= 100 :
    print(num)
    num += 1

# WAP to print num 100 to 1

num = 100
while num >= 1 :
    print(num)
    num -= 1

# WAP to print multipical table of n

n = int(input("Enter a num : "))
i = 1
while i <= 10 :
    print(f"{n}*{i}={i*n}")
    i +=1

# WAP to print following numbers : [1,4,9,16,25,36,49,64,81,100]

num = 1
i = 1
while i <=10 :
    print(num)
    j = 2*i
    num = j+num+1
    i +=1

# WAP to print the list - [1,4,9,16,25,36,49,64,81,100]  using loop

list = [1,4,9,16,25,36,49,64,81,100]

for num_list in list :
    print(num_list)

# wap to find x in the tuple (1,4,9,16,25,36,49,64,81,100)

tup = (1,4,9,16,25,36,49,64,81,100)
x = 36
indx = 0
for num in tup :
    if (num == x):
        print("X is found on index" , indx)
    indx +=1