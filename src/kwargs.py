def print_info(**kwargs):
    print(type(kwargs), kwargs)
    for key, value in kwargs.items():
        print(f"{key:<10} : {value}")


person = {"name": "Mohd Zama", "age": 20, "city": "Muradnagar"}
# calling by unpacking the dictionary.
print_info(**person)
# calling by variable number of keyword arguments.
print_info(name="Mohd Zama", age=20, course="B.Tech", branch="IT", city="Muradnagar")
