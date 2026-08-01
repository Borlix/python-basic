# Set - Collection of unorder item and its element can't be mutate but set can mutate 

set1 = { 1, 2, 3, 4, 5}
set_empty = set() # returns empty set
print(set1)
print(set_empty) 
print(type(set_empty))

# methods of set

set2 = {"apple" , "ball" , "cat" , "dog"}
print(set2)
set2.add("egle")
print(set2)
set2.remove("egle")
print(set2)
set2.pop()
print(set2)

set3 = { 1, 2, 3}
set4 = { 3, 4, 5}

print(set3.union(set4))
print(set3.intersection(set4))