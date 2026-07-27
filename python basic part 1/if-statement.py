#6th python program - learning if- statement!
#                     (if, elsif , else)  

age = int(input("Enter your age: "))
Bus_rent = True

print (age)

if age >= 50 :
    print ("you are an old guy!")
    print ("you don't need to pay ")
elif age >=18 :
    print ("you are an adult!")
    print ("you need to pay bus rent!")
else : 
    print (" you are still a child")
    print ("you don't need to pay ")


