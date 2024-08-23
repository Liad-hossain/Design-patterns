from abc import ABC, abstractmethod

from Design_patterns.creational_design_patterns.builder_design_pattern.example_1.Meal import \
    Meal


class MealBuilder(ABC):
    @abstractmethod
    def add_main_course(self) -> None:
        pass

    @abstractmethod
    def add_side_dish(self) -> None:
        pass

    @abstractmethod
    def add_dessert(self) -> None:
        pass

    @abstractmethod
    def add_drink(self) -> None:
        pass

    @abstractmethod
    def get_meal(self) -> Meal:
        pass
