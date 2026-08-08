with open(r"Learning.txt","r") as f:
    data = f.read()

new_data = data.replace("python" , "java")
print(new_data)

with open(r"Learning.txt","w") as f:
    data = f.write(new_data)