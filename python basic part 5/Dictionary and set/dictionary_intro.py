# Dictionary - Use to store Data value { key:value } in pairs , they are mutable but can't be duplicated
dict = {
    "Name" : "peace",
    "Address" : "Haven",
    "Class" : 1 ,
    "Mark"  : 30.73
} 

print(dict)
print(type(dict))
print(len(dict))
dict["Name"] = "Borlix"
print(dict)

#Null dictionary
Null_dict = {}
Null_dict["flower"] = "Rose"
print(Null_dict)

#Nested dictionary

Food = {
    "fruit" : {
            "Banana" : 9,
            "Apple" : 6,
            "mango" : 3 
        
    },
    "veg" : ""
}

print(Food)
print(Food["fruit"])
print(Food["fruit"]["Apple"])