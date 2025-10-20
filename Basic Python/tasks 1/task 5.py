# 5.Password Generator    
# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix 
# of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new 
# password every time the user asks for a new password. Include your run-time code in a main method.
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.


import string
import random

# for weak
def weak():
    words = "humtum","kingdom","umt","ucp","america","pakistan"
    passward = random.choice(words) + random.choice(words)
    return passward

# for normal
def normal():
    char = string.ascii_lowercase + string.digits
    passward_length = random.randint(8,12)
    passward = ''.join(random.choice(char) for _ in range(passward_length))
    return passward

# for strong
def strong():
    char = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    passward_length = random.randint(10,15)
    passward = ''.join(random.choice(char) for _ in range(passward_length))
    return passward


def main():
    print("choose passward type?")
    print("1. Weak (Just words)")
    print("2. Normal (Words + numbers)")
    print("3. Strong (lowercase,upercase, numbers, and symbols)")
    
    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        print("Generating a weak password...")
        password = weak()
    elif choice == "2":
        print("Generating a moderate password...")
        password = normal()
    elif choice == "3":
        print("Generating a strong password...")
        password = strong()
    else:
        print("Invalid choice generating a default strong password...")
        password = strong()
    
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()
