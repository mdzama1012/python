"""Python progarm to demonstrate all datatype supported
"""

x = "Hello World"
print(f"x = {x}, type: {type(x)}")

x = 50
print(f"x = {x}, type: {type(x)}")

x = 60.5
print(f"x = {x}, type: {type(x)}")

x = 2 + 3j
print(f"x = {x}, type: {type(x)}")

x = ["geeks", "for", "geeks"]
print(f"x = {x}, type: {type(x)}")

x = ("geeks", "for", "geeks")
print(f"x = {x}, type: {type(x)}")

x = range(10)
print(f"x = {x}, type: {type(x)}")

x = {"name": "Suraj", "age": 24}
print(f"x = {x}, type: {type(x)}")

x = {"geeks", "for", "geeks"}
print(f"x = {x}, type: {type(x)}")

x = frozenset({"geeks", "for", "geeks"})
print(f"x = {x}, type: {type(x)}")

x = True
print(f"x = {x}, type: {type(x)}")

x = b"Geeks"
print(f"x = {x}, type: {type(x)}")

x = bytearray(4)
print(f"x = {x}, type: {type(x)}")

x = memoryview(bytes(6))
print(f"x = {x}, type: {type(x)}")

x = None
print(f"x = {x}, type: {type(x)}")
