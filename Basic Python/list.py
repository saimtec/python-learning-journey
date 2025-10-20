# lists act like a container and used to store data of different type
data = ["saim" , "anwar" , 22 , "apple",2.22]
print(data)
# just like string we can do indexing in list
print(data[2])
data[0]="sameer"
print(data)
# just like string we can do slicing in list
print(data[1:4])

# a string is immutable as when we perform a function on string 
# it does not change the orignal string it make another new string and make changes in that
#  but list can mutable and whenever some function we perform on list it make changes on orignal list


# some functions of list
abc = ["saim" , "anwar" , 2.7 , "broken",6]
abc.append("left")             # add left on the last of the list
abc.insert(2,"when")           #insert when on index 2    
print(abc)

abc.remove("saim")            #remove the saim from list
print(abc)
print(abc.pop(2))                   #remove the value present on index 2

abc.reverse()        #print the list in reverse order
print(abc)

aa = [1,2,35,6,7,78,78,1,2,3,4,5,6,7,8]
aa.sort()             #print the sorted list
print(aa)