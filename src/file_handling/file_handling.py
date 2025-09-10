"""Python program to demonstrate file handling"""

from typing import List

"""Modes of file:

"r": read from file
"w": write to file
"a": append to file
"r+": read from file and write to file
"""

# Below method is not recommended.
f = open("test1.txt", "r")
print(f.name)
f.close()

# use keyword "with" because it automatically closes the file.
with open("test1.txt", "r") as f:
    pass

# Example-1: read() method.
with open("test1.txt", "r") as f:
    content: str = f.read()
    print(content)

# Example-2: readline() method.
with open("test1.txt", "r") as f:
    content: str = (
        f.readline()
    )  # read till '\n' char is not found (also reads '\n' char).
    print(content, end="")
    # start reading where it left before.
    content: str = f.readline()
    print(content, end="")

# Example-3: readlines() method.
with open("test1.txt", "r") as f:
    # return list of str that contains all the line. (every string includes '\n' char).
    content: List[str] = f.readlines()
    print(content)

# Example-4: read file content in chunks.
with open("test1.txt", "r") as f:
    chunk = 10
    content: str = f.read(chunk)
    while len(content) > 0:
        print(content, end="")
        content: str = f.read(chunk)

# Example-5: seek(), method resets the reading pointer to specified position.
with open("test1.txt", "r") as f:
    chunk = 10
    content: str = f.read(chunk)
    print(content, end="")

    f.seek(0)  # resets the reading point to 0.

    content: str = f.read(chunk)
    print(content)

# Example-6: write() method.
with open("test2.txt", "w") as f:
    f.write("Test ")

# Example-7: opening a file in append mode.
with open("test2.txt", "a") as f:
    f.write("File")
