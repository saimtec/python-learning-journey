file= open("file handling\practice.txt" , "r") 
file.close()


# a) Read whole content
with open("file handling\practice.txt" , "r") as file:
    print(file.read())

# b) Read line by line using readline()
with open("file handling\practice.txt" , "r") as file:
    line1=file.readline()
    print(line1.strip())

# c) Read all lines into a list
with open("file handling\practice.txt" , "r") as file:
    lines=file.readlines()
    print(line1.strip())
    for line in lines:
        print(line.strip())


# a) Overwrite with "w" (dangerous - clears old content!)
with open("file handling\practice.txt" , "w") as file:
    file.write("this is line 1:")
    file.write("this is line 2:")


# b) Append to existing file
with open("file handling\practice.txt" , "a") as file:
        file.write("appending line 1:\n")  
        file.write("appending line 2:\n")  





#  5. Check if File Exists
import os
if os.path.exists("file handling\practice.txt"):
     print("file exist:")
else:
     print("not exist")


# # 6. Delete a File
# if os.path.exists("file handling\practice.txt"):
#      os.remove("name of that file if want to remove")



# 7. File Pointer: seek() and tell()
with open("file handling\practice.txt" , "r") as file:
     print(file.tell())   #tell the position of the cursor
     print(file.read(2))
     print(file.tell())    #new position
     file.seek(0)                #move cursor to 0 index
     print(file.read())
     


