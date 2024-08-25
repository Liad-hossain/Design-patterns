from Design_patterns.creational_design_patterns.builder_design_pattern.example_1.Meal import (
    Meal,
)
from Design_patterns.creational_design_patterns.builder_design_pattern.example_1.MealBuilder import (
    MealBuilder,
)


class VegMealBuilder(MealBuilder):
    def __init__(self):
        self.meal = Meal()

    def add_main_course(self):
        self.meal.main_course = "Grilled Tofu"

    def add_side_dish(self):
        self.meal.side_dish = "Salad"

    def add_dessert(self):
        self.meal.dessert = "Fruit Salad"

    def add_drink(self):
        self.meal.drink = "Green Tea"

    def get_meal(self) -> Meal:
        return self.meal
