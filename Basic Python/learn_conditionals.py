# # point out the heigest number among all numbers entered by the user
a=int(input("enter a number :"))
b=int(input("enter second number :"))
c=int(input("enter third number :"))
d=int(input("enter fourth number :"))

if(a>b and a>c and a>d):
    print(f"{a} is greater")
elif(b>a and b>c and b>d):
    print(f"{b} is greater")
elif(c>a and c>b and c>d):
    print(f"{c} is greater")
else:
     print(f"{d} is greater")
    


# get marks input from user and decide student pass or fail (in every subject pass requirement is 33% and total 40%)
a=int(input("enter a englis number :"))
b=int(input("enter math number :"))
c=int(input("enter science number :"))
t_percent = 100*(a+b+c)/300

if(t_percent>40 and a>33 and b>33 and c>33):
    print(f"you are pass .You got {a} in english \n and {b} in math \n and {c} in science \n and got {t_percent} total percentage")
else:
    print("you failed .Better luck next time")





# make a spam keyword detector
a="umt"
b="girl"
c="broken"

xyz=input("enter a line")
if((a in xyz),(b in xyz) , (c in xyz)):
    print("it is a spam")
else:
    print("not a spam")



# check this post is about saim or not
# in function is unable to find out between lower and uppercase for that we use a trick
a="hi SAim, kesa ho kya kar raha ho"
zx=input("enter a word to check :")
if(zx.upper() in a.upper()):
    print("this post is about saim")
else:
    print("yhis post is not about you")