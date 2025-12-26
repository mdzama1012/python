"""Use Cases of list and tuple:
List: Preferred when the data may need to be modified, such as adding or removing elements.
Tuple: Suitable for situations where immutability is desired, like representing fixed collections of values.
"""

# Normal syntax to create a tuple
my_tuple = (1, 2, 3)

# Syntax for single element tuple and single element list.
my_list = [1]
my_tuple = (1,)
print(type(my_tuple), my_tuple)

# All built-In methods of tuple.
my_tuple = (1, 2, 3, 4, 5, 2, 3, 3)
print(len(my_tuple))
print(my_tuple.count(3))
print(my_tuple.index(4))

# concatenate two tuples.
t1 = (1, 2)
t2 = (5, 7)
t3 = t1 + t2

print(t3)
