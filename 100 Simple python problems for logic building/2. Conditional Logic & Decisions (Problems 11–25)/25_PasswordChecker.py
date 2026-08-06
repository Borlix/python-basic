# 25. Passcode Match: Check if a user-entered password matches a stored secret password. [1, 2, 3, 4, 5]

password = int(input("Enter a number as a password : "))
SecPass = [1,2,3,4,5]

if password in SecPass :
    print("Yes ,user-entered password matches a stored secret password ")
else :
    print("No ,user-entered password Do not matches a stored secret password")
