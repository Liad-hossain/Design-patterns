from Design_patterns.behavioral_design_patterns.command_design_pattern.example_1.Command import (
    Command,
)
from Design_patterns.behavioral_design_patterns.command_design_pattern.example_1.Order import (
    Order,
)


class ApplyDiscountCommand(Command):
    def __init__(self, order: Order, discount: float):
        self.order = order
        self.discount = discount

    def execute(self) -> None:
        self.order.apply_discount(self.discount)

    def undo(self) -> None:
        self.order.apply_discount(-self.discount)
