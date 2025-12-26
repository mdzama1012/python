"""Python program to demonstrate type hints, annotations and typing module in python."""

# Example-1: simple use of type annotations.
x: str = "Mohd Zama"
print(x)


# Example-2: use of type annotations in functions.
def get_star_pattern(n: int) -> str:
    """Function to return star pattern string."""
    ans = ""
    for i in range(1, n + 1):
        ans += f'{"*" * i:>8}\n'
    return ans


print(get_star_pattern(8))


# Example-3: List of all the commonly used type and there type annotations.
a: int = 20
b: float = 3.141
c: str = "Mohd Zama"
d: bool = False
j: tuple = (5, 9, "Mohd Zama", 1, 3.141)

from typing import List

e: List[int] = [5, 2, 1, 9, 7]
f: List[List[int]] = [[2, 4], [5, 9]]

from typing import Dict, Any

g: Dict[str, Any] = {"name": "Mohd Zama", "age": 20, "working": True}
h: Dict[str, str] = {"name": "Mohd Zama", "age": "20"}

from typing import Set

i: Set[str] = {"apple", "pineapple", "mango", "orange"}

# Custom type is used when we have very complicated types like 2D list, etc.
matrix = List[List[int]]


def print_grid(grid: matrix) -> None:
    N = len(grid)
    for i in range(N):
        print(*grid[i])


grid = [[5, 2, 9], [1, 2, 3], [5, 9, 9], [7, 8, 2]]
print_grid(grid)
