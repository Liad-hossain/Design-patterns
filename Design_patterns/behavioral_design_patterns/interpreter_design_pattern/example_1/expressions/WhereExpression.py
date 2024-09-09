from Design_patterns.behavioral_design_patterns.interpreter_design_pattern.example_1.Context import (
    Context,
)
from Design_patterns.behavioral_design_patterns.interpreter_design_pattern.example_1.Expression import (
    Expression,
)


class WhereExpression(Expression):
    def __init__(self, column, value):
        self.column = column
        self.value = value

    def interpret(self, context: Context):
        return [row for row in context.data if row.get(self.column) == self.value]
