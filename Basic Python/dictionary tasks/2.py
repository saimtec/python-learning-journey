# 2.Write a Python script to check whether a given key already exists in a dictionary.

my_dict = {1: 100, 2: 200, 3: 300}

key = int(input("Enter a key to check: "))

if (key in my_dict):
    print(f"Key {key} exists in the dictionary.")
else:
    print(f"Key {key} does not exist in the dictionary.")
