# 43. Inverted Right Triangle: Print an inverted right-angled triangle pattern.
for row in range(5,0,-1) :
    for col in range(row):
        print("* ",end="" )
    print()