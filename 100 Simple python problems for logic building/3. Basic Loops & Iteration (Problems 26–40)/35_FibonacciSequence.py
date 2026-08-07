# 35. Fibonacci Sequence: Print the first N terms of the Fibonacci sequence.

n = int(input("Enter a number : "))
a = 0
b = 1
while n >= 0 :
    print(a,end="+")
    c = a + b
    a = b
    b = c
    n -=1
    