"""Python program to demonstrate class attribute."""

import math


class Employee:
    # class attribute.
    raise_amt = 1.05

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

    def fullname(self):
        return f"{self.fname} {self.lname}"

    def apply_raise(self):
        # self over Employee enables us to set different raise for diff employee.
        self.pay = math.floor(self.pay * self.raise_amt)


# instantiate class Employee.
emp1 = Employee("Corey", "Schafer", 32, 50000)
emp2 = Employee("Mohd", "Zama", 20, 30000)

print(emp1.pay, emp2.pay)
emp1.apply_raise()
emp2.apply_raise()
print(emp1.pay, emp2.pay)

print(emp1.__dict__)
emp1.raise_amt = 1.10  # This created a instance level attribute only for emp1.
print(emp1.__dict__)

print(emp1.pay, emp2.pay)
emp1.apply_raise()
emp2.apply_raise()
print(emp1.pay, emp2.pay)
