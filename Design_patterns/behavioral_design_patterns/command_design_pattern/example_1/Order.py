from Design_patterns.behavioral_design_patterns.command_design_pattern.example_1.Product import (
    Product,
)


class Order:
    def __init__(self):
        self.items = []
        self.total_cost = 0

    def add_product(self, product: Product):
        self.items.append(product)
        self.total_cost += product.price
        print(f"Added {product}. Total is now ${self.total_cost:.2f}.")

    def remove_product(self, product: Product):
        self.items.remove(product)
        self.total_cost -= product.price
        print(f"Removed {product}. Total is now ${self.total_cost:.2f}.")

    def apply_discount(self, discount: float):
        self.total_cost -= discount
        print(
            f"Applied discount of ${discount:.2f}. Total is now ${self.total_cost:.2f}.",
        )
