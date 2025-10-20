# we use contional sattements to check contions
# if else
age=int(input("Enter your age: "))
if(age>=18):
    print("you are an adult")
else:
    "you are a child"

# if elif else laddar
age=int(input("Enter your age: "))
if(age>=18):
    print("you are an adult")
elif(age == 0):
    print("you are entering zero")
elif(age < 0):
    print("please enter a right age")
else:
    "you are a child"


# elif can be any in numbers 
# else runs only when all  conditions like if and elif becomed false

# if can also run independently but not elif and else
# we can run if independently and then again if and else elif
a=int(input("Enter your height: "))
if(a%2==0):
    print("your height is even")

if(a>=6):
    print("you have a good height")
else:
    "no no"