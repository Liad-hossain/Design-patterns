from Design_patterns.behavioral_design_patterns.interpreter_design_pattern.example_1.Context import (
    Context,
)
from Design_patterns.behavioral_design_patterns.interpreter_design_pattern.example_1.Expression import (
    Expression,
)


class AndExpression(Expression):
    def __init__(self, expr1: Expression, expr2: Expression):
        self.expr1 = expr1
        self.expr2 = expr2

    def interpret(self, context: Context):
        result1 = self.expr1.interpret(context)
        temp_context = Context(result1)  # Create new context from the first result
        return self.expr2.interpret(temp_context)
