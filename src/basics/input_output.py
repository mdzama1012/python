"""Python program to demonstrate
different input and output methods.
"""

# input int
x = int(input("Enter a number: "))
print(type(x), x)

# input multiple variables in one line using list comprehensions.
x, y, z = [int(_) for _ in input("Enter value of x, y and z: ").strip().split()]
print("Value of x = {}".format(x))
print("Value of y = {}".format(y))
print("Value of z = {}".format(z))
x, y = [int(_) for _ in input("Enter value of x and y: ").strip().split()]
print("Value of x = {}".format(x))
print("Value of y = {}".format(y))

# input multiple variables in one line using map() method.
x, y, z = map(int, input("Enter value of x, y and z: ").strip().split())
print("Value of x = {}".format(x))
print("Value of y = {}".format(y))
print("Value of z = {}".format(z))
x, y = map(int, input("Enter value of x and y: ").strip().split())
print("Value of x = {}".format(x))
print("Value of y = {}".format(y))

# input list (array) of floats
a = [float(_) for _ in input("Enter array of float: ").strip().split()]
print("Array a of length {}\n{}".format(len(a), a))
# input list of int using map() method
b = list(map(int, input("Enter array of integer: ").strip().split()))
print("Array b of length {}\n{}".format(len(b), b))

# print array in one-line using print() method.
arr = [12, 5, 9, 0, 1, 10, 5]
for value in arr:
    print(value, end=" ")
print("")

# print array in one-line using * symbol.
print(*arr)

# print date in different format.
# DD  MM  YYYY
date = [10, 12, 2002]
print(date[0], date[1], date[2], sep="|")
print(date[0], date[1], date[2], sep="/")
print(date[0], date[1], date[2], sep="-")
print(date[0], date[1], date[2], sep=".")

# print list of fruits separated by there order.
fruits = ["apple", "banana", "orange", "mango", "pineapple", "grapes"]
for index, fruit in enumerate(fruits):
    print(f"{index+1}) {fruit}")

exit()
