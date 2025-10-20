# just like strings tuples are immutable we cannot change after once write it 

a=("saim","anwar",22,6,2.7,"when")     #declaration of tuple
print(type(a))
print(a)

b=()      #declaration of empty tuple
print(type(b))
print(b)
c=(1,)    #declaration of tuple if we not use , then it will be considered as integer
print(type(c))
print(c)


# some functions of tuple

b=("saim","nidaum",22,6,2.7,"when") 
print(b.count(22))        #gives how much time 22 occur in my tuple
print(b.index(22))        #return the index number on which 22 is present

t = (5, 1, 9)
print(max(t))  # gives the largest number

print(min(t))  #gives the minimum value
print(sum(t))  #add all the values of tupple and give 

t = (5, 1, 9)
q,w,e =t      #assign tupple values to q,w and e
print(q,w,e)      

t = (1, 2, 3, 4)
print(t[1:3])      #do slicing output will be 23

a = (1, 2)
b = (3, 4)
print(a + b)  #we can concatinate two tuples like this



