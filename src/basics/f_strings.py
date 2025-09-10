"""Python program to demonstrate
different use case of f-string.
"""

# Example 1: F-strings provide a concise and convenient way to embed Python expressions inside string literals for formatting.
name = "Mohd Zama"
age = 20
weight = 67  # weight in kg.
print(f"Myself {name}, I am {age} year old and my weight is {weight}kg.")

# Example 2: use of expression inside f-string.
print(f"Myself {name}, I am {age} year old and my weight is {weight*2.20462:.2f}lb.")

# Example 3: use of function on a variable.
print(f"Myself {name.upper()}, I am {age} year old.")

# Example 4: same as example 3.
my_list = [9, 0, 52, 4, 11, 12, 5]
print(f"Unsorted list:\n{my_list}\nSorted list:\n{sorted(my_list)}")

# Example 5: use of string list inside a f-string.
person = {"name": "Mohd Zama", "age": 20, "weight": 67}
print(
    f"Myself {person['name']}, I am {person['age']} year old and my weight is {person['weight']}kg."
)
