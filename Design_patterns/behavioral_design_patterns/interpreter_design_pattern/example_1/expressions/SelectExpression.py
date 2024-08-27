from Design_patterns.behavioral_design_patterns.interpreter_design_pattern.example_1.Context import (
    Context,
)
from Design_patterns.behavioral_design_patterns.interpreter_design_pattern.example_1.Expression import (
    Expression,
)


class SelectExpression(Expression):
    def __init__(self, columns):
        self.columns = columns

    def interpret(self, context: Context) -> None:
        if self.columns == "*":
            return context.data  # Select all columns
        return [{col: row[col] for col in self.columns} for row in context.data]
