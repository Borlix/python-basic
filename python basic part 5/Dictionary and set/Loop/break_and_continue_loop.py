# loop with continue 

i = 1
while i <= 10 :
    if (i%2==0) :
        i += 1
        continue
    print(i)
    i += 1

#loop with break 
i = 1
while i <= 10 :
    print("This worked!")
    if i == 6  :
        break
    i += 1
