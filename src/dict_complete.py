"""Python code to demonstrate
dictionary datatype in python.
"""

# creating a dict.
d = {}
print(type(d), d, sep="\n")
d = {"apple": 24, "banana": 12, "orange": 6}
print(type(d), d, sep="\n")

# insert element in a dict.
d["pineapple"] = 36

# update element in a dict.
if "pineapple" in d:  # search for key.
    d["pineapple"] += 5
else:
    d["pineapple"] = 36

# iterate dict with keys only.
for key in d.keys():
    print(key)

# iterate dict with values only.
for value in d.values():
    print(value)

# iterate dict with key-value pair.
for key, value in d.items():
    print(f"{key} --> {value}")

# iterate dict with index, key and value.
for index, (key, value) in enumerate(d.items()):
    print(f"{index} {key} --> {value}")
