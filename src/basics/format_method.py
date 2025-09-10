"""Python program to demonstrate .format() method for string formatting.
"""

# Example 1: simple use.
sentence = "I am {} and I am {} year old.".format("Mohd Zama", 20)
print(sentence)

# Example 2: use of index to map the correct value to the correct place holder.
sentence = "I am {1} and I am {0} year old.".format(20, "Mohd Zama")
print(sentence)

# Example 3: use of index becomes important, when we want to repeat the same value over and over in the string.
tag = "h1"
txt = "This is a h1 tag"
html_code = "<{0}>{1}</{0}>".format(tag, txt)
print(html_code)

# Example 4: formatting by passing keyword arguments
sentence = "I am {name} and I am {age} year old.".format(name="Zama", age=20)
print(sentence)

# Example 5: Unpacking of dictionary.
person = {"name": "Mohd Zama", "age": 20, "home_town": "Muradnagar"}
sentence = "I am {name}, I am {age} year old and I live in {home_town}".format(**person)
print(sentence)

# Example 6: Unpacking of list to print fruits in sorted order.
l = ["banana", "mango", "orange", "berry", "pineapple", "grapes"]
sentence = "I like to eat {0}, {1}, {2}, {3}, {4}, and {5}".format(*sorted(l))
print(sentence)
