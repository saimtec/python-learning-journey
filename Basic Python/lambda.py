# lamda function (short format for small tasks  lamda argument : expression)
square= lambda x:x*x
print(square(4))

# map
num=[1,2,3,4,5]
square=list(map(lambda x:x**x,num))
print(square)

# filter
num=[1,2,3,4,5,6,7,8,9]
even=list(filter(lambda x:x%2==0,num))
print(even)