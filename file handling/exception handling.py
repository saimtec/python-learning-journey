# handle errors gracefuly (try and except)
# errors like zerodivisionerror , fileexisterror , fileexistalready , typeError , valueError , nameError , attributeError


try:
     with open("lml.txt" , "r") as file:
          print(file.read())
except FileNotFoundError:
     print("file not found:")




# 10. Create New File with "x" Mode
try:
     with open("abc.txt" , "x") as file:
          print("file created")

except FileExistsError:
     print("file already exist:")




try:
    x=50/0
    print(x)
except:
    print("division by zero not possible : ")




try:
     a=int(input("enter first integer:"))
     b=int(input("enter second integer:"))
     z=a/b
     print(z)
except ZeroDivisionError:
     print("entered a zero : please enter only non zero integer ")

except ValueError:
     print("entered a string :please enter only non zero integer ")

except:
     print("some error occur , Try again")
     