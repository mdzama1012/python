"""Python program to demonstrate all
important and useful set methods.
"""

s = set([5, 6, 7, 1, 7])
print(type(s), s)

# Function-1: add(), Adds an element to the set.
s = {5, 9, 2, 11, 12}
s.add(10)
print(s)

# Function-2: update(), add elements from another iterable.
s = {5, 9, 2, 10}
s.update([9, 0, 4])
print(s)

# Function-3: discard(), removes a specified element from the set (if present) without raising an error if the element is not found. (always use discard() instead of remove())
s = {5, 2, 2, 9, 10, 4}
s.discard(2)
print(s)

# Function-4: clear(), removes all elements from set.
s = {1, 2, 3, 4}
s.clear()
print(s)

# ---------------------------------- SET OPERATIONS ----------------------------------

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# operation-1: union()
union_set = set1.union(set2)  # operator overloaded is "|"
print(union_set)

# operation-2: intersection()
intersection_set = set1.intersection(set2)  # operator overloaded is "&"
print(intersection_set)

# operation-3: difference()
difference_set = set1.difference(set2)  # operator overloaded is "-"
print(difference_set)

# operation-4: symmetric_difference()
symmetric_difference_set = set1.symmetric_difference(set2)  # operator overloaded is "^"
print(symmetric_difference_set)

# operator-5: issubset() return True if set1 is subset of set2, False otherwise.
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
is_subset = set1.issubset(set2)
print(is_subset)  # operator overloaded are "<=, >=, <, >, == and !="

# operator-5: issuperset() return True if set1 is superset of set2, False otherwise.
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}
is_superset = set1.issuperset(set2)
print(is_superset)  # operator overloaded are "<=, >=, <, >, == and !="
