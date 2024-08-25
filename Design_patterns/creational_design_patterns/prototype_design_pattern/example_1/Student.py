from Design_patterns.creational_design_patterns.prototype_design_pattern.example_1.Person import (
    Person,
)


class Student(Person):
    def __init__(
        self,
        name: str,
        age: int,
        gender: str,
        student_id: str,
        department: str,
    ) -> None:
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.department = department

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nStudent ID: {self.student_id}\nDepartment: {self.department}"
