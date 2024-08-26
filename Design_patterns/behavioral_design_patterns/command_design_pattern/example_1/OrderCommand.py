from Design_patterns.behavioral_design_patterns.command_design_pattern.example_1.Command import (
    Command,
)
from Design_patterns.behavioral_design_patterns.command_design_pattern.example_1.Order import (
    Order,
)
from Design_patterns.behavioral_design_patterns.command_design_pattern.example_1.Product import (
    Product,
)


class AddToOrderCommand(Command):
    def __init__(self, order: Order, product: Product):
        self.order = order
        self.product = product

    def execute(self) -> None:
        self.order.add_product(self.product)

    def undo(self) -> None:
        self.order.remove_product(self.product)
