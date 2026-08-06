# 21. Character Type: Check if an input character is an alphabet, digit, or special character.

char = input("Enter a Character : ")

if char.isalpha() :
    print("Character is Alphabat")
elif char.isdigit() :
    print("Character is Digit")
else : 
    print("Character is Special character")