#Grade Distrubution as per Marks!

Mark = float(input("Enter your Marks : "))

if Mark >= 90 :
    print("A+")
elif Mark >= 80 :
    print("A")
elif Mark >= 70 :
    print("B+")
elif Mark >= 60 :
    print("B")
elif Mark >= 50 :
    print("c+")
elif Mark >= 40 :
    print("c")
else :
    print("Don't Worry, try again with more efforts!")

# WAP to check Weather a number Enter by the user is even or odd.
Num = int(input(">>>ITS A PROGRAM TO CHECK NUMBER IS EVEN OR ODD<<<\nEnter a number : "))

Num = Num%2

if Num == 0 :
    print("Even")
elif Num == 1 :
    print("Odd")
else :
    print("ERROR!")

# WAP to find greatest of 3 Numbers enterd by user.
print("IT's a Program to check Greatest number! ")
num1= int(input("Enter a number 1: "))
num2= int(input("Enter a number 2: "))
num3= int(input("Enter a number 3: "))

if num1 >= num2 and num2 > num3:
    print(f"{num1} is Greatest!")
elif num2 >= num1 and num1 > num3:
    print(f"{num2} is Greatest!")
else :
    print(f"{num3} is Greatest")

#WAP a program to check weather a number is in multiples of 5 or not.

print("Lets check that number is in multiples of 5 or not")
num = int(input("Enter any numbers : "))
num = num%5

if num == 0:
    print("Yes it was in multiples of 5")
else :
    print("No we don't found it in multiples of 5")