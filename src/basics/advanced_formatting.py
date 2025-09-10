"""Program to demonstrate advance formatting technique.
"""

# Example 0: '<' and '>' left-align and right-align to the given value.
print(f'{"*":>10}')
print("{:>10}".format("*"))

# Example 1: ',' used for adding thousands separators to numerical values in f-strings and the .format().
n = 10**10
print(f"{n} -> {n:,}")
print("{0} -> {0:,}".format(n))

# Example 2: '+' used to include sing for +ve and -ve values.
pos_val, neg_val = 7, -5
print(f"({pos_val}, {neg_val}) -> ({pos_val:+}, {neg_val:+})")
print("({0}, {1}) -> ({0:+}, {1:+})".format(pos_val, neg_val))

# Example 3: '0' used to pad numeric values with 0.
for _ in range(1, 11):
    table_12 = f"12 x {_} = {12 * _:03}"
    table_15 = "15 x {} = {:03}".format(_, _ * 15)
    print(f"{table_12:<15}{table_15}")

# Example 4: Changing precision.
pi = 3.1415926535  # 10 decimal places.
print(f"Value of PI up to 5 decimal places: {pi:.5f}")
print("Value of PI up to 3 decimal places: {:.3f}".format(pi))

# Example 5: change the format of date, b -> binary, o -> octal, and x -> Hexadecimal.
num = 571
print(f"{num} in binary: {num:b}")
print("{0} in binary: {0:b}".format(num))
