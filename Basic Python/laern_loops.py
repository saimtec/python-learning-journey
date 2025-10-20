# print a table using for loop
# a=int(input("Enter a number: "))
# for i in range(11):
#     print(f"{a} x {i} = {a*i}")
    


# check for prime number
# b=int(input("enter a number to check : "))
# for i in range(2,b):
#     if(b%i==0):
#         print(f"{b} is not a prime number")
#         break
# else:
#      print(f"{b} is a prime number")



# # from a list great to just persons 
# li=["abc","haider","saim",12,2,3]
# for name in li:
#     if(name.startswith("h")):
#         print(f"hello {name}")



# print sum of natural numbers
n=int(input("enter a number: "))
sum=0
i=1
while(i<n+1):
    sum +=i
    i=i+1
print(sum)



# factorial of a number
b=int(input("enter a number: "))
product=1
for i in range(1,b+1):
    product=product*i
print(f"fatorial of {b} is ", product)




# print a pattarn 
#     *
#    ***
#   *****

q=int(input("enter a number: "))
for i in range(1,q+1):
    print(" " * (q-i),end="")
    print("*" * (2*i-1),end="")           #in print ends use to not go on next line
    print("")



    # another pattern
w=int(input("enter a number: "))
for i in range(1,w+1):
    if i==1 or i==w:
        print("*" * (w)) 
    else:
         print("*" + " "* (w-2) + "*")
   

   