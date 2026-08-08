# WAP to replace java with python in "Learning.txt" file

with open("Learning.txt","r") as f :
    data = f.read()

new_data = data.replace("java","python")
print(new_data)

with open("Learning.txt","w") as f :
    data = f.write(new_data)
    
# To Search weather the word exist in file or not :  


word = "Hi"                
with open("Learning.txt","r") as f :
    data = f.read()
    if (data.find(word)!=-1):
        print("Found!")
    else :
        print("Not found!")