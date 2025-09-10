"""Python program to demonstrate 6 looping
techniques that are used in DSA and CP problems.
"""

# way-1: iterate any iterable with index and value at that index.
my_list = ["apple", "pineapple", "orange", "mango"]
for index, value in enumerate(my_list):
    print(index, value)

# way-2: iterate different containers at same time using zip() method.
my_list = ["apple", "pineapple", "orange", "mango"]
my_tuple = (8, 2, 1, 9, 0, 5)
my_set = {9, "USA", (5, 0), "Mohd Zama"}
# iterate till the smaller container ends
for val1, val2, val3 in zip(my_list, my_tuple, my_set):
    print(val1, val2, val3)

# way-3: iterate key-value pair in dictionary using items() method.
fruit_bucket = {"apple": 10, "pineapple": 12, "orange": 36, "mango": 102}
for key, value in fruit_bucket.items():
    print(f"{key:<10} : {value}")

# way-4: iterate keys in dictionary using keys() method.
for key in fruit_bucket.keys():
    print(f"{key:<10} : {fruit_bucket[key]}")

# way-5: iterate values in dictionary using values() method.
for value in fruit_bucket.values():
    print(value)

"""
way-6: iterate any sequence (list, tuple, string, etc.) in sorted order, using sorted() method.
1. syntax: sorted(iterable, key=None, reverse=False)
2. No matter what a container is mutable or immutable, sorted() return a new sorted list,
	while keeping the original container as it is.
"""
container = (8, 2, 1, 9, 0, 5)
# sort in descending order.
for value in sorted(container, reverse=True):
    print(value, end=" ")
print("")

# way-7: iterate using reversed() method.
my_tuple = (8, 2, 1, 9, 0, 5)
i = reversed(my_tuple)
print(type(i), i)  # returns a reverse iterator.
for value in i:
    print(value, end=" ")
print("")
