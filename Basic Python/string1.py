# strings are immutable(cannot changed if write)
name ="saim"
# a string can be sliced to be the part of the string

# for particular string how to gets its short string    string name(start index : end index(end index not included))
s_name = name[0:3]  
# it will print the name from 0 index to 2
print(s_name)


# there is also a negative slicing in string  (in negative -1 means the last index and -2 mean second lasst index and so on)
x_name = name[-3:-1]    # also equals to [1:4]
print(x_name)
y_name = name[1:3]
print(y_name)

# also if there is missing value after or before colon
z_name = name[:3]  #it mean start from 0 index
print(z_name)
c_name = name[2:] #it mean till last index or last-1
print(c_name)

# skip values in this([1:8:3] in this the third value is of skip mean jump this number value)
a="123456789"
b=a[1:7:3]
print(b)


# now some functions string
q=name.capitalize()        #make first letter capitalize
w=name.startswith("sa")     #retrun true as name starts with sa
e=name.endswith("im")       #return true as end with im
s_name = len(name)          # for length of string
r=name.count("a")            #give 1 as a occur in string for only 1 time
index =name.find("s")       #give the indedx number on which s is present
replace =name.replace("m", "a")  #it will change saim to saia




# there are escape sequence  (\t as a tab space , \n as a new line , \"\" to print something in quotes)
abc= "i am here for everyone \n but everyone used me just for their \t purpose \"asdf\" "
print(abc)