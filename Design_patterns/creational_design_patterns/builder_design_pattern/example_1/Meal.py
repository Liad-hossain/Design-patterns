class Meal:
    def __init__(self):
        self.main_course = None
        self.side_dish = None
        self.dessert = None
        self.drink = None

    def __str__(self):
        return f"Main Course: {self.main_course}\nSide Dish: {self.side_dish}\nDessert: {self.dessert}\nDrink: {self.drink}"
