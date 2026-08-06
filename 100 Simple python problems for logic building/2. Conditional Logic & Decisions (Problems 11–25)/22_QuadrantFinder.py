# 22. Quadrant Finder: Determine which quadrant a coordinate point (x, y) lies in.

x = int(input("Enter value of x-axis : "))
y = int(input("Enter value of y-axis : "))

if x >= 0 and y >= 0 :
    print(f"{(x,y)} is in First Quadrant")
elif x >= 0 and y < 0 :
    print(f"{(x,y)} is in Forth Quadrant")
elif x < 0 and y >=0 :
    print(f"{(x,y)} is in Second Quadrant")
elif x < 0 and y < 0 :
    print(f"{(x,y)} is in Third Quadrant")