"""Python program to demonstrate global scop,
local scop, 'global' keyword, and 'nonlocal' keyword.
"""


def f():
    global s  # Error: nonlocal s
    s += " Zama"
    i = 10

    def g():
        nonlocal i  # Error: global i
        for i in range(5 + 1):
            print(i, end=" ")

    g()
    print(f"\n{i}")


# Global scope
s = "Mohd"
f()
print("After f()", s)
