# JSON (JavaScript Object Notation) is a text format used to store and exchange data.


# | JSON Type        | Python Type      | Example JSON    | Example Python  |
# | ---------------- | ---------------- | --------------- | --------------- |
# | `object`         | `dict`           | `{"a": 1}`      | `{"a": 1}`      |
# | `array`          | `list`           | `[1, 2, 3]`     | `[1, 2, 3]`     |
# | `string`         | `str`            | `"hello"`       | `"hello"`       |
# | `number`         | `int` / `float`  | `42`, `3.14`    | `42`, `3.14`    |
# | `true` / `false` | `True` / `False` | `true`, `false` | `True`, `False` |
# | `null`           | `None`           | `null`          | `None`          |





# Parse JSON - Convert from JSON string to Python - json.loads()
import json

# a JSON string representing a book
x = '{ "title":"The Hitchhiker\'s Guide to the Galaxy", "author":"Douglas Adams", "published_year":1979, "genres":["Sci-Fi", "Comedy"]}'

# parse x
y = json.loads(x)

print(y)
# string is converted into dictionary
print(type(y))




# now converting dic into object(str)
a = {
    "recipe_name": "Guacamole",
    "ingredients": ["avocado", "onion", "lime", "cilantro", "salt"],
    "preparation_time_minutes": 10
}

z=json.dumps(a)

print(z)

print(type(z))



