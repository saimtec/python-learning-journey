# getting input in list
l=[]
a=input("enter the name ")
l.append(a) 
b=input("enter the name ")
l.append(b) 
c=input("enter the name ")
l.append(c) 
d=input("enter the name ")
l.append(d)
print(l)


# getting input of marks and sorting them
li = []

q = int(input("Enter the marks: "))
li.append(q)

w = int(input("Enter the marks: "))
li.append(w)

e = int(input("Enter the marks: "))
li.append(e)

r = int(input("Enter the marks: "))
li.append(r)
print("Original list:", li)

li.sort()
print("Sorted list:", li)