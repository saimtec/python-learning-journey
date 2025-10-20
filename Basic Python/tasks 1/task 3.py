# 3.Take two lists, from user.
# and write a program that returns a list that contains only the elements that are common between 
# the lists (without duplicates). Make sure your program works on two lists of different sizes.


a = [int(i) for i in input("Enter list A: ").split()]
b = [int(i) for i in input("Enter list B: ").split()]
same = [i for i in set(a) if i in b]
print("Common elements without duplicates:", same)
