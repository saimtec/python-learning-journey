#sets are used to store values but distinct 
# sets are unindexed , unordered and not changeable
a=set()   #we can create empty set like that

s={1,2,32,345,12}
print(s)



# some functions of set
s.add(2323)   #it will add this value in my set
s.remove(2)    #it will remove this value from my set
s.pop()       #it will remove a random number or value from our set  (not good)
s.clear()     #it will clear our set

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7}

print("union is :", s1.union(s2))
print("intersection is :",s1.intersection(s2))
print("differnce is :", s1.difference(s2))
print("does s1 is subste of s2 :",s1.issubset(s2))
print({1,2}.issubset(s1))