# the piece of code that we can use agaiin and again
# there are two types of functions built in like "print,max,min" and user defined which we do with keyword "def"

def abc():     #function defination
    print("hello")

abc()      #function call

# argument in function
def ab(name):   
    print("hello" + name)

ab("saim")  

# now return if we use function in other variable we do return otherwise it will give none
def a(name):   
    print("hello" + name)
    return "ok" 
x=ab("saim")  
print(x)

# default parameter
def aaa(name,end="good"):   #if i provide argument for end it will print that otherwise print default good
    print("hello" + name)
    print(end)
aaa("saim")  




# factorail or recursion
def fact(n):
    if(n==0 or n==1):
        return 1
    return n * fact(n-1)

a=int(input("enter a number : "))
print(f"factorial of {a} is {fact(a)}")





