# WAP to store some word and difination in a dicitionary 

word = {
    "Table" : "Furnitur",
    "Cat" : ["Pet Animal","Wild Animal"],
    "Lion" : "Wild Animal",
    "Buffalo" : ("wild animal", "Domastic Animal")
}
print(word)

# You are given a list of subject for student . Assume 1 class requride for 1 subject. how many classroom needed by all student
# list -("python", "java", "c++", "python", "javascript", "c++", "python", "c")

classes = {
"class_python" : ("python","python","python"),
"class_java" : ("java"),
"class_Cplus" : ("c++", "c++"),
"class_js" : ("javascript"),
"class_c" : ("c")
}
print(f"It needs {len(classes)} Classrooms as per 1 class in 1 subject for all student")

# WAP to enter marks of 3 subjects from user and store it in dictionary. start with a empty dictionary and add one by one .

mark1 = float(input("Enter your mark of Physics : "))
mark2 = float(input("Enter your mark of Chemistry : "))
mark3 = float(input("Enter your mark of Math : "))

empty_mark1 = set()
empty_mark1.add(mark1)
empty_mark2 = set()
empty_mark2.add(mark2)
empty_mark3 = set()
empty_mark3.add(mark3)

print(empty_mark1)
print(empty_mark2)
print(empty_mark3)

dict_subject = {
    "Physics" : "",
    "chemistry" : "",
    "math" : ""
}

dict_subject.update({"Physics": empty_mark1}) 
dict_subject.update({"chemistry": empty_mark2}) 
dict_subject.update({"math": empty_mark3})
print(dict_subject)