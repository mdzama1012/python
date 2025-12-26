"""Python programs to demonstrate string
methods and tricks.
"""

s = "mohd zama"
print(len(s))

# Function :- convert string to lower and upper.
s = "upper AND lower"
new_str = s.lower()
print(new_str)
new_str = s.upper()
print(new_str)

# Function :- capitalize a string
s = "mohd zama zaidi"
print(s.capitalize())

# Function :- make title of string.
s = "mohd zama zaidi"
print(s.title())

# Function :- replace a specified sub-string to any string.
s = "banana"
new_str = s.replace("n", "xx")
print(new_str)

# Function :- return index where sub-string found.
s = "mohd zama zaidi"
print(s.find("zaidi"))

# Function :- return frequency of a specified sub-string.
s = "mohd zama zaidi"
print(s.count("a"))

# Function: - return a list of sub-strings, split by specified separator.
sentence = "count words in this sentence."
split_list = sentence.split()
print(len(split_list), split_list)

# Function: - join list (multiple) string, by using specified separator in between.
name = ["mohd", "zama", "zaidi"]
date = ["10", "12", "2002"]
print(" ".join(name))
print("/".join(date))

# Function :- isalpha(), isnumeric(), and isalnum()
a, b, c = "abc", "123", "abc123"
print(a.isalpha())
print(b.isnumeric())
print(c.isalnum())
