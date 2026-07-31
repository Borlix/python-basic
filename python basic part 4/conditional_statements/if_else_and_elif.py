# Rough
Name = input("Enter your name : ")
is_true = Name

if is_true :
    print("We got your name!")
    print(f"your name is {Name}")
else :
    print("We don't get your name, Enter your name")

#if- else
print("...Find the value of b...\na + b = 10 \na = 5\nb = ?")

b = int(input("Enter value of b : "))
if b == 5:
    print("Right!")
else :
    print("Wrong!")

#if-else-elif

age = int(input("Enter your age : "))

if age <= 18 :
    print(f"You are still a child, your age is {age}")
elif age >= 60 :
    print(f"You had became old ,Your age is {age}")
else :
    print(f"perfect, its show time!, your age is {age}")