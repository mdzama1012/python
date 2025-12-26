msg = "global variables"

def greeting(name):
    print("hello, " + name)

def addNum(*args):
    ans = 0
    for num in args:
        ans += num
    return ans

def main():
    res = addNum(1, 2, 3, 4, 5, 6, 7, 8, 9)
    print(res)
    greeting("Zama")

# tell I'm using main() here just like c++ or c
if __name__ == "__main__": main()
