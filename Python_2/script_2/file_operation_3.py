a = input("Enter the Name of the File : ")
b = input("Entered the content to be stored in the file : ".format(a))

f = open(f"{a}", "w")
f.write("{}".format(b))
f.close()
print("A file named {0} is created with “{1}” as its contents".format(a,b))