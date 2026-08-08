# file - input and output to read , write or update the file 

f = open(r"C:\Users\HP\OneDrive\Desktop\learn python\python basic part 2\bool.py","r")
data = f.read()
print(data)
f.close()

f = open(r"C:\Users\HP\OneDrive\Desktop\learn python\python basic part 2\bool.py","r")
data = f.read(8) # as much only we want / parameter
print(data)
f.close()

# With syntax

with open(r"C:\Users\HP\OneDrive\Desktop\learn python\python basic part 7\File Input Output\Lets learn more","+a") as f :
    f.write("\nSO this syntax makes work better and faster! ")

