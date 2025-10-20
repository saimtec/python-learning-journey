#get input from user and give mean of that 
dic={
  "a":"apple",
  "b":"bnnana",
  "c":"cat"
}
a=input("enter form a ,b and c to gets its abbrivation: ")
print(dic[a])



#input multiple numbers from user and print it once
a=set()
q=int(input("enter a number :"))
a.add(q)
w=int(input("enter a number :"))
a.add(w)
e=int(input("enter a number :"))
a.add(e)
r=int(input("enter a number :"))
a.add(r)
t=int(input("enter a number :"))
a.add(t)
print(a)


#what will be the length of the set
s=set()
s.add(20.0)     #the length will be 2 1 int and 1 as string as 20.0 and 20 are equal 
                #compiler check the numeric value if it is same it count as one
s.add("20")
s.add(20)
