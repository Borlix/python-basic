# 17. Triangle Validity: Check if a triangle is valid given its three internal angles.

angA = int(input("Enter angle A : "))
angB = int(input("Enter angle B : "))
angC = int(input("Enter angle C : "))

if angA+angB+angC == 180 :
    print("Triangle is Valid")
else :
    print("Triangle is not Valid")