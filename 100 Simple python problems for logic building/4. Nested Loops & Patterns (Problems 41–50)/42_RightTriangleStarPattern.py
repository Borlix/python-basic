# 42. Right Triangle Star: Print a right-angled triangle pattern of asterisks.

for colum in range(5):
    for row in range(colum):
        print("* ",end="")
    print()