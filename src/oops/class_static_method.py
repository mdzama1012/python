"""Python program to demonstrate class attributes."""

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
        return f"Employee('{self.fname}', '{self.lname}', {self.age}, {self.pay})"

    def fullname(self):
        return f"{self.fname} {self.lname}"

    def apply_raise(self):
        self.pay = math.floor(self.pay * self.raise_amt)

    @classmethod  # decorator
    def set_raise_amt(cls, amt):
        cls.raise_amt = amt

    @classmethod  # we also use classmethod as alternative constructor.
    def from_csv(cls):
        with open("employee.csv", "r") as f:
            lines = csv.reader(f)
            next(lines)
            for row in lines:
                cls(row[0], row[1], int(row[2]), int(row[3]))

    @staticmethod
    def is_working(date):
        if date.weekday() == 5 or date.weekday() == 6:
            return "Weekend Holiday!"
        return "Working Day!"


# instantiate class Employee.
Employee.from_csv()
print(*Employee.all_employee, sep="\n")

import datetime

my_date = datetime.date(2023, 12, 10)
print(Employee.is_working(my_date))
