# 4.Check Primality Functions   
# Ask the user for a number and determine whether the number is prime or not. 
# (For those who have forgotten, a prime number is a number that has no divisors.).


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:  
            return False
    return True 

num = int(input("Enter a number to check if it is prime or not : "))

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
