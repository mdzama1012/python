"""Python program to demonstrate
list comprehensions in python.
"""

from typing import List


def solve(N: int, target: int) -> List[List[int]]:
    """
    Task1: Provide a pair of numbers, "N" and "target"; display all potential triplets where each number falls within the range from 0 to "N" and collectively sums up to the "target".
    """
    return [
        [x, y, z]
        for x in range(N)
        for y in range(N)
        for z in range(N)
        if x + y + z == target
    ]


N, target = map(int, input("Enter 2 numbers: ").strip().split())
print(solve(N, target))

# task2: print square of odd values form 1 to 20
odd_sq = [_ * _ for _ in range(1, 20 + 1) if _ % 2 == 1]
print(*odd_sq)

# task3: clean the string.
s = "$Gee*k;s..fo, r'Ge^eks?"
print(f"Before:\n{s}")
s = "".join([char for char in s if char.isalpha()])
print(f"After:\n{s}")

# task4: creat a list if L, R (inclusive) and jump is given.
L, R, jump = map(int, input("Enter 3 numbers: ").strip().split())
if jump < 0:
    R -= 1
else:
    R += 1

my_list = [x for x in range(L, R, jump)]
print(*my_list)
