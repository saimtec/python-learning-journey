# program to print the content presetn in directory using os module 

import os
# specifying firectory now is f
directory_path = '/'
# listing all files and folders in one directory
contents = os.listdir(directory_path)
# print file and directory name    
for item in contents: 
    print(item)