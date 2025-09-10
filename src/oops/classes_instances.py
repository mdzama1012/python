"""Python program to demonstrate instantiation and creation of class."""


class Employee:
    # type checking is good practice.
    def __init__(self, fname: str, lname: str, age: int, pay: float):
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


# instantiate class Employee.
emp1 = Employee("Corey", "Schafer", 32, 50000)
emp2 = Employee("Mohd", "Zama", 20, 30000)

print(emp1.fullname(), emp1.age, emp1.pay, emp1.email, sep="\n")
print(emp2.fullname(), emp2.age, emp2.pay, emp2.email, sep="\n")
