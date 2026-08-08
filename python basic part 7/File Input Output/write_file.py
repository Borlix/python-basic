file = open(r"Lets learn more","w")   # we can over write and create a file .
file.write("Hi , so this works")     
file.close()

file = open(r"Lets learn more","a")   # we can over write and create a file .
file.write("\nIts time to sleep i guess!")     
file.close()