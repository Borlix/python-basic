# 41. Square Star Pattern: Print a 5 × 5 square grid of asterisks (*).

asterisks =1
while asterisks <= 5 :
    print("* "*5)
    asterisks +=1

# Using Nested for loop
for row in range(5):
    for col in range(5):
        print("* ", end="")
    print()