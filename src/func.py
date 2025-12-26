# function declaration or definition
def greet():
    print("hello, huda!")

fn = greet
fn()
greet() # function invoked or invocation

# basic principles of function:
# 1. single responsibility principle.
# 2. it should be easy to use for others.
# 3. generic input (follow rule 2 for this rule to apply)

# "name" here is function parameters
def greet_with_name(name):
    print("hello, " + name)

# "zama" here is an function arguments
greet_with_name("zama")
greet_with_name("huda")

# pass unlimited arguments by using *args in python function.
def addNum(*args):
    ans = 0
    for num in args:
        ans += num
    return ans

res = addNum(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(res)

# TODO: how to pass iterables in python function

# global, local and nonlocal variables
msg = "global msg"
def message(msg):
    print("================================================")
    print(msg)
    print("================================================")

message("this is a msg!")

# nonlocal example.
# In Python, the nonlocal keyword is used within nested functions to indicate that a variable is not local to the inner function, but rather belongs to an enclosing function’s scope.
msg = "global"

# def outer():
#     msg = "outer variable"
#     def inner():
#         nonlocal msg # most important line.
#         msg = "inner variable"
#         print(msg)
#     inner()
#     print(msg)

# outer()

def outer():
    global msg
    msg = "outer variable"
    def inner():
        global msg # most important line.
        msg = "inner variable"
        print(msg)
    inner()
    print(msg)

outer()
print(msg)
