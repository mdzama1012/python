"""Python program to demonstrate
different methods of string
concatenation
"""

# Method 1: Using the + operator to concatenate two or more strings.
s1 = "Mohd"
s2 = "Zama"
s3 = s1 + s2
print(f"{s1} -> {id(s1)}")
print(f"{s2} -> {id(s2)}")
print(f"{s3} -> {id(s3)}")

# Method 2: Using the .join() method.
date = ["10", "Dec", "2023"]
print(f"{date} -> {id(date)}")
date = "/".join(date)
print(f"{date} -> {id(date)}")

# Method 3: Using % operator with a tuple of strings to concatenate.
t = ("Mohd", "Zama", "Zaid")
s = "%s%s%s" % t
print(f"{s} -> {id(s)}")

# Quick recap of .format() method.
x = "I love {}, I hate {}, but I throw {}".format("apple", "banana", "mango")
print(x)
y = "I love {2}, I hate {0}, but I throw {1}".format("apple", "banana", "mango")
print(y)
z = "I love {f2}, I hate {f3}, but I throw {f1}".format(
    f1="apple", f2="banana", f3="mango"
)
print(z)

# Method 4: Using the .format() method (new way for string formatting).
s4 = "{}{}".format(s1, s2)
print(f"{s4} -> {id(s4)}")
