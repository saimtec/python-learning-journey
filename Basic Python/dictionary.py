# dictionary is mutable , order does not matter and it is indexed 
aaa={     #empty dictionary

}

marks = {
    "saim" : 40,              #on left side it is key and on right side it is value  (key cannot be repeat)
    "haider" : 50,
    "nida" : 60
}
print(marks , type(marks))   #print full dictionary
print(marks["nida"])        #just like a[2]  print marks of nida



# some functions of dictionary
print(marks.keys())     #print just the keys
print(marks.values())   #print just the values
print(marks.items())    #give dictionary in form of tuple(every key and value separate)

marks.update({"saim": 70 , "fahad" : 65})    #can update the value already present in dic or also add anew key and value also
print(marks)

print(marks.get("saim"))     #both will give same answer but the difference is that get method will give none if we write 
print(marks["saim"])         #wrong key but when we just use [] it will give error if we write any wrong key or not present key
 
c=marks.pop("saim")      #remove the vlaue of saim and also saim key
print(c)
d=marks.pop("aaaa","not present")      #to handle the error we use this sort of pop if key is not present
print(d) 