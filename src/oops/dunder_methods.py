"""Program to demonstrate dunder methods in python."""

import math, csv


class Employee:
    # class attribute.
    raise_amt = 1.05
    emp_count = 0
    all_employee = []

    # constructor or Dunder init method.
    def __init__(self, fname: str, lname: str, age: int, pay: int):
        # validation of data.
        assert age > 18, "Underage, age must be 18+."
        assert pay >= 0, "Non-negative pay not allowed."
        # initialization of instance attribute.
        self.fname = fname
        self.lname = lname
        self.age = age
        self.pay = pay
        self.email = f"{fname.lower()}{lname.capitalize()}@company.com"
        Employee.emp_count += 1
        Employee.all_employee.append(self)

    def __repr__(self):
        # Defines the "formal" or unambiguous string representation of an object.
        return f"Employee('{self.fname}', '{self.lname}', {self.age}, {self.pay})"

    def __str__(self):
        # Defines the "informal" or user-friendly string representation of an object.
        return f"{self.fullname()} - {self.email}"

    def fullname(self):
        return f"{self.fname} {self.lname}"

    def apply_raise(self):
        self.pay = math.floor(self.pay * self.raise_amt)


# instantiate class Employee.
emp1 = Employee("William", "Taylor", 32, 62000)
emp2 = Employee("Sophia", "Anderson", 50, 85000)

print(str(emp1))  # emp1.__str__()
print(repr(emp1))  # emp1.__repr__()

"""There are many dunder methods, we can also achieve operator overloading using dunder methods."""
