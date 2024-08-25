from Design_patterns.creational_design_patterns.prototype_design_pattern.example_1.Person import (
    Person,
)


class Employee(Person):
    def __init__(
        self,
        name: str,
        age: int,
        gender: str,
        employee_id: str,
        salary: int,
    ) -> None:
        super().__init__(name, age, gender)
        self.employee_id = employee_id
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nEmployee ID: {self.employee_id}\nSalary: {self.salary}"
