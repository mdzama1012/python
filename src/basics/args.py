def get_sum(*args):
    print(type(args), args)
    ans = 0
    for arg in args:
        ans += arg
    return ans


nums_list = (5, 2, 9, 10, 4)
nums_tuple = [4, 8, 1, 3, 70]
interval = range(1, 5 + 1, 1)
# calling by unpacking the tuple, list, range, etc.
print(get_sum(*nums_list))
print(get_sum(*nums_tuple))
print(get_sum(*nums_list, *nums_tuple))
print(get_sum(*interval))
# calling by variable number of arguments.
print(get_sum(5, 9, 3, 1, 2))
