from Design_patterns.behavioral_design_patterns.command_design_pattern.example_1.DiscountCommand import (
    ApplyDiscountCommand,
)
from Design_patterns.behavioral_design_patterns.command_design_pattern.example_1.Order import (
    Order,
)
from Design_patterns.behavioral_design_patterns.command_design_pattern.example_1.OrderCommand import (
    AddToOrderCommand,
)
from Design_patterns.behavioral_design_patterns.command_design_pattern.example_1.Product import (
    Product,
)


class OrderInvoker:
    def __init__(self):
        self.commands = []
        self.undo_command = None

    def set_command(self, command):
        self.commands.append(command)

    def execute_commands(self):
        for command in self.commands:
            command.execute()
            self.undo_command = command

    def undo_last_command(self):
        if self.undo_command:
            self.undo_command.undo()


# Client Code
if __name__ == "__main__":
    # Products
    pizza = Product("Pizza", 12.99)
    soda = Product("Soda", 1.99)

    # Receiver
    my_order = Order()

    # Concrete Commands
    add_pizza = AddToOrderCommand(my_order, pizza)
    add_soda = AddToOrderCommand(my_order, soda)
    apply_discount = ApplyDiscountCommand(my_order, 5.00)

    # Invoker
    order_invoker = OrderInvoker()

    # Setting commands
    order_invoker.set_command(add_pizza)
    order_invoker.set_command(add_soda)
    order_invoker.set_command(apply_discount)

    # Executing all commands
    print("Executing order commands:")
    order_invoker.execute_commands()

    # Undoing the last command
    print("\nUndoing last command:")
    order_invoker.undo_last_command()
