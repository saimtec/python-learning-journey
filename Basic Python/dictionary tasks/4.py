# 4. Write a Python program to create a dictionary of keys x, y, and z 
# where each key has as value a list from 11-20, 21-30, and 31-40 respectively.
#  Access the fifth value of each key from the dictionary.

# {'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
# 'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
# 'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}


my_dict = {
    'x': list(range(11, 20)),
    'y': list(range(21, 30)),
    'z': list(range(31, 40))
}

# Access 5th value (index 4) of each key
print("Fifth values:")
print("x:", my_dict['x'][4])
print("y:", my_dict['y'][4])
print("z:", my_dict['z'][4])
