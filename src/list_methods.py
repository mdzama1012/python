"""Program to demonstrate list
functions and trick.
"""

# Function-1: len()
nums = [1, 2, 3, 4, 5]
print(len(nums))  # Output: 5

# Function-2: append()
nums = [5, 2, 7, 5]
nums.append(17)
print(*nums)

# Function-3: Concatenate 2 lists.
nums = [5, 2, 0, 1]
# we can pass any iterable (list, tuple, string, set, range())
nums.extend([13, 9, 17, 2])
print(*nums)

# Function-4: Concatenate 2 lists.
nums = [5, 2, 0, 1]
# functionality of extend can also be achieved by using "+" operator.
# to use "+" both the operand must be a list.
new_nums = nums + [1, 2, 3, 4]
print(*new_nums)

# Function-5: use to insert new value .insert(position, value)
nums = [5, 2, 7, 5]
nums.insert(2, 17)
print(*nums)

# Function-6: Removes and returns the element at a index (or the last element if no index is specified).
nums = [5, 9, 2, 0, 4, 8, 17, 2, 9, 5]
recent_poped = nums.pop(1)
print(f"Recent Pop: {recent_poped}", nums, sep="\n")
recent_poped = nums.pop()
print(f"Recent Pop: {recent_poped}", nums, sep="\n")

# Function-7: index()
nums = [5, 9, 2, 0, 4, 8, 17, 2, 9, 5]
print(nums.index(100))

# Function-8: count() return freq of a value.
nums = [5, 9, 2, 9, 4, 8, 17, 2, 9, 5]
print(nums.count(9))

# Function-9: sort() and reverse().
nums = [5, 9, 2, 9, 4, 8, 17, 2, 9, 5]
nums.sort(key=None, reverse=True)
print(*nums)
nums.reverse()  # dose not take any arguments.
print(*nums)

# Function-10: iterate list with index and value simultaneously.
nums = [5, 9, 4, 8, 17, 2, 9]
for index, value in enumerate(nums):
    print(f"value at {index}th is {value}")
