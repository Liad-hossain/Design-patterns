class Person:
    def __init__(self, name: str, age: int, gender: str) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def get_name(self) -> str:
        return self.name

    def get_age(self) -> int:
        return self.age

    def get_gender(self) -> str:
        return self.gender

    def set_name(self, name: str) -> str:
        self.name = name

    def set_age(self, age: int) -> int:
        self.age = age

    def set_gender(self, gender: str) -> str:
        self.gender = gender
