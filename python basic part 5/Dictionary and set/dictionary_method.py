dict = {
    "space" : "rocket",
    "physics" : "f2",
    "biology" : "gen",
    "math" : "claculus"
}

print(dict)                                #Prints a dict
print(dict.values())                       #Prints only values 
print(dict.items())                        #Prints all the items
print(dict.keys())                         #Prints only keys
print(dict.get("physics"))                  #Prints only the value of key/physics
print(dict.update({"chemistry":"magic"}))  #update dict with more key:value added
print(dict)
dict["math"] ="Calculus"                   
print(dict)