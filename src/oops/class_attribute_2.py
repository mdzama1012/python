"""Python program to demonstrate class attributes."""

import math


class Employee:
    # class attribute.
    raise_amt = 1.05
    emp_count = 0

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

    def fullname(self):
        return f"{self.fname} {self.lname}"

    def apply_raise(self):
        self.pay = math.floor(self.pay * self.raise_amt)


# instantiate class Employee.
print(Employee.emp_count)
emp1 = Employee("Corey", "Schafer", 32, 50000)
emp2 = Employee("Mohd", "Zama", 20, 30000)
print(Employee.emp_count)
