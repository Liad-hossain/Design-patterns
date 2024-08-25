from Design_patterns.creational_design_patterns.builder_design_pattern.example_1.Meal import (
    Meal,
)
from Design_patterns.creational_design_patterns.builder_design_pattern.example_1.MealBuilder import (
    MealBuilder,
)


class Chef:
    def __init__(self, builder: MealBuilder) -> None:
        self.builder = builder

    def prepare_meal(self) -> None:
        self.builder.add_main_course()
        self.builder.add_side_dish()
        self.builder.add_dessert()
        self.builder.add_drink()

    def get_meal(self) -> Meal:
        self.prepare_meal()
        return self.builder.get_meal()
