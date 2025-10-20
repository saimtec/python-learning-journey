# to read data from the file
# filename  ,mode(read,write,append) , format, type(text,binary)

with open("file handling\data.txt" , "r") as file:
    data = file.read()
    print(data)


print("\n \t now we print the data")
with open("file handling\data.txt","r") as file:
    for city in file:
        print(city.upper().strip())


print("\n \t writing or creating new file")
with open("abc.txt" , "w") as file:    #write will rewrite all the data or if file not present it will create it and write the data
    file.write("save this in file")
    print("saved successfully:")


print("\n \t appending data")
with open("file handling\abc.txt" , "a") as file:   
    file.write("append this in file\n")
    file.write("append this in file\n")
    file.write("append this in file\n")
    file.write("append this in file\n")
    print("appended  successfully:")


data=["universit of management\n cybersecurity\n observation\n"]
with open("file handling\abc.txt" , "a") as file:   
    file.writelines(data)



print("\n \t write and read at the same time")
with open("file handling\abc.txt","w+") as file:
    file.write("writing data in the file \n Computer \nScience")
    file.seek(0)
    print(file.read())



