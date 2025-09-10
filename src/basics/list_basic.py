"""Python program to demonstrate
use of list (dynamic arrays) in python.
"""


from typing import List


def print_2d_list(grid: List[List[int]]) -> None:
    """
    Python function to print 2D list.
    """
    print(f"Size: {len(grid)}x{len(grid[0])}")
    for row in grid:
        print(*row)


def print_list(arr: List[int]) -> None:
    """
    Python function to print a list.
    """
    print(f"Size: {len(arr)}")
    print(*arr)


# Taking input of a list (method-1).
my_list = list(map(int, input("Enter array: ").strip().split()))
print_list(my_list)

# Taking input of a list (method-2).
my_list = [int(_) for _ in input("Enter array: ").strip().split()]
print_list(my_list)

# Taking input of a 2D list.
N, M = map(int, input().strip().split())  # matrix of N*M
grid = [list(map(int, input().strip().split())) for _ in range(N)]
print_2d_list(grid)
