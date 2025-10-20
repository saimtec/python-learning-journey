name=input("enter your name :")
print(f"hello {name} ")       #print hello before name saim


# detect double space  
a="i am here for  everyone"      
b=a.find("  ")       #if return any number mean double is present on that index if return -1 mean there is no double space is present
print(b)

# replacing double space with sib=ngle space
a="i am here for  everyone"   
c=a.replace("  "," ")       # this replace functions makes another string and make changes in that string  and not chanege your orignal string
print(c)
d=c.find("  ")
print(d)